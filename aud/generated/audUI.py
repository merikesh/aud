from .base import Prim, Attribute, Property

class NodeGraphNodeAPI(Prim):
    """

    """

    displayColor = Attribute(
        name = 'ui:nodegraph:node:displayColor',
        as_type = 'color3f',
        is_uniform = True,
        docstring = """,
        """,

    )
    expansionState = Attribute(
        name = 'ui:nodegraph:node:expansionState',
        as_type = 'token',
        is_uniform = True,
        allowedTokens = ["open", "closed", "minimized"],
        docstring = """,
        """,

    )
    icon = Attribute(
        name = 'ui:nodegraph:node:icon',
        as_type = 'asset',
        is_uniform = True,
        docstring = """,
        """,

    )
    pos = Attribute(
        name = 'ui:nodegraph:node:pos',
        as_type = 'float2',
        is_uniform = True,
        docstring = """,
        """,

    )
    for_ = Attribute(
        name = 'for',
        as_type = 'store',
        docstring = """,
        """,

    )
    size = Attribute(
        name = 'ui:nodegraph:node:size',
        as_type = 'float2',
        is_uniform = True,
        docstring = """,
        """,

    )
    stackingOrder = Attribute(
        name = 'ui:nodegraph:node:stackingOrder',
        as_type = 'int',
        is_uniform = True,
        docstring = """,
        """,

    )

class SceneGraphPrimAPI(Prim):
    """

    """

    displayGroup = Attribute(
        name = 'ui:displayGroup',
        as_type = 'token',
        is_uniform = True,
        docstring = """,
        When publishing a nodegraph or a material, it can be useful to        provide an optional display group, for organizational purposes and
        readability. This is because often the usd shading hierarchy is rather
        flat while we want to display it in organized groups.
        """,

    )
    displayName = Attribute(
        name = 'ui:displayName',
        as_type = 'token',
        is_uniform = True,
        docstring = """,
        When publishing a nodegraph or a material, it can be useful to        provide an optional display name, for readability.
        """,

    )

class Backdrop(Prim):
    """
    Provides a 'group-box' for the purpose of node graph organization.
    Unlike containers, backdrops do not store the Shader nodes inside of them.
    Backdrops are an organizational tool that allows Shader nodes to be visually
    grouped together in a node-graph UI, but there is no direct relationship
    between a Shader node and a Backdrop.
    The guideline for a node-graph UI is that a Shader node is considered part
    of a Backdrop when the Backdrop is the smallest Backdrop a Shader node's
    bounding-box fits inside.
    Backdrop objects are contained inside a NodeGraph, similar to how Shader
    objects are contained inside a NodeGraph.
    Backdrops have no shading inputs or outputs that influence the rendered
    results of a NodeGraph. Therefore they can be safely ignored during import.
    Like Shaders and NodeGraphs, Backdrops subscribe to the NodeGraphNodeAPI to
    specify position and size.

    """

    as_type = "Backdrop"
    description = Attribute(
        name = 'ui:description',
        as_type = 'token',
        is_uniform = True,
        docstring = """,
        The text label that is displayed on the backdrop in the node        graph. This help-description explains what the nodes in a backdrop do.
        """,

    )