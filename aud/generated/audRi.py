from .base import Prim, Attribute, Property

class StatementsAPI(Prim):
    """
    Container namespace schema for all renderman statements.
    \\note The longer term goal is for clients to go directly to primvar
    or render-attribute API's, instead of using UsdRi StatementsAPI
    for inherited attributes.  Anticpating this, StatementsAPI
    can smooth the way via a few environment variables:
    * USDRI_STATEMENTS_WRITE_NEW_ENCODING: Causes StatementsAPI to write
    attributes to primvars in the \ri:\ namespace.

    """

    pass

class RisObject(Prim):
    """
    \\deprecated Specialized RIS shader schemas have been deprecated in    favor of all shader prims being simple UsdShadeShader.
    Represents a ris object with connectable parameters.

    """

    as_type = "RisObject"
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

class RisPattern(Prim):
    """
    \\deprecated Specialized RIS shader schemas have been deprecated in    favor of all shader prims being simple UsdShadeShader.
    Represents a ris pattern object. Multiple of these can be assigned.

    """

    as_type = "RisPattern"
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

class RisOslPattern(Prim):
    """
    \\deprecated Specialized RIS shader schemas have been deprecated in    favor of all shader prims being simple UsdShadeShader.
    Represents a ris osl pattern object.

    """

    as_type = "RisOslPattern"
    filePath = Attribute(
        name = 'info:filePath',
        as_type = 'asset',
        value = @PxrOSL@,
        hidden = true,
        docstring = """,
        """,

    )
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

class RisBxdf(Prim):
    """
    \\deprecated Specialized RIS shader schemas have been deprecated in    favor of all shader prims being simple UsdShadeShader.
    Represents a ris bxdf object. One of these is assigned at one time.

    """

    as_type = "RisBxdf"
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

class RisIntegrator(Prim):
    """
    Integrator. Only one can be declared in a rib scene.

    """

    as_type = "RisIntegrator"

class RiMaterialAPI(Prim):
    """
    This API provides outputs that connect a material prim to prman    shaders and RIS objects.

    """

    displacement = Attribute(
        name = 'outputs:ri:displacement',
        as_type = 'token',
        displayGroup = "Outputs",
        docstring = """,
        """,

    )
    surface = Attribute(
        name = 'outputs:ri:surface',
        as_type = 'token',
        displayGroup = "Outputs",
        docstring = """,
        """,

    )
    volume = Attribute(
        name = 'outputs:ri:volume',
        as_type = 'token',
        displayGroup = "Outputs",
        docstring = """,
        """,

    )

class RiLightAPI(Prim):
    """
    RiLightAPI is an API schema that provides an interface    to add Renderman-specific attributes to lights.

    """

    intensityNearDist = Attribute(
        name = 'ri:intensityNearDist',
        as_type = 'float',
        displayGroup = "Refine",
        displayName = "Intensity Near Dist",
        docstring = """,
        Near distance between the point being illuminated and the        light at which the sample doesn't get brighter. This may help you
        avoid hot spots and sampling issues where a light is near a
        surface.
        """,

    )
    lightGroup = Attribute(
        name = 'ri:lightGroup',
        as_type = 'string',
        displayGroup = "Advanced",
        displayName = "Light Group",
        docstring = """,
        Specify the light group name used for light group LPEs.        This is useful to generate per-light AOVs for later adjustment
        in compositing.
        """,

    )
    fixedSampleCount = Attribute(
        name = 'ri:sampling:fixedSampleCount',
        as_type = 'int',
        displayGroup = "Advanced",
        displayName = "Light Samples",
        docstring = """,
        Specifies an override of the number of light samples to be        taken for this light source. If set to something other than zero,
        it will override the sampling performed by the integrator and can
        result in a performance impact. For scenes that have lots of lights,
        resulting in some lights that are under-sampled, you may want to set
        it to non-zero.
        """,

    )
    importanceMultiplier = Attribute(
        name = 'ri:sampling:importanceMultiplier',
        as_type = 'float',
        value = 1,
        displayGroup = "Advanced",
        displayName = "Importance Multiplier",
        docstring = """,
        Importance of this light for noise control.
        """,

    )
    thinShadow = Attribute(
        name = 'ri:shadow:thinShadow',
        as_type = 'bool',
        displayGroup = "Advanced",
        displayName = "Thin Shadow",
        docstring = """,
        Enable thin shadow and disable refraction caustics for this        light. This parameter will ignored if Trace Light Paths is
        enabled. This is a non-physical control that creates "fake"
        colored shadows for transmissive objects without needing to
        generate photons for caustics.
        """,

    )
    lightPaths = Attribute(
        name = 'ri:trace:lightPaths',
        as_type = 'bool',
        displayGroup = "Advanced",
        displayName = "Trace Light Paths",
        docstring = """,
        Enable light and photon tracing from this light. This        value enforces a physically-based light and as a side-effect
        disables the above Shadows controls. Users may use this feature
        to selectively decide which lights emit photons when using the
        PxrVCM or PxrUPBP Integrators.
        """,

    )

