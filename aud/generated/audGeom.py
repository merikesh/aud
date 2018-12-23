from .base import Prim, Attribute, Property

class Imageable(Prim):
    """
    Base class for all prims that may require rendering or    visualization of some sort. The primary attributes of Imageable
    are visibility and purpose, which each provide instructions for
    what geometry should be included for processing by rendering and other
    computations.
    <Deprecated> Imageable also provides API for accessing primvars, which
    have been moved to the UsdGeomPrimvarsAPI schema.  This API is planned
    to be removed, UsdGeomPrimvarsAPI should be used directly instead.

    """

    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )

class PrimvarsAPI(Prim):
    """
    UsdGeomPrimvarsAPI encodes geometric \primitive variables\,    as UsdGeomPrimvar, which interpolate across a primitive's topology,
    can override shader inputs, and inherit down namespace.

    """

    pass

class Xformable(Prim):
    """
    Base class for all transformable prims, which allows arbitrary    sequences of component affine transformations to be encoded.
    \\note
    You may find it useful to review while reading
    this class description.
    <b>Supported Component Transformation Operations</b>
    UsdGeomXformable currently supports arbitrary sequences of the following
    operations, each of which can be encoded in an attribute of the proper
    shape in any supported precision:
    - translate - 3D
    - scale     - 3D
    - rotateX   - 1D angle in degrees
    - rotateY   - 1D angle in degrees
    - rotateZ   - 1D angle in degrees
    - rotateABC - 3D where ABC can be any combination of the six principle
    Euler Angle sets: XYZ, XZY, YXZ, YZX, ZXY, ZYX.  See
    \note on rotation packing order\

    """

    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Scope(Prim):
    """
    Scope is the simplest grouping primitive, and does not carry the    baggage of transformability.  Note that transforms should inherit down
    through a Scope successfully - it is just a guaranteed no-op from a
    transformability perspective.

    """

    as_type = "Scope"
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )

