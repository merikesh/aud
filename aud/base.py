import os
import weakref

__version__ = "0.0.2"


def formatted_value(value, array=True):
    """Format a given input value to be compliant for USD

    Args:
        array (bool): If provided, will treat iterables as an array rather than a tuple

    """
    if isinstance(value, str):
        value = '"{}"'.format(value.replace('"', '\\"'))
    elif isinstance(value, (list, tuple)):
        temp = []

        for val in value:
            if isinstance(val, str):
                val = formatted_value(val, array=False)
            temp.append(str(val))
        value = '{}{}{}'.format(
            '[' if array else '(',
            ', '.join(temp),
            ']' if array else ')'
        )

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
        self.keyframes = {}

    def indent(self, level=None):
        """Returns the indentation string"""
        if level is None:
            level = self.level
        return indentation(level)

    def lines(self, indent=0):
        """Create the lines required to write out"""
        self.level = indent
        return []

    def formatted_name(self):
        name = self.name
        if self.keyframes:
            name = '{}.timeSamples'.format(name)

        return name

    def formatted_value(self, frame=None):
        if frame is None:
            value = self.value
        elif frame in self.keyframes:
            value = self.keyframes[frame]
        else:
            raise KeyError("No keyframe value for frame: {}".format(frame))

        return formatted_value(value, array=self.as_type and '[' in self.as_type)




    def set_value(self, value):
        self.was_set = True
        self.value = value

    def unset_value(self):
        self.was_set = False
        self.value = None

    def set_parent(self, parent):
        if parent:
            self.parent = weakref.proxy(parent)
        else:
            self.parent = None

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

    def set_attribute(self, attr, value, as_type=None, is_uniform=None):
        attr_obj = self.get_attribute(attr, defaults=True)
        if not attr_obj:
            attr_obj = self.add_attribute(attr, as_type=as_type, is_uniform=is_uniform)
        elif attr_obj not in self.attributes:
            attr_obj = self.add_attribute(attr_obj)

        attr_obj.set_value(value)
        if as_type is not None:
            attr_obj.as_type = as_type
        if is_uniform is not None:
            attr_obj.is_uniform = is_uniform
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

    def remove_child(self, prim):
        """Remove the prim. Returns a boolean if it was a child or not"""
        assert isinstance(prim, Prim), "Child must be a primitive"
        if prim not in self.children:
            return False

        self.children.pop(self.children.index(prim))
        prim.set_parent(None)

        return True

    def _class_inheritence(self):
        classes = list(self.__class__.__bases__)
        classes.append(self.__class__)

        return classes

    def set_keyframe(self, frame, value):
        self.value = None
        self.keyframes[frame] = value


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

        lines.append('\n{}{}'.format(self.indent(), ' '.join(tokens)))
        if self.properties:
            lines.append(' (')
            lines.append('\n')
            self.level += 1

            for prop in (self.variants + self.references + self.inherits + self.properties):
                lines.extend(prop.lines(indent=self.level))
                lines.append("\n")

            self.level -= 1
            lines.append('{})'.format(self.indent()))

        lines.append('\n{0}{{\n'.format(self.indent()))

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

    def set_xform_order(self, order='trs'):
        ops = []
        for o in order:
            if o == 't':
                ops.append('xformOp:translate')
            elif o == 'r':
                ops.append('xformOp:rotateXYZ')
            elif o == 's':
                ops.append('xformOp:scale')
            else:
                raise ValueError('Cannot understand xform order: {}'.format(o))

        self.set_attribute('xformOpOrder', ops, as_type='token[]', is_uniform=True)


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

        tokens.extend([self.formatted_name(), '='])
        if self.keyframes:
            tokens.append('{')
        else:
            tokens.append(self.formatted_value())

        tokens = [str(t) for t in tokens]

        tokens = ' '.join([t for t in tokens if t])

        lines.append("{}{}\n".format(self.indent(), tokens))

        if not self.keyframes:
            return lines

        self.level += 1
        for frame, value in self.keyframes:
            lines.append("{}{}:{},\n".format(
                self.indent(), frame, self.formatted_value(frame=frame)
            ))
        self.level -= 1
        lines.append("{}}}\n".format(self.indent(), ))


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

        tokens.append(self.formatted_name())

        tokens.append('=')
        if self.keyframes:
            tokens.append('{\n')
        else:
            tokens.append(self.formatted_value())
        tokens = [str(t) for t in tokens]

        lines.append('{}{}'.format(self.indent(), ' '.join(tokens)))
        if self.keyframes:
            self.level += 1
            for frame in self.keyframes:
                lines.append('{}{}: {},\n'.format(
                    self.indent(),
                    frame,
                    self.formatted_value(frame=frame)
                ))

            self.level -= 1
            lines.append('{}}}\n'.format(self.indent()))


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