class RiLightFilterAPI(Prim):
    """
    Renderman-specific attributes for light filters.

    """

    combineMode = Attribute(
        name = 'ri:combineMode',
        as_type = 'token',
        allowedTokens = ["multiply", "max", "min", "screen"],
        docstring = """,
        Specifies how this filter combines with others.        Valid values are:
        - multiply: The results of filters are multiplied together
        - max: The maximum result of the filters is used.  This
        works best for grey-scale filters.
        - min: The minimum result of the filters is used. This
        works best for grey-scale filters.
        - screen: Similar to max, but combines gradients in a smoother
        way by using a screen operation:
        <pre>screen(a,b) = 1-(1-a)(1-b)</pre>
        This works best for grey-scale filters.
        Light filters on a light are grouped by their combine mode.
        Each group is executed and combined using that mode.  Then,
        the final results of each group are multiplied together.
        Fallback: multiply
        """,

    )
    density = Attribute(
        name = 'ri:density',
        as_type = 'float',
        docstring = """,
        Scales the strength of the filter.
        """,

    )
    diffuse = Attribute(
        name = 'ri:diffuse',
        as_type = 'float',
        docstring = """,
        A multiplier for the effect of this light on the diffuse        response of materials.  This is a non-physical control.
        """,

    )
    exposure = Attribute(
        name = 'ri:exposure',
        as_type = 'float',
        value = 0,
        docstring = """,
        Exposure control for the multiplier.
        """,

    )
    intensity = Attribute(
        name = 'ri:intensity',
        as_type = 'float',
        docstring = """,
        Multipier for the diffuse and specular result.
        """,

    )
    invert = Attribute(
        name = 'ri:invert',
        as_type = 'bool',
        docstring = """,
        When true, inverts the output of the light filter.
        """,

    )
    specular = Attribute(
        name = 'ri:specular',
        as_type = 'float',
        docstring = """,
        A multiplier for the effect of this light on the specular        response of materials.  This is a non-physical control.
        """,

    )

class RiLightPortalAPI(Prim):
    """
    Renderman-specific attributes for light portals.

    """

    intensity = Attribute(
        name = 'ri:portal:intensity',
        as_type = 'float',
        displayGroup = "Basic",
        docstring = """,
        Intensity adjustment relative to the light intensity.        This gets multiplied by the light's intensity and power
        """,

    )
    tint = Attribute(
        name = 'ri:portal:tint',
        as_type = 'color3f',
        displayGroup = "Basic",
        displayName = "Color Tint",
        docstring = """,
        tint: This parameter tints the color from the dome texture.
        """,

    )

