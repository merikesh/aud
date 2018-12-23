from .base import Prim, Attribute, Property

class BlindDataObject(Prim):
    """
    Container namespace schema for katana blind data from the klf file

    """

    as_type = "BlindDataObject"
    suppressGroupToAssemblyPromotion = Attribute(
        name = 'katana:suppressGroupToAssemblyPromotion',
        as_type = 'bool',
        docstring = """,
        If true don't promote a group to an assembly.
        """,

    )

class LookAPI(Prim):
    """
    Katana-specific extensions of UsdShadeMaterial.

    """

    primName = Attribute(
        name = 'katana:primName',
        as_type = 'string',
        is_uniform = True,
        docstring = """,
        When a Material derives from another, \base\ Material (see        \SetBaseMaterial()\), it seems
        """,

    )
    in_ = Attribute(
        name = 'in',
        as_type = 'recursion',
        docstring = """,
        """,

    )