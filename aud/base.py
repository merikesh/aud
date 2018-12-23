import os
import weakref

__version__ = "0.0.1"


def formatted_value(value):
    """Format a given input value to be compliant for USD"""
    if isinstance(value, str):
        value = '"{}"'.format(value.replace('"', '\\"'))
    elif isinstance(value, (list, tuple)):
        temp = []

        for val in value:
            if isinstance(val, str):
                val = '"{}"'.format(val.replace('"', '\\"'))
            temp.append(str(val))
        value = '[{}]'.format(', '.join(temp))

    return str(value)


def indentation(level):
    """Return the indentation string for a given level of indentation"""
    return level * 4 * ' '


class AbstractData(object):
    """Base class for all our primitives"""
    as_type = None

    def __init__(self, *args, **kwargs):
        super(AbstractData, self).__init__()
        self.level = 0
        self.children = []
        self.properties = []
        self.attributes = []
        self.was_set = False
        self.name = None
        self.value = None
        self.parent = None

    def indent(self, level=None):
        """Returns the indentation string"""
        if level is None:
            level = self.level
        return indentation(level)

    def lines(self, indent=0):
        """Create the lines required to write out"""
        self.level = indent
        return []

    def formatted_value(self):
        return formatted_value(self.value)

    def set_value(self, value):
        self.was_set = True
        self.value = value

    def unset_value(self):
        self.was_set = False
        self.value = None

    def set_parent(self, parent):
        self.parent = weakref.proxy(parent)

    def unset_parent(self):
        self.parent = None

    def path(self):
        tokens = []
        node = self

        while node:
            tokens.append(node.name)
            node = node.parent
            if not node:
                tokens.append('/')

        tokens = [t for t in tokens[::-1] if t]
        path = os.path.join(*tokens)
        return path

    def set_property(self, prop, value):
        prop_obj = self.get_property(prop, defaults=True)
        if not prop_obj:
            prop_obj = self.add_property(prop)
        elif prop_obj not in self.properties:
            prop_obj = self.add_property(prop_obj)

        prop_obj.set_value(value)
        return prop_obj

    def set_attribute(self, attr, value, as_type=None, is_uniform=False):
        attr_obj = self.get_attribute(attr, defaults=True)
        if not attr_obj:
            attr_obj = self.add_attribute(attr, as_type=as_type, is_uniform=is_uniform)
        elif attr_obj not in self.attributes:
            attr_obj = self.add_attribute(attr_obj)

        attr_obj.set_value(value)
        return attr_obj

    def get_property(self, name, defaults=False):
        for prop in self.properties:
            if name == prop.name:
                return prop

        if not defaults:
            return

        for cls in self._class_inheritence():
            for k, v in cls.__dict__.items():
                if not isinstance(v, Property):
                    continue

                if name == v.name:
                    prop = Property(
                        name=v.name,
                        value=v.value,
                        values=v.values
                    )

                    return prop

    def get_attribute(self, name, defaults=False):
        for attr in self.attributes:
            if name == attr.name:
                return attr

        if not defaults:
            return

        for cls in self._class_inheritence():
            for k, v in cls.__dict__.items():
                if not isinstance(v, Attribute):
                    continue

                if name == v.name:
                    attr = Attribute(
                        name=v.name,
                        value=v.value,
                        is_uniform=v.is_uniform,
                        as_type=v.as_type,
                        allowedTokens=v.allowed_tokens
                    )

                    return attr

    def add_property(self, prop):
        if not isinstance(prop, Property):
            prop = Property(prop)

        for pr in self.properties:
            if pr.name == prop.name:
                return pr

        self.properties.append(prop)
        prop.set_parent(self)
        return prop

    def add_attribute(self, attr, value=None, as_type=None, is_uniform=False):
        if not isinstance(attr, Attribute):
            attr = Attribute(name=attr, value=value, as_type=as_type, is_uniform=is_uniform)

        for at in self.attributes:
            if at.name == attr.name:
                return at

        self.attributes.append(attr)
        attr.set_parent(self)
        return attr

    def remove_property(self, prop):
        if isinstance(prop, Property):
            for i, pr in enumerate(self.properties):
                if pr.name == prop.name:
                    return self.properties.pop(i)

        else:
            for i, pr in enumerate(self.properties):
                if pr.name == prop.name:
                    return self.properties.pop(i)

    def add_child(self, prim):
        assert isinstance(prim, Prim), "Child must be a primitive"
        self.children.append(prim)
        prim.set_parent(self)
        return prim

    def _class_inheritence(self):
        classes = list(self.__class__.__bases__)
        classes.append(self.__class__)

        return classes


