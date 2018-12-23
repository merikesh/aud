from .base import Prim, Attribute, Property

class Light(Prim):
    """
    Base class for all lights.
    <b>Linking</b>
    Lights can be linked to geometry.  Linking controls which geometry
    a light illuminates, and which geometry casts shadows from the light.
    Linking is specified as collections (UsdCollectionAPI) which can
    be accessed via GetLightLinkCollection() and GetShadowLinkCollection().
    Note however that there are extra semantics in how UsdLuxLight
    uses its collections: if a collection is empty, the light is treated
    as linked to <i>all</i> geometry for the respective purpose.
    UsdCollectionAPI and UsdCollectionAPI::MembershipQuery are unaware
    of this light-specific interpretation.

    """

    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:lightLink", "CollectionAPI:shadowLink"])
    color = Attribute(
        name = 'color',
        as_type = 'color3f',
        value = (1, 1, 1),
        docstring = """,
        The color of emitted light, in energy-linear terms.
        """,

    )
    colorTemperature = Attribute(
        name = 'colorTemperature',
        as_type = 'float',
        value = 6500,
        displayName = "Color Temperature",
        docstring = """,
        Color temperature, in degrees Kelvin, representing the        white point.  The default is a common white point, D65.  Lower
        values are warmer and higher values are cooler.  The valid range
        is from 1000 to 10000. Only takes effect when
        enableColorTemperature is set to true.  When active, the
        computed result multiplies against the color attribute.
        See UsdLuxBlackbodyTemperatureAsRgb().
        """,

    )
    diffuse = Attribute(
        name = 'diffuse',
        as_type = 'float',
        value = 1,
        displayName = "Diffuse Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the diffuse        response of materials.  This is a non-physical control.
        """,

    )
    enableColorTemperature = Attribute(
        name = 'enableColorTemperature',
        as_type = 'bool',
        value = 0,
        displayName = "Enable Color Temperature",
        docstring = """,
        Enables using colorTemperature.
        """,

    )
    exposure = Attribute(
        name = 'exposure',
        as_type = 'float',
        value = 0,
        docstring = """,
        Scales the power of the light exponentially as a power        of 2 (similar to an F-stop control over exposure).  The result
        is multiplied against the intensity.
        """,

    )
    filters = Attribute(
        name = 'filters',
        as_type = 'rel',
        docstring = """,
        Relationship to the light filters that apply to this light.
        """,

    )
    intensity = Attribute(
        name = 'intensity',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scales the power of the light linearly.
        """,

    )
    normalize = Attribute(
        name = 'normalize',
        as_type = 'bool',
        value = 0,
        displayName = "Normalize Power",
        docstring = """,
        Normalizes power by the surface area of the light.        This makes it easier to independently adjust the power and shape
        of the light, by causing the power to not vary with the area or
        angular size of the light.
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
    specular = Attribute(
        name = 'specular',
        as_type = 'float',
        value = 1,
        displayName = "Specular Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the specular        response of materials.  This is a non-physical control.
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

class ListAPI(Prim):
    """
    API schema to support discovery and publishing of lights in a scene.
    Discovering Lights via Traversal
    To motivate this API, consider what is required to discover all
    lights in a scene.  We must load all payloads and traverse all prims:
    \\code
    01  // Load everything on the stage so we can find all lights,
    02  // including those inside payloads
    03  stage->Load();
    04
    05  // Traverse all prims, checking if they are of type UsdLuxLight
    06  // (Note: ignoring instancing and a few other things for simplicity)
    07  SdfPathVector lights;
    08  for (UsdPrim prim: stage->Traverse()) {
    09      if (prim.IsA<UsdLuxLight>()) {
    10          lights.push_back(i->GetPath());
    11      }
    12  }
    \\endcode
    This traversal -- suitably elaborated to handle certain details --
    is the first and simplest thing UsdLuxListAPI provides.
    UsdLuxListAPI::ComputeLightList() performs this traversal and returns
    all lights in the scene:
    \\code
    01  UsdLuxListAPI listAPI(stage->GetPseudoRoot());
    02  SdfPathVector lights = listAPI.ComputeLightList();
    \\endcode
    Publishing a Cached Light List
    Consider a USD client that needs to quickly discover lights but
    wants to defer loading payloads and traversing the entire scene
    where possible, and is willing to do up-front computation and
    caching to achieve that.
    UsdLuxListAPI provides a way to cache the computed light list,
    by publishing the list of lights onto prims in the model
    hierarchy.  Consider a big set that contains lights:
    \\code
    01  def Xform "BigSetWithLights" (
    02      kind = "assembly"
    03      payload = @BigSetWithLights.usd@   // Heavy payload
    04  ) {
    05      // Pre-computed, cached list of lights inside payload
    06      rel lightList = [
    07          <./Lights/light_1>,
    08          <./Lights/light_2>,
    09          ...
    10      ]
    11      token lightList:cacheBehavior = "consumeAndContinue";
    12  }
    \\endcode
    The lightList relationship encodes a set of lights, and the
    lightList:cacheBehavior property provides fine-grained
    control over how to use that cache.  (See details below.)
    The cache can be created by first invoking
    ComputeLightList(ComputeModeIgnoreCache) to pre-compute the list
    and then storing the result with UsdLuxListAPI::StoreLightList().
    To enable efficient retrieval of the cache, it should be stored
    on a model hierarchy prim.  Furthermore, note that while you can
    use a UsdLuxListAPI bound to the pseudo-root prim to query the
    lights (as in the example above) because it will perform a
    traversal over descendants, you cannot store the cache back to the
    pseduo-root prim.
    To consult the cached list, we invoke
    ComputeLightList(ComputeModeConsultModelHierarchyCache):
    \\code
    01  // Find and load all lights, using lightList cache where available
    02  UsdLuxListAPI list(stage->GetPseudoRoot());
    03  SdfPathSet lights = list.ComputeLightList(
    04      UsdLuxListAPI::ComputeModeConsultModelHierarchyCache);
    05  stage.LoadAndUnload(lights, SdfPathSet());
    \\endcode
    In this mode, ComputeLightList() will traverse the model
    hierarchy, accumulating cached light lists.
    Controlling Cache Behavior
    The lightList:cacheBehavior property gives additional fine-grained
    control over cache behavior:
    - The fallback value, "ignore", indicates that the lightList should
    be disregarded.  This provides a way to invalidate cache entries.
    Note that unless "ignore" is specified, a lightList with an empty
    list of targets is considered a cache indicating that no lights
    are present.
    - The value "consumeAndContinue" indicates that the cache should
    be consulted to contribute lights to the scene, and that recursion
    should continue down the model hierarchy in case additional lights
    are added as descedants. This is the default value established when
    StoreLightList() is invoked. This behavior allows the lights within
    a large model, such as the BigSetWithLights example above, to be
    published outside the payload, while also allowing referencing and
    layering to add additional lights over that set.
    - The value "consumeAndHalt" provides a way to terminate recursive
    traversal of the scene for light discovery. The cache will be
    consulted but no descendant prims will be examined.
    Instancing
    Where instances are present, UsdLuxListAPI::ComputeLightList() will
    return the instance-unique paths to any lights discovered within
    those instances.  Lights within a UsdGeomPointInstancer will
    not be returned, however, since they cannot be referred to
    solely via paths.

    """

    lightList = Attribute(
        name = 'lightList',
        as_type = 'rel',
        docstring = """,
        Relationship to lights in the scene.
        """,

    )
    cacheBehavior = Attribute(
        name = 'lightList:cacheBehavior',
        as_type = 'token',
        allowedTokens = ["consumeAndHalt", "consumeAndContinue", "ignore"],
        docstring = """,
        Controls how the lightList should be interpreted.        Valid values are:
        - consumeAndHalt: The lightList should be consulted,
        and if it exists, treated as a final authoritative statement
        of any lights that exist at or below this prim, halting
        recursive discovery of lights.
        - consumeAndContinue: The lightList should be consulted,
        but recursive traversal over nameChildren should continue
        in case additional lights are added by descendants.
        - ignore: The lightList should be entirely ignored.  This
        provides a simple way to temporarily invalidate an existing
        cache.  This is the fallback behavior.
        """,

    )

class ShapingAPI(Prim):
    """
    Controls for shaping a light's emission.

    """

    angle = Attribute(
        name = 'shaping:cone:angle',
        as_type = 'float',
        value = 90,
        displayGroup = "Shaping",
        docstring = """,
        Angular limit off the primary axis to restrict the        light spread.
        """,

    )
    softness = Attribute(
        name = 'shaping:cone:softness',
        as_type = 'float',
        value = 0,
        displayGroup = "Shaping",
        docstring = """,
        Controls the cutoff softness for cone angle.        TODO: clarify semantics
        """,

    )
    focus = Attribute(
        name = 'shaping:focus',
        as_type = 'float',
        value = 0,
        displayGroup = "Shaping",
        docstring = """,
        A control to shape the spread of light.  Higher focus        values pull light towards the center and narrow the spread.
        Implemented as an off-axis cosine power exponent.
        TODO: clarify semantics
        """,

    )
    focusTint = Attribute(
        name = 'shaping:focusTint',
        as_type = 'color3f',
        value = (0, 0, 0),
        displayGroup = "Shaping",
        docstring = """,
        Off-axis color tint.  This tints the emission in the        falloff region.  The default tint is black.
        TODO: clarify semantics
        """,

    )
    angleScale = Attribute(
        name = 'shaping:ies:angleScale',
        as_type = 'float',
        displayGroup = "Shaping",
        docstring = """,
        Rescales the angular distribution of the IES profile.        TODO: clarify semantics
        """,

    )
    file_ = Attribute(
        name = 'shaping:ies:file',
        as_type = 'asset',
        displayGroup = "Shaping",
        docstring = """,
        An IES (Illumination Engineering Society) light        profile describing the angular distribution of light.
        """,

    )

class ShadowAPI(Prim):
    """
    Controls to refine a light's shadow behavior.  These are    non-physical controls that are valuable for visual lighting work.

    """

    color = Attribute(
        name = 'shadow:color',
        as_type = 'color3f',
        value = (0, 0, 0),
        displayGroup = "Shadows",
        docstring = """,
        The color of shadows cast by the light.  This is a        non-physical control.  The default is to cast black shadows.
        """,

    )
    distance = Attribute(
        name = 'shadow:distance',
        as_type = 'float',
        displayGroup = "Shadows",
        docstring = """,
        The maximum distance shadows are cast.        There is no limit unless this attribute value is overridden.
        """,

    )
    enable = Attribute(
        name = 'shadow:enable',
        as_type = 'bool',
        value = 1,
        displayGroup = "Shadows",
        docstring = """,
        Enables shadows to be cast by this light.
        """,

    )
    exclude = Attribute(
        name = 'shadow:exclude',
        as_type = 'rel',
        displayGroup = "Shadows",
        displayName = "Shadow Exclude Subset",
        docstring = """,
        Set of geometry to ignore for the purpose of casting shadows from a light.  If this is not specified, all geometry is used for shadowing.
        """,

    )
    falloff = Attribute(
        name = 'shadow:falloff',
        as_type = 'float',
        displayGroup = "Shadows",
        docstring = """,
        The near distance at which shadow falloff beings.        There is no falloff unless this attribute value is overridden.
        """,

    )
    falloffGamma = Attribute(
        name = 'shadow:falloffGamma',
        as_type = 'float',
        value = 1,
        displayGroup = "Shadows",
        docstring = """,
        A gamma (i.e., exponential) control over shadow strength        with linear distance within the falloff zone.
        This requires the use of shadowDistance and shadowFalloff.
        """,

    )
    include = Attribute(
        name = 'shadow:include',
        as_type = 'rel',
        displayGroup = "Shadows",
        displayName = "Shadow Include Subset",
        docstring = """,
        Set of geometry to consider for the purpose of casting shadows from a light.  If this is not specified, all geometry is used for shadowing.
        """,

    )

class LightFilter(Prim):
    """
    A light filter modifies the effect of a light.    Lights refer to filters via relationships so that filters may be
    shared.
    <b>Linking</b>
    Filters can be linked to geometry.  Linking controls which geometry
    a light-filter affects, when considering the light filters attached
    to a light illuminating the geometry.
    Linking is specified as a collection (UsdCollectionAPI) which can
    be accessed via GetFilterLinkCollection().
    Note however that there are extra semantics in how UsdLuxLightFilter
    uses its collection: if a collection is empty, the filter is treated
    as linked to <i>all</i> geometry for the respective purpose.
    UsdCollectionAPI and UsdCollectionAPI::MembershipQuery are unaware
    of this filter-specific interpretation.

    """

    as_type = "LightFilter"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:filterLink"])
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

class DistantLight(Prim):
    """
    Light emitted from a distant source along the -Z axis.    Also known as a directional light.

    """

    as_type = "DistantLight"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:lightLink", "CollectionAPI:shadowLink"])
    angle = Attribute(
        name = 'angle',
        as_type = 'float',
        value = 0.53,
        docstring = """,
        Angular size of the light in degrees.        As an example, the Sun is approximately 0.53 degrees as seen from Earth.
        Higher values broaden the light and therefore soften shadow edges.
        """,

    )
    color = Attribute(
        name = 'color',
        as_type = 'color3f',
        value = (1, 1, 1),
        docstring = """,
        The color of emitted light, in energy-linear terms.
        """,

    )
    colorTemperature = Attribute(
        name = 'colorTemperature',
        as_type = 'float',
        value = 6500,
        displayName = "Color Temperature",
        docstring = """,
        Color temperature, in degrees Kelvin, representing the        white point.  The default is a common white point, D65.  Lower
        values are warmer and higher values are cooler.  The valid range
        is from 1000 to 10000. Only takes effect when
        enableColorTemperature is set to true.  When active, the
        computed result multiplies against the color attribute.
        See UsdLuxBlackbodyTemperatureAsRgb().
        """,

    )
    diffuse = Attribute(
        name = 'diffuse',
        as_type = 'float',
        value = 1,
        displayName = "Diffuse Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the diffuse        response of materials.  This is a non-physical control.
        """,

    )
    enableColorTemperature = Attribute(
        name = 'enableColorTemperature',
        as_type = 'bool',
        value = 0,
        displayName = "Enable Color Temperature",
        docstring = """,
        Enables using colorTemperature.
        """,

    )
    exposure = Attribute(
        name = 'exposure',
        as_type = 'float',
        value = 0,
        docstring = """,
        Scales the power of the light exponentially as a power        of 2 (similar to an F-stop control over exposure).  The result
        is multiplied against the intensity.
        """,

    )
    filters = Attribute(
        name = 'filters',
        as_type = 'rel',
        docstring = """,
        Relationship to the light filters that apply to this light.
        """,

    )
    intensity = Attribute(
        name = 'intensity',
        as_type = 'float',
        value = 50000,
        docstring = """,
        Scales the emission of the light linearly.        The DistantLight has a high default intensity to approximate the Sun.
        """,

    )
    normalize = Attribute(
        name = 'normalize',
        as_type = 'bool',
        value = 0,
        displayName = "Normalize Power",
        docstring = """,
        Normalizes power by the surface area of the light.        This makes it easier to independently adjust the power and shape
        of the light, by causing the power to not vary with the area or
        angular size of the light.
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
    specular = Attribute(
        name = 'specular',
        as_type = 'float',
        value = 1,
        displayName = "Specular Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the specular        response of materials.  This is a non-physical control.
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

class DiskLight(Prim):
    """
    Light emitted from one side of a circular disk.    The disk is centered in the XY plane and emits light along the -Z axis.

    """

    as_type = "DiskLight"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:lightLink", "CollectionAPI:shadowLink"])
    color = Attribute(
        name = 'color',
        as_type = 'color3f',
        value = (1, 1, 1),
        docstring = """,
        The color of emitted light, in energy-linear terms.
        """,

    )
    colorTemperature = Attribute(
        name = 'colorTemperature',
        as_type = 'float',
        value = 6500,
        displayName = "Color Temperature",
        docstring = """,
        Color temperature, in degrees Kelvin, representing the        white point.  The default is a common white point, D65.  Lower
        values are warmer and higher values are cooler.  The valid range
        is from 1000 to 10000. Only takes effect when
        enableColorTemperature is set to true.  When active, the
        computed result multiplies against the color attribute.
        See UsdLuxBlackbodyTemperatureAsRgb().
        """,

    )
    diffuse = Attribute(
        name = 'diffuse',
        as_type = 'float',
        value = 1,
        displayName = "Diffuse Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the diffuse        response of materials.  This is a non-physical control.
        """,

    )
    enableColorTemperature = Attribute(
        name = 'enableColorTemperature',
        as_type = 'bool',
        value = 0,
        displayName = "Enable Color Temperature",
        docstring = """,
        Enables using colorTemperature.
        """,

    )
    exposure = Attribute(
        name = 'exposure',
        as_type = 'float',
        value = 0,
        docstring = """,
        Scales the power of the light exponentially as a power        of 2 (similar to an F-stop control over exposure).  The result
        is multiplied against the intensity.
        """,

    )
    filters = Attribute(
        name = 'filters',
        as_type = 'rel',
        docstring = """,
        Relationship to the light filters that apply to this light.
        """,

    )
    intensity = Attribute(
        name = 'intensity',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scales the power of the light linearly.
        """,

    )
    normalize = Attribute(
        name = 'normalize',
        as_type = 'bool',
        value = 0,
        displayName = "Normalize Power",
        docstring = """,
        Normalizes power by the surface area of the light.        This makes it easier to independently adjust the power and shape
        of the light, by causing the power to not vary with the area or
        angular size of the light.
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
        as_type = 'float',
        value = 0.5,
        docstring = """,
        Radius of the disk.
        """,

    )
    specular = Attribute(
        name = 'specular',
        as_type = 'float',
        value = 1,
        displayName = "Specular Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the specular        response of materials.  This is a non-physical control.
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

class RectLight(Prim):
    """
    Light emitted from one side of a rectangle.    The rectangle is centered in the XY plane and emits light along the -Z axis.
    The rectangle is 1 unit in length in the X and Y axis.

    """

    as_type = "RectLight"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:lightLink", "CollectionAPI:shadowLink"])
    color = Attribute(
        name = 'color',
        as_type = 'color3f',
        value = (1, 1, 1),
        docstring = """,
        The color of emitted light, in energy-linear terms.
        """,

    )
    colorTemperature = Attribute(
        name = 'colorTemperature',
        as_type = 'float',
        value = 6500,
        displayName = "Color Temperature",
        docstring = """,
        Color temperature, in degrees Kelvin, representing the        white point.  The default is a common white point, D65.  Lower
        values are warmer and higher values are cooler.  The valid range
        is from 1000 to 10000. Only takes effect when
        enableColorTemperature is set to true.  When active, the
        computed result multiplies against the color attribute.
        See UsdLuxBlackbodyTemperatureAsRgb().
        """,

    )
    diffuse = Attribute(
        name = 'diffuse',
        as_type = 'float',
        value = 1,
        displayName = "Diffuse Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the diffuse        response of materials.  This is a non-physical control.
        """,

    )
    enableColorTemperature = Attribute(
        name = 'enableColorTemperature',
        as_type = 'bool',
        value = 0,
        displayName = "Enable Color Temperature",
        docstring = """,
        Enables using colorTemperature.
        """,

    )
    exposure = Attribute(
        name = 'exposure',
        as_type = 'float',
        value = 0,
        docstring = """,
        Scales the power of the light exponentially as a power        of 2 (similar to an F-stop control over exposure).  The result
        is multiplied against the intensity.
        """,

    )
    filters = Attribute(
        name = 'filters',
        as_type = 'rel',
        docstring = """,
        Relationship to the light filters that apply to this light.
        """,

    )
    height = Attribute(
        name = 'height',
        as_type = 'float',
        value = 1,
        docstring = """,
        Height of the rectangle, in the local Y axis.
        """,

    )
    intensity = Attribute(
        name = 'intensity',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scales the power of the light linearly.
        """,

    )
    normalize = Attribute(
        name = 'normalize',
        as_type = 'bool',
        value = 0,
        displayName = "Normalize Power",
        docstring = """,
        Normalizes power by the surface area of the light.        This makes it easier to independently adjust the power and shape
        of the light, by causing the power to not vary with the area or
        angular size of the light.
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
    specular = Attribute(
        name = 'specular',
        as_type = 'float',
        value = 1,
        displayName = "Specular Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the specular        response of materials.  This is a non-physical control.
        """,

    )
    file_ = Attribute(
        name = 'texture:file',
        as_type = 'asset',
        docstring = """,
        A color texture to use on the rectangle.
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
    width = Attribute(
        name = 'width',
        as_type = 'float',
        value = 1,
        docstring = """,
        Width of the rectangle, in the local X axis.
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

class SphereLight(Prim):
    """
    Light emitted outward from a sphere.

    """

    as_type = "SphereLight"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:lightLink", "CollectionAPI:shadowLink"])
    color = Attribute(
        name = 'color',
        as_type = 'color3f',
        value = (1, 1, 1),
        docstring = """,
        The color of emitted light, in energy-linear terms.
        """,

    )
    colorTemperature = Attribute(
        name = 'colorTemperature',
        as_type = 'float',
        value = 6500,
        displayName = "Color Temperature",
        docstring = """,
        Color temperature, in degrees Kelvin, representing the        white point.  The default is a common white point, D65.  Lower
        values are warmer and higher values are cooler.  The valid range
        is from 1000 to 10000. Only takes effect when
        enableColorTemperature is set to true.  When active, the
        computed result multiplies against the color attribute.
        See UsdLuxBlackbodyTemperatureAsRgb().
        """,

    )
    diffuse = Attribute(
        name = 'diffuse',
        as_type = 'float',
        value = 1,
        displayName = "Diffuse Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the diffuse        response of materials.  This is a non-physical control.
        """,

    )
    enableColorTemperature = Attribute(
        name = 'enableColorTemperature',
        as_type = 'bool',
        value = 0,
        displayName = "Enable Color Temperature",
        docstring = """,
        Enables using colorTemperature.
        """,

    )
    exposure = Attribute(
        name = 'exposure',
        as_type = 'float',
        value = 0,
        docstring = """,
        Scales the power of the light exponentially as a power        of 2 (similar to an F-stop control over exposure).  The result
        is multiplied against the intensity.
        """,

    )
    filters = Attribute(
        name = 'filters',
        as_type = 'rel',
        docstring = """,
        Relationship to the light filters that apply to this light.
        """,

    )
    intensity = Attribute(
        name = 'intensity',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scales the power of the light linearly.
        """,

    )
    normalize = Attribute(
        name = 'normalize',
        as_type = 'bool',
        value = 0,
        displayName = "Normalize Power",
        docstring = """,
        Normalizes power by the surface area of the light.        This makes it easier to independently adjust the power and shape
        of the light, by causing the power to not vary with the area or
        angular size of the light.
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
        as_type = 'float',
        value = 0.5,
        docstring = """,
        Radius of the sphere.
        """,

    )
    specular = Attribute(
        name = 'specular',
        as_type = 'float',
        value = 1,
        displayName = "Specular Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the specular        response of materials.  This is a non-physical control.
        """,

    )
    treatAsPoint = Attribute(
        name = 'treatAsPoint',
        as_type = 'bool',
        value = 0,
        docstring = """,
        A hint that this light can be treated as a 'point'        light (effectively, a zero-radius sphere) by renderers that
        benefit from non-area lighting. Renderers that only support
        area lights can disregard this.
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

class CylinderLight(Prim):
    """
    Light emitted outward from a cylinder.    The cylinder is centered at the origin and has its major axis on the X axis.
    The cylinder does not emit light from the flat end-caps.

    """

    as_type = "CylinderLight"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:lightLink", "CollectionAPI:shadowLink"])
    color = Attribute(
        name = 'color',
        as_type = 'color3f',
        value = (1, 1, 1),
        docstring = """,
        The color of emitted light, in energy-linear terms.
        """,

    )
    colorTemperature = Attribute(
        name = 'colorTemperature',
        as_type = 'float',
        value = 6500,
        displayName = "Color Temperature",
        docstring = """,
        Color temperature, in degrees Kelvin, representing the        white point.  The default is a common white point, D65.  Lower
        values are warmer and higher values are cooler.  The valid range
        is from 1000 to 10000. Only takes effect when
        enableColorTemperature is set to true.  When active, the
        computed result multiplies against the color attribute.
        See UsdLuxBlackbodyTemperatureAsRgb().
        """,

    )
    diffuse = Attribute(
        name = 'diffuse',
        as_type = 'float',
        value = 1,
        displayName = "Diffuse Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the diffuse        response of materials.  This is a non-physical control.
        """,

    )
    enableColorTemperature = Attribute(
        name = 'enableColorTemperature',
        as_type = 'bool',
        value = 0,
        displayName = "Enable Color Temperature",
        docstring = """,
        Enables using colorTemperature.
        """,

    )
    exposure = Attribute(
        name = 'exposure',
        as_type = 'float',
        value = 0,
        docstring = """,
        Scales the power of the light exponentially as a power        of 2 (similar to an F-stop control over exposure).  The result
        is multiplied against the intensity.
        """,

    )
    filters = Attribute(
        name = 'filters',
        as_type = 'rel',
        docstring = """,
        Relationship to the light filters that apply to this light.
        """,

    )
    intensity = Attribute(
        name = 'intensity',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scales the power of the light linearly.
        """,

    )
    length = Attribute(
        name = 'length',
        as_type = 'float',
        value = 1,
        docstring = """,
        Width of the rectangle, in the local X axis.
        """,

    )
    normalize = Attribute(
        name = 'normalize',
        as_type = 'bool',
        value = 0,
        displayName = "Normalize Power",
        docstring = """,
        Normalizes power by the surface area of the light.        This makes it easier to independently adjust the power and shape
        of the light, by causing the power to not vary with the area or
        angular size of the light.
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
        as_type = 'float',
        value = 0.5,
        docstring = """,
        Radius of the cylinder.
        """,

    )
    specular = Attribute(
        name = 'specular',
        as_type = 'float',
        value = 1,
        displayName = "Specular Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the specular        response of materials.  This is a non-physical control.
        """,

    )
    treatAsLine = Attribute(
        name = 'treatAsLine',
        as_type = 'bool',
        value = 0,
        docstring = """,
        A hint that this light can be treated as a 'line'        light (effectively, a zero-radius cylinder) by renderers that
        benefit from non-area lighting. Renderers that only support
        area lights can disregard this.
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

class GeometryLight(Prim):
    """
    Light emitted outward from a geometric prim (UsdGeomGprim),    which is typically a mesh.

    """

    as_type = "GeometryLight"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:lightLink", "CollectionAPI:shadowLink"])
    color = Attribute(
        name = 'color',
        as_type = 'color3f',
        value = (1, 1, 1),
        docstring = """,
        The color of emitted light, in energy-linear terms.
        """,

    )
    colorTemperature = Attribute(
        name = 'colorTemperature',
        as_type = 'float',
        value = 6500,
        displayName = "Color Temperature",
        docstring = """,
        Color temperature, in degrees Kelvin, representing the        white point.  The default is a common white point, D65.  Lower
        values are warmer and higher values are cooler.  The valid range
        is from 1000 to 10000. Only takes effect when
        enableColorTemperature is set to true.  When active, the
        computed result multiplies against the color attribute.
        See UsdLuxBlackbodyTemperatureAsRgb().
        """,

    )
    diffuse = Attribute(
        name = 'diffuse',
        as_type = 'float',
        value = 1,
        displayName = "Diffuse Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the diffuse        response of materials.  This is a non-physical control.
        """,

    )
    enableColorTemperature = Attribute(
        name = 'enableColorTemperature',
        as_type = 'bool',
        value = 0,
        displayName = "Enable Color Temperature",
        docstring = """,
        Enables using colorTemperature.
        """,

    )
    exposure = Attribute(
        name = 'exposure',
        as_type = 'float',
        value = 0,
        docstring = """,
        Scales the power of the light exponentially as a power        of 2 (similar to an F-stop control over exposure).  The result
        is multiplied against the intensity.
        """,

    )
    filters = Attribute(
        name = 'filters',
        as_type = 'rel',
        docstring = """,
        Relationship to the light filters that apply to this light.
        """,

    )
    geometry = Attribute(
        name = 'geometry',
        as_type = 'rel',
        docstring = """,
        Relationship to the geometry to use as the light source.
        """,

    )
    intensity = Attribute(
        name = 'intensity',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scales the power of the light linearly.
        """,

    )
    normalize = Attribute(
        name = 'normalize',
        as_type = 'bool',
        value = 0,
        displayName = "Normalize Power",
        docstring = """,
        Normalizes power by the surface area of the light.        This makes it easier to independently adjust the power and shape
        of the light, by causing the power to not vary with the area or
        angular size of the light.
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
    specular = Attribute(
        name = 'specular',
        as_type = 'float',
        value = 1,
        displayName = "Specular Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the specular        response of materials.  This is a non-physical control.
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

class DomeLight(Prim):
    """
    Light emitted inward from a distant external environment,    such as a sky or IBL light probe.

    """

    as_type = "DomeLight"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:lightLink", "CollectionAPI:shadowLink"])
    color = Attribute(
        name = 'color',
        as_type = 'color3f',
        value = (1, 1, 1),
        docstring = """,
        The color of emitted light, in energy-linear terms.
        """,

    )
    colorTemperature = Attribute(
        name = 'colorTemperature',
        as_type = 'float',
        value = 6500,
        displayName = "Color Temperature",
        docstring = """,
        Color temperature, in degrees Kelvin, representing the        white point.  The default is a common white point, D65.  Lower
        values are warmer and higher values are cooler.  The valid range
        is from 1000 to 10000. Only takes effect when
        enableColorTemperature is set to true.  When active, the
        computed result multiplies against the color attribute.
        See UsdLuxBlackbodyTemperatureAsRgb().
        """,

    )
    diffuse = Attribute(
        name = 'diffuse',
        as_type = 'float',
        value = 1,
        displayName = "Diffuse Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the diffuse        response of materials.  This is a non-physical control.
        """,

    )
    enableColorTemperature = Attribute(
        name = 'enableColorTemperature',
        as_type = 'bool',
        value = 0,
        displayName = "Enable Color Temperature",
        docstring = """,
        Enables using colorTemperature.
        """,

    )
    exposure = Attribute(
        name = 'exposure',
        as_type = 'float',
        value = 0,
        docstring = """,
        Scales the power of the light exponentially as a power        of 2 (similar to an F-stop control over exposure).  The result
        is multiplied against the intensity.
        """,

    )
    filters = Attribute(
        name = 'filters',
        as_type = 'rel',
        docstring = """,
        Relationship to the light filters that apply to this light.
        """,

    )
    intensity = Attribute(
        name = 'intensity',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scales the power of the light linearly.
        """,

    )
    normalize = Attribute(
        name = 'normalize',
        as_type = 'bool',
        value = 0,
        displayName = "Normalize Power",
        docstring = """,
        Normalizes power by the surface area of the light.        This makes it easier to independently adjust the power and shape
        of the light, by causing the power to not vary with the area or
        angular size of the light.
        """,

    )
    portals = Attribute(
        name = 'portals',
        as_type = 'rel',
        docstring = """,
        Optional portals to guide light sampling.
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
    specular = Attribute(
        name = 'specular',
        as_type = 'float',
        value = 1,
        displayName = "Specular Multiplier",
        docstring = """,
        A multiplier for the effect of this light on the specular        response of materials.  This is a non-physical control.
        """,

    )
    file_ = Attribute(
        name = 'texture:file',
        as_type = 'asset',
        docstring = """,
        A color texture to use on the dome, such as an HDR (high        dynamic range) texture intended for IBL (image based lighting).
        """,

    )
    format_ = Attribute(
        name = 'texture:format',
        as_type = 'token',
        value = "automatic",
        allowedTokens = ["automatic", "latlong", "mirroredBall", "angular", "cubeMapVerticalCross"],
        docstring = """,
        Specifies the parameterization of the color map file.        Valid values are:
        - automatic: Tries to determine the layout from the file itself.
        For example, Renderman texture files embed an explicit
        parameterization.
        - latlong: Latitude as X, longitude as Y.
        - mirroredBall: An image of the environment reflected in a
        sphere, using an implicitly orthogonal projection.
        - angular: Similar to mirroredBall but the radial dimension
        is mapped linearly to the angle, providing better sampling
        at the edges.
        - cubeMapVerticalCross: A cube map with faces laid out as a
        vertical cross.
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

class LightPortal(Prim):
    """
    A rectangular portal in the local XY plane that guides sampling    of a dome light.  Transmits light in the -Z direction.
    The rectangle is 1 unit in length.

    """

    as_type = "LightPortal"
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