class Xform(Prim):
    """
    Concrete prim schema for a transform, which implements Xformable

    """

    as_type = "Xform"
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Boundable(Prim):
    """
    Boundable introduces the ability for a prim to persistently    cache a rectilinear, local-space, extent.
    Why Extent and not Bounds ?
    Boundable introduces the notion of \extent\, which is a cached computation
    Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
    transform not applied), without accounting for any shader-induced
    displacement.  Whenever any geometry-affecting attribute is authored
    for any gprim in a layer, extent must also be authored at the same
    timesample; failure to do so will result in incorrect bounds-computation.
    \\sa \\ref UsdGeom_Boundable_Extent.
    An authored extent on a prim which has children is expected to include
    the extent of all children, as they will be pruned from BBox computation
    during traversal.

    """

    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Gprim(Prim):
    """
    Base class for all geometric primitives.
    Gprim encodes basic graphical properties such as doubleSided and
    orientation, and provides primvars for "display color" and "display
    opacity" that travel with geometry to be used as shader overrides.

    """

    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
        transform not applied), without accounting for any shader-induced
        displacement.  Whenever any geometry-affecting attribute is authored
        for any gprim in a layer, extent must also be authored at the same
        timesample; failure to do so will result in incorrect bounds-computation.
        \\sa \\ref UsdGeom_Boundable_Extent.
        An authored extent on a prim which has children is expected to include
        the extent of all children, as they will be pruned from BBox computation
        during traversal.
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Cube(Prim):
    """
    Defines a primitive rectilinear cube centered at the origin.
    The fallback values for Cube, Sphere, Cone, and Cylinder are set so that
    they all pack into the same volume/bounds.

    """

    as_type = "Cube"
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is re-defined on Cube only to provide a fallback value.        \\sa UsdGeomGprim::GetExtentAttr().
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    size = Attribute(
        name = 'size',
        as_type = 'double',
        value = 2,
        docstring = """,
        Indicates the length of each edge of the cube.  If you        author size you must also author extent.
        \\sa GetExtentAttr()
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Sphere(Prim):
    """
    Defines a primitive sphere centered at the origin.
    The fallback values for Cube, Sphere, Cone, and Cylinder are set so that
    they all pack into the same volume/bounds.

    """

    as_type = "Sphere"
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is re-defined on Sphere only to provide a fallback        value. \\sa UsdGeomGprim::GetExtentAttr().
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    radius = Attribute(
        name = 'radius',
        as_type = 'double',
        value = 1,
        docstring = """,
        Indicates the sphere's radius.  If you        author radius you must also author extent.
        \\sa GetExtentAttr()
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Cylinder(Prim):
    """
    Defines a primitive cylinder with closed ends, centered at the    origin, whose spine is along the specified axis.
    The fallback values for Cube, Sphere, Cone, and Cylinder are set so that
    they all pack into the same volume/bounds.

    """

    as_type = "Cylinder"
    axis = Attribute(
        name = 'axis',
        as_type = 'token',
        value = "Z",
        is_uniform = True,
        allowedTokens = ["X", "Y", "Z"],
        docstring = """,
        The axis along which the spine of the cylinder is aligned
        """,

    )
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is re-defined on Cylinder only to provide a fallback        value. \\sa UsdGeomGprim::GetExtentAttr().
        """,

    )
    height = Attribute(
        name = 'height',
        as_type = 'double',
        value = 2,
        docstring = """,
        The size of the cylinder's spine along the specified        axis.  If you author height you must also author extent.
        \\sa GetExtentAttr()
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    radius = Attribute(
        name = 'radius',
        as_type = 'double',
        value = 1,
        docstring = """,
        The radius of the cylinder. If you author radius        you must also author extent.
        \\sa GetExtentAttr()
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Capsule(Prim):
    """
    Defines a primitive capsule, i.e. a cylinder capped by two half    spheres, centered at the origin, whose spine is along the specified
    axis.

    """

    as_type = "Capsule"
    axis = Attribute(
        name = 'axis',
        as_type = 'token',
        value = "Z",
        is_uniform = True,
        allowedTokens = ["X", "Y", "Z"],
        docstring = """,
        The axis along which the spine of the capsule is aligned
        """,

    )
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is re-defined on Capsule only to provide a fallback        value. \\sa UsdGeomGprim::GetExtentAttr().
        """,

    )
    height = Attribute(
        name = 'height',
        as_type = 'double',
        value = 1,
        docstring = """,
        The size of the capsule's spine along the specified        axis excluding the size of the two half spheres, i.e.
        the size of the cylinder portion of the capsule.
        If you author height you must also author extent.
        \\sa GetExtentAttr()
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    radius = Attribute(
        name = 'radius',
        as_type = 'double',
        value = 0.5,
        docstring = """,
        The radius of the capsule.  If you        author radius you must also author extent.
        \\sa GetExtentAttr()
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Cone(Prim):
    """
    Defines a primitive cone, centered at the origin, whose spine    is along the specified axis, with the apex of the cone pointing
    in the direction of the positive axis.
    The fallback values for Cube, Sphere, Cone, and Cylinder are set so that
    they all pack into the same volume/bounds.

    """

    as_type = "Cone"
    axis = Attribute(
        name = 'axis',
        as_type = 'token',
        value = "Z",
        is_uniform = True,
        allowedTokens = ["X", "Y", "Z"],
        docstring = """,
        The axis along which the spine of the cone is aligned
        """,

    )
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is re-defined on Cone only to provide a fallback        value. \\sa UsdGeomGprim::GetExtentAttr().
        """,

    )
    height = Attribute(
        name = 'height',
        as_type = 'double',
        value = 2,
        docstring = """,
        The size of the cone's spine along the specified        axis.  If you author height you must also author extent.
        \\sa GetExtentAttr()
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    radius = Attribute(
        name = 'radius',
        as_type = 'double',
        value = 1,
        docstring = """,
        The radius of the cone.  If you        author radius you must also author extent.
        \\sa GetExtentAttr()
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class PointBased(Prim):
    """
    Base class for all UsdGeomGprims that possess points,    providing common attributes such as normals and velocities.

    """

    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
        transform not applied), without accounting for any shader-induced
        displacement.  Whenever any geometry-affecting attribute is authored
        for any gprim in a layer, extent must also be authored at the same
        timesample; failure to do so will result in incorrect bounds-computation.
        \\sa \\ref UsdGeom_Boundable_Extent.
        An authored extent on a prim which has children is expected to include
        the extent of all children, as they will be pruned from BBox computation
        during traversal.
        Provide an object-space orientation for individual points,        which, depending on subclass, may define a surface, curve, or free
        points.  Note that 'normals' should not be authored on any Mesh that
        is subdivided, since the subdivision algorithm will define its own
        normals. 'normals' is not a generic primvar, but the number of elements
        in this attribute will be determined by its 'interpolation'.  See
        . If 'normals' and 'primvars:normals'
        are both specified, the latter has precedence.
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        The primary geometry attribute for all PointBased        primitives, describes points in (local) space.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        If provided, 'velocities' should be used by renderers to
        compute positions between samples for the 'points' attribute, rather
        than interpolating between neighboring 'points' samples.  This is the
        only reasonable means of computing motion blur for topologically
        varying PointBased primitives.  It follows that the length of each
        'velocities' sample must match the length of the corresponding
        'points' sample.  Velocity is measured in position units per second,
        as per most simulation software. To convert to position units per
        UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond().
        See also .
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Mesh(Prim):
    """
    Encodes a mesh surface whose definition and feature-set    will converge with that of OpenSubdiv, http://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html. Current exceptions/divergences include:
    1. Certain interpolation (\tag\) parameters not yet supported
    The vertex indices of all vertices that are sharp corners.The sharpness values for corners: each corner gets a single        sharpness value (Usd.Mesh.SHARPNESS_INFINITE for a perfectly sharp
    corner), so the size of this array must match that of
    'cornerIndices'
    The indices of all vertices forming creased edges.  The size of        this array must be equal to the sum of all elements of the
    'creaseLengths' attribute.
    The length of this array specifies the number of creases on the        surface. Each element gives the number of (must be adjacent) vertices in
    each crease, whose indices are linearly laid out in the 'creaseIndices'
    attribute. Since each crease must be at least one edge long, each
    element of this array should be greater than one.
    The per-crease or per-edge sharpness for all creases        (Usd.Mesh.SHARPNESS_INFINITE for a perfectly sharp crease).  Since
    'creaseLengths' encodes the number of vertices in each crease, the
    number of elements in this array will be either len(creaseLengths) or
    the sum over all X of (creaseLengths[X] - 1). Note that while
    the RI spec allows each crease to have either a single sharpness
    or a value per-edge, USD will encode either a single sharpness
    per crease on a mesh, or sharpnesses for all edges making up
    the creases on a mesh.

    """

    as_type = "Mesh"
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
        transform not applied), without accounting for any shader-induced
        displacement.  Whenever any geometry-affecting attribute is authored
        for any gprim in a layer, extent must also be authored at the same
        timesample; failure to do so will result in incorrect bounds-computation.
        \\sa \\ref UsdGeom_Boundable_Extent.
        An authored extent on a prim which has children is expected to include
        the extent of all children, as they will be pruned from BBox computation
        during traversal.
        """,

    )
    faceVaryingLinearInterpolation = Attribute(
        name = 'faceVaryingLinearInterpolation',
        as_type = 'token',
        value = "cornersPlus1",
        allowedTokens = ["all", "none", "boundaries", "cornersOnly", "cornersPlus1", "cornersPlus2"],
        docstring = """,
        Specifies how face varying data is interpolated.  Valid values        are "all" (no smoothing), "cornersPlus1" (the default, Smooth UV),
        "none" (Same as "cornersPlus1" but does not infer the presence
        of corners where two faceVarying edges meet at a single face), or
        "boundaries" (smooth only near vertices that are not at a
        discontinuous boundary).
        See http://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html#face-varying-interpolation-rules
        Provides the number of vertices in each face of the mesh,        which is also the number of consecutive indices in 'faceVertexIndices'
        that define the face.  The length of this attribute is the number of
        faces in the mesh.  If this attribute has more than
        one timeSample, the mesh is considered to be topologically varying.
        Flat list of the index (into the 'points' attribute) of each        vertex of each face in the mesh.  If this attribute has more than
        one timeSample, the mesh is considered to be topologically varying.
        The face indices (indexing into the 'faceVertexCounts'        attribute) of all faces that should be made invisible.
        """,

    )
    interpolateBoundary = Attribute(
        name = 'interpolateBoundary',
        as_type = 'token',
        value = "edgeAndCorner",
        allowedTokens = ["none", "edgeAndCorner", "edgeOnly"],
        docstring = """,
        Specifies how interpolation boundary face edges are        interpolated. Valid values are "none",
        "edgeAndCorner" (the default), or "edgeOnly".
        Provide an object-space orientation for individual points,        which, depending on subclass, may define a surface, curve, or free
        points.  Note that 'normals' should not be authored on any Mesh that
        is subdivided, since the subdivision algorithm will define its own
        normals. 'normals' is not a generic primvar, but the number of elements
        in this attribute will be determined by its 'interpolation'.  See
        . If 'normals' and 'primvars:normals'
        are both specified, the latter has precedence.
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        The primary geometry attribute for all PointBased        primitives, describes points in (local) space.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    subdivisionScheme = Attribute(
        name = 'subdivisionScheme',
        as_type = 'token',
        value = "catmullClark",
        is_uniform = True,
        allowedTokens = ["catmullClark", "loop", "bilinear", "none"],
        docstring = """,
        The subdivision scheme to be applied to the surface.        Valid values are "catmullClark" (the default), "loop", "bilinear", and
        "none" (i.e. a polymesh with no subdivision - the primary difference
        between schemes "bilinear" and "none" is that bilinearly subdivided
        meshes can be considered watertight, whereas there is no such guarantee
        for un-subdivided polymeshes, and more mesh features (e.g. holes) may
        apply to bilinear meshes but not polymeshes.  Polymeshes may be
        lighterweight and faster to render, depending on renderer and render
        mode.)
        """,

    )
    triangleSubdivisionRule = Attribute(
        name = 'triangleSubdivisionRule',
        as_type = 'token',
        value = "catmullClark",
        allowedTokens = ["catmullClark", "smooth"],
        docstring = """,
        Specifies what weights are used during triangle subdivision for        the Catmull-Clark scheme. Valid values are "catmullClark" (the default)
        and "smooth".
        See http://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html#triangle-subdivision-rule
        If provided, 'velocities' should be used by renderers to
        compute positions between samples for the 'points' attribute, rather
        than interpolating between neighboring 'points' samples.  This is the
        only reasonable means of computing motion blur for topologically
        varying PointBased primitives.  It follows that the length of each
        'velocities' sample must match the length of the corresponding
        'points' sample.  Velocity is measured in position units per second,
        as per most simulation software. To convert to position units per
        UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond().
        See also .
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class GeomSubset(Prim):
    """
    Encodes a subset of a piece of geometry (i.e. a UsdGeomImageable)    as a set of indices. Currently only supports encoding of face-subsets, but
    could be extended in the future to support subsets representing edges,
    segments, points etc.
    To apply to a geometric prim, a GeomSubset prim must be defined as a
    child of it in namespace. This restriction makes it easy and efficient
    to discover subsets of a prim. We might want to relax this restriction if
    it's common to have multiple <b>families</b> of subsets on a gprim and if
    it's useful to be able to organize subsets belonging to a </b>family</b>
    under a common scope. See 'familyName' attribute for more info on defining
    a family of subsets.
    Note that a GeomSubset isn't an imageable (i.e. doesn't derive from
    UsdGeomImageable). So, you can't author <b>visibility</b> for it or
    override its <b>purpose</b>.
    Materials are bound to GeomSubsets just as they are for regular
    geometry using API available in UsdShade (UsdShadeMaterial::Bind).

    """

    as_type = "GeomSubset"
    elementType = Attribute(
        name = 'elementType',
        as_type = 'token',
        value = "face",
        is_uniform = True,
        allowedTokens = ["face"],
        docstring = """,
        The type of element that the indices target. Currently only        allows "face" and defaults to it.
        """,

    )
    familyName = Attribute(
        name = 'familyName',
        as_type = 'token',
        value = "",
        is_uniform = True,
        docstring = """,
        The name of the family of subsets that this subset belongs to.        This is optional and is primarily useful when there are multiple
        families of subsets under a geometric prim. In some cases, this could
        also be used for achieving proper roundtripping of subset data between
        DCC apps.
        When multiple subsets belonging to a prim have the same familyName, they
        are said to belong to the family. A <i>familyType</i> value can be
        encoded on the owner of a family of subsets as a token using the static
        method UsdGeomSubset::SetFamilyType(). "familyType" can have one of the
        following values:
        <ul><li><b>UsdGeomTokens->partition</b>: implies that every element of
        the whole geometry appears exactly once in only one of the subsets
        belonging to the family.</li>
        <li><b>UsdGeomTokens->nonOverlapping</b>: an element that appears in one
        subset may not appear in any other subset belonging to the family.</li>
        <li><b>UsdGeomTokens->unrestricted</b>: implies that there are no
        restrictions w.r.t. the membership of elements in the subsets. They
        could be overlapping and the union of all subsets in the family may
        not represent the whole.</li>
        </ul>
        \\note The validity of subset data is not enforced by the authoring
        APIs, however they can be checked using UsdGeomSubset::ValidateFamily().
        The set of indices included in this subset. The indices need not        be sorted, but the same index should not appear more than once.
        """,

    )

class NurbsPatch(Prim):
    """
    Encodes a rational or polynomial non-uniform B-spline    surface, with optional trim curves.
    The encoding mostly follows that of RiNuPatch and RiTrimCurve:
    https://renderman.pixar.com/resources/current/RenderMan/geometricPrimitives.html#rinupatch , with some minor renaming and coalescing for clarity.
    The layout of control vertices in the points attribute inherited
    from UsdGeomPointBased is row-major with U considered rows, and V columns.
    \\anchor UsdGeom_NurbsPatch_Form
    <b>NurbsPatch Form</b>
    The authored points, orders, knots, weights, and ranges are all that is
    required to render the nurbs patch.  However, the only way to model closed
    surfaces with nurbs is to ensure that the first and last control points
    along the given axis are coincident.  Similarly, to ensure the surface is
    not only closed but also C2 continuous, the last order - 1 control
    points must be (correspondingly) coincident with the first order - 1
    control points, and also the spacing of the last corresponding knots
    must be the same as the first corresponding knots.
    <b>Form</b> is provided as an aid to interchange between modeling and
    animation applications so that they can robustly identify the intent with
    which the surface was modelled, and take measures (if they are able) to
    preserve the continuity/concidence constraints as the surface may be rigged
    or deformed.
    - An open-form NurbsPatch has no continuity constraints.
    - A closed-form NurbsPatch expects the first and last control points
    to overlap
    - A periodic-form NurbsPatch expects the first and last
    order - 1 control points to overlap.
    <b>Nurbs vs Subdivision Surfaces</b>
    Nurbs are an important modeling primitive in CAD/CAM tools and early
    computer graphics DCC's.  Because they have a natural UV parameterization
    they easily support \trim curves\, which allow smooth shapes to be

    """

    as_type = "NurbsPatch"
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
        transform not applied), without accounting for any shader-induced
        displacement.  Whenever any geometry-affecting attribute is authored
        for any gprim in a layer, extent must also be authored at the same
        timesample; failure to do so will result in incorrect bounds-computation.
        \\sa \\ref UsdGeom_Boundable_Extent.
        An authored extent on a prim which has children is expected to include
        the extent of all children, as they will be pruned from BBox computation
        during traversal.
        Provide an object-space orientation for individual points,        which, depending on subclass, may define a surface, curve, or free
        points.  Note that 'normals' should not be authored on any Mesh that
        is subdivided, since the subdivision algorithm will define its own
        normals. 'normals' is not a generic primvar, but the number of elements
        in this attribute will be determined by its 'interpolation'.  See
        . If 'normals' and 'primvars:normals'
        are both specified, the latter has precedence.
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        The primary geometry attribute for all PointBased        primitives, describes points in (local) space.
        Optionally provides \w\ components for each control point,        thus must be the same length as the points attribute.  If authored,
        the patch will be rational.  If unauthored, the patch will be
        polynomial, i.e. weight for all points is 1.0.
        \\note Some DCC's pre-weight the points, but in this schema,
        points are not pre-weighted.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        Each element specifies how many curves are present in each        "loop" of the trimCurve, and the length of the array determines how
        many loops the trimCurve contains.  The sum of all elements is the
        total nuber of curves in the trim, to which we will refer as
        nCurves in describing the other trim attributes.
        Flat list of parametric values for each of the        nCurves curves.  There will be as many knots as the sum over
        all elements of vertexCounts plus the sum over all elements of
        orders.
        Flat list of orders for each of the nCurves curves.Flat list of homogeneous 2D points (u, v, w) that comprise        the nCurves curves.  The number of points should be equal to the
        um over all elements of vertexCounts.
        Flat list of minimum and maximum parametric values        (as defined by knots) for each of the nCurves curves.
        Flat list of number of vertices for each of the         nCurves curves.
        """,

    )
    uForm = Attribute(
        name = 'uForm',
        as_type = 'token',
        value = "open",
        is_uniform = True,
        allowedTokens = ["open", "closed", "periodic"],
        docstring = """,
        Interpret the control grid and knot vectors as representing        an open, geometrically closed, or geometrically closed and C2 continuous
        surface along the U dimension.
        \\sa "NurbsPatch Form"
        Knot vector for U direction providing U parameterization.        The length of this array must be ( uVertexCount + uOrder ), and its
        entries must take on monotonically increasing values.
        """,

    )
    uOrder = Attribute(
        name = 'uOrder',
        as_type = 'int',
        docstring = """,
        Order in the U direction.  Order must be positive and is        equal to the degree of the polynomial basis to be evaluated, plus 1.
        """,

    )
    uRange = Attribute(
        name = 'uRange',
        as_type = 'double2',
        docstring = """,
        Provides the minimum and maximum parametric values (as defined        by uKnots) over which the surface is actually defined.  The minimum
        must be less than the maximum, and greater than or equal to the
        value of uKnots[uOrder-1].  The maxium must be less than or equal
        to the last element's value in uKnots.
        """,

    )
    uVertexCount = Attribute(
        name = 'uVertexCount',
        as_type = 'int',
        docstring = """,
        Number of vertices in the U direction.  Should be at least as        large as uOrder.
        If provided, 'velocities' should be used by renderers to
        compute positions between samples for the 'points' attribute, rather
        than interpolating between neighboring 'points' samples.  This is the
        only reasonable means of computing motion blur for topologically
        varying PointBased primitives.  It follows that the length of each
        'velocities' sample must match the length of the corresponding
        'points' sample.  Velocity is measured in position units per second,
        as per most simulation software. To convert to position units per
        UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond().
        See also .
        """,

    )
    vForm = Attribute(
        name = 'vForm',
        as_type = 'token',
        value = "open",
        is_uniform = True,
        allowedTokens = ["open", "closed", "periodic"],
        docstring = """,
        Interpret the control grid and knot vectors as representing        an open, geometrically closed, or geometrically closed and C2 continuous
        surface along the V dimension.
        \\sa "NurbsPatch Form"
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        Knot vector for V direction providing U parameterization.        The length of this array must be ( vVertexCount + vOrder ), and its
        entries must take on monotonically increasing values.
        """,

    )
    vOrder = Attribute(
        name = 'vOrder',
        as_type = 'int',
        docstring = """,
        Order in the V direction.  Order must be positive and is        equal to the degree of the polynomial basis to be evaluated, plus 1.
        """,

    )
    vRange = Attribute(
        name = 'vRange',
        as_type = 'double2',
        docstring = """,
        Provides the minimum and maximum parametric values (as defined        by vKnots) over which the surface is actually defined.  The minimum
        must be less than the maximum, and greater than or equal to the
        value of vKnots[vOrder-1].  The maxium must be less than or equal
        to the last element's value in vKnots.
        """,

    )
    vVertexCount = Attribute(
        name = 'vVertexCount',
        as_type = 'int',
        docstring = """,
        Number of vertices in the V direction.  Should be at least as        large as vOrder.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Curves(Prim):
    """
    Base class for BasisCurves and NurbsCurves.  The BasisCurves             schema is designed to be analagous to offline renderers' notion
    of batched curves (such as the classical RIB definition via
    Basis and Curves statements), while the NurbsCurve schema
    is designed to be analgous to the NURBS curves found in packages
    like Maya and Houdini while retaining their consistency with the
    RenderMan specification for NURBS Patches.
    Curves-derived primitives can represent multiple distinct,        potentially disconnected curves.  The length of 'curveVertexCounts'
    gives the number of such curves, and each element describes the
    number of vertices in the corresponding curve

    """

    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
        transform not applied), without accounting for any shader-induced
        displacement.  Whenever any geometry-affecting attribute is authored
        for any gprim in a layer, extent must also be authored at the same
        timesample; failure to do so will result in incorrect bounds-computation.
        \\sa \\ref UsdGeom_Boundable_Extent.
        An authored extent on a prim which has children is expected to include
        the extent of all children, as they will be pruned from BBox computation
        during traversal.
        Provide an object-space orientation for individual points,        which, depending on subclass, may define a surface, curve, or free
        points.  Note that 'normals' should not be authored on any Mesh that
        is subdivided, since the subdivision algorithm will define its own
        normals. 'normals' is not a generic primvar, but the number of elements
        in this attribute will be determined by its 'interpolation'.  See
        . If 'normals' and 'primvars:normals'
        are both specified, the latter has precedence.
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        The primary geometry attribute for all PointBased        primitives, describes points in (local) space.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        If provided, 'velocities' should be used by renderers to
        compute positions between samples for the 'points' attribute, rather
        than interpolating between neighboring 'points' samples.  This is the
        only reasonable means of computing motion blur for topologically
        varying PointBased primitives.  It follows that the length of each
        'velocities' sample must match the length of the corresponding
        'points' sample.  Velocity is measured in position units per second,
        as per most simulation software. To convert to position units per
        UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond().
        See also .
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        Provides width specification for the curves, whose application        will depend on whether the curve is oriented (normals are defined for
        it), in which case widths are \ribbon width\, or unoriented, in which
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class BasisCurves(Prim):
    """
    BasisCurves are a batched curve representation analogous to the    classic RIB definition via Basis and Curves statements. BasisCurves are
    often used to render dense aggregate geometry like hair or grass.
    A 'matrix' and 'vstep' associated with the basis are used to
    interpolate the vertices of a cubic BasisCurves. (The basis attribute
    is unused for linear BasisCurves.)
    A single prim may have many curves whose count is determined implicitly by
    the length of the curveVertexCounts vector.  Each individual curve is
    composed of one or more segments. Each segment is defined by four vertices
    for cubic curves and two vertices for linear curves. See the next section
    for more information on how to map curve vertex counts to segment counts.
    Segment Indexing
    Interpolating a curve requires knowing how to decompose it into its
    individual segments.
    The segments of a cubic curve are determined by the vertex count,
    the wrap (periodicity), and the vstep of the basis. For linear
    curves, the basis token is ignored and only the vertex count and
    wrap are needed.
    cubic basis   | vstep
    ------------- | ------
    bezier        | 3
    catmullRom    | 1
    bspline       | 1
    hermite       | 2
    power         | 4
    The first segment of a cubic (nonperiodic) curve is always defined by its
    first four points. The vstep is the increment used to determine what
    vertex indices define the next segment.  For a two segment (nonperiodic)
    bspline basis curve (vstep = 1), the first segment will be defined by
    interpolating vertices [0, 1, 2, 3] and the second segment will be defined
    by [1, 2, 3, 4].  For a two segment bezier basis curve (vstep = 3), the
    first segment will be defined by interpolating vertices [0, 1, 2, 3] and
    the second segment will be defined by [3, 4, 5, 6].  If the vstep is not
    one, then you must take special care to make sure that the number of cvs
    properly divides by your vstep. (The indices described are relative to
    the initial vertex index for a batched curve.)
    For periodic curves, at least one of the curves' initial vertices are
    repeated to close the curve.
    (TODO: Explain the rules for how to repeat vertices for periodic curves.)
    Linear curve segments are defined by two vertices.
    A two segment linear curve's first segment would be defined by
    interpolating vertices [0, 1]. The second segment would be defined by
    vertices [1, 2]. (Again, for a batched curve indices are relative to
    the initial vertex index.)
    When validating curve topology, each renderable entry in the
    curveVertexCounts vector must pass this check.
    type    | wrap           | validitity
    ------- | -------------- | ----------------
    linear  | nonperiodic    | curveVertexCounts[i] > 2
    linear  | periodic       | curveVertexCounts[i] > 3
    cubic   | nonperiodic    | (curveVertexCounts[i] - 4) % vstep == 0
    cubic   | periodic       | (curveVertexCounts[i]) % vstep == 0
    Cubic Vertex Interpolation
    \\image html USDCurveBasisMatrix.png width=750
    Linear Vertex Interpolation
    Linear interpolation is always used on curves of type linear.
    't' with domain [0, 1], the curve is defined by the equation
    P0 * (1-t) + P1 * t. t at 0 describes the first point and t at 1 describes
    the end point.
    Primvar Interpolation
    For cubic curves, primvar data can be either interpolated cubically between
    vertices or linearly across segments.  The corresponding token
    for cubic interpolation is 'vertex' and for linear interpolation is
    'varying'.  Per vertex data should be the same size as the number
    of vertices in your curve.  Segment varying data is dependent on the
    wrap (periodicity) and number of segments in your curve.  For linear curves,
    varying and vertex data would be interpolated the same way.  By convention
    varying is the preferred interpolation because of the association of
    varying with linear interpolation.
    \\image html USDCurvePrimvars.png
    To convert an entry in the curveVertexCounts vector into a segment count
    for an individual curve, apply these rules.  Sum up all the results in
    order to compute how many total segments all curves have.
    The following tables describe the expected segment count for the 'i'th
    curve in a curve batch as well as the entire batch. Python syntax
    like '[:]' (to describe all members of an array) and 'len(...)'
    (to describe the length of an array) are used.
    type    | wrap          | curve segment count                    | batch segment count
    ------- | ------------- | -------------------------------------- | --------------------------
    linear  | nonperiodic   | curveVertexCounts[i] - 1               | sum(curveVertexCounts[:]) - len(curveVertexCounts)
    linear  | periodic      | curveVertexCounts[i]                   | sum(curveVertexCounts[:])
    cubic   | nonperiodic   | (curveVertexCounts[i] - 4) / vstep + 1 | sum(curveVertexCounts[:] - 4) / vstep + len(curveVertexCounts)
    cubic   | periodic      | curveVertexCounts[i] / vstep           | sum(curveVertexCounts[:]) / vstep
    The following table descrives the expected size of varying
    (linearly interpolated) data, derived from the segment counts computed
    above.
    wrap          | curve varying count          | batch varying count
    ------------- | ---------------------------- | ------------------------------------------------
    nonperiodic   | segmentCounts[i] + 1         | sum(segmentCounts[:]) + len(curveVertexCounts)
    periodic      | segmentCounts[i]             | sum(segmentCounts[:])
    Both curve types additionally define 'constant' interpolation for the
    entire prim and 'uniform' interpolation as per curve data.
    \\note Take care when providing support for linearly interpolated data for
    cubic curves. Its shape doesn't provide a one to one mapping with either
    the number of curves (like 'uniform') or the number of vertices (like
    'vertex') and so it is often overlooked. This is the only primitive in
    UsdGeom (as of this writing) where this is true. For meshes, while they
    use different interpolation methods, 'varying' and 'vertex' are both
    specified per point. It's common to assume that curves follow a similar
    pattern and build in structures and language for per primitive, per
    element, and per point data only to come upon these arrays that don't
    quite fit into either of those categories. It is
    also common to conflate 'varying' with being per segment data and use the
    segmentCount rules table instead of its neighboring varying data table
    rules. We suspect that this is because for the common case of
    nonperiodic cubic curves, both the provided segment count and varying data
    size formula end with '+ 1'. While debugging, users may look at the double
    '+ 1' as a mistake and try to remove it.  We take this time to enumerate
    these issues because we've fallen into them before and hope that we save
    others time in their own implementations.
    As an example of deriving per curve segment and varying primvar data counts from
    the wrap, type, basis, and curveVertexCount, the following table is provided.
    wrap          | type    | basis   | curveVertexCount  | curveSegmentCount  | varyingDataCount
    ------------- | ------- | ------- | ----------------- | ------------------ | -------------------------
    nonperiodic   | linear  | N/A     | [2 3 2 5]         | [1 2 1 4]          | [2 3 2 5]
    nonperiodic   | cubic   | bezier  | [4 7 10 4 7]      | [1 2 3 1 2]        | [2 3 4 2 3]
    nonperiodic   | cubic   | bspline | [5 4 6 7]         | [2 1 3 4]          | [3 2 4 5]
    periodic      | cubic   | bezier  | [6 9 6]           | [2 3 2]            | [2 3 2]
    periodic      | linear  | N/A     | [3 7]             | [3 7]              | [3 7]
    Tubes and Ribbons
    The strictest definition of a curve as an infinitely thin wire is not
    particularly useful for describing production scenes. The additional
    widths and normals attributes can be used to describe cylindrical
    tubes and or flat oriented ribbons.
    Curves with only widths defined are imaged as tubes with radius
    'width / 2'. Curves with both widths and normals are imaged as ribbons
    oriented in the direction of the interpolated normal vectors.
    While not technically UsdGeomPrimvars, widths and normals
    also have interpolation metadata. It's common for authored widths to have
    constant, varying, or vertex interpolation
    (see UsdGeomCurves::GetWidthsInterpolation()).  It's common for
    authored normals to have varying interpolation
    (see UsdGeomPointBased::GetNormalsInterpolation()).
    \\image html USDCurveHydra.png
    The file used to generate these curves can be found in
    pxr/extras/examples/usdGeomExamples/basisCurves.usda.  It's provided
    as a reference on how to properly image both tubes and ribbons. The first
    row of curves are linear; the second are cubic bezier. (We aim in future
    releases of HdSt to fix the discontinuity seen with broken tangents to
    better match offline renderers like RenderMan.) The yellow and violet
    cubic curves represent cubic vertex width interpolation for which there is
    no equivalent for linear curves.
    \\note How did this prim type get its name?  This prim is a portmanteau of
    two different statements in the original RenderMan specification:
    'Basis' and 'Curves'.

    """

    as_type = "BasisCurves"
    basis = Attribute(
        name = 'basis',
        as_type = 'token',
        value = "bezier",
        is_uniform = True,
        allowedTokens = ["bezier", "bspline", "catmullRom", "hermite", "power"],
        docstring = """,
        The basis specifies the vstep and matrix used for cubic interpolation.Curves-derived primitives can represent multiple distinct,        potentially disconnected curves.  The length of 'curveVertexCounts'
        gives the number of such curves, and each element describes the
        number of vertices in the corresponding curve
        """,

    )
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
        transform not applied), without accounting for any shader-induced
        displacement.  Whenever any geometry-affecting attribute is authored
        for any gprim in a layer, extent must also be authored at the same
        timesample; failure to do so will result in incorrect bounds-computation.
        \\sa \\ref UsdGeom_Boundable_Extent.
        An authored extent on a prim which has children is expected to include
        the extent of all children, as they will be pruned from BBox computation
        during traversal.
        Provide an object-space orientation for individual points,        which, depending on subclass, may define a surface, curve, or free
        points.  Note that 'normals' should not be authored on any Mesh that
        is subdivided, since the subdivision algorithm will define its own
        normals. 'normals' is not a generic primvar, but the number of elements
        in this attribute will be determined by its 'interpolation'.  See
        . If 'normals' and 'primvars:normals'
        are both specified, the latter has precedence.
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        The primary geometry attribute for all PointBased        primitives, describes points in (local) space.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    type_ = Attribute(
        name = 'type',
        as_type = 'token',
        value = "cubic",
        is_uniform = True,
        allowedTokens = ["linear", "cubic"],
        docstring = """,
        Linear curves interpolate linearly between two vertices.        Cubic curves use a basis matrix with four vertices to interpolate a segment.
        If provided, 'velocities' should be used by renderers to
        compute positions between samples for the 'points' attribute, rather
        than interpolating between neighboring 'points' samples.  This is the
        only reasonable means of computing motion blur for topologically
        varying PointBased primitives.  It follows that the length of each
        'velocities' sample must match the length of the corresponding
        'points' sample.  Velocity is measured in position units per second,
        as per most simulation software. To convert to position units per
        UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond().
        See also .
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        Provides width specification for the curves, whose application        will depend on whether the curve is oriented (normals are defined for
        it), in which case widths are \ribbon width\, or unoriented, in which
        """,

    )
    wrap = Attribute(
        name = 'wrap',
        as_type = 'token',
        value = "nonperiodic",
        is_uniform = True,
        allowedTokens = ["nonperiodic", "periodic"],
        docstring = """,
        If wrap is set to periodic, the curve when rendered will        repeat the initial vertices (dependent on the vstep) to close the
        curve.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class NurbsCurves(Prim):
    """
    This schema is analagous to NURBS Curves in packages like Maya    and Houdini, often used for interchange of rigging and modeling curves.
    Unlike Maya, this curve spec supports batching of multiple curves into a
    single prim, widths, and normals in the schema.  Additionally, we require
    'numSegments + 2 * degree + 1' knots (2 more than maya does).  This is to
    be more consistent with RenderMan's NURBS patch specification.
    To express a periodic curve:
    - knot[0] = knot[1] - (knots[-2] - knots[-3];
    - knot[-1] = knot[-2] + (knot[2] - knots[1]);
    To express a nonperiodic curve:
    - knot[0] = knot[1];
    - knot[-1] = knot[-2];
    In spite of these slight differences in the spec, curves generated in Maya
    should be preserved when roundtripping.
    order and range, when representing a batched NurbsCurve should be
    authored one value per curve.  knots should be the concatentation of
    all batched curves.
    Curves-derived primitives can represent multiple distinct,        potentially disconnected curves.  The length of 'curveVertexCounts'
    gives the number of such curves, and each element describes the
    number of vertices in the corresponding curve

    """

    as_type = "NurbsCurves"
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
        transform not applied), without accounting for any shader-induced
        displacement.  Whenever any geometry-affecting attribute is authored
        for any gprim in a layer, extent must also be authored at the same
        timesample; failure to do so will result in incorrect bounds-computation.
        \\sa \\ref UsdGeom_Boundable_Extent.
        An authored extent on a prim which has children is expected to include
        the extent of all children, as they will be pruned from BBox computation
        during traversal.
        Knot vector providing curve parameterization.        The length of the slice of the array for the ith curve
        must be ( curveVertexCount[i] + order[i] ), and its
        entries must take on monotonically increasing values.
        Provide an object-space orientation for individual points,        which, depending on subclass, may define a surface, curve, or free
        points.  Note that 'normals' should not be authored on any Mesh that
        is subdivided, since the subdivision algorithm will define its own
        normals. 'normals' is not a generic primvar, but the number of elements
        in this attribute will be determined by its 'interpolation'.  See
        . If 'normals' and 'primvars:normals'
        are both specified, the latter has precedence.
        Order of the curve.  Order must be positive and is        equal to the degree of the polynomial basis to be evaluated, plus 1.
        Its value for the 'i'th curve must be less than or equal to
        curveVertexCount[i]
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        The primary geometry attribute for all PointBased        primitives, describes points in (local) space.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        Provides the minimum and maximum parametric values (as defined        by knots) over which the curve is actually defined.  The minimum must
        be less than the maximum, and greater than or equal to the value of the
        knots['i'th curve slice][order[i]-1]. The maxium must be less
        than or equal to the last element's value in knots['i'th curve slice].
        \tRange maps to (vmin, vmax) in the RenderMan spec.
        If provided, 'velocities' should be used by renderers to
        compute positions between samples for the 'points' attribute, rather
        than interpolating between neighboring 'points' samples.  This is the
        only reasonable means of computing motion blur for topologically
        varying PointBased primitives.  It follows that the length of each
        'velocities' sample must match the length of the corresponding
        'points' sample.  Velocity is measured in position units per second,
        as per most simulation software. To convert to position units per
        UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond().
        See also .
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        Provides width specification for the curves, whose application        will depend on whether the curve is oriented (normals are defined for
        it), in which case widths are \ribbon width\, or unoriented, in which
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Points(Prim):
    """
    Points are analogous to the <A HREF=\https://renderman.pixar.com/resources/current/RenderMan/appnote.18.html\>RiPoints spec</A>.
    Points can be an efficient means of storing and rendering particle
    effects comprised of thousands or millions of small particles.  Points
    generally receive a single shading sample each, which should take
    normals into account, if present.
    While not technically UsdGeomPrimvars, the widths and normals also
    have interpolation metadata.  It's common for authored widths and normals
    to have constant or varying interpolation.

    """

    as_type = "Points"
    doubleSided = Attribute(
        name = 'doubleSided',
        as_type = 'bool',
        value = 0,
        is_uniform = True,
        docstring = """,
        Although some renderers treat all parametric or polygonal        surfaces as if they were effectively laminae with outward-facing
        normals on both sides, some renderers derive significant optimizations
        by considering these surfaces to have only a single outward side,
        typically determined by control-point winding order and/or
        orientation.  By doing so they can perform \backface culling\ to
        """,

    )
    culling = Attribute(
        name = 'culling',
        as_type = 'backface',
        docstring = """,
        Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
        transform not applied), without accounting for any shader-induced
        displacement.  Whenever any geometry-affecting attribute is authored
        for any gprim in a layer, extent must also be authored at the same
        timesample; failure to do so will result in incorrect bounds-computation.
        \\sa \\ref UsdGeom_Boundable_Extent.
        An authored extent on a prim which has children is expected to include
        the extent of all children, as they will be pruned from BBox computation
        during traversal.
        Ids are optional; if authored, the ids array should be the same                 length as the points array, specifying (at each timesample if
        point identities are changing) the id of each point. The
        type is signed intentionally, so that clients can encode some
        binary state on Id'd points without adding a separate
        primvar.
        Provide an object-space orientation for individual points,        which, depending on subclass, may define a surface, curve, or free
        points.  Note that 'normals' should not be authored on any Mesh that
        is subdivided, since the subdivision algorithm will define its own
        normals. 'normals' is not a generic primvar, but the number of elements
        in this attribute will be determined by its 'interpolation'.  See
        . If 'normals' and 'primvars:normals'
        are both specified, the latter has precedence.
        """,

    )
    orientation = Attribute(
        name = 'orientation',
        as_type = 'token',
        value = "rightHanded",
        is_uniform = True,
        allowedTokens = ["rightHanded", "leftHanded"],
        docstring = """,
        Orientation specifies whether the gprim's surface normal        should be computed using the right hand rule, or the left hand rule.
        Please see for a deeper explanation and
        generalization of orientation to composed scenes with transformation
        hierarchies.
        The primary geometry attribute for all PointBased        primitives, describes points in (local) space.
        It is useful to have an "official" colorSet that can be used        as a display or modeling color, even in the absence of any specified
        shader for a gprim.  DisplayColor serves this role; because it is a
        UsdGeomPrimvar, it can also be used as a gprim override for any shader
        that consumes a displayColor parameter.
        Companion to displayColor that specifies opacity, broken        out as an independent attribute rather than an rgba color, both so that
        each can be independently overridden, and because shaders rarely consume
        rgba parameters.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        If provided, 'velocities' should be used by renderers to
        compute positions between samples for the 'points' attribute, rather
        than interpolating between neighboring 'points' samples.  This is the
        only reasonable means of computing motion blur for topologically
        varying PointBased primitives.  It follows that the length of each
        'velocities' sample must match the length of the corresponding
        'points' sample.  Velocity is measured in position units per second,
        as per most simulation software. To convert to position units per
        UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond().
        See also .
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        Widths are defined as the diameter of the points, in                 object space.  'widths' is not a generic Primvar, but
        the number of elements in this attribute will be determined by
        its 'interpolation'.  See .  If
        'widths' and 'primvars:widths' are both specified, the latter
        has precedence.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class PointInstancer(Prim):
    """
    Encodes vectorized instancing of multiple, potentially    animated, prototypes (object/instance masters), which can be arbitrary
    prims/subtrees on a UsdStage.
    PointInstancer is a \multi instancer\, as it allows multiple prototypes
    If authored, per-instance angular velocity vector to be used for      interoplating orientations.  Angular velocities should be considered
    mandatory if both protoIndices and orientations are animated.
    Angular velocity is measured in <b>degrees</b> per second. To convert
    to degrees per UsdTimeCode, divide by
    UsdStage::GetTimeCodesPerSecond().
    See also .
    Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
    transform not applied), without accounting for any shader-induced
    displacement.  Whenever any geometry-affecting attribute is authored
    for any gprim in a layer, extent must also be authored at the same
    timesample; failure to do so will result in incorrect bounds-computation.
    \\sa \\ref UsdGeom_Boundable_Extent.
    An authored extent on a prim which has children is expected to include
    the extent of all children, as they will be pruned from BBox computation
    during traversal.
    Ids are optional; if authored, the ids array should be the same      length as the protoIndices array, specifying (at each timeSample if
    instance identities are changing) the id of each instance. The
    type is signed intentionally, so that clients can encode some
    binary state on Id'd instances without adding a separate primvar.
    See also \\ref UsdGeomPointInstancer_varyingTopo
    A list of id's to make invisible at the evaluation time.      See .
    If authored, per-instance orientation of each instance about its      prototype's origin, represented as a unit length quaternion, which
    allows us to encode it with sufficient precision in a compact GfQuath.
    It is client's responsibility to ensure that authored quaternions are
    unit length; the convenience API below for authoring orientations from
    rotation matrices will ensure that quaternions are unit length, though
    it will not make any attempt to select the \better (for interpolation
    <b>Required property</b>. Per-instance position.  See also      .
    <b>Required property</b>. Per-instance index into      prototypes relationship that identifies what geometry should be
    drawn for each instance.  <b>Topology attribute</b> - can be animated,
    but at a potential performance impact for streaming.

    """

    as_type = "PointInstancer"
    prototypes = Attribute(
        name = 'prototypes',
        as_type = 'rel',
        docstring = """,
        <b>Required property</b>. Orders and targets the prototype root      prims, which can be located anywhere in the scenegraph that is convenient,
        although we promote organizing prototypes as children of the
        PointInstancer.  The position of a prototype in this relationship defines
        the value an instance would specify in the protoIndices attribute to
        instance that prototype. Since relationships are uniform, this property
        cannot be animated.
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        If authored, per-instance scale to be applied to      each instance, before any rotation is applied.
        See also .
        If provided, per-instance 'velocities' will be used to       compute positions between samples for the 'positions' attribute,
        rather than interpolating between neighboring 'positions' samples.
        Velocities should be considered mandatory if both protoIndices
        and positions are animated.  Velocity is measured in position
        units per second, as per most simulation software. To convert to
        position units per UsdTimeCode, divide by
        UsdStage::GetTimeCodesPerSecond().
        See also
        .
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class Camera(Prim):
    """
    Transformable camera.
    Describes optical properties of a camera via a common set of attributes
    that provide control over the camera's frustum as well as its depth of
    field. For stereo, the left and right camera are individual prims tagged
    through the \stereoRole attribute\.
    Additional, arbitrarily oriented clipping planes.                 A vector (a,b,c,d) encodes a clipping plane that cuts off
    (x,y,z) with a * x + b * y + c * z + d * 1 < 0 where (x,y,z)
    are the coordinates in the camera's space.

    """

    as_type = "Camera"
    clippingRange = Attribute(
        name = 'clippingRange',
        as_type = 'float2',
        value = (1, 1000000),
        docstring = """,
        Near and far clipping distances in centimeters (or, more                 general, world units).
        """,

    )
    focalLength = Attribute(
        name = 'focalLength',
        as_type = 'float',
        value = 50,
        docstring = """,
        Perspective focal length in millimeters (or, more general,                 tenths of a world unit).
        """,

    )
    focusDistance = Attribute(
        name = 'focusDistance',
        as_type = 'float',
        value = 0,
        docstring = """,
        Distance from the camera to the focus plane in centimeters (or                 more general, world units).
        """,

    )
    fStop = Attribute(
        name = 'fStop',
        as_type = 'float',
        value = 0,
        docstring = """,
        Lens aperture. Defaults to 0.0, which turns off focusing.
        """,

    )
    horizontalAperture = Attribute(
        name = 'horizontalAperture',
        as_type = 'float',
        value = 20.955,
        docstring = """,
        Horizontal aperture in millimeters (or, more general, tenths                 of a world unit).
        Defaults to the standard 35mm spherical projector aperture.
        """,

    )
    horizontalApertureOffset = Attribute(
        name = 'horizontalApertureOffset',
        as_type = 'float',
        value = 0,
        docstring = """,
        Horizontal aperture offset in the same units as                 horizontalAperture. Defaults to 0.
        """,

    )
    projection = Attribute(
        name = 'projection',
        as_type = 'token',
        value = "perspective",
        allowedTokens = ["perspective", "orthographic"],
        docstring = """,
        """,

    )
    proxyPrim = Attribute(
        name = 'proxyPrim',
        as_type = 'rel',
        docstring = """,
        The proxyPrim relationship allows us to link a        prim whose purpose is "render" to its (single target)
        purpose="proxy" prim.  This is entirely optional, but can be
        useful in several scenarios:
        - In a pipeline that does pruning (for complexity management)
        by deactivating prims composed from asset references, when we
        deactivate a purpose="render" prim, we will be able to discover
        and additionally deactivate its associated purpose="proxy" prim,
        so that preview renders reflect the pruning accurately.
        - DCC importers may be able to make more aggressive optimizations
        for interactive processing and display if they can discover the proxy
        for a given render prim.
        - With a little more work, a Hydra-based application will be able
        to map a picked proxy prim back to its render geometry for selection.
        \\note It is only valid to author the proxyPrim relationship on
        prims whose purpose is "render".
        """,

    )
    purpose = Attribute(
        name = 'purpose',
        as_type = 'token',
        value = "default",
        is_uniform = True,
        allowedTokens = ["default", "render", "proxy", "guide"],
        docstring = """,
        Purpose is a concept we have found useful in our pipeline for        classifying geometry into categories that can each be independently
        included or excluded from traversals of prims on a stage, such as
        rendering or bounding-box computation traversals.  The fallback
        purpose, default indicates that a prim has "no special purpose"
        and should generally be included in all traversals.  Subtrees rooted
        at a prim with purpose render should generally only be included
        when performing a "final quality" render.  Subtrees rooted at a prim
        with purpose proxy should generally only be included when
        performing a lightweight proxy render (such as openGL).  Finally,
        subtrees rooted at a prim with purpose guide should generally
        only be included when an interactive application has been explicitly
        asked to "show guides".
        In the previous paragraph, when we say "subtrees rooted at a prim",
        we mean the most ancestral or tallest subtree that has an authored,
        non-default opinion.  If the purpose of </RootPrim> is set to
        "render", then the effective purpose of </RootPrim/ChildPrim> will
        be "render" even if that prim has a different authored value for
        purpose.  <b>See ComputePurpose() for details of how purpose
        inherits down namespace</b>.
        As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
        accept combinations of included purposes as an input.
        Purpose render can be useful in creating "light blocker"
        geometry for raytracing interior scenes.  Purposes render and
        proxy can be used together to partition a complicated model
        into a lightweight proxy representation for interactive use, and a
        fully realized, potentially quite heavy, representation for rendering.
        One can use UsdVariantSets to create proxy representations, but doing
        so requires that we recompose parts of the UsdStage in order to change
        to a different runtime level of detail, and that does not interact
        well with the needs of multithreaded rendering. Purpose provides us with
        a better tool for dynamic, interactive complexity management.
        """,

    )
    close = Attribute(
        name = 'shutter:close',
        as_type = 'double',
        value = 0,
        docstring = """,
        Frame relative shutter close time, analogous comments from                 shutter:open apply. A value greater or equal to shutter:open
        should be authored, otherwise there is no exposure and a
        renderer should produce a black image.
        """,

    )
    open_ = Attribute(
        name = 'shutter:open',
        as_type = 'double',
        value = 0,
        docstring = """,
        Frame relative shutter open time in UsdTimeCode units (negative                 value indicates that the shutter opens before the current
        frame time). Used for motion blur.
        """,

    )
    stereoRole = Attribute(
        name = 'stereoRole',
        as_type = 'token',
        value = "mono",
        is_uniform = True,
        allowedTokens = ["mono", "left", "right"],
        docstring = """,
        If different from mono, the camera is intended to be the left                 or right camera of a stereo setup.
        """,

    )
    verticalAperture = Attribute(
        name = 'verticalAperture',
        as_type = 'float',
        value = 15.2908,
        docstring = """,
        Vertical aperture in millimeters (or, more general, tenths of                 a world unit).
        Defaults to the standard 35mm spherical projector aperture.
        """,

    )
    verticalApertureOffset = Attribute(
        name = 'verticalApertureOffset',
        as_type = 'float',
        value = 0,
        docstring = """,
        Vertical aperture offset in the same units as                 verticalAperture. Defaults to 0.
        """,

    )
    visibility = Attribute(
        name = 'visibility',
        as_type = 'token',
        value = "inherited",
        allowedTokens = ["inherited", "invisible"],
        docstring = """,
        Visibility is meant to be the simplest form of "pruning"        visibility that is supported by most DCC apps.  Visibility is
        animatable, allowing a sub-tree of geometry to be present for some
        segment of a shot, and absent from others; unlike the action of
        deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Encodes the sequence of transformation operations in the        order in which they should be pushed onto a transform stack while
        visiting a UsdStage's prims in a graph traversal that will effect
        the desired positioning for this prim and its descendant prims.
        You should rarely, if ever, need to manipulate this attribute directly.
        It is managed by the AddXformOp(), SetResetXformStack(), and
        SetXformOpOrder(), and consulted by GetOrderedXformOps() and
        GetLocalTransformation().
        """,

    )

class GeomModelAPI(Prim):
    """
    UsdGeomModelAPI extends the generic UsdModelAPI schema with    geometry specific concepts such as cached extents for the entire model,
    constraint targets, and geometry-inspired extensions to the payload
    lofting process.
    As described in GetExtentsHint() below, it is useful to cache extents
    at the model level.  UsdGeomModelAPI provides schema for computing and
    storing these cached extents, which can be consumed by UsdGeomBBoxCache to
    provide fast access to precomputed extents that will be used as the model's
    bounds ( see UsdGeomBBoxCache::UsdGeomBBoxCache() ).
    Draw Modes
    Draw modes provide optional alternate imaging behavior for USD subtrees with
    kind model. model:drawMode (which is inheritable) and
    model:applyDrawMode (which is not) are resolved into a decision to stop
    traversing the scene graph at a certain point, and replace a USD subtree
    with proxy geometry.
    The value of model:drawMode determines the type of proxy geometry:
    - origin - Draw the model-space basis vectors of the replaced prim.
    - bounds - Draw the model-space bounding box of the replaced prim.
    - cards - Draw textured quads as a placeholder for the replaced prim.
    - default - An explicit opinion to draw the USD subtree as normal.
    model:drawMode is inheritable so that a whole scene, a large group, or
    all prototypes of a model hierarchy PointInstancer can be assigned a draw
    mode with a single attribute edit.  model:applyDrawMode is meant to be
    written when an asset is authored, and provides flexibility for different
    asset types. For example, a character assembly (composed of character,
    clothes, etc) might have model:applyDrawMode set at the top of the
    subtree so the whole group can be drawn as a single card object. An effects
    subtree might have model:applyDrawMode set at a lower level so each
    particle group draws individually.
    Models of kind component are treated as if model:applyDrawMode
    were true.  This means a prim is drawn with proxy geometry when: the
    prim has kind component, and/or model:applyDrawMode is set; and
    the prim or an ancestor has a non-default value for model:drawMode.
    A value for model:drawMode on a child prim takes precedence over a
    value on a parent prim.
    Cards Geometry
    The specific geometry used in cards mode is controlled by the
    model:cardGeometry attribute:
    - cross - Generate a quad normal to each basis direction and negative.
    Locate each quad so that it bisects the model extents.
    - box   - Generate a quad normal to each basis direction and negative.
    Locate each quad on a face of the model extents, facing out.
    - fromTexture - Generate a quad for each supplied texture from
    attributes stored in that texture's metadata.
    For cross and box mode, the extents are calculated for purposes
    default, proxy, and render, at their earliest authored time.
    If the model has no textures, all six card faces are rendered using
    model:drawModeColor. If one or more textures are present, only axes
    with one or more textures assigned are drawn.  For each axis, if both
    textures (positive and negative) are specified, they'll be used on the
    corresponding card faces; if only one texture is specified, it will be
    mapped to the opposite card face after being flipped on the texture's
    s-axis. Any card faces with invalid asset paths will be drawn with
    model:drawModeColor.
    Both model:cardGeometry and model:drawModeColor should be
    authored on the prim where the draw mode takes effect, since these
    attributes are not inherited.
    For fromTexture mode, only card faces with valid textures assigned
    are drawn. The geometry is generated by pulling the worldtoscreen
    attribute out of texture metadata.  This is expected to be a 4x4 matrix
    mapping the model-space position of the card quad to the clip-space quad
    with corners (-1,-1,0) and (1,1,0).  The card vertices are generated by
    transforming the clip-space corners by the inverse of worldtoscreen.
    Textures are mapped so that (s) and (t) map to (+x) and (+y) in clip space.
    If the metadata cannot be read in the right format, or the matrix can't
    be inverted, the card face is not drawn.
    All card faces are drawn and textured as single-sided.
    \\todo CreatePayload()

    """

    applyDrawMode = Attribute(
        name = 'model:applyDrawMode',
        as_type = 'bool',
        is_uniform = True,
        docstring = """,
        If true, and this prim or parent prims have model:drawMode                 set, apply an alternate imaging mode to this prim. See
        \\ref UsdGeomModelAPI_drawMode.
        """,

    )
    cardGeometry = Attribute(
        name = 'model:cardGeometry',
        as_type = 'token',
        is_uniform = True,
        allowedTokens = ["cross", "box", "fromTexture"],
        docstring = """,
        The geometry to generate for imaging prims inserted for \\em                 cards imaging mode. See for
        geometry descriptions. If unspecified, it should be interpreted
        as cross.
        """,

    )
    cardTextureXNeg = Attribute(
        name = 'model:cardTextureXNeg',
        as_type = 'asset',
        docstring = """,
        In cards imaging mode, the texture applied to the X- quad.                 The texture axes (s,t) are mapped to model-space axes (y, -z).
        """,

    )
    cardTextureXPos = Attribute(
        name = 'model:cardTextureXPos',
        as_type = 'asset',
        docstring = """,
        In cards imaging mode, the texture applied to the X+ quad.                 The texture axes (s,t) are mapped to model-space axes (-y, -z).
        """,

    )
    cardTextureYNeg = Attribute(
        name = 'model:cardTextureYNeg',
        as_type = 'asset',
        docstring = """,
        In cards imaging mode, the texture applied to the Y- quad.                 The texture axes (s,t) are mapped to model-space axes (-x, -z).
        """,

    )
    cardTextureYPos = Attribute(
        name = 'model:cardTextureYPos',
        as_type = 'asset',
        docstring = """,
        In cards imaging mode, the texture applied to the Y+ quad.                 The texture axes (s,t) are mapped to model-space axes (x, -z).
        """,

    )
    cardTextureZNeg = Attribute(
        name = 'model:cardTextureZNeg',
        as_type = 'asset',
        docstring = """,
        In cards imaging mode, the texture applied to the Z- quad.                 The texture axes (s,t) are mapped to model-space axes (-x, -y).
        """,

    )
    cardTextureZPos = Attribute(
        name = 'model:cardTextureZPos',
        as_type = 'asset',
        docstring = """,
        In cards imaging mode, the texture applied to the Z+ quad.                 The texture axes (s,t) are mapped to model-space axes (x, -y).
        """,

    )
    drawMode = Attribute(
        name = 'model:drawMode',
        as_type = 'token',
        is_uniform = True,
        allowedTokens = ["origin", "bounds", "cards", "default"],
        docstring = """,
        Alternate imaging mode; applied to this prim or child prims                 where model:applyDrawMode is true, or where the prim
        has kind component. See \\ref UsdGeomModelAPI_drawMode
        for mode descriptions.
        """,

    )
    Vec3f = Attribute(
        name = 'Vec3f',
        as_type = 'uniform',
        docstring = """,
        The base color of imaging prims inserted for alternate                 imaging modes. For origin and bounds modes, this
        controls line color; for cards mode, this controls the
        fallback quad color. If unspecified, it should be interpreted
        as (0.18, 0.18, 0.18).
        """,

    )

class MotionAPI(Prim):
    """
    UsdGeomMotionAPI encodes data that can live on any prim that    may affect computations involving:
    - computed motion for motion blur
    - sampling for motion blur
    For example, UsdGeomMotionAPI provides *velocityScale*
    (GetVelocityScaleAttr()) for controlling how motion-blur samples should
    be computed by velocity-consuming schemas.

    """

    velocityScale = Attribute(
        name = 'motion:velocityScale',
        as_type = 'float',
        value = 1,
        docstring = """,
        VelocityScale is an **inherited** float attribute that        velocity-based schemas (e.g. PointBased, PointInstancer) can consume
        to compute interpolated positions and orientations by applying
        velocity and angularVelocity, which is required for interpolating
        between samples when topology is varying over time.  Although these
        quantities are generally physically computed by a simulator, sometimes
        we require more or less motion-blur to achieve the desired look.
        VelocityScale allows artists to dial-in, as a post-sim correction,
        a scale factor to be applied to the velocity prior to computing
        interpolated positions from it.
        See also ComputeVelocityScale()
        """,

    )