class Stage(AbstractData):
    """Represents the main USD stage that contains all the elements"""

    def save(self, location):

        # Always force a usda extension
        base, ext = os.path.splitext(location)
        location = '{}.usda'.format(base)

        with open(location, 'w') as f:
            f.writelines(self.lines())

    def lines(self, indent=0):
        lines = super(Stage, self).lines(indent)

        lines.append('#usda 1.0\n')
        lines.append('(\n')
        self.level += 1

        lines.append('{}"Written by AUD v{}"\n'.format(self.indent(), __version__))

        for property in self.properties:
            lines.extend(property.lines(self.level))

        self.level -= 1
        lines.append(')\n\n')

        for child in self.children:
            lines.extend(child.lines(self.level))

        return lines

    def set_frame_range(self, start, end):
        self.set_property('startTimeCode', start)
        self.set_property('endTimeCode', end)

    def set_framerate(self, fps):
        self.set_property('timeCodesPerSecond', fps)

    def set_up_axis(self, axis="Y"):
        self.set_property('upAxis', axis.upper())


class Prim(AbstractData):
    """The basic USD object in the hierarchy"""
    as_type = None

    def __init__(self, name, is_class=False, is_over=False, as_type=None):
        super(Prim, self).__init__()
        self.name = name
        self.is_class = is_class
        self.is_over = is_over

        self.as_type = as_type or self.as_type

        self.references = []
        self.inherits = []
        self.variants = []

    def lines(self, indent=0):
        lines = super(Prim, self).lines(indent=indent)

        tokens = []
        if self.is_class:
            tokens.append('class')
        elif self.is_over:
            tokens.append('over')
        else:
            tokens.append('def')

        if self.as_type:
            tokens.append(self.as_type)

        tokens.append('"{}"'.format(self.name))

        lines.append('\n{}{} (\n'.format(self.indent(), ' '.join(tokens)))
        self.level += 1

        for prop in (self.variants + self.references + self.inherits + self.properties):
            lines.extend(prop.lines(indent=self.level))
            lines.append("\n")

        self.level -= 1
        lines.append('{0})\n{0}{{\n'.format(self.indent()))

        self.level += 1
        for attr in self.attributes:
            lines.extend(attr.lines(indent=self.level))
            lines.append("\n")

        for child in self.children:
            lines.extend(child.lines(indent=self.level))

        self.level -= 1

        lines.append('\n{}}}\n'.format(self.indent()))

        return lines

    def add_reference(self, ref, mode=None):
        if mode not in Iterable.modes:
            raise ValueError("{} is not a valid mode".format(mode))

        for iterable in self.references:
            if iterable.mode == mode:
                break
        else:
            iterable = Iterable(name='reference', mode=mode)
            self.references.append(iterable)

        if not isinstance(ref, IterObject):
            ref = IterObject(ref, is_file=True)

        iterable.append(ref)

    def add_inherit(self, inherits, mode=None):
        if mode not in Iterable.modes:
            raise ValueError("{} is not a valid mode".format(mode))

        for iterable in self.inherits:
            if iterable.mode == mode:
                break
        else:
            iterable = Iterable(name='inherits', mode=mode)
            self.references.append(iterable)

        if not isinstance(inherits, IterObject):
            inherits = IterObject(inherits, is_file=False)

        iterable.append(inherits)

    def add_variant(self, variant, mode=None):
        if mode not in Iterable.modes:
            raise ValueError("{} is not a valid mode".format(mode))

        for iterable in self.inherits:
            if iterable.mode == mode:
                break
        else:
            iterable = Iterable(name='variantSets', mode=mode)
            self.variants.append(iterable)

        if not isinstance(variant, IterObject):
            variant = IterObject(variant)

        iterable.append(variant)


