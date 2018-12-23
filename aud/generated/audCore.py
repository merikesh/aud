from .base import Prim, Attribute, Property

class APISchemaBase(Prim):
    """
    The base class for all API schemas.
    An API schema provides an interface to a prim's qualities, but does not
    specify a typeName for the underlying prim. The prim's qualities include
    its inheritance structure, attributes, relationships etc. Since it cannot
    provide a typeName, an API schema is considered to be non-concrete.
    To auto-generate an API schema using usdGenSchema, simply leave the
    typeName empty and make it inherit from \/APISchemaBase\ or from another

    """

    pass

class ModelAPI(Prim):
    """
    UsdModelAPI is an API schema that provides an interface to a prim's    model qualities, if it does, in fact, represent the root prim of a model.
    The first and foremost model quality is its kind, i.e. the metadata
    that establishes it as a model (See KindRegistry).  UsdModelAPI provides
    various methods for setting and querying the prim's kind, as well as
    queries (also available on UsdPrim) for asking what category of model
    the prim is.  See \Kind and Model-ness\.

    """

    pass

class CollectionAPI(Prim):
    """
    This is a general purpose API schema, used to describe a    collection of heterogeneous objects within the scene. \Objects\ here may be

    """

    excludes = Attribute(
        name = 'excludes',
        as_type = 'rel',
        docstring = """,
        Specifies a list of targets that are excluded below        the included paths in this collection. This can target prims or
        properties directly, but cannot target another collection. This is to
        keep the membership determining logic simple, efficient and easier to
        reason about. Finally, it is invalid for a collection to exclude
        paths that are not included in it. The presence of such "orphaned"
        excluded paths will not affect the set of paths included in the
        collection, but may affect the performance of querying membership of
        a path in the collection (see
        UsdCollectionAPI::MembershipQuery::IsPathIncluded)
        or of enumerating the objects belonging to the collection (see
        UsdCollectionAPI::GetIncludedObjects).
        """,

    )
    expansionRule = Attribute(
        name = 'expansionRule',
        as_type = 'token',
        is_uniform = True,
        docstring = """,
        Specifies how the paths that are included in        the collection must be expanded to determine its members.
        """,

    )
    includeRoot = Attribute(
        name = 'includeRoot',
        as_type = 'bool',
        is_uniform = True,
        docstring = """,
        Boolean attribute indicating whether the pseudo-root        path &lt;/&gt; should be counted as one of the included target
        paths.  The fallback is false.  This separate attribute is
        required because relationships cannot directly target the root.
        """,

    )
    includes = Attribute(
        name = 'includes',
        as_type = 'rel',
        docstring = """,
        Specifies a list of targets that are included in the collection.        This can target prims or properties directly. A collection can insert
        the rules of another collection by making its <i>includes</i>
        relationship target the <b>collection:{collectionName}</b> property on
        the owning prim of the collection to be included
        """,

    )

class ClipsAPI(Prim):
    """
    UsdClipsAPI is an API schema that provides an interface to    a prim's clip metadata. Clips are a \value resolution\ feature that

    """

    pass