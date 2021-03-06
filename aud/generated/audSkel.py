from .base import Prim, Attribute, Property

class SkelRoot(Prim):
    """
    Boundable prim type used to identify a scope beneath which    skeletally-posed primitives are defined.
    A SkelRoot must be defined at or above a skinned primitive for any skinning
    behaviors in UsdSkel.
    See the extented "Skel Root Schema" documentation for
    more information.
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

    as_type = "SkelRoot"
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

class Skeleton(Prim):
    """
    Describes a skeleton.
    See the extended "Skeleton Schema" documentation for
    more information.

    """

    as_type = "Skeleton"
    matrix4d = Attribute(
        name = 'matrix4d',
        as_type = 'uniform',
        docstring = """,
        Specifies the bind-pose transforms of each joint in        **world space**, in the ordering imposed by *joints*.
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
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        An array of path tokens identifying the set of joints that make        up the skeleton, and their order. Each token in the array must be valid
        when parsed as an SdfPath. The parent-child relationships of the
        corresponding paths determine the parent-child relationships of each
        joint.
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
    matrix4d = Attribute(
        name = 'matrix4d',
        as_type = 'uniform',
        docstring = """,
        Specifies the rest-pose transforms of each joint in        **local space**, in the ordering imposed by *joints*. This provides
        fallback values for joint transforms when a Skeleton either has no
        bound animation source, or when that animation source only contains
        animation for a subset of a Skeleton's joints.
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

class SkelAnimation(Prim):
    """
    Describes a skel animation, where joint animation is stored in a    vectorized form.
    See the extended "Skel Animation"
    documentation for more information.

    """

    as_type = "SkelAnimation"
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Array of tokens identifying which blend shapes this         animation's data applies to. The tokens for blendShapes correspond to
        the tokens set in the *skel:blendShapes* binding property of the
        UsdSkelBindingAPI.
        Array of weight values for each blend shape. Each weight value        is associated with the corresponding blend shape identified within the
        *blendShapes* token array, and therefore must have the same length as
        *blendShapes.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Array of tokens identifying which joints this animation's        data applies to. The tokens for joints correspond to the tokens of
        Skeleton primitives. The order of the joints as listed here may
        vary from the order of joints on the Skeleton itself.
        Joint-local unit quaternion rotations of all affected joints,        in 32-bit precision. Array length should match the size of the
        *joints* attribute.
        Joint-local scales of all affected joints, in        16 bit precision. Array length should match the size of the *joints*
        attribute.
        Joint-local translations of all affected joints. Array length        should match the size of the *joints* attribute.
        """,

    )

class PackedJointAnimation(Prim):
    """
    Deprecated. Please use SkelAnimation instead.

    """

    as_type = "PackedJointAnimation"
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Array of tokens identifying which blend shapes this         animation's data applies to. The tokens for blendShapes correspond to
        the tokens set in the *skel:blendShapes* binding property of the
        UsdSkelBindingAPI.
        Array of weight values for each blend shape. Each weight value        is associated with the corresponding blend shape identified within the
        *blendShapes* token array, and therefore must have the same length as
        *blendShapes.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        Array of tokens identifying which joints this animation's        data applies to. The tokens for joints correspond to the tokens of
        Skeleton primitives. The order of the joints as listed here may
        vary from the order of joints on the Skeleton itself.
        Joint-local unit quaternion rotations of all affected joints,        in 32-bit precision. Array length should match the size of the
        *joints* attribute.
        Joint-local scales of all affected joints, in        16 bit precision. Array length should match the size of the *joints*
        attribute.
        Joint-local translations of all affected joints. Array length        should match the size of the *joints* attribute.
        """,

    )

class SkelBindingAPI(Prim):
    """
    Provides API for authoring and extracting all the skinning-related    data that lives in the "geometry hierarchy" of prims and models that want
    to be skeletally deformed.
    See the extended "UsdSkelBindingAPI schema"
    documentation for more about bindings and how they apply in a scene graph.

    """

    geomBindTransform = Attribute(
        name = 'primvars:skel:geomBindTransform',
        as_type = 'matrix4d',
        docstring = """,
        Encodes the bind-time world space transforms of the prim.        If the transform is identical for a group of gprims that share a common
        ancestor, the transform may be authored on the ancestor, to "inherit"
        down to all the leaf gprims. If this transform is unset, an identity
        transform is used instead.
        Indices into the *joints* attribute of the closest        (in namespace) bound Skeleton that affect each point of a PointBased
        gprim. The primvar can have either *constant* or *vertex* interpolation.
        This primvar's *elementSize* will determine how many joint influences
        apply to each point. Indices must point be valid. Null influences should
        be defined by setting values in jointWeights to zero.
        See UsdGeomPrimvar for more information on interpolation and
        elementSize.
        Weights for the joints that affect each point of a PointBased        gprim. The primvar can have either *constant* or *vertex* interpolation.
        This primvar's *elementSize* will determine how many joints influences
        apply to each point. The length, interpolation, and elementSize of
        *jointWeights* must match that of *jointIndices*. See UsdGeomPrimvar
        for more information on interpolation and elementSize.
        """,

    )
    animationSource = Attribute(
        name = 'skel:animationSource',
        as_type = 'rel',
        docstring = """,
        Animation source to be bound to Skeleton primitives at or        beneath the location at which this property is defined.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        An array of tokens defining the order onto which blend shape        weights from an animation source map onto the *skel:blendShapeTargets*
        rel of a binding site. If authored, the number of elements must be equal
        to the number of targets in the _blendShapeTargets_ rel. This property
        is not inherited hierarchically, and is expected to be authored directly
        on the skinnable primitive to which the blend shapes apply.
        """,

    )
    blendShapeTargets = Attribute(
        name = 'skel:blendShapeTargets',
        as_type = 'rel',
        docstring = """,
        Ordered list of all target blend shapes. This property is not        inherited hierarchically, and is expected to be authored directly on
        the skinnable primitive to which the the blend shapes apply.
        """,

    )
    token = Attribute(
        name = 'token',
        as_type = 'uniform',
        docstring = """,
        An (optional) array of tokens defining the list of        joints to which jointIndices apply. If not defined, jointIndices applies
        to the ordered list of joints defined in the bound Skeleton's *joints*
        attribute. If undefined on a primitive, the primitive inherits the
        value of the nearest ancestor prim, if any.
        """,

    )
    skeleton = Attribute(
        name = 'skel:skeleton',
        as_type = 'rel',
        docstring = """,
        Skeleton to be bound to this prim and its descendents that        possess a mapping and weighting to the joints of the identified
        Skeleton.
        """,

    )

class BlendShape(Prim):
    """
    Describes a target blend shape, possibly containing inbetween      shapes.
    See the extended "Blend Shape Schema
    documentation for information.

    """

    as_type = "BlendShape"
    vector3f = Attribute(
        name = 'vector3f',
        as_type = 'uniform',
        docstring = """,
        **Required property**. Position offsets which, when added to the        base pose, provides the target shape.
        """,

    )
    uint = Attribute(
        name = 'uint',
        as_type = 'uniform',
        docstring = """,
        **Optional property**. Indices into the original mesh that        correspond to the values in *offsets* and of any inbetween shapes. If
        authored, the number of elements must be equal to the number of elements
        in the *offsets* array.
        """,

    )