class Property(AbstractData):
    """A property for a USD Prim that appears between the parenthesis"""

    def __init__(self, name, value=None, values=None):
        super(Property, self).__init__()
        self.name = name
        self.values = values
        self.value = value

    def lines(self, indent=0):
        lines = super(Property, self).lines(indent=indent)
        if not self.was_set:
            return lines

        tokens = []
        if self.as_type:
            tokens.append(self.as_type)

        tokens.extend([self.name, '=', self.formatted_value()])
        tokens = [str(t) for t in tokens]

        tokens = ' '.join([t for t in tokens if t])

        lines.append("{}{}\n".format(self.indent(), tokens))

        return lines


class Attribute(AbstractData):
    """Data attributes that provide actual information about a prim between its {}"""

    def __init__(self, name, value=None, is_uniform=False,
                 as_type=None, docstring=None,
                 allowedTokens=None, **kwargs):
        super(Attribute, self).__init__()
        self.__doc__ = self.docstring = docstring
        self.is_uniform = is_uniform
        self.value = value
        self.name = name
        self.as_type = as_type
        self.allowed_tokens = self.allowedTokens = allowedTokens

    def lines(self, indent=0):
        lines = super(Attribute, self).lines(indent=indent)
        if not self.was_set:
            return lines

        tokens = []
        if self.is_uniform:
            tokens.append('uniform')

        if self.as_type:
            tokens.append(self.as_type)

        tokens.append(self.name)

        tokens.append('=')
        tokens.append(self.formatted_value())
        tokens = [str(t) for t in tokens]

        lines.append('{}{}'.format(self.indent(), ' '.join(tokens)))
        if not self.properties:
            return lines

        lines.append(" (\n")
        self.level += 1

        for prop in self.properties:
            lines.extend(prop.lines(indent=self.level))

        self.level -= 1
        lines.append('{})'.format(self.indent()))

        return lines


class Iterable(list):
    """Represents a USD list"""
    mode = None
    modes = (None, 'add', 'prepend', 'del')

    def __init__(self, name, mode=None):
        super(Iterable, self).__init__()
        self.name = name
        if mode not in self.modes:
            raise ValueError("{} is not a valid mode for an iterable".format(mode))
        self.mode = mode
        self.level = 0

    def indent(self, level=None):
        """Returns the indentation string"""
        if level is None:
            level = self.level
        return indentation(level)

    def lines(self, indent=0):
        self.level = indent
        lines = []

        tokens = []
        if self.mode:
            tokens.append(self.mode)

        tokens.extend([self.name, '='])

        lines.append('{0}{1} [\n{2}{3}\n{0}]'.format(
            self.indent(),
            ' '.join(tokens),
            indentation(self.level + 1),
            '{},\n'.format(indentation(self.level + 1).join(str(i) for i in self if i))
        ))

        return lines


class IterObject(object):
    """Represents an object inside a USD list and can format to various formats"""
    reference = False
    location = None
    object_name = None
    is_file = False

    def __init__(self, value=None, object_name=None, is_file=False):
        super(IterObject, self).__init__()
        if isinstance(value, AbstractData):
            object_name = value.path()
            value = None
            is_file = False

        self.value = value
        self.object_name = object_name
        self.is_file = is_file

    def formatted(self):
        val = self.value or ''
        if not val and not self.object_name:
            return

        if not self.object_name and not self.is_file:
            return formatted_value(val)

        if self.is_file:
            val = '@{}@'.format(val)

        if self.object_name:
            val += '<{}>'.format(self.object_name)

        return str(val) or None

    def __str__(self):
        return self.formatted()


class VariantSet(Prim):
    """Create a Variant Set inside a prim"""

    def lines(self, indent=0):
        lines = AbstractData.lines(self, indent=indent)

        lines.append('{}variantSet "{}" = {{\n'.format(self.indent(), self.name))
        self.level += 1

        for child in self.children:
            lines.extend(child.lines(indent=self.level))
            lines.append('\n')

        self.level -= 1
        lines.append('{0}}}\n'.format(self.indent()))

        return lines


class Variant(Prim):
    """Create a Variant inside a Variant Set"""

    def lines(self, indent=0):
        lines = AbstractData.lines(self, indent=indent)

        lines.append('{}"{}" {{\n'.format(self.indent(), self.name))

        self.level += 1

        for child in self.children:
            lines.extend(child.lines(indent=self.level))
            lines.append('\n')

        self.level -= 1
        lines.append('{0}}}\n'.format(self.indent()))

        return lines