class RiSplineAPI(Prim):
    """
    RiSplineAPI is a general purpose API schema used to describe    a named spline stored as a set of attributes on a prim.
    It is an add-on schema that can be applied many times to a prim with
    different spline names. All the attributes authored by the schema
    are namespaced under "$NAME:spline:", with the name of the
    spline providing a namespace for the attributes.
    The spline describes a 2D piecewise cubic curve with a position and
    value for each knot. This is chosen to give straightforward artistic
    control over the shape. The supported basis types are:
    - linear (UsdRiTokens->linear)
    - bspline (UsdRiTokens->bspline)
    - Catmull-Rom (UsdRiTokens->catmullRom)

    """

    pass

class RiTextureAPI(Prim):
    """
    RiTextureAPI is an API schema that provides an interface    to add Renderman-specific attributes to adjust textures.

    """

    gamma = Attribute(
        name = 'ri:texture:gamma',
        as_type = 'float',
        docstring = """,
        Gamma-correct the texture
        """,

    )
    saturation = Attribute(
        name = 'ri:texture:saturation',
        as_type = 'float',
        docstring = """,
        Adjust the texture's saturation
        """,

    )

class PxrEnvDayLight(Prim):
    """

    """

    as_type = "PxrEnvDayLight"
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
    day = Attribute(
        name = 'day',
        as_type = 'int',
        value = 1,
        displayGroup = "MsApprox",
        displayName = "Day",
        docstring = """,
        day: Day of the month, 1 through 31.        This is ignored if month is 0.
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
    haziness = Attribute(
        name = 'haziness',
        as_type = 'float',
        value = 2,
        displayGroup = "MsApprox",
        displayName = "Haziness",
        docstring = """,
        haziness: The turbidity of the sky.  The lower limit of the        model is 1.7 for  an exceptionally clear sky, and 10, for an
        nversion, is the upper  limit.
        """,

    )
    hour = Attribute(
        name = 'hour',
        as_type = 'float',
        value = 14.633333,
        displayGroup = "MsApprox",
        displayName = "Hour",
        docstring = """,
        hour: Hours since midnight, local standard time.  May be        fractional to include minutes and seconds.  If daylight saving time
        is in effect, subtract 1 to correct to standard time.  This is
        ignored if month is 0.
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
    latitude = Attribute(
        name = 'latitude',
        as_type = 'float',
        value = 47.602,
        displayGroup = "MsApprox",
        displayName = "Latitude",
        docstring = """,
        latitude: Latitude in degrees.  Positive for north, negative        for south.  Ranges frmo -90 to +90 degrees. This is ignored if
        month is 0.
        """,

    )
    longitude = Attribute(
        name = 'longitude',
        as_type = 'float',
        value = -122.332,
        displayGroup = "MsApprox",
        displayName = "Longitude",
        docstring = """,
        longitude: Longitude in degrees.  Positive for east, negative        for west.  Ranges frmo -180 to +180 degrees.    This is ignored
        if month is 0.
        """,

    )
    month = Attribute(
        name = 'month',
        as_type = 'int',
        value = 0,
        displayGroup = "MsApprox",
        displayName = "Month",
        docstring = """,
        month: Month of the year, 1 through 12.      The default,        0, means to use the explicitly given sun direction   instead of
        automatically computing it.
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
    skyTint = Attribute(
        name = 'skyTint',
        as_type = 'color3f',
        value = (1, 1, 1),
        displayGroup = "MsApprox",
        displayName = "Sky Tint",
        docstring = """,
        skyTint: Tweak the sky's contribution and color.  The        default, white (1,1,1),  gives results based on measured
        physical values.
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
    sunDirection = Attribute(
        name = 'sunDirection',
        as_type = 'vector3f',
        value = (0, 0, 1),
        displayGroup = "MsApprox",
        displayName = "Direction",
        docstring = """,
        sunDirection: The *apparent* direction towards the center        of the sun. The zenith  is at +Y (for noon light) and the horizon
        is in the XZ plane (for  sunrise/set).  Note that the Y component
        must non- negative.  Ignored if a month is given.
        """,

    )
    sunSize = Attribute(
        name = 'sunSize',
        as_type = 'float',
        value = 1,
        displayGroup = "MsApprox",
        displayName = "Sun Size",
        docstring = """,
        sunSize: Scale the apparent size of the sun in the sky.        Leave at 1 for a  realistic sun size with an 0.55 degree
        angular diameter.
        """,

    )
    sunTint = Attribute(
        name = 'sunTint',
        as_type = 'color3f',
        value = (1, 1, 1),
        displayGroup = "MsApprox",
        displayName = "Sun Tint",
        docstring = """,
        sunTint: Tweak the sun's contribution and color.  The        default, white (1,1,1),  gives results based on measured
        physical values. Setting this to black removes the sun
        contribution.
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
    year = Attribute(
        name = 'year',
        as_type = 'int',
        value = 2015,
        displayGroup = "MsApprox",
        displayName = "Year",
        docstring = """,
        year: Four-digit year.    This is ignored if month is 0.
        """,

    )
    zone = Attribute(
        name = 'zone',
        as_type = 'float',
        value = -8,
        displayGroup = "MsApprox",
        displayName = "Time Zone",
        docstring = """,
        zone: Standard time zone offset from GMT/UTC in hours.        Positive for east,  negative for west.  For example, this would
        be -8 for Pacific time.    This is ignored if month is 0.
        """,

    )

class PxrAovLight(Prim):
    """

    """

    as_type = "PxrAovLight"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:lightLink", "CollectionAPI:shadowLink"])
    aovName = Attribute(
        name = 'aovName',
        as_type = 'string',
        value = "",
        displayGroup = "Advanced",
        displayName = "AOV Name",
        docstring = """,
        The name of the AOV to write to.
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
    inPrimaryHit = Attribute(
        name = 'inPrimaryHit',
        as_type = 'bool',
        value = 1,
        displayGroup = "Refine",
        displayName = "In Primvary Hit",
        docstring = """,
        If this is on, the usual mask of the illuminated objects        is generated. If this is off, you can get a mask of only in the
        refraction or reflection.
        """,

    )
    inReflection = Attribute(
        name = 'inReflection',
        as_type = 'bool',
        value = 0,
        displayGroup = "Refine",
        displayName = "In Reflection",
        docstring = """,
        If this is on, the rays are traced through the specular        reflections to get  the masking signal.  Warning: this will
        require some amount of samples to get a clean mask.
        """,

    )
    inRefraction = Attribute(
        name = 'inRefraction',
        as_type = 'bool',
        value = 0,
        displayGroup = "Refine",
        displayName = "In Refraction",
        docstring = """,
        If this is on, the rays are traced through the glass        refractions  to get the masking signal.  Warning: this will
        require some amount of samples to get a clean mask.
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
    invert = Attribute(
        name = 'invert',
        as_type = 'bool',
        value = 0,
        displayGroup = "Refine",
        displayName = "Invert",
        docstring = """,
        If this is on, it inverts the signal for the AOV.
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
    onVolumeBoundaries = Attribute(
        name = 'onVolumeBoundaries',
        as_type = 'bool',
        value = 1,
        displayGroup = "Refine",
        displayName = "On Volume Boundaries",
        docstring = """,
        If this is on, the bounding box or shape of volumes will        appear in the mask. Since this is not always desirable, this can
        be turned off.
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
    useColor = Attribute(
        name = 'useColor',
        as_type = 'bool',
        value = 0,
        displayGroup = "Refine",
        displayName = "Use Color",
        docstring = """,
        If this is on, it outputs a RGB color image instead of a        float image for the AOV.
        """,

    )
    useThroughput = Attribute(
        name = 'useThroughput',
        as_type = 'bool',
        value = 1,
        displayGroup = "Refine",
        displayName = "Use Throughput",
        docstring = """,
        If this is on, the values in the mask for the reflected        or refracted rays will be affected by the strength of the reflection
        or refraction. This can lead to values below and above 1.0. Turn
        this off if you want a more solid mask.
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

class PxrIntMultLightFilter(Prim):
    """
    Multiplies the intensity of a given light.

    """

    as_type = "PxrIntMultLightFilter"
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

class PxrBarnLightFilter(Prim):
    """
    Simulated geometric barn doors that control the spread of light.

    """

    as_type = "PxrBarnLightFilter"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:filterLink"])
    apex = Attribute(
        name = 'analytic:apex',
        as_type = 'float',
        value = 0,
        docstring = """,
        Shear the projection along the Y axis.
        """,

    )
    exponent = Attribute(
        name = 'analytic:density:exponent',
        as_type = 'float',
        value = 0,
        docstring = """,
        Power exponent of the density interpolation.
        """,

    )
    farDistance = Attribute(
        name = 'analytic:density:farDistance',
        as_type = 'float',
        value = 0,
        docstring = """,
        Distance from the barn where the density interpolation        ends.
        """,

    )
    farValue = Attribute(
        name = 'analytic:density:farValue',
        as_type = 'float',
        value = 0,
        docstring = """,
        Density multiplier at the end of interpolation.
        """,

    )
    nearDistance = Attribute(
        name = 'analytic:density:nearDistance',
        as_type = 'float',
        value = 0,
        docstring = """,
        Distance from the barn where the density        interpolation starts.
        """,

    )
    nearValue = Attribute(
        name = 'analytic:density:nearValue',
        as_type = 'float',
        value = 0,
        docstring = """,
        Density multiplier where the density interpolation starts.
        """,

    )
    directional = Attribute(
        name = 'analytic:directional',
        as_type = 'bool',
        value = 0,
        docstring = """,
        When this is on, the texture projects along a direction        using the orthographic projection. When it is off, the texture
        projects using a focal point specified by the analytic:apex.
        """,

    )
    shearX = Attribute(
        name = 'analytic:shearX',
        as_type = 'float',
        value = 0,
        docstring = """,
        Shear the projection along the X axis.
        """,

    )
    shearY = Attribute(
        name = 'analytic:shearY',
        as_type = 'float',
        value = 0,
        docstring = """,
        Shear the projection along the Y axis.
        """,

    )
    useLightDirection = Attribute(
        name = 'analytic:useLightDirection',
        as_type = 'bool',
        value = 0,
        docstring = """,
        When this is on, If this is on, the projection direction        is determined by the position of the center of the light source.
        Otherwise, it only follows the orientation of the barn. WARNING:
        This does not work with dome and mesh lights.
        """,

    )
    barnMode = Attribute(
        name = 'barnMode',
        as_type = 'token',
        value = "physical",
        allowedTokens = ["physical", "analytic"],
        docstring = """,
        Chooses a physical or analytic evaluation model for        the barn.
        """,

    )
    bottom = Attribute(
        name = 'edge:bottom',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the top region.
        """,

    )
    left = Attribute(
        name = 'edge:left',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the left region.
        """,

    )
    right = Attribute(
        name = 'edge:right',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the left region.
        """,

    )
    top = Attribute(
        name = 'edge:top',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the top region.
        """,

    )
    edgeThickness = Attribute(
        name = 'edgeThickness',
        as_type = 'float',
        value = 0,
        docstring = """,
        Thickness of the edge region.  Larger values will        soften the edge shape.
        """,

    )
    height = Attribute(
        name = 'height',
        as_type = 'float',
        value = 1,
        docstring = """,
        Height of the inner region of the barn (Y axis).
        """,

    )
    preBarnEffect = Attribute(
        name = 'preBarnEffect',
        as_type = 'token',
        value = "noEffect",
        allowedTokens = ["noEffect", "cone", "noLight"],
        docstring = """,
        The effect on light before it reaches the barn        geometry.
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
        Radius of the corners of the inner barn square.
        """,

    )
    bottom = Attribute(
        name = 'refine:bottom',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the top region.
        """,

    )
    left = Attribute(
        name = 'refine:left',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the left region.
        """,

    )
    right = Attribute(
        name = 'refine:right',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the left region.
        """,

    )
    top = Attribute(
        name = 'refine:top',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the top region.
        """,

    )
    height = Attribute(
        name = 'scale:height',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scale the height of the inner barn shape.
        """,

    )
    width = Attribute(
        name = 'scale:width',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scale the width of the inner barn shape.
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
        Width of the inner region of the barn (X axis).
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

class PxrCookieLightFilter(Prim):
    """
    A textured surface that filters light.

    """

    as_type = "PxrCookieLightFilter"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:filterLink"])
    apex = Attribute(
        name = 'analytic:apex',
        as_type = 'float',
        value = 0,
        docstring = """,
        Shear the projection along the Y axis.
        """,

    )
    amount = Attribute(
        name = 'analytic:blur:amount',
        as_type = 'float',
        value = 0,
        docstring = """,
        Specify the blur of projected texture from 0-1. This        gets multiplied by the blurNear/blurFar interpolation. This
        blurs between the projected color and the fill color when the
        texture is not repeating.
        """,

    )
    exponent = Attribute(
        name = 'analytic:blur:exponent',
        as_type = 'float',
        value = 0,
        docstring = """,
        Power exponent of the blur interpolation.
        """,

    )
    farDistance = Attribute(
        name = 'analytic:blur:farDistance',
        as_type = 'float',
        value = 0,
        docstring = """,
        Distance from the cookie where the blur interpolation ends.
        """,

    )
    farValue = Attribute(
        name = 'analytic:blur:farValue',
        as_type = 'float',
        value = 0,
        docstring = """,
        Blur multiplier at the end of interpolation.
        """,

    )
    midpoint = Attribute(
        name = 'analytic:blur:midpoint',
        as_type = 'float',
        value = 0,
        docstring = """,
        Distance between near and far where midValue is located.
        """,

    )
    midValue = Attribute(
        name = 'analytic:blur:midValue',
        as_type = 'float',
        value = 0,
        docstring = """,
        Blur multiplier in the middle of interpolation.
        """,

    )
    nearDistance = Attribute(
        name = 'analytic:blur:nearDistance',
        as_type = 'float',
        value = 0,
        docstring = """,
        Distance from the cookie where the blur interpolation        starts.
        """,

    )
    nearValue = Attribute(
        name = 'analytic:blur:nearValue',
        as_type = 'float',
        value = 0,
        docstring = """,
        Blur multiplier where the blur interpolation starts.
        """,

    )
    sMult = Attribute(
        name = 'analytic:blur:sMult',
        as_type = 'float',
        value = 0,
        docstring = """,
        Blur multiplier in the S direction.
        """,

    )
    tMult = Attribute(
        name = 'analytic:blur:tMult',
        as_type = 'float',
        value = 0,
        docstring = """,
        Blur multiplier in the T direction.
        """,

    )
    exponent = Attribute(
        name = 'analytic:density:exponent',
        as_type = 'float',
        value = 0,
        docstring = """,
        Power exponent of the density interpolation.
        """,

    )
    farDistance = Attribute(
        name = 'analytic:density:farDistance',
        as_type = 'float',
        value = 0,
        docstring = """,
        Distance from the cookie where the density interpolation        ends.
        """,

    )
    farValue = Attribute(
        name = 'analytic:density:farValue',
        as_type = 'float',
        value = 0,
        docstring = """,
        Density multiplier at the end of interpolation.
        """,

    )
    midpoint = Attribute(
        name = 'analytic:density:midpoint',
        as_type = 'float',
        value = 0,
        docstring = """,
        Distance between near and far where midValue is located.
        """,

    )
    midValue = Attribute(
        name = 'analytic:density:midValue',
        as_type = 'float',
        value = 0,
        docstring = """,
        Density multiplier in the middle of interpolation.
        """,

    )
    nearDistance = Attribute(
        name = 'analytic:density:nearDistance',
        as_type = 'float',
        value = 0,
        docstring = """,
        Distance from the cookie where the density        interpolation starts.
        """,

    )
    nearValue = Attribute(
        name = 'analytic:density:nearValue',
        as_type = 'float',
        value = 0,
        docstring = """,
        Density multiplier where the density interpolation starts.
        """,

    )
    directional = Attribute(
        name = 'analytic:directional',
        as_type = 'bool',
        value = 0,
        docstring = """,
        When this is on, the texture projects along a direction        using the orthographic projection. When it is off, the texture
        projects using a focal point specified by the analytic:apex.
        """,

    )
    shearX = Attribute(
        name = 'analytic:shearX',
        as_type = 'float',
        value = 0,
        docstring = """,
        Shear the projection along the X axis.
        """,

    )
    shearY = Attribute(
        name = 'analytic:shearY',
        as_type = 'float',
        value = 0,
        docstring = """,
        Shear the projection along the Y axis.
        """,

    )
    useLightDirection = Attribute(
        name = 'analytic:useLightDirection',
        as_type = 'bool',
        value = 0,
        docstring = """,
        When this is on, If this is on, the projection direction        is determined by the position of the center of the light source.
        Otherwise, it only follows the orientation of the filter. WARNING:
        This does not work with dome and mesh lights.
        """,

    )
    contrast = Attribute(
        name = 'color:contrast',
        as_type = 'float',
        value = 1,
        docstring = """,
        Contrast control (less than 1 = contrast reduction,        larger than 1 = contrast increase).
        """,

    )
    midpoint = Attribute(
        name = 'color:midpoint',
        as_type = 'float',
        value = 0.18,
        docstring = """,
        Midpoint for the contrast control.
        """,

    )
    saturation = Attribute(
        name = 'color:saturation',
        as_type = 'float',
        value = 1,
        docstring = """,
        Saturation of the result (0=greyscale, 1=normal,        >1=boosted colors).
        """,

    )
    tint = Attribute(
        name = 'color:tint',
        as_type = 'color3f',
        docstring = """,
        Tint of the resulting color after saturation, contrast        and clamp.
        """,

    )
    whitepoint = Attribute(
        name = 'color:whitepoint',
        as_type = 'float',
        value = 1,
        docstring = """,
        White point for the contrast control if (contrast > 1.0).
        """,

    )
    cookieMode = Attribute(
        name = 'cookieMode',
        as_type = 'token',
        value = "physical",
        allowedTokens = ["physical", "analytic"],
        docstring = """,
        Chooses a physical or analytic evaluation model for        the cookie:
        - physical: The cookie behaves like a stained glass window
        through which light falls. The falloff and blur are determined
        by the size of the light, the distance to the light and distance
        from the cookie.
        - analytic: The cookie has a fixed projection and manual blur
        and falloff controls.
        """,

    )
    height = Attribute(
        name = 'height',
        as_type = 'float',
        value = 1,
        docstring = """,
        Height of the rect the light is shining through.
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
    fillColor = Attribute(
        name = 'texture:fillColor',
        as_type = 'color3f',
        docstring = """,
        If the texture is not repeating, this specifies the        color for the region outside of and behind the projected rectangle.
        """,

    )
    invertU = Attribute(
        name = 'texture:invertU',
        as_type = 'bool',
        value = 0,
        docstring = """,
        Flips the texture from left to right. By default, the        orientation of the texture as seen from the light source matches
        the orientation as it is viewed in an image viewer.
        """,

    )
    invertV = Attribute(
        name = 'texture:invertV',
        as_type = 'bool',
        value = 0,
        docstring = """,
        Flips the texture from top to bottom. By default, the        orientation of the texture as seen from the light source matches
        the orientation as it is viewed in an image viewer.
        """,

    )
    map_ = Attribute(
        name = 'texture:map',
        as_type = 'asset',
        docstring = """,
        A color texture to use on the cookie.  May use alpha.
        """,

    )
    offsetU = Attribute(
        name = 'texture:offsetU',
        as_type = 'float',
        value = 0,
        docstring = """,
        Offsets the texture in the U direction.
        """,

    )
    offsetV = Attribute(
        name = 'texture:offsetV',
        as_type = 'float',
        value = 0,
        docstring = """,
        Offsets the texture in the V direction.
        """,

    )
    scaleU = Attribute(
        name = 'texture:scaleU',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scales the U dimension.
        """,

    )
    scaleV = Attribute(
        name = 'texture:scaleV',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scales the V dimension.
        """,

    )
    wrapMode = Attribute(
        name = 'texture:wrapMode',
        as_type = 'token',
        value = "off",
        allowedTokens = ["off", "repeat", "clamp"],
        docstring = """,
        Specifies what value to use outside the texture's domain:        - off: no repeat
        - repeat: repeats in X and Y
        - clamp: uses the value from the nearest edge
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
        Width of the rect the light is shining through.
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

class PxrRampLightFilter(Prim):
    """
    A ramp to modulate how a light falls off with distance.

    """

    as_type = "PxrRampLightFilter"
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
    rampMode = Attribute(
        name = 'rampMode',
        as_type = 'token',
        value = "distanceToLight",
        allowedTokens = ["distanceToLight", "linear", "spherical", "radial"],
        docstring = """,
        Specifies the direction in which the ramp is applied
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

class PxrRodLightFilter(Prim):
    """
    Simulates a rod or capsule-shaped region to modulate light.

    """

    as_type = "PxrRodLightFilter"
    apiSchemas = Property(name='apiSchemas', values=["CollectionAPI:filterLink"])
    saturation = Attribute(
        name = 'color:saturation',
        as_type = 'float',
        value = 1,
        docstring = """,
        Saturation of the result (0=greyscale, 1=normal,        >1=boosted colors).
        """,

    )
    depth = Attribute(
        name = 'depth',
        as_type = 'float',
        value = 1,
        docstring = """,
        Depth of the inner region of the rod (Z axis).
        """,

    )
    back = Attribute(
        name = 'edge:back',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the back region.
        """,

    )
    bottom = Attribute(
        name = 'edge:bottom',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the top region.
        """,

    )
    front = Attribute(
        name = 'edge:front',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the front region.
        """,

    )
    left = Attribute(
        name = 'edge:left',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the left region.
        """,

    )
    right = Attribute(
        name = 'edge:right',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the left region.
        """,

    )
    top = Attribute(
        name = 'edge:top',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the top region.
        """,

    )
    edgeThickness = Attribute(
        name = 'edgeThickness',
        as_type = 'float',
        value = 0,
        docstring = """,
        Thickness of the edge region.  Larger values will        soften the edge shape.
        """,

    )
    height = Attribute(
        name = 'height',
        as_type = 'float',
        value = 1,
        docstring = """,
        Height of the inner region of the rod (Y axis).
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
        Radius of the corners of the inner rod box.
        """,

    )
    back = Attribute(
        name = 'refine:back',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the back region.
        """,

    )
    bottom = Attribute(
        name = 'refine:bottom',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the top region.
        """,

    )
    front = Attribute(
        name = 'refine:front',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the front region.
        """,

    )
    left = Attribute(
        name = 'refine:left',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the left region.
        """,

    )
    right = Attribute(
        name = 'refine:right',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the left region.
        """,

    )
    top = Attribute(
        name = 'refine:top',
        as_type = 'float',
        value = 0,
        docstring = """,
        Additional adjustment to the top region.
        """,

    )
    depth = Attribute(
        name = 'scale:depth',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scale the depth of the inner rod shape.
        """,

    )
    height = Attribute(
        name = 'scale:height',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scale the height of the inner rod shape.
        """,

    )
    width = Attribute(
        name = 'scale:width',
        as_type = 'float',
        value = 1,
        docstring = """,
        Scale the width of the inner rod shape.
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
        Width of the inner region of the rod (X axis).
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