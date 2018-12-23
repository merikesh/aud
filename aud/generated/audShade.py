from .base import Prim, Attribute, Property

class NodeGraph(Prim):
    """
    A node-graph is a container for shading nodes, as well as other    node-graphs. It has a public input interface and provides a list of public
    outputs.
    <b>Node Graph Interfaces</b>
    One of the most important functions of a node-graph is to host the "interface"
    with which clients of already-built shading networks will interact.  Please
    see "Interface Inputs" for a detailed
    explanation of what the interface provides, and how to construct and
    use it, to effectively share/instance shader networks.
    <b>Node Graph Outputs</b>
    These behave like outputs on a shader and are typically connected to an
    output on a shader inside the node-graph.

    """

    as_type = "NodeGraph"

class Material(Prim):
    """
    A Material provides a container into which multiple \render targets\

    """

    as_type = "Material"
    displacement = Attribute(
        name = 'outputs:displacement',
        as_type = 'token',
        displayGroup = "Outputs",
        docstring = """,
        Represents the universal "displacement" output terminal of a        material.
        """,

    )
    surface = Attribute(
        name = 'outputs:surface',
        as_type = 'token',
        displayGroup = "Outputs",
        docstring = """,
        Represents the universal "surface" output terminal of a        material.
        """,

    )
    volume = Attribute(
        name = 'outputs:volume',
        as_type = 'token',
        displayGroup = "Outputs",
        docstring = """,
        Represents the universal "volume" output terminal of a        material.
        """,

    )

class Shader(Prim):
    """
    Base class for all USD shaders. Shaders are the building blocks    of shading networks. While UsdShadeShader objects are not target specific,
    each renderer or application target may derive its own renderer-specific
    shader object types from this base, if needed.
    Objects of this class generally represent a single shading object, whether
    it exists in the target renderer or not. For example, a texture, a fractal,
    or a mix node.
    The main property of this class is the info:id token, which uniquely
    identifies the type of this node. The id resolution into a renderable
    shader target is deferred to the consuming application.
    The purpose of representing them in Usd is two-fold:
    - To represent, via "connections" the topology of the shading network
    that must be reconstructed in the renderer. Facilities for authoring and
    manipulating connections are encapsulated in the Has-A schema
    UsdShadeConnectableAPI.
    - To present a (partial or full) interface of typed input parameters
    whose values can be set and overridden in Usd, to be provided later at
    render-time as parameter values to the actual render shader objects. Shader
    input parameters are encapsulated in the property schema UsdShadeInput.

    """

    as_type = "Shader"
    id_ = Attribute(
        name = 'info:id',
        as_type = 'token',
        is_uniform = True,
        docstring = """,
        The id is an identifier for the type or purpose of the        shader. E.g.: Texture or FractalFloat.
        The use of this id will depend on the render target: some will turn it
        into an actual shader path, some will use it to generate shader source
        code dynamically.
        \\sa SetShaderId()
        """,

    )
    implementationSource = Attribute(
        name = 'info:implementationSource',
        as_type = 'token',
        value = "id",
        is_uniform = True,
        allowedTokens = ["id", "sourceAsset", "sourceCode"],
        docstring = """,
        Specifies the attribute that should be consulted to get the        shader's implementation or its source code.
        * If set to \id\, the \info:id\ attribute's value is used to
        """,

    )
    corresponding = Attribute(
        name = 'corresponding',
        as_type = 'attribute',
        docstring = """,
        """,

    )
    to = Attribute(
        name = 'to',
        as_type = 'corresponding',
        docstring = """,
        """,

    )

class ConnectableAPI(Prim):
    """
    UsdShadeConnectableAPI is an API schema that provides a common    interface for creating outputs and making connections between shading
    parameters and outputs. The interface is common to all UsdShade schemas
    that support Inputs and Outputs, which currently includes UsdShadeShader,
    UsdShadeNodeGraph, and UsdShadeMaterial .
    One can construct a UsdShadeConnectableAPI directly from a UsdPrim, or
    from objects of any of the schema classes listed above.  If it seems
    onerous to need to construct a secondary schema object to interact with
    Inputs and Outputs, keep in mind that any function whose purpose is either
    to walk material/shader networks via their connections, or to create such
    networks, can typically be written entirely in terms of
    UsdShadeConnectableAPI objects, without needing to care what the underlying
    prim type is.
    Additionally, the most common UsdShadeConnectableAPI behaviors
    (creating Inputs and Outputs, and making connections) are wrapped as
    convenience methods on the prim schema classes (creation) and
    UsdShadeInput and UsdShadeOutput.

    """

    pass

class MaterialBindingAPI(Prim):
    """
    UsdShadeMaterialBindingAPI is an API schema that provides an    interface for binding materials to prims or collections of prims
    (represented by UsdCollectionAPI objects).
    In the USD shading model, each renderable gprim computes a single
    <b>resolved Material</b> that will be used to shade the gprim (exceptions,
    of course, for gprims that possess UsdGeomSubsets, as each subset can be
    shaded by a different Material).  A gprim <b>and each of its ancestor
    prims</b> can possess, through the MaterialBindingAPI, both a
    <b>direct</b> binding to a Material, and any number of
    <b>collection-based</b> bindings to Materials; each binding can be generic
    or declared for a particular <b>purpose</b>, and given a specific <b>binding
    strength</b>. It is the process of \material resolution\ (see

    """

    pass