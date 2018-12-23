from __future__ import print_function

import logging
import os
import re
import subprocess
import sys
import keyword

logging.basicConfig()
logger = logging.getLogger('aud-builder')
logger.setLevel(logging.DEBUG)

PY2 = sys.version_info.major == 2

reserved = set(keyword.kwlist)
if PY2:
    import __builtin__

    reserved.update(dir(__builtin__))
else:
    import builtins

    reserved.update(dir(builtins))


def target_file_name(schema_name):
    name = re.sub('^usd', 'aud', schema_name)
    name = '{}.py'.format(os.path.splitext(name)[0])
    if name == 'aud.py':
        name = 'audCore.py'
    return name


def generate_python(version, schema_root, target_directory):
    init = make_init(schema_root, target_directory, version)

    for schema in os.listdir(schema_root):
        if not schema.endswith('.usda'):
            continue

        source = os.path.join(schema_root, schema)
        target = os.path.join(target_directory, target_file_name(schema))
        convert_schema(source, target)

    os.chdir(target_directory)
    subprocess.call(['git', 'add', '.'])


def make_init(schema_root, target_directory, version):
    file_path = os.path.join(target_directory, '__init__.py')
    with open(file_path, 'w') as f:
        f.write('__usd_version__ = "{}"\n'.format(version))


def convert_schema(source, target):
    try:
        schema_parser = ParseSchema(source)
        schema_parser.process()
        lines = schema_parser.lines
    except:
        logger.exception('Could not parse %s', source)
        lines = None

    with open(target, 'w') as f:
        f.writelines('\n'.join(lines or []))


class USDDataParser(object):
    def __init__(self):
        super(USDDataParser, self).__init__()
        self.doc = ''
        self._indent = 0
        self.properties = []
        self.name = None
        self.value = None
        self.as_type = None

    def indent(self):
        return ' ' * (self._indent * 4)

    def add_property_from_line(self, line):
        line = line.strip()
        tokens = line.split(' ', 2)
        prop = USDPropertyParser()
        prop.name = tokens[0]
        prop.value = tokens[-1]
        self.properties.append(prop)

    def __repr__(self):
        return "{} - {}".format(self.name, super(USDDataParser, self).__repr__())

    def lines(self, indent=0):
        self._indent = indent
        logger.debug("Called USDDataParser.lines(). Please implement for %s", self)
        return []


class USDPropertyParser(USDDataParser):

    def lines(self, indent=0):
        self._indent = indent
        lines = []
        name = self.name
        if name in reserved:
            name += "_"
        lines.append("{0}{1} = Property(name='{1}', values={2})".format(
            self.indent(),
            name,
            self.value
        ))
        return lines


class USDAttributeParser(USDDataParser):
    def __init__(self):
        super(USDAttributeParser, self).__init__()
        self.uniform = False

    def lines(self, indent=0):
        self._indent = indent
        lines = []

        name = self.name.split(':')[-1]
        if name in reserved:
            name += "_"

        lines.append("{}{} = Attribute(".format(self.indent(), name))
        self._indent += 1

        lines.append("{}name = '{}',".format(self.indent(), self.name))

        lines.append("{}as_type = '{}',".format(self.indent(), self.as_type))

        if self.value:
            lines.append('{}value = {},'.format(self.indent(), self.value))

        if self.uniform:
            lines.append('{}is_uniform = True,'.format(self.indent()))

        # Handle properties
        for prop in self.properties:
            lines.append('{0}{1} = {2},'.format(
                self.indent(),
                prop.name,
                prop.value
            ))

        # Handle docstring
        docs = ''
        for line in self.doc.split('\n'):
            stripped = line.strip()
            if not stripped: continue
            docs += ('{}{}\n'.format(
                self.indent(),
                line.strip()
            ))
        lines.append('{0}docstring = {1}\n{2}{0}{1}\n'.format(
            self.indent(),
            "'''" if '"""' in docs else '""",',
            docs
        ))

        self._indent = indent
        lines.append("{})".format(self.indent()))
        return lines


class USDClassParser(USDDataParser):
    definition_pattern = re.compile(r'^class ((?P<type>\w+) )?\"(?P<name>\w+)\" \(')
    doc_start_pattern = re.compile(r'doc = ([\"\"\"|\'\'\'])(.*)')
    property_pattern = re.compile(r'^(?P<name>\w+) \= ')
    attribute_pattern = re.compile(
        r'^(?P<uniform>uniform )?(?P<type>[a-z0-9]+) (?P<name>[a-zA-Z0-9:]+)'
        r'(?P<has_value> \= )?(?P<value>.*)\('
    )

    def __init__(self, lines):
        super(USDClassParser, self).__init__()
        self._input_lines = lines
        self.bases = ['Prim']
        self.attributes = []

    def process(self):
        found_class = False
        in_doc = False
        doc_quotes = '"""'
        in_params = False
        current_structure = self
        in_structure = False
        in_attributes = False

        for line in self._input_lines:

            stripped = line.strip()

            # Start a class definition
            if not found_class and line.startswith('class'):
                match = self.definition_pattern.match(line)
                if not match:
                    continue

                found_class = True
                in_params = True
                match = match.groupdict()
                self.name = match['name']
                self.as_type = match.get('type')
                if stripped.endswith(')'):
                    in_params = False
                continue

            # If we haven't found a class something is wrong
            if not found_class:
                continue
                logger.error("Parsing warning. No class found: %s", line)

            # Process doc strings
            if not in_doc:
                doc_match = self.doc_start_pattern.search(stripped)
                if doc_match:
                    in_doc = True
                    doc_quotes = doc_match.groups()[0]
                    doc_line = doc_match.groups()[1]
                    current_structure.doc += doc_line.replace(doc_quotes, '')
                    if doc_line.endswith(doc_quotes):
                        in_doc = False
                    continue
            else:
                if doc_quotes in line:
                    line = line.replace(doc_quotes, '')
                    in_doc = False
                current_structure.doc += line
                continue

            # Process parameters
            if in_params and stripped.startswith(')'):
                in_params = False

            if in_params:
                property_match = self.property_pattern.match(stripped)
                if property_match:
                    current_structure.add_property_from_line(line)
                    continue

            # Process Attributes
            if stripped.startswith('{'):
                in_attributes = True
                continue
            elif stripped.startswith('}'):
                in_attributes = False
                continue

            if in_attributes:
                if stripped.endswith('('):
                    in_params = True
                match = self.attribute_pattern.match(stripped)
                if match:
                    attribute = USDAttributeParser()
                    current_structure = attribute
                    self.attributes.append(attribute)
                    match_dict = match.groupdict()

                    attribute.name = match_dict['name']
                    attribute.uniform = bool(match_dict.get('uniform'))
                    attribute.as_type = match_dict['type']
                    if match_dict.get('has_value'):
                        attribute.value = match_dict['value'].strip()
                    continue

    def lines(self, indent=0):
        self._indent = indent
        lines = []
        if not self.name:
            self.process()

        if not self.name:
            return lines

        # Make class def
        lines.append('\nclass {}({}):'.format(self.name, ', '.join(self.bases)))
        self._indent += 1
        docs = ''
        for line in self.doc.split('\n'):
            stripped = line.strip()
            if not stripped: continue
            docs += ('{}{}\n'.format(
                self.indent(),
                line.strip()
            ))
        lines.append('{0}{1}\n{2}\n{0}{1}\n'.format(
            self.indent(),
            "'''" if '"""' in docs else '"""',
            docs
        ))
        if self.as_type:
            lines.append('{}as_type = "{}"'.format(self.indent(), self.as_type))

        for prop in self.properties:
            lines.extend(prop.lines(indent=self._indent))

        for attr in self.attributes:
            lines.extend(attr.lines(indent=self._indent))

        if not any([self.attributes, self.properties, self.as_type]):
            lines.append("{}pass".format(self.indent()))

        return lines


class ParseSchema(object):
    def __init__(self, source):
        super(ParseSchema, self).__init__()
        self.source = source
        self.lines = []

        self.class_lines = []

    def process(self):
        self.make_imports()
        self.collect_structures()

        for cls_lines in self.class_lines:
            schema_class = USDClassParser(cls_lines)
            self.lines.extend(schema_class.lines())

    def make_imports(self):
        self.lines.append('from .base import Prim, Attribute, Property')

    def collect_structures(self):
        with open(self.source, 'r') as f:
            lines = f.readlines()

        structure = []
        in_class = False
        for line in lines:
            # Add classes
            if line.startswith('class '):
                in_class = True
                structure.append(line)
            elif in_class and line.startswith('}'):
                in_class = False
                self.class_lines.append(structure)
                structure = []
                in_class = False
            elif in_class:
                structure.append(line)
