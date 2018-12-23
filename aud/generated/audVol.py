from .base import Prim, Attribute, Property

class Volume(Prim):
    """
    A renderable volume primitive. A volume is made up of any number             of FieldBase primitives bound together in this volume. Each
    FieldBase primitive is specified as a relationship with a
    namespace prefix of \field\.

    """

    as_type = "Volume"
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

class FieldBase(Prim):
    """
    Base class for field primitives.Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
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

class FieldAsset(Prim):
    """
    Base class for field primitives defined by an external file.Extent is a three dimensional range measuring the geometric        extent of the authored gprim in its own local space (i.e. its own
    transform not applied), without accounting for any shader-induced
    displacement.  Whenever any geometry-affecting attribute is authored
    for any gprim in a layer, extent must also be authored at the same
    timesample; failure to do so will result in incorrect bounds-computation.
    \\sa \\ref UsdGeom_Boundable_Extent.
    An authored extent on a prim which has children is expected to include
    the extent of all children, as they will be pruned from BBox computation
    during traversal.

    """

    filePath = Attribute(
        name = 'filePath',
        as_type = 'asset',
        docstring = """,
        An asset path attribute that points to a file on disk.                 For each supported file format, a separate FieldAsset
        subclass is required. Any further information required to
        extract the field from the file (such as a name or index to
        choose a single field from a file that can store multiple
        fields) will be defined on the FieldAsset subclass.
        This attribute's value can be animated over time, as most
        volume asset formats represent just a single timeSample of
        a volume.  However, it does not, at this time, support
        any pattern substitutions like \$F\.
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

class Field3DAsset(Prim):
    """
    Field3D field primitive. The FieldAsset filePath attribute must             specify a file in the Field3D format on disk.
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

    as_type = "Field3DAsset"
    fieldIndex = Attribute(
        name = 'fieldIndex',
        as_type = 'int',
        docstring = """,
        A Field3D file can contain multiple fields with the same                 name. This attribute is an index used to disambiguate
        between these multiple fields with the same name.
        """,

    )
    fieldName = Attribute(
        name = 'fieldName',
        as_type = 'token',
        docstring = """,
        Name of an individual field within the file specified by                 the filePath attribute.
        """,

    )
    filePath = Attribute(
        name = 'filePath',
        as_type = 'asset',
        docstring = """,
        An asset path attribute that points to a file on disk.                 For each supported file format, a separate FieldAsset
        subclass is required. Any further information required to
        extract the field from the file (such as a name or index to
        choose a single field from a file that can store multiple
        fields) will be defined on the FieldAsset subclass.
        This attribute's value can be animated over time, as most
        volume asset formats represent just a single timeSample of
        a volume.  However, it does not, at this time, support
        any pattern substitutions like \$F\.
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

class OpenVDBAsset(Prim):
    """
    OpenVDB field primitive. The FieldAsset filePath attribute must             specify a file in the OpenVDB format on disk.
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

    as_type = "OpenVDBAsset"
    fieldName = Attribute(
        name = 'fieldName',
        as_type = 'token',
        docstring = """,
        Name of an individual grid within the file specified by                 the filePath attribute.
        """,

    )
    filePath = Attribute(
        name = 'filePath',
        as_type = 'asset',
        docstring = """,
        An asset path attribute that points to a file on disk.                 For each supported file format, a separate FieldAsset
        subclass is required. Any further information required to
        extract the field from the file (such as a name or index to
        choose a single field from a file that can store multiple
        fields) will be defined on the FieldAsset subclass.
        This attribute's value can be animated over time, as most
        volume asset formats represent just a single timeSample of
        a volume.  However, it does not, at this time, support
        any pattern substitutions like \$F\.
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