# encoding: utf-8
# module adlx.ADLX
# by generator 1.147
""" ADLX python binding for all interfaces """

from typing import List, Tuple, Dict, Any, Optional

class ADLX_RESULT:
    """Indicates the result returned from an ADLX function or from an ADLX method.

    More info at: https://gpuopen.com/manuals/adlx/adlx-enumerations/#adlx-result
    """

    # fmt:off
    ADLX_OK = None                      # (!) This result indicates success. Real value is '<ADLX_RESULT.ADLX_OK: 0>'
    ADLX_ALREADY_ENABLED = None         # (!) This result indicates that the asked action is already enabled. Real value is '<ADLX_RESULT.ADLX_ALREADY_ENABLED: 1>'
    ADLX_ALREADY_INITIALIZED = None     # (!) This result indicates that ADLX has a unspecified type of initialization. Real value is '<ADLX_RESULT.ADLX_ALREADY_INITIALIZED: 2>'
    ADLX_FAIL = None                    # (!) This result indicates an unspecified failure. Real value is '<ADLX_RESULT.ADLX_FAIL: 3>'
    ADLX_INVALID_ARGS = None            # (!) This result indicates that the arguments are invalid. Real value is '<ADLX_RESULT.ADLX_INVALID_ARGS: 4>'
    ADLX_BAD_VER = None                 # (!) This result indicates that the asked version is incompatible with the current version. Real value is '<ADLX_RESULT.ADLX_BAD_VER: 5>'
    ADLX_UNKNOWN_INTERFACE = None       # (!) This result indicates that an unknown interface was asked. Real value is '<ADLX_RESULT.ADLX_UNKNOWN_INTERFACE: 6>'
    ADLX_TERMINATED = None              # (!) This result indicates that the calls were made in an interface after ADLX was terminated. Real value is '<ADLX_RESULT.ADLX_TERMINATED: 7>'
    ADLX_ADL_INIT_ERROR = None          # (!) This result indicates that the ADL initialization failed. Real value is '<ADLX_RESULT.ADLX_ADL_INIT_ERROR: 8>'
    ADLX_NOT_FOUND = None               # (!) This result indicates that the item is not found. Real value is '<ADLX_RESULT.ADLX_NOT_FOUND: 9>'
    ADLX_INVALID_OBJECT = None          # (!) This result indicates that the method was called into an invalid object. Real value is '<ADLX_RESULT.ADLX_INVALID_OBJECT: 10>'
    ADLX_ORPHAN_OBJECTS = None          # (!) This result indicates that ADLX was terminated with outstanding ADLX objects. Any interface obtained from ADLX points to invalid memory and calls in their methods will result in unexpected behavior. Real value is '<ADLX_RESULT.ADLX_ORPHAN_OBJECTS: 11>'
    ADLX_NOT_SUPPORTED = None           # (!) This result indicates that the asked feature is not supported. Real value is '<ADLX_RESULT.ADLX_NOT_SUPPORTED: 12>'
    ADLX_PENDING_OPERATION = None       # (!) This result indicates a failure due to an operation currently in progress. Real value is '<ADLX_RESULT.ADLX_PENDING_OPERATION: 13>'
    ADLX_GPU_INACTIVE = None            # (!) This result indicates that the GPU is inactive. Real value is '<ADLX_RESULT.ADLX_GPU_INACTIVE: 14>'
    ADLX_GPU_IN_USE = None              # (!) This result indicates that the GPU is in used by applications. Real value is '<ADLX_RESULT.ADLX_GPU_IN_USE: 15>'
    ADLX_TIMEOUT_OPERATION = None       # (!) This result indicates that the operation is timeout. Real value is '<ADLX_RESULT.ADLX_TIMEOUT_OPERATION: 16>'
    ADLX_NOT_ACTIVE = None              # (!) This result indicates that the asked feature is inactive. Real value is '<ADLX_RESULT.ADLX_NOT_ACTIVE: 17>'
    ADLX_RESET_NEEDED = None            # (!) This result indicates that the specified feature needs to be reset to factory settings. Real value is '<ADLX_RESULT.ADLX_RESET_NEEDED: 18>'
    # fmt:on

class ADLX_3DLUT_COLORSPACE:
    """Indicates the custom 3D LUT color space."""

    CS_BT2020 = None
    CS_DCIP3 = None
    CS_NATIVE = None
    CS_SRGB = None

class ADLX_3DLUT_TRANSFER_FUNCTION:
    """Indicates the User 3D LUT transfer function."""

    TF_G22 = None
    TF_PQ = None
    TF_SRGB = None

class ADLX_AFMF_ALGORITHM:
    """Indicates the AMD Fluid Motion Frames algorithm type."""

    AFMF_ALGORITHM_AUTO = None
    AFMF_ALGORITHM_ENHANCED = None
    AFMF_ALGORITHM_STANDARD = None

class ADLX_AFMF_FAST_MOTION_RESP:
    """Indicates the AMD Fluid Motion Frames fast motion response type."""

    AFMF_RESP_BLENDED_FRAMES = None
    AFMF_RESP_REPEAT_FRAMES = None

class ADLX_AFMF_PERFORMANCE_MODE_TYPE:
    """Indicates the AMD Fluid Motion Frames performance mode type."""

    AFMF_PERFORMANCE_MODE_AUTO = None
    AFMF_PERFORMANCE_MODE_PERFORMANCE = None
    AFMF_PERFORMANCE_MODE_QUALITY = None

class ADLX_AFMF_SEARCH_MODE_TYPE:
    """Indicates the AMD Fluid Motion Frames search mode type."""

    AFMF_SEARCH_MODE_AUTO = None
    AFMF_SEARCH_MODE_HIGH = None
    AFMF_SEARCH_MODE_STANDARD = None

class ADLX_SSM_BIAS_MODE:
    """Indicates the SmartShift Max bias mode."""

    SSM_BIAS_AUTO = None    # (!) Automatic bias mode
    SSM_BIAS_MANUAL = None  # (!) Manual bias mode

class ADLX_SMARTSHIFT_ECO_INACTIVE_REASON:
    """Indicates the reason SmartShift Eco is inactive."""

    INACTIVE_REASON_UNKNOWN = None                           # (!) Unknown reason
    INACTIVE_REASON_PRIMARY_DISPLAY_CONNECTED_TO_DGPU = None # (!) Primary display connected to dGPU
    INACTIVE_REASON_DETACHABLE_GPU_CONNECTED = None          # (!) Detachable GPU connected
    INACTIVE_REASON_SESSION_INACTIVE = None                  # (!) Session inactive
    INACTIVE_REASON_MULTIPLE_SESSION_ACTIVE = None           # (!) Multiple sessions active

class ADLX_VARIABLE_GRAPHICS_MEMORY_MODE:
    """Indicates the Variable Graphics Memory mode."""

    VARIABLE_GRAPHICS_MEMORY_MODE_AUTO = None    # (!) Automatic mode
    VARIABLE_GRAPHICS_MEMORY_MODE_CUSTOM = None  # (!) Custom mode

class ADLX_ANISOTROPIC_FILTERING_LEVEL:
    """Indicates the Anisotropic Filtering level."""

    AF_LEVEL_INVALID = None  # (!) The Anisotropic Filtering level is invalid
    AF_LEVEL_X2 = None       # (!) The Anisotropic Filtering level is 2X
    AF_LEVEL_X4 = None       # (!) The Anisotropic Filtering level is 4X
    AF_LEVEL_X8 = None       # (!) The Anisotropic Filtering level is 8X
    AF_LEVEL_X16 = None      # (!) The Anisotropic Filtering level is 16X

class ADLX_ANTILAG_STATE:
    """Indicates the Anti-Lag state."""

    ANTILAG = None
    ANTILAGNEXT = None

class ADLX_ANTI_ALIASING_LEVEL:
    """Indicates the anti-aliasing level."""

    AA_LEVEL_INVALID = None  # (!) The anti-aliasing level is invalid
    AA_LEVEL_2X = None       # (!) The anti-aliasing level is 2X
    AA_LEVEL_2XEQ = None     # (!) The anti-aliasing level is 2XEQ
    AA_LEVEL_4X = None       # (!) The anti-aliasing level is 4X
    AA_LEVEL_4XEQ = None     # (!) The anti-aliasing level is 4XEQ
    AA_LEVEL_8X = None       # (!) The anti-aliasing level is 8X
    AA_LEVEL_8XEQ = None     # (!) The anti-aliasing level is 8XEQ

class ADLX_ANTI_ALIASING_METHOD:
    """Indicates the anti-aliasing method."""

    AA_METHOD_MULTISAMPLING = None           # (!) The multi-sampling method
    AA_METHOD_ADAPTIVE_MULTISAMPLING = None  # (!) The adaptive multi-sampling method
    AA_METHOD_SUPERSAMPLING = None           # (!) The super-sampling method

class ADLX_ANTI_ALIASING_MODE:
    """Indicates the anti-aliasing mode."""

    AA_MODE_USE_APP_SETTINGS = None       # (!) The anti-aliasing mode uses application settings
    AA_MODE_ENHANCE_APP_SETTINGS = None   # (!) The anti-aliasing mode enhances the application settings
    AA_MODE_OVERRIDE_APP_SETTINGS = None  # (!) The anti-aliasing mode overrides the application settings

class ADLX_APP_GPU_DEPENDENCY:
    """Indicates the application GPU dependency."""

    APP_GPU_UNKNOWN = None     # (!) The application GPU dependency is unknown
    APP_GPU_BOUND = None       # (!) The application is bound to the GPU
    APP_GPU_NOT_BOUND = None   # (!) The application is not bound to the GPU

class ADLX_ASIC_FAMILY_TYPE:
    """Indicates the ASIC family type."""

    ASIC_UNDEFINED = None   # (!) The ASIC family type is not defined
    ASIC_RADEON = None      # (!) The ASIC family type is discrete
    ASIC_FIREPRO = None     # (!) The ASIC family type is Firepro
    ASIC_FIREMV = None      # (!) The ASIC family type is FireMV
    ASIC_FIRESTREAM = None  # (!) The ASIC family type is FireStream
    ASIC_FUSION = None      # (!) The ASIC family type is Fusion
    ASIC_EMBEDDED = None    # (!) The ASIC family type is Embedded

class ADLX_COLOR_DEPTH:
    """Indicates the color/bit depth, which is the number of bits used to indicate the color of a single pixel."""

    BPC_6 = None   # (!) A color component/pixel with 6 bits
    BPC_8 = None   # (!) A color component/pixel with 8 bits
    BPC_10 = None  # (!) A color component/pixel with 10 bits
    BPC_12 = None  # (!) A color component/pixel with 12 bits
    BPC_14 = None  # (!) A color component/pixel with 14 bits
    BPC_16 = None  # (!) A color component/pixel with 16 bits

class ADLX_DESKTOP_TYPE:
    """Types of desktops in respect to display composition."""

    DESKTOP_SINGLE = None     # (!) Single display desktop: one display showing the entire desktop
    DESKTOP_DUPLCATE = None   # (!) Duplicate desktop: two or more displays each show the entire desktop
    DESKTOP_EYEFINITY = None  # (!) AMD Eyefinity desktop: two or more displays each show a portion of the desktop

class ADLX_DISPLAY_CONNECTOR_TYPE:
    """Indicates the display connector type."""

    DISPLAY_CONTYPE_COMPOSITE = None
    DISPLAY_CONTYPE_CVDONGLE_JPN = None
    DISPLAY_CONTYPE_CVDONGLE_NONI2C_JPN = None
    DISPLAY_CONTYPE_CVDONGLE_NONI2C_NTSC = None
    DISPLAY_CONTYPE_CVDONGLE_NTSC = None
    DISPLAY_CONTYPE_DISPLAYPORT = None
    DISPLAY_CONTYPE_DVI_D = None
    DISPLAY_CONTYPE_DVI_I = None
    DISPLAY_CONTYPE_EDP = None
    DISPLAY_CONTYPE_HDMI_TYPE_A = None
    DISPLAY_CONTYPE_HDMI_TYPE_B = None
    DISPLAY_CONTYPE_RCA_3COMPONENT = None
    DISPLAY_CONTYPE_SVIDEO = None
    DISPLAY_CONTYPE_UNKNOWN = None
    DISPLAY_CONTYPE_USB_TYPE_C = None
    DISPLAY_CONTYPE_VGA = None
    DISPLAY_CONTYPE_WIRELESSDISPLAY = None

class ADLX_DISPLAY_SCAN_TYPE:
    """Indicates the display scan type."""

    PROGRESSIVE = None  # (!) The display scan type is progressive mode
    INTERLACED = None   # (!) The display scan type is interlaced mode

class ADLX_DISPLAY_TYPE:
    """Indicates the display type."""

    DISPLAY_TYPE_UNKOWN = None              # (!) The display type is an unknown display
    DISPLAY_TYPE_MONITOR = None             # (!) The display type is a monitor display
    DISPLAY_TYPE_TELEVISION = None          # (!) The display type is a TV display
    DISPLAY_TYPE_LCD_PANEL = None           # (!) The display type is an LCD display
    DISPLAY_TYPE_DIGITAL_FLAT_PANEL = None  # (!) The display type is a DFP display
    DISPLAY_TYPE_COMPONENT_VIDEO = None     # (!) The display type is a component video display
    DISPLAY_TYPE_PROJECTOR = None           # (!) The display type is a projector display

class ADLX_GAMUT_SPACE:
    """Indicates the predefined gamut space."""

    GAMUT_SPACE_CCIR_709 = None   # (!) The predefined gamut space is GAMUT_SPACE_CCIR_709
    GAMUT_SPACE_CCIR_601 = None   # (!) The predefined gamut space is GAMUT_SPACE_CCIR_601
    GAMUT_SPACE_ADOBE_RGB = None  # (!) The predefined gamut space is GAMUT_SPACE_ADOBE_RGB
    GAMUT_SPACE_CIE_RGB = None    # (!) The predefined gamut space is GAMUT_SPACE_CIE_RGB
    GAMUT_SPACE_CCIR_2020 = None  # (!) The predefined gamut space is GAMUT_SPACE_CCIR_2020
    GAMUT_SPACE_CUSTOM = None     # (!) The predefined gamut space is GAMUT_SPACE_CUSTOM

class ADLX_GPU_TYPE:
    """Indicates the GPU type."""

    GPUTYPE_UNDEFINED = None    # (!) The GPU type is unknown
    GPUTYPE_INTEGRATED = None   # (!) The GPU type is an integrated GPU
    GPUTYPE_DISCRETE = None     # (!) The GPU type is a discrete GPU

class ADLX_HG_TYPE:
    """Indicates the type of Hybrid Graphic.

    More info at: https://gpuopen.com/manuals/adlx/adlx-enumerations/#adlx-hg-type
    """

    NONE = None   # (!) This is not a Hybrid Graphics system. Real value is '<ADLX_HG_TYPE.NONE: 0>'
    AMD = None    # (!) This is an AMD integrated GPU. Real value is '<ADLX_HG_TYPE.AMD: 1>'
    OTHER = None  # (!) This is a non-AMD integrated GPU. Real value is '<ADLX_HG_TYPE.OTHER: 2>'

class ADLX_I2C_LINE:
    """Indicates the I2C line options."""

    I2C_LINE_OEM = None          # (!) The I2C line is OEM
    I2C_LINE_OD_CONTROL = None   # (!) The I2C line is Over Driver Control
    I2C_LINE_OEM2 = None         # (!) The I2C line is OEM2
    I2C_LINE_OEM3 = None         # (!) The I2C line is OEM3
    I2C_LINE_OEM4 = None         # (!) The I2C line is OEM4
    I2C_LINE_OEM5 = None         # (!) The I2C line is OEM5
    I2C_LINE_OEM6 = None         # (!) The I2C line is OEM6

class ADLX_LOG_DESTINATION:
    """Indicates the location of the log traces that are generated from the internal code execution of ADLX."""

    LOCALFILE = None    # (!) The log destination is a file
    DBGVIEW = None      # (!) The log destination is the application debugger
    APPLICATION = None  # (!) The log destination is the application

class ADLX_LOG_SEVERITY:
    """Indicates the severity level for ADLX logs."""

    LDEBUG = None     # (!) The log captures errors, warnings and debug information
    LWARNING = None   # (!) The log captures errors and warnings
    LERROR = None     # (!) The log captures errors

class ADLX_MEMORYTIMING_DESCRIPTION:
    """Indicates the memory timing description."""

    MEMORYTIMING_DEFAULT = None                # (!) The memory timing is default
    MEMORYTIMING_FAST_TIMING = None            # (!) The memory timing is fast timing
    MEMORYTIMING_FAST_TIMING_LEVEL_2 = None    # (!) The memory timing is fast timing level 2
    MEMORYTIMING_AUTOMATIC = None              # (!) The memory timing is automatic
    MEMORYTIMING_MEMORYTIMING_LEVEL_1 = None   # (!) The memory timing is level 1
    MEMORYTIMING_MEMORYTIMING_LEVEL_2 = None   # (!) The memory timing is level 2

class ADLX_MGPU_MODE:
    """Indicates the multi-GPU mode."""

    MGPU_NONE = None       # (!) This GPU is not in Multi-GPU mode
    MGPU_PRIMARY = None    # (!) This is the Primary GPU in Multi-GPU mode
    MGPU_SECONDARY = None  # (!) This is the Secondary GPU in Multi-GPU mode

class ADLX_ORIENTATION:
    """Indicates the orientation."""

    ORIENTATION_LANDSCAPE = None          # (!) The orientation is landscape
    ORIENTATION_PORTRAIT = None           # (!) The orientation is Portrait
    ORIENTATION_LANDSCAPE_FLIPPED = None  # (!) The orientation is landscape (flipped)
    ORIENTATION_PORTRAIT_FLIPPED = None   # (!) The orientation is Portrait (flipped)

class ADLX_DP_LINK_RATE:
    """Indicates the DP link rate."""

    DP_LINK_RATE_UNKNOWN = None    # (!) The DP link rate is unknown
    DP_LINK_RATE_RBR = None        # (!) The DP link rate is 1.62 Gbps/Lane
    DP_LINK_RATE_2_16GBPS = None   # (!) The DP link rate is 2.16 Gbps/Lane
    DP_LINK_RATE_2_43GBPS = None   # (!) The DP link rate is 2.43 Gbps/Lane
    DP_LINK_RATE_HBR = None        # (!) The DP link rate is 2.70 Gbps/Lane
    DP_LINK_RATE_4_32GBPS = None   # (!) The DP link rate is 4.32 Gbps/Lane
    DP_LINK_RATE_HBR2 = None       # (!) The DP link rate is 5.40 Gbps/Lane
    DP_LINK_RATE_HBR3 = None       # (!) The DP link rate is 8.10 Gbps/Lane
    DP_LINK_RATE_UHBR10 = None     # (!) The DP link rate is 10 Gbps/Lane
    DP_LINK_RATE_UHBR13D5 = None   # (!) The DP link rate is 13.5 Gbps/Lane
    DP_LINK_RATE_UHBR20 = None     # (!) The DP link rate is 20 Gbps/Lane

class ADLX_PCI_BUS_TYPE:
    """Indicates the PCI bus type."""

    UNDEFINED = None  # (!) The PCI bus type is not defined
    PCI = None        # (!) The PCI bus type is PCI bus
    AGP = None        # (!) The PCI bus type is AGP bus
    PCIE = None       # (!) The PCI bus type is PCI Express bus
    PCIE_2_0 = None   # (!) The PCI bus type is PCI Express 2nd generation bus
    PCIE_3_0 = None   # (!) The PCI bus type is PCI Express 3rd generation bus
    PCIE_4_0 = None   # (!) The PCI bus type is PCI Express 4th generation bus
    PCIE_5_0 = None   # (!) The PCI bus type is PCI Express 5th generation bus

class ADLX_PIXEL_FORMAT:
    """Indicates the pixel format to encode images for the display."""

    FORMAT_UNKNOWN = None      # (!) The pixel format is unknown
    RGB_444_FULL = None        # (!) The pixel format is RGB 4:4:4 PC Standard (Full RGB)
    RGB_444_LIMITED = None     # (!) The pixel format is RGB 4:4:4 Studio (Limited RGB)
    YCBCR_420 = None           # (!) The pixel format is YCbCr 4:2:0 Pixel Format
    YCBCR_422 = None           # (!) The pixel format is YCbCr 4:2:2
    YCBCR_444 = None           # (!) The pixel format is YCbCr 4:4:4

class ADLX_SCALE_MODE:
    """Indicates the methods to stretch and position the image to fit on the display."""

    PRESERVE_ASPECT_RATIO = None  # (!) The scale mode preserves aspect ratio
    FULL_PANEL = None             # (!) The scale mode extends to full panel
    CENTERED = None               # (!) The scale mode is centered on screen

class ADLX_SYNC_ORIGIN:
    """Indicates the origin of an event."""

    SYNC_ORIGIN_UNKNOWN = None   # (!) The event origin is unknown
    SYNC_ORIGIN_INTERNAL = None  # (!) The event is from an ADLX setting
    SYNC_ORIGIN_EXTERNAL = None  # (!) The event is from an external setting (such as AMD Adrenalin Edition, or third party app)

class ADLX_TESSELLATION_LEVEL:
    """Indicates the tessellation level on a GPU."""

    T_LEVEL_OFF = None   # (!) The tessellation level is Off
    T_LEVEL_2X = None    # (!) The tessellation level is 2X
    T_LEVEL_4X = None    # (!) The tessellation level is 4X
    T_LEVEL_6X = None    # (!) The tessellation level is 6X
    T_LEVEL_8X = None    # (!) The tessellation level is 8X
    T_LEVEL_16X = None   # (!) The tessellation level is 16X
    T_LEVEL_32X = None   # (!) The tessellation level is 32X
    T_LEVEL_64X = None   # (!) The tessellation level is 64X

class ADLX_TESSELLATION_MODE:
    """Indicates the tessellation setting on a GPU."""

    T_MODE_AMD_OPTIMIZED = None         # (!) This mode uses AMD optimization
    T_MODE_USE_APP_SETTINGS = None      # (!) This mode uses application settings
    T_MODE_OVERRIDE_APP_SETTINGS = None # (!) This mode uses override application settings

class ADLX_TIMING_STANDARD:
    """Timing standard for custom resolution."""

    CVT = None       # (!) Coordinated Video Timings(CVT) VESA standard for generating and defining the display timings
    CVT_RB = None    # (!) Coordinated Video Timings-Reduced Blanking(CVT-RB). Reduces horizontal and vertical blanking periods
    DMT = None       # (!) Display Monitor Timmings(DMT). VESA standard that lists pre-defined display timings
    GTF = None       # (!) Generalized Timing Formula(GTF). A method of generating industry standard display timings
    MANUAL = None    # (!) Manual control

class ADLX_WAIT_FOR_VERTICAL_REFRESH_MODE:
    """Indicates the modes of VSync settings."""

    WFVR_ALWAYS_OFF = None                 # (!) VSync is always off
    WFVR_OFF_UNLESS_APP_SPECIFIES = None   # (!) VSync is off, unless specified by the application
    WFVR_ON_UNLESS_APP_SPECIFIES = None    # (!) VSync is on, unless specified by application
    WFVR_ALWAYS_ON = None                  # (!) VSync is always on

class ADLX_WHITE_POINT:
    """Indicates the standardized white point setting."""

    WHITE_POINT_5000K = None   # (!) The white point setting is 5000k
    WHITE_POINT_6500K = None   # (!) The white point setting is 6500k
    WHITE_POINT_7500K = None   # (!) The white point setting is 7500k
    WHITE_POINT_9300K = None   # (!) The white point setting is 9300k
    WHITE_POINT_CUSTOM = None  # (!) The white point setting is customized

class ADLX_CustomResolution:
    """This structure contains information for custom resolution parameters on a given display."""

    resWidth: int                           # The resolution width
    resHeight: int                          # The resolution height
    refreshRate: int                        # The refresh rate
    presentation: int                       # The presentation method, 0 PROGRESSIVE; 1 INTERLACED
    timingStandard: ADLX_TIMING_STANDARD   # The display timing standard
    GPixelClock: int                        # The speed at which pixels are transmitted within on a refresh cycle
    detailedTiming: bool                    # The detailed timing information

class ADLX_GamutColorSpace:
    """This structure contains information on driver-supported gamut coordinates."""

    red: ADLX_Point    # The red channel chromaticity coordinate
    green: ADLX_Point  # The green channel chromaticity coordinate
    blue: ADLX_Point   # The blue channel chromaticity coordinate

class ADLX_IntRange:
    """This structure contains information on the integer range."""

    minValue: int  # The minimum integer value
    maxValue: int  # The maximum integer value
    step: int      # The accepted integer range step

class ADLX_UINT16_RGB:
    """This structure contains information on the RGB."""

    red: int  # The red integer value
    green: int  # The green integer value
    blue: int      # The blue integer value

class ADLX_LUID:
    """This structure contains the locally unique identifier information of the adapter."""

    highPart: int  # The high part of the LUID
    lowPart: int   # The low part of the LUID

class ADLX_Point:
    """This structure contains information on driver point coordinates, and is used to store the driver-point coordinates for gamut, as well as white point."""

    x: int  # The x coordinate
    y: int  # The y coordinate

class ADLX_RGB:
    """This structure contains RGB information."""

    gamutR: float  # Red
    gamutG: float  # Green
    gamutB: float  # Blue

class ADLX_RegammaCoeff:
    """This structure contains information on driver-supported re-gamma coefficients used to build the re-gamma curve."""

    coefficientA0: int  # The a0 gamma coefficient
    coefficientA1: int  # The a1 gamma coefficient
    coefficientA2: int  # The a2 gamma coefficient
    coefficientA3: int  # The a3 gamma coefficient
    gamma: int          # The regamma divider

class ADLX_TimingInfo:
    """This structure contains display timing information."""

    timingFlags: int    # The detailed timing flag
    hTotal: int         # The total number of pixels that compose all scan lines during a horizontal sync
    hDisplay: int       # The number of horizontal pixels within the active area
    hFrontPorch: int    # The number of horizontal pixels between the end of the active area and the next sync
    hSyncWidth: int     # The number of pixels that compose a scan line during a horizontal sync
    hPolarity: int      # The horizontal polarity of sync signals, 0 POSITIVE; 1 NEGATIVE
    vTotal: int         # The total number of vertical pixels permitted/processed per sync
    vDisplay: int       # The number of vertical pixels within the active display area
    vFrontPorch: int    # The number of vertical pixels between the end of the active area and the next sync
    vSyncWidth: int     # The number of vertical pixels permitted/processed during a sync
    vPolarity: int      # The vertical polarity of sync signals, 0 POSITIVE; 1 NEGATIVE

class IADLXInterface:
    """The base interface for all ADLX interfaces."""

    def Acquire(self) -> int:
        """Increments the reference count."""
        pass

    def Release(self) -> int:
        """Decrements the reference count."""
        pass

    def QueryInterface(self, interfaceId: str):
        """Queries for a different interface."""
        pass

class IADLMapping(IADLXInterface):
    """The IADLMapping interface provides methods to convert between ADL and ADLX data."""

    def ADLIdsFromADLXDesktop(self, pDesktop: IADLXDesktop) -> PyADLIdsFromADLX:
        """Gets ADL IDs from an ADLX desktop.
        
        Returns:
            PyADLIdsFromADLX: Object containing adapterIndex, VidPnSourceId, bus, device, and function.
        """
        pass

    def ADLIdsFromADLXDisplay(self, pDisplay: IADLXDisplay) -> PyADLIdsFromADLX:
        """Gets ADL IDs from an ADLX display.
        
        Returns:
            PyADLIdsFromADLX: Object containing adapterIndex, VidPnSourceId, bus, device, and function.
        """
        pass

    def AdlAdapterIndexFromADLXGPU(self, pGPU: IADLXGPU) -> int | None:
        """Gets ADL adapter index from an ADLX GPU.
        
        Returns:
            int | None: Adapter index if successful, None otherwise.
        """
        pass

    def BdfFromADLXGPU(self, pGPU: IADLXGPU) -> PyBdfFromADLXGPU:
        """Gets BDF (Bus, Device, Function) from an ADLX GPU.
        
        Returns:
            PyBdfFromADLXGPU: Object containing bus, device, and function.
        """
        pass

    def GetADLXDesktopFromADLIds(self, adapterIndex: int, VidPnSource: int, bus: int, device: int, function: int) -> IADLXDesktop | None:
        """Gets an ADLX desktop from ADL IDs.
        
        Returns:
            IADLXDesktop | None: Desktop interface if found, None otherwise.
        """
        pass

    def GetADLXDisplayFromADLIds(self, adapterIndex: int, displayIndex: int, bus: int, device: int, function: int) -> IADLXDisplay | None:
        """Gets an ADLX display from ADL IDs.
        
        Returns:
            IADLXDisplay | None: Display interface if found, None otherwise.
        """
        pass

    def GetADLXGPUFromAdlAdapterIndex(self, adlAdapterIndex: int) -> IADLXGPU | None:
        """Gets an ADLX GPU from ADL adapter index.
        
        Returns:
            IADLXGPU | None: GPU interface if found, None otherwise.
        """
        pass

    def GetADLXGPUFromBdf(self, bus: int, device: int, function: int) -> IADLXGPU | None:
        """Gets an ADLX GPU from BDF (Bus, Device, Function).
        
        Returns:
            IADLXGPU | None: GPU interface if found, None otherwise.
        """
        pass

    def GetADLXGPUFromBdf(self, bus: int, device: int, function: int) -> IADLXGPU:
        """Gets an ADLX GPU from BDF."""
        pass

class IADLX3DImageSharpenDesktop(IADLXInterface):
    """The IADLX3DImageSharpenDesktop interface provides methods for AMD Radeon Image Sharpening on desktop."""

    def IsEnabled(self) -> bool:
        """Checks if Image Sharpening is enabled."""
        pass

    def IsSupported(self) -> bool:
        """Checks if Image Sharpening is supported."""
        pass

    def SetEnabled(self, enabled: bool) -> ADLX_RESULT:
        """Sets Image Sharpening enabled state."""
        pass

class IADLX3DRadeonSuperResolution(IADLXInterface):
    """The IADLX3DRadeonSuperResolution interface provides methods for AMD Radeon Super Resolution.
    
    Radeon Super Resolution is an upscaling feature for faster game frame rates.
    """

    def IsSupported(self) -> bool:
        """Checks if Radeon Super Resolution is supported.
        
        Returns:
            bool: True if supported, False otherwise.
        """
        pass

    def IsEnabled(self) -> bool | None:
        """Checks if Radeon Super Resolution is enabled.
        
        Returns:
            bool | None: True if enabled, False if disabled, None if query fails.
        """
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets the activation status of Radeon Super Resolution.
        
        Args:
            enable: The new state. Set True to enable, False to disable.
            
        Returns:
            ADLX_RESULT: ADLX_OK if successful, error code otherwise.
        """
        pass

    def GetSharpnessRange(self) -> Dict[str, int]:
        """Gets the Radeon Super Resolution sharpness range.
        
        Returns:
            Dict[str, int]: Dictionary with keys 'maxValue', 'minValue', and 'step'.
        """
        pass

    def GetSharpness(self) -> int | None:
        """Gets the Radeon Super Resolution current sharpness.
        
        Returns:
            int | None: Current sharpness value if successful, None otherwise.
        """
        pass

    def SetSharpness(self, sharpness: int) -> ADLX_RESULT:
        """Sets the Radeon Super Resolution sharpness.
        
        Args:
            sharpness: The new sharpness value.
            
        Returns:
            ADLX_RESULT: ADLX_OK if successful, error code otherwise.
        """
        pass

class IADLXApplication(IADLXInterface):
    """The IADLXApplication interface provides information about an application."""

    def FullPath(self) -> str:
        """Gets the full path of the application."""
        pass

    def GPUDependencyType(self) -> ADLX_APP_GPU_DEPENDENCY:
        """Gets the GPU dependency type of the application."""
        pass

    def Name(self) -> str:
        """Gets the name of the application."""
        pass

    def ProcessID(self) -> int:
        """Gets the process ID of the application."""
        pass

class IADLXChangedEvent(IADLXInterface):
    """The IADLXChangedEvent interface provides methods for handling changed events."""

    def GetOrigin(self) -> ADLX_SYNC_ORIGIN:
        """Gets the origin of the event."""
        pass

class IADLXDisplay3DLUTChangedEvent(IADLXInterface):
    """The IADLXDisplay3DLUTChangedEvent interface provides methods for handling display 3D LUT changed events."""

    def GetDisplay(self):
        """Gets the display interface."""
        pass

    def GetOrigin(self) -> ADLX_SYNC_ORIGIN:
        """Gets the origin of the event."""
        pass

    def IsCustom3DLUTChanged(self) -> bool:
        """Checks if custom 3D LUT is changed."""
        pass

    def IsSCEChanged(self) -> bool:
        """Checks if SCE is changed."""
        pass

class IADLXDisplayBlanking(IADLXInterface):
    """The IADLXDisplayBlanking interface provides methods for display blanking control."""

    def IsCurrentBlanked(self) -> bool:
        """Checks if display is currently blanked."""
        pass

    def IsCurrentUnblanked(self) -> bool:
        """Checks if display is currently unblanked."""
        pass

    def IsSupported(self) -> bool:
        """Checks if display blanking is supported."""
        pass

    def SetBlanked(self) -> ADLX_RESULT:
        """Sets display to blanked state."""
        pass

    def SetUnblanked(self) -> ADLX_RESULT:
        """Sets display to unblanked state."""
        pass

class IADLXDisplayConnectivityExperience(IADLXInterface):
    """The IADLXDisplayConnectivityExperience interface provides methods for display connectivity experience settings."""

    def IsSupportedHDMIQualityDetection(self) -> bool:
        """Checks if HDMI quality detection is supported."""
        pass

    def IsSupportedDPLink(self) -> bool:
        """Checks if DP link is supported."""
        pass

    def IsEnabledHDMIQualityDetection(self) -> bool:
        """Checks if HDMI quality detection is enabled."""
        pass

    def SetEnabledHDMIQualityDetection(self, enabled: bool) -> ADLX_RESULT:
        """Sets the enabled state for HDMI quality detection."""
        pass

    def GetDPLinkRate(self) -> ADLX_DP_LINK_RATE:
        """Gets the DP link rate."""
        pass

    def GetNumberOfActiveLanes(self) -> int:
        """Gets the number of active lanes."""
        pass

    def GetNumberOfTotalLanes(self) -> int:
        """Gets the total number of lanes."""
        pass

    def GetRelativePreEmphasis(self) -> int:
        """Gets the relative preset emphasis."""
        pass

    def SetRelativePreEmphasis(self, relativePreEmphasis: int) -> ADLX_RESULT:
        """Sets the relative preset emphasis."""
        pass

    def GetRelativeVoltageSwing(self) -> int:
        """Gets the relative voltage swing."""
        pass

    def SetRelativeVoltageSwing(self, relativeVoltageSwing: int) -> ADLX_RESULT:
        """Sets the relative voltage swing."""
        pass

    def IsEnabledLinkProtection(self) -> bool:
        """Checks if link protection is enabled."""
        pass

class IADLXDisplayDynamicRefreshRateControl(IADLXInterface):
    """The IADLXDisplayDynamicRefreshRateControl interface provides methods for dynamic refresh rate control."""

    def IsSupported(self) -> bool:
        """Checks if Dynamic Refresh Rate Control is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if Dynamic Refresh Rate Control is enabled."""
        pass

    def SetEnabled(self, enabled: bool) -> ADLX_RESULT:
        """Sets the Dynamic Refresh Rate Control state."""
        pass

class IADLXDisplayFreeSyncColorAccuracy(IADLXInterface):
    """The IADLXDisplayFreeSyncColorAccuracy interface provides methods for FreeSync color accuracy configuration."""

    def IsSupported(self) -> bool:
        """Checks if FreeSync color accuracy is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if FreeSync color accuracy is enabled."""
        pass

    def SetEnabled(self, enabled: bool) -> ADLX_RESULT:
        """Sets the FreeSync color accuracy state."""
        pass

class IADLXDisplayGammaChangedEvent(IADLXInterface):
    """The IADLXDisplayGammaChangedEvent interface provides methods for handling display gamma changed events."""

    def GetDisplay(self):
        """Gets the display interface."""
        pass

    def GetOrigin(self) -> ADLX_SYNC_ORIGIN:
        """Gets the origin of the event."""
        pass

    def IsDeGammaChanged(self) -> bool:
        """Checks if de-gamma is changed."""
        pass

    def IsGammaCoefficientChanged(self) -> bool:
        """Checks if gamma coefficient is changed."""
        pass

    def IsGammaRampChanged(self) -> bool:
        """Checks if gamma ramp is changed."""
        pass

    def IsReGammaChanged(self) -> bool:
        """Checks if re-gamma is changed."""
        pass

class IADLXDisplayGamutChangedEvent(IADLXInterface):
    """The IADLXDisplayGamutChangedEvent interface provides methods for handling display gamut changed events."""

    def GetDisplay(self):
        """Gets the display interface."""
        pass

    def GetOrigin(self) -> ADLX_SYNC_ORIGIN:
        """Gets the origin of the event."""
        pass

    def IsGamutChanged(self) -> bool:
        """Checks if gamut is changed."""
        pass

    def IsWhitePointChanged(self) -> bool:
        """Checks if white point is changed."""
        pass

class IADLXDisplayResolution(IADLXInterface):
    """The IADLXDisplayResolution interface provides information about a display resolution."""

    pass

class IADLXDisplaySettingsChangedEvent(IADLXInterface):
    """The IADLXDisplaySettingsChangedEvent interface provides methods for handling display settings changed events."""

    def GetDisplay(self):
        """Gets the display interface."""
        pass

    def GetOrigin(self) -> ADLX_SYNC_ORIGIN:
        """Gets the origin of the event."""
        pass

    def IsColorDepthChanged(self) -> bool:
        """Checks if color depth changed."""
        pass

    def IsCustomColorBrightnessChanged(self) -> bool:
        """Checks if custom color brightness changed."""
        pass

    def IsCustomColorContrastChanged(self) -> bool:
        """Checks if custom color contrast changed."""
        pass

    def IsCustomColorHueChanged(self) -> bool:
        """Checks if custom color hue changed."""
        pass

    def IsCustomColorSaturationChanged(self) -> bool:
        """Checks if custom color saturation changed."""
        pass

    def IsCustomColorTemperatureChanged(self) -> bool:
        """Checks if custom color temperature changed."""
        pass

    def IsCustomResolutionChanged(self) -> bool:
        """Checks if custom resolution changed."""
        pass

    def IsFreeSyncChanged(self) -> bool:
        """Checks if FreeSync changed."""
        pass

    def IsGPUScalingChanged(self) -> bool:
        """Checks if GPU scaling changed."""
        pass

    def IsHDCPChanged(self) -> bool:
        """Checks if HDCP changed."""
        pass

    def IsIntegerScalingChanged(self) -> bool:
        """Checks if integer scaling changed."""
        pass

    def IsPixelFormatChanged(self) -> bool:
        """Checks if pixel format changed."""
        pass

    def IsScalingModeChanged(self) -> bool:
        """Checks if scaling mode changed."""
        pass

    def IsVSRChanged(self) -> bool:
        """Checks if VSR changed."""
        pass

    def IsVariBrightChanged(self) -> bool:
        """Checks if Vari-Bright changed."""
        pass

    def IsDisplayBlankingChanged(self) -> bool:
        """Checks if display blanking changed (IADLXDisplaySettingsChangedEvent1)."""
        pass

    def IsDisplayConnectivityExperienceChanged(self) -> bool:
        """Checks if display connectivity experience changed (IADLXDisplaySettingsChangedEvent2)."""
        pass

    def IsDisplayDynamicRefreshRateControlChanged(self) -> bool:
        """Checks if display dynamic refresh rate control changed (IADLXDisplaySettingsChangedEvent3)."""
        pass

    def IsFreeSyncColorAccuracyChanged(self) -> bool:
        """Checks if FreeSync color accuracy changed (IADLXDisplaySettingsChangedEvent3)."""
        pass

class IADLXEyefinityDesktop(IADLXInterface):
    """The IADLXEyefinityDesktop interface provides methods for AMD Eyefinity desktop management."""

    pass

class IADLXGPUAutoTuningCompleteEvent(IADLXInterface):
    """The IADLXGPUAutoTuningCompleteEvent interface provides methods for handling GPU auto-tuning complete events."""

    def GetGPU(self) -> IADLXGPU:
        """Gets the GPU interface."""
        pass

    def GetOrigin(self) -> ADLX_SYNC_ORIGIN:
        """Gets the origin of the event."""
        pass

    def IsAutoTuningCompleted(self) -> bool:
        """Checks if auto-tuning is completed."""
        pass

class IADLXGPUTuningChangedEvent(IADLXInterface):
    """The IADLXGPUTuningChangedEvent interface provides methods for handling GPU tuning changed events."""

    def GetGPU(self) -> IADLXGPU:
        """Gets the GPU interface."""
        pass

    def GetOrigin(self) -> ADLX_SYNC_ORIGIN:
        """Gets the origin of the event."""
        pass

    def IsAutomaticTuningChanged(self) -> bool:
        """Checks if automatic tuning is changed."""
        pass

    def IsManualFanTuningChanged(self) -> bool:
        """Checks if manual fan tuning is changed."""
        pass

    def IsManualGFXTuningChanged(self) -> bool:
        """Checks if manual GFX tuning is changed."""
        pass

    def IsManualPowerTuningChanged(self) -> bool:
        """Checks if manual power tuning is changed."""
        pass

    def IsManualVRAMTuningChanged(self) -> bool:
        """Checks if manual VRAM tuning is changed."""
        pass

    def IsPresetTuningChanged(self) -> bool:
        """Checks if preset tuning is changed."""
        pass

    def IsSmartAccessMemoryChanged(self) -> bool:
        """Checks if Smart Access Memory is changed (IADLXGPUTuningChangedEvent1)."""
        pass

    def GetSmartAccessMemoryStatus(self) -> Tuple[bool, bool]:
        """Gets the Smart Access Memory status (IADLXGPUTuningChangedEvent1).

        :return: (enabled, completed)
        :rtype: Tuple[bool, bool]
        """
        pass

class IADLXList(IADLXInterface):
    """The IADLXList interface provides methods for list management."""

    def At(self, index: int):
        """Gets an item at the specified index."""
        pass

    def Back(self):
        """Gets the last item in the list."""
        pass

    def Begin(self):
        """Gets an iterator to the first item."""
        pass

    def Clear(self) -> ADLX_RESULT:
        """Clears the list."""
        pass

    def Empty(self) -> bool:
        """Checks if the list is empty."""
        pass

    def End(self):
        """Gets an iterator to the end of the list."""
        pass

    def Front(self):
        """Gets the first item in the list."""
        pass

    def Size(self) -> int:
        """Gets the size of the list."""
        pass

class IADLXDisplayResolutionList(IADLXList):
    """The IADLXDisplayResolutionList interface provides methods for managing a list of display resolutions."""

    def Add_Back(self, item: IADLXDisplayResolution) -> ADLX_RESULT:
        """Adds an item to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last item from the list."""
        pass

class IADLXManualFanTuningStateList(IADLXList):
    """The IADLXManualFanTuningStateList interface provides methods for managing a list of manual fan tuning states."""

    def Add_Back(self, item: IADLXManualFanTuningState) -> ADLX_RESULT:
        """Adds an item to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last item from the list."""
        pass

class IADLXManualTuningStateList(IADLXList):
    """The IADLXManualTuningStateList interface provides methods for managing a list of manual tuning states."""

    def Add_Back(self, item: IADLXManualTuningState) -> ADLX_RESULT:
        """Adds an item to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last item from the list."""
        pass

class IADLXMemoryTimingDescriptionList(IADLXList):
    """The IADLXMemoryTimingDescriptionList interface provides methods for managing a list of memory timing descriptions."""

    def Add_Back(self, item: IADLXMemoryTimingDescription) -> ADLX_RESULT:
        """Adds an item to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last item from the list."""
        pass

class IADLXManualFanTuningState(IADLXInterface):
    """The IADLXManualFanTuningState interface provides methods for manual fan tuning state."""

    pass

class IADLXManualTuningState(IADLXInterface):
    """The IADLXManualTuningState interface provides methods for manual tuning state."""

    pass

class IADLXMemoryTimingDescription(IADLXInterface):
    """The IADLXMemoryTimingDescription interface provides information about memory timing descriptions."""

    def GetDescription(self) -> ADLX_MEMORYTIMING_DESCRIPTION:
        """Gets the memory timing description."""
        pass

class IADLX3DAntiLag(IADLXInterface):
    """The IADLX3DAntiLag interface provides methods for AMD Radeon Anti-Lag."""

    def IsSupported(self) -> bool:
        """Checks if AMD Radeon Anti-Lag is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if AMD Radeon Anti-Lag is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets AMD Radeon Anti-Lag enabled state."""
        pass

class IADLX3DAnisotropicFiltering(IADLXInterface):
    """The IADLX3DAnisotropicFiltering interface provides methods for Anisotropic Filtering."""

    def IsSupported(self) -> bool:
        """Checks if Anisotropic Filtering is supported."""
        pass

    def IsEnabled(self) -> bool | None:
        """Checks if Anisotropic Filtering is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets Anisotropic Filtering enabled state."""
        pass

    def GetLevel(self) -> ADLX_ANISOTROPIC_FILTERING_LEVEL | None:
        """Gets the current Anisotropic Filtering level."""
        pass

    def SetLevel(self, level: ADLX_ANISOTROPIC_FILTERING_LEVEL) -> ADLX_RESULT:
        """Sets the Anisotropic Filtering level."""
        pass

class IADLX3DAntiAliasing(IADLXInterface):
    """The IADLX3DAntiAliasing interface provides methods for Anti-Aliasing."""

    def IsSupported(self) -> bool:
        """Checks if Anti-Aliasing is supported."""
        pass

    def GetMode(self) -> ADLX_ANTI_ALIASING_MODE | None:
        """Gets the current Anti-Aliasing mode."""
        pass

    def SetMode(self, mode: ADLX_ANTI_ALIASING_MODE) -> ADLX_RESULT:
        """Sets the Anti-Aliasing mode."""
        pass

    def GetMethod(self) -> ADLX_ANTI_ALIASING_METHOD | None:
        """Gets the current Anti-Aliasing method."""
        pass

    def SetMethod(self, method: ADLX_ANTI_ALIASING_METHOD) -> ADLX_RESULT:
        """Sets the Anti-Aliasing method."""
        pass

    def GetLevel(self) -> ADLX_ANTI_ALIASING_LEVEL | None:
        """Gets the current Anti-Aliasing level."""
        pass

    def SetLevel(self, level: ADLX_ANTI_ALIASING_LEVEL) -> ADLX_RESULT:
        """Sets the Anti-Aliasing level."""
        pass

class IADLX3DBoost(IADLXInterface):
    """The IADLX3DBoost interface provides methods for AMD Radeon Boost."""

    def IsSupported(self) -> bool:
        """Checks if AMD Radeon Boost is supported."""
        pass

    def IsEnabled(self) -> bool | None:
        """Checks if AMD Radeon Boost is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets AMD Radeon Boost enabled state."""
        pass

    def GetResolutionRange(self) -> Dict[str, int]:
        """Gets the resolution range for AMD Radeon Boost with maxValue, minValue, and step."""
        pass

    def GetResolution(self) -> int | None:
        """Gets the current resolution for AMD Radeon Boost."""
        pass

    def SetResolution(self, minRes: int) -> ADLX_RESULT:
        """Sets the resolution for AMD Radeon Boost."""
        pass

class IADLX3DChill(IADLXInterface):
    """The IADLX3DChill interface provides methods for AMD Radeon Chill."""

    def IsSupported(self) -> bool:
        """Checks if AMD Radeon Chill is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if AMD Radeon Chill is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets AMD Radeon Chill enabled state."""
        pass

    def GetFPSRange(self) -> Dict[str, int]:
        """Gets the FPS range for AMD Radeon Chill.
        
        Returns a dictionary with keys: 'minValue', 'maxValue', 'step'
        """
        pass

    def GetMinFPS(self) -> int | None:
        """Gets the minimum FPS for AMD Radeon Chill.
        
        Returns the minimum FPS value on success, or None on failure.
        """
        pass

    def GetMaxFPS(self) -> int | None:
        """Gets the maximum FPS for AMD Radeon Chill.
        
        Returns the maximum FPS value on success, or None on failure.
        """
        pass

    def SetMinFPS(self, minFPS: int) -> ADLX_RESULT:
        """Sets the minimum FPS for AMD Radeon Chill."""
        pass

    def SetMaxFPS(self, maxFPS: int) -> ADLX_RESULT:
        """Sets the maximum FPS for AMD Radeon Chill."""
        pass

class IADLX3DEnhancedSync(IADLXInterface):
    """The IADLX3DEnhancedSync interface provides methods for AMD Radeon Enhanced Sync."""

    def IsSupported(self) -> bool:
        """Checks if AMD Radeon Enhanced Sync is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if AMD Radeon Enhanced Sync is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets AMD Radeon Enhanced Sync enabled state."""
        pass

class IADLX3DFrameRateTargetControl(IADLXInterface):
    """The IADLX3DFrameRateTargetControl interface provides methods for Frame Rate Target Control."""

    def IsSupported(self) -> bool:
        """Checks if Frame Rate Target Control is supported.
        
        Returns:
            bool: True if supported, False otherwise.
        """
        pass

    def IsEnabled(self) -> bool | None:
        """Checks if Frame Rate Target Control is enabled.
        
        Returns:
            bool | None: True if enabled, False if disabled, None if query fails.
        """
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets Frame Rate Target Control enabled state.
        
        Args:
            enable: The new state. Set True to enable, False to disable.
            
        Returns:
            ADLX_RESULT: ADLX_OK if successful, error code otherwise.
        """
        pass

    def GetFPSRange(self) -> Dict[str, int]:
        """Gets the FPS range for Frame Rate Target Control.
        
        Returns:
            Dict[str, int]: Dictionary with keys 'maxValue', 'minValue', and 'step'.
        """
        pass

    def GetFPS(self) -> int | None:
        """Gets the current FPS for Frame Rate Target Control.
        
        Returns:
            int | None: Current FPS value if successful, None otherwise.
        """
        pass

    def SetFPS(self, fps: int) -> ADLX_RESULT:
        """Sets the FPS for Frame Rate Target Control.
        
        Args:
            fps: The target FPS value.
            
        Returns:
            ADLX_RESULT: ADLX_OK if successful, error code otherwise.
        """
        pass

class IADLX3DImageSharpening(IADLXInterface):
    """The IADLX3DImageSharpening interface provides methods for AMD Radeon Image Sharpening."""

    def IsSupported(self) -> bool:
        """Checks if AMD Radeon Image Sharpening is supported."""
        pass

    def IsEnabled(self) -> bool | None:
        """Checks if AMD Radeon Image Sharpening is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets AMD Radeon Image Sharpening enabled state."""
        pass

    def GetSharpnessRange(self) -> Dict[str, int]:
        """Gets the sharpness range for AMD Radeon Image Sharpening with maxValue, minValue, and step."""
        pass

    def GetSharpness(self) -> int | None:
        """Gets the current sharpness for AMD Radeon Image Sharpening."""
        pass

    def SetSharpness(self, sharpness: int) -> ADLX_RESULT:
        """Sets the sharpness for AMD Radeon Image Sharpening."""
        pass

class IADLX3DMorphologicalAntiAliasing(IADLXInterface):
    """The IADLX3DMorphologicalAntiAliasing interface provides methods for Morphological Anti-Aliasing."""

    def IsSupported(self) -> bool:
        """Checks if Morphological Anti-Aliasing is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if Morphological Anti-Aliasing is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets Morphological Anti-Aliasing enabled state."""
        pass

class IADLX3DResetShaderCache(IADLXInterface):
    """The IADLX3DResetShaderCache interface provides methods for resetting the shader cache."""

    def IsSupported(self) -> bool:
        """Checks if Reset Shader Cache is supported."""
        pass

    def ResetShaderCache(self) -> ADLX_RESULT:
        """Resets the shader cache."""
        pass

class IADLX3DTessellation(IADLXInterface):
    """The IADLX3DTessellation interface provides methods for Tessellation."""

    def IsSupported(self) -> bool:
        """Checks if Tessellation is supported."""
        pass

    def GetMode(self) -> ADLX_TESSELLATION_MODE | None:
        """Gets the current Tessellation mode."""
        pass

    def SetMode(self, mode: ADLX_TESSELLATION_MODE) -> ADLX_RESULT:
        """Sets the Tessellation mode."""
        pass

    def GetLevel(self) -> ADLX_TESSELLATION_LEVEL | None:
        """Gets the current Tessellation level."""
        pass

    def SetLevel(self, level: ADLX_TESSELLATION_LEVEL) -> ADLX_RESULT:
        """Sets the Tessellation level."""
        pass

class IADLX3DWaitForVerticalRefresh(IADLXInterface):
    """The IADLX3DWaitForVerticalRefresh interface provides methods for Wait for Vertical Refresh (VSync)."""

    def IsEnabled(self) -> bool | None:
        """Checks if Wait for Vertical Refresh is enabled."""
        pass

    def IsSupported(self) -> bool:
        """Checks if Wait for Vertical Refresh is supported."""
        pass

    def GetMode(self) -> ADLX_WAIT_FOR_VERTICAL_REFRESH_MODE | None:
        """Gets the current Wait for Vertical Refresh mode."""
        pass

    def SetMode(self, mode: ADLX_WAIT_FOR_VERTICAL_REFRESH_MODE) -> ADLX_RESULT:
        """Sets the Wait for Vertical Refresh mode."""
        pass

class IADLX3DAMDFluidMotionFrames(IADLXInterface):
    """The IADLX3DAMDFluidMotionFrames interface provides methods for AMD Fluid Motion Frames."""

    def IsSupported(self) -> bool:
        """Checks if AMD Fluid Motion Frames is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if AMD Fluid Motion Frames is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets AMD Fluid Motion Frames enabled state."""
        pass

    def IsSupportedAlgorithm(self) -> bool:
        """Checks if AMD Fluid Motion Frames algorithm selection is supported."""
        pass

    def GetAlgorithm(self) -> ADLX_AFMF_ALGORITHM:
        """Gets the current AMD Fluid Motion Frames algorithm.
        
        :return: The current algorithm type
        :rtype: ADLX_AFMF_ALGORITHM
        """
        pass

    def SetAlgorithm(self, algorithm: ADLX_AFMF_ALGORITHM) -> ADLX_RESULT:
        """Sets the AMD Fluid Motion Frames algorithm.
        
        :param algorithm: The algorithm type to set
        :type algorithm: ADLX_AFMF_ALGORITHM
        :return: ADLX_RESULT indicating success or failure
        :rtype: ADLX_RESULT
        """
        pass

    def GetSearchMode(self) -> ADLX_AFMF_SEARCH_MODE_TYPE:
        """Gets the current AMD Fluid Motion Frames search mode.
        
        :return: The current search mode type
        :rtype: ADLX_AFMF_SEARCH_MODE_TYPE
        """
        pass

    def SetSearchMode(self, mode: ADLX_AFMF_SEARCH_MODE_TYPE) -> ADLX_RESULT:
        """Sets the AMD Fluid Motion Frames search mode.
        
        :param mode: The search mode type to set
        :type mode: ADLX_AFMF_SEARCH_MODE_TYPE
        :return: ADLX_RESULT indicating success or failure
        :rtype: ADLX_RESULT
        """
        pass

    def GetPerformanceMode(self) -> ADLX_AFMF_PERFORMANCE_MODE_TYPE:
        """Gets the current AMD Fluid Motion Frames performance mode.
        
        :return: The current performance mode type
        :rtype: ADLX_AFMF_PERFORMANCE_MODE_TYPE
        """
        pass

    def SetPerformanceMode(self, mode: ADLX_AFMF_PERFORMANCE_MODE_TYPE) -> ADLX_RESULT:
        """Sets the AMD Fluid Motion Frames performance mode.
        
        :param mode: The performance mode type to set
        :type mode: ADLX_AFMF_PERFORMANCE_MODE_TYPE
        :return: ADLX_RESULT indicating success or failure
        :rtype: ADLX_RESULT
        """
        pass

    def GetFastMotionResponse(self) -> ADLX_AFMF_FAST_MOTION_RESP:
        """Gets the current AMD Fluid Motion Frames fast motion response.
        
        :return: The current fast motion response type
        :rtype: ADLX_AFMF_FAST_MOTION_RESP
        """
        pass

    def SetFastMotionResponse(self, response: ADLX_AFMF_FAST_MOTION_RESP) -> ADLX_RESULT:
        """Sets the AMD Fluid Motion Frames fast motion response.
        
        :param response: The fast motion response type to set
        :type response: ADLX_AFMF_FAST_MOTION_RESP
        :return: ADLX_RESULT indicating success or failure
        :rtype: ADLX_RESULT
        """
        pass

class IADLX3DFidelityFXSuperResolution(IADLXInterface):
    """The IADLX3DFidelityFXSuperResolution interface provides methods for FidelityFX Super Resolution (FSR) settings."""

    def IsEnabled(self) -> bool:
        """Checks if FidelityFX Super Resolution is enabled.
        
        :return: True if FSR is enabled, False otherwise
        :rtype: bool
        """
        pass

    def IsSupported(self) -> bool:
        """Checks if FidelityFX Super Resolution is supported.
        
        :return: True if FSR is supported, False otherwise
        :rtype: bool
        """
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets FidelityFX Super Resolution enabled state.
        
        :param enable: True to enable, False to disable
        :type enable: bool
        :return: ADLX_RESULT indicating success or failure
        :rtype: ADLX_RESULT
        """
        pass

class IADLX3DFidelityFXFrameGenUpgrade(IADLXInterface):
    """The IADLX3DFidelityFXFrameGenUpgrade interface provides methods for FidelityFX Frame Generation Upgrade settings."""

    def IsEnabled(self) -> bool:
        """Checks if FidelityFX Frame Generation Upgrade is enabled.
        
        :return: True if enabled, False otherwise
        :rtype: bool
        """
        pass

    def IsSupported(self) -> bool:
        """Checks if FidelityFX Frame Generation Upgrade is supported.
        
        :return: True if supported, False otherwise
        :rtype: bool
        """
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets FidelityFX Frame Generation Upgrade enabled state.
        
        :param enable: True to enable, False to disable
        :type enable: bool
        :return: ADLX_RESULT indicating success or failure
        :rtype: ADLX_RESULT
        """
        pass

class IADLX3DSettingsChangedHandling(IADLXInterface):
    """The IADLX3DSettingsChangedHandling interface provides methods for registering and unregistering for 3D settings change notifications."""

    def AddChangedListener(self, listener) -> ADLX_RESULT:
        """Adds a listener for 3D settings changes."""
        pass

    def RemoveChangedListener(self, listener) -> ADLX_RESULT:
        """Removes a listener for 3D settings changes."""
        pass

class IADLXDesktop(IADLXInterface):
    """The IADLXDesktop interface provides information about a desktop."""

    def Type(self) -> ADLX_DESKTOP_TYPE:
        """Gets the desktop type."""
        pass

    def Orientation(self) -> ADLX_ORIENTATION:
        """Gets the desktop orientation."""
        pass

    def GetDisplays(self) -> List:
        """Gets the list of displays on this desktop."""
        pass

    def GetNumberOfDisplays(self) -> int:
        """Gets the number of displays on this desktop."""
        pass

    def Size(self) -> Tuple[int, int]:
        """Gets the desktop size (width and height)."""
        pass

    def TopLeft(self) -> Tuple[int, int]:
        """Gets the top-left position of the desktop."""
        pass

class IADLXDesktopList(IADLXList):
    """The IADLXDesktopList interface provides methods for managing a list of desktops."""

    def Add_Back(self, item: IADLXDesktop) -> ADLX_RESULT:
        """Adds a desktop to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last desktop from the list."""
        pass

class IADLXDesktopChangedHandling(IADLXInterface):
    """The IADLXDesktopChangedHandling interface provides methods for registering and unregistering for desktop change notifications."""

    def AddChangedListener(self, listener) -> ADLX_RESULT:
        """Adds a listener for desktop changes."""
        pass

    def RemoveChangedListener(self, listener) -> ADLX_RESULT:
        """Removes a listener for desktop changes."""
        pass

class IADLXSimpleEyefinity(IADLXInterface):
    """The IADLXSimpleEyefinity interface provides methods for AMD Eyefinity desktop management."""

    def IsSupported(self) -> bool:
        """Checks if AMD Eyefinity is supported."""
        pass

    def Create(self, item: IADLXEyefinityDesktop) -> ADLX_RESULT:
        """Creates an AMD Eyefinity desktop."""
        pass

    def Destroy(self, item: IADLXEyefinityDesktop) -> ADLX_RESULT:
        """Destroys an AMD Eyefinity desktop."""
        pass

    def DestroyAll(self) -> ADLX_RESULT:
        """Destroys all AMD Eyefinity desktops."""
        pass

class IADLXDisplay(IADLXInterface):
    """The IADLXDisplay interface provides information about a display."""

    def ManufacturerID(self) -> int | None:
        """Gets the manufacturer ID of the display.
        
        Returns:
            int | None: Manufacturer ID if successful, None otherwise.
        """
        pass

    def DisplayType(self) -> ADLX_DISPLAY_TYPE | None:
        """Gets the display type.
        
        Returns:
            ADLX_DISPLAY_TYPE | None: Display type if successful, None otherwise.
        """
        pass

    def ConnectorType(self) -> ADLX_DISPLAY_CONNECTOR_TYPE | None:
        """Gets the connector type of the display.
        
        Returns:
            ADLX_DISPLAY_CONNECTOR_TYPE | None: Connector type if successful, None otherwise.
        """
        pass

    def Name(self) -> str:
        """Gets the name of the display.
        
        Returns:
            str: Display name.
        """
        pass

    def EDID(self) -> str:
        """Gets the EDID of the display.
        
        Returns:
            str: Display EDID string.
        """
        pass

    def NativeResolution(self) -> Tuple[int, int]:
        """Gets the native resolution of the display.
        
        Returns:
            Tuple[int, int]: Native resolution as (horizontal, vertical).
        """
        pass

    def RefreshRate(self) -> float | None:
        """Gets the refresh rate of the display.
        
        Returns:
            float | None: Refresh rate in Hz if successful, None otherwise.
        """
        pass

    def PixelClock(self) -> int | None:
        """Gets the pixel clock of the display.
        
        Returns:
            int | None: Pixel clock if successful, None otherwise.
        """
        pass

    def ScanType(self) -> ADLX_DISPLAY_SCAN_TYPE | None:
        """Gets the scan type of the display.
        
        Returns:
            ADLX_DISPLAY_SCAN_TYPE | None: Scan type if successful, None otherwise.
        """
        pass

    def UniqueId(self) -> int | None:
        """Gets the unique ID of the display.
        
        Returns:
            int | None: Unique display ID if successful, None otherwise.
        """
        pass

    def GetGPU(self) -> IADLXGPU | None:
        """Gets the GPU associated with the display.
        
        Returns:
            IADLXGPU | None: GPU interface if successful, None otherwise.
        """
        pass

class IADLXDisplayList(IADLXList):
    """The IADLXDisplayList interface provides methods for managing a list of displays."""

    def Add_Back(self, item: IADLXDisplay) -> ADLX_RESULT:
        """Adds a display to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last display from the list."""
        pass

class IADLXDisplay3DLUT(IADLXInterface):
    """The IADLXDisplay3DLUT interface provides methods for display 3D LUT control."""

    def ClearUser3DLUT(self) -> ADLX_RESULT:
        """Clears the User 3D LUT data."""
        pass

    def GetAllUser3DLUT(self) -> Dict[str, Any]:
        """Gets all User 3D LUT data including transfer function, color space, points number, and RGB data."""
        pass

    def GetHDRUser3DLUT(self) -> Dict[str, Any]:
        """Gets HDR User 3D LUT data including transfer function, color space, points number, and RGB data."""
        pass

    def GetSCEDynamicContrast(self) -> int:
        """Gets the SCE dynamic contrast value."""
        pass

    def GetSCEDynamicContrastRange(self) -> Dict[str, int]:
        """Gets the SCE dynamic contrast range with maxValue, minValue, and step."""
        pass

    def GetSDRUser3DLUT(self) -> Dict[str, Any]:
        """Gets SDR User 3D LUT data including transfer function, color space, points number, and RGB data."""
        pass

    def GetUser3DLUTIndex(self, lutSize: int, rgbCoordinate: Any) -> int:
        """Gets the User 3D LUT index for given coordinates."""
        pass

    def IsCurrentSCEDisabled(self) -> bool:
        """Checks if SCE (Smart Contrast Enhancement) is currently disabled."""
        pass

    def IsCurrentSCEDynamicContrast(self) -> bool:
        """Checks if SCE dynamic contrast is currently enabled."""
        pass

    def IsCurrentSCEVividGaming(self) -> bool:
        """Checks if SCE vivid gaming is currently enabled."""
        pass

    def IsSupportedSCE(self) -> bool:
        """Checks if SCE (Smart Contrast Enhancement) is supported."""
        pass

    def IsSupportedSCEDynamicContrast(self) -> bool:
        """Checks if SCE dynamic contrast is supported."""
        pass

    def IsSupportedSCEVividGaming(self) -> bool:
        """Checks if SCE vivid gaming is supported."""
        pass

    def IsSupportedUser3DLUT(self) -> bool:
        """Checks if User 3D LUT is supported."""
        pass

    def SetAllUser3DLUT(self, transferFunction: ADLX_3DLUT_TRANSFER_FUNCTION, colorSpace: ADLX_3DLUT_COLORSPACE, pointsNumber: int, data: Dict[str, Any]) -> ADLX_RESULT:
        """Sets all User 3D LUT data."""
        pass

    def SetHDRUser3DLUT(self, transferFunction: ADLX_3DLUT_TRANSFER_FUNCTION, colorSpace: ADLX_3DLUT_COLORSPACE, pointsNumber: int, data: Dict[str, Any]) -> ADLX_RESULT:
        """Sets HDR User 3D LUT data."""
        pass

    def SetSCEDisabled(self) -> ADLX_RESULT:
        """Disables SCE (Smart Contrast Enhancement)."""
        pass

    def SetSCEDynamicContrast(self, contrast: int) -> ADLX_RESULT:
        """Sets SCE dynamic contrast value."""
        pass

    def SetSCEVividGaming(self) -> ADLX_RESULT:
        """Enables SCE vivid gaming."""
        pass

    def SetSDRUser3DLUT(self, transferFunction: ADLX_3DLUT_TRANSFER_FUNCTION, colorSpace: ADLX_3DLUT_COLORSPACE, pointsNumber: int, data: Dict[str, Any]) -> ADLX_RESULT:
        """Sets SDR User 3D LUT data."""
        pass

    def QueryInterface(self, interfaceId: str) -> 'IADLXDisplay3DLUT':
        """Queries for an interface."""
        pass

class IADLXDisplayColorDepth(IADLXInterface):
    """The IADLXDisplayColorDepth interface provides methods for display color depth control."""

    def IsSupported(self) -> bool:
        """Checks if color depth control is supported."""
        pass

    def IsSupportedBPC_6(self) -> bool:
        """Checks if 6 BPC is supported."""
        pass

    def IsSupportedBPC_8(self) -> bool:
        """Checks if 8 BPC is supported."""
        pass

    def IsSupportedBPC_10(self) -> bool:
        """Checks if 10 BPC is supported."""
        pass

    def IsSupportedBPC_12(self) -> bool:
        """Checks if 12 BPC is supported."""
        pass

    def IsSupportedBPC_14(self) -> bool:
        """Checks if 14 BPC is supported."""
        pass

    def IsSupportedBPC_16(self) -> bool:
        """Checks if 16 BPC is supported."""
        pass

    def IsSupportedColorDepth(self, colorDepth: ADLX_COLOR_DEPTH) -> bool:
        """Checks if a specific color depth is supported."""
        pass

    def GetValue(self) -> ADLX_COLOR_DEPTH | None:
        """Gets the current color depth."""
        pass

    def SetValue(self, bpp: ADLX_COLOR_DEPTH) -> ADLX_RESULT:
        """Sets the color depth."""
        pass

class IADLXDisplayPixelFormat(IADLXInterface):
    """The IADLXDisplayPixelFormat interface provides methods for display pixel format control."""

    def IsSupported(self) -> bool:
        """Checks if pixel format control is supported."""
        pass

    def IsSupportedPixelFormat(self, pixelFormat: ADLX_PIXEL_FORMAT) -> bool:
        """Checks if a specific pixel format is supported."""
        pass

    def IsSupportedRGB444Full(self) -> bool:
        """Checks if RGB 444 Full is supported."""
        pass

    def IsSupportedRGB444Limited(self) -> bool:
        """Checks if RGB 444 Limited is supported."""
        pass

    def IsSupportedYCbCr420(self) -> bool:
        """Checks if YCbCr 420 is supported."""
        pass

    def IsSupportedYCbCr422(self) -> bool:
        """Checks if YCbCr 422 is supported."""
        pass

    def IsSupportedYCbCr444(self) -> bool:
        """Checks if YCbCr 444 is supported."""
        pass

    def GetValue(self) -> ADLX_PIXEL_FORMAT:
        """Gets the current pixel format."""
        pass

    def SetValue(self, format: ADLX_PIXEL_FORMAT) -> ADLX_RESULT:
        """Sets the pixel format."""
        pass

class IADLXDisplayCustomColor(IADLXInterface):
    """The IADLXDisplayCustomColor interface provides methods for display custom color control."""

    def GetBrightness(self) -> int | None:
        """Gets the brightness value."""
        pass

    def GetBrightnessRange(self) -> ADLX_IntRange:
        """Gets the brightness range."""
        pass

    def GetContrast(self) -> int | None:
        """Gets the contrast value."""
        pass

    def GetContrastRange(self) -> ADLX_IntRange:
        """Gets the contrast range."""
        pass

    def GetHue(self) -> int | None:
        """Gets the hue value."""
        pass

    def GetHueRange(self) -> ADLX_IntRange:
        """Gets the hue range."""
        pass

    def GetSaturation(self) -> int | None:
        """Gets the saturation value."""
        pass

    def GetSaturationRange(self) -> ADLX_IntRange:
        """Gets the saturation range."""
        pass

    def GetTemperature(self) -> int | None:
        """Gets the temperature value."""
        pass

    def GetTemperatureRange(self) -> ADLX_IntRange:
        """Gets the temperature range."""
        pass

    def IsBrightnessSupported(self) -> bool:
        """Checks if brightness control is supported."""
        pass

    def IsContrastSupported(self) -> bool:
        """Checks if contrast control is supported."""
        pass

    def IsHueSupported(self) -> bool:
        """Checks if hue control is supported."""
        pass

    def IsSaturationSupported(self) -> bool:
        """Checks if saturation control is supported."""
        pass

    def IsTemperatureSupported(self) -> bool:
        """Checks if temperature control is supported."""
        pass

    def SetBrightness(self, brightness: int) -> ADLX_RESULT:
        """Sets the brightness value."""
        pass

    def SetContrast(self, contrast: int) -> ADLX_RESULT:
        """Sets the contrast value."""
        pass

    def SetHue(self, hue: int) -> ADLX_RESULT:
        """Sets the hue value."""
        pass

    def SetSaturation(self, saturation: int) -> ADLX_RESULT:
        """Sets the saturation value."""
        pass

    def SetTemperature(self, temperature: int) -> ADLX_RESULT:
        """Sets the temperature value."""
        pass

class IADLXDisplayCustomResolution(IADLXInterface):
    """The IADLXDisplayCustomResolution interface provides methods for display custom resolution control."""

    def IsSupported(self) -> bool:
        """Checks if custom resolution is supported."""
        pass

    def GetResolutionList(self) -> IADLXDisplayResolutionList:
        """Gets the list of custom resolutions."""
        pass

    def CreateNewResolution(self, resolution: IADLXDisplayResolution) -> ADLX_RESULT:
        """Creates a new custom resolution."""
        pass

    def DeleteResolution(self, resolution: IADLXDisplayResolution) -> ADLX_RESULT:
        """Deletes a custom resolution."""
        pass

class IADLXDisplayFreeSync(IADLXInterface):
    """The IADLXDisplayFreeSync interface provides methods for AMD FreeSync control."""

    def IsSupported(self) -> bool:
        """Checks if AMD FreeSync is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if AMD FreeSync is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets AMD FreeSync enabled state."""
        pass

class IADLXDisplayGamma(IADLXInterface):
    """The IADLXDisplayGamma interface provides methods for display gamma control."""

    def GetGammaCoefficient(self) -> ADLX_RegammaCoeff:
        """Gets the current gamma coefficient."""
        pass

    def GetGammaRamp(self) -> List[int]:
        """Gets the current gamma ramp."""
        pass

    def IsCurrentDeGammaRamp(self) -> bool | None:
        """Checks if current de-gamma ramp is enabled."""
        pass

    def IsCurrentReGamma36(self) -> bool | None:
        """Checks if current re-gamma is 3.6."""
        pass

    def IsCurrentReGammaBT709(self) -> bool | None:
        """Checks if current re-gamma is BT709."""
        pass

    def IsCurrentReGammaPQ(self) -> bool | None:
        """Checks if current re-gamma is PQ."""
        pass

    def IsCurrentReGammaPQ2084Interim(self) -> bool | None:
        """Checks if current re-gamma is PQ2084 interim."""
        pass

    def IsCurrentReGammaRamp(self) -> bool | None:
        """Checks if current re-gamma ramp is enabled."""
        pass

    def IsCurrentReGammaSRGB(self) -> bool | None:
        """Checks if current re-gamma is sRGB."""
        pass

    def IsCurrentRegammaCoefficient(self) -> bool | None:
        """Checks if current re-gamma coefficient is enabled."""
        pass

    def IsSupportedReGamma36(self) -> bool:
        """Checks if re-gamma 3.6 is supported."""
        pass

    def IsSupportedReGammaBT709(self) -> bool:
        """Checks if re-gamma BT709 is supported."""
        pass

    def IsSupportedReGammaPQ(self) -> bool:
        """Checks if re-gamma PQ is supported."""
        pass

    def IsSupportedReGammaPQ2084Interim(self) -> bool:
        """Checks if re-gamma PQ2084 interim is supported."""
        pass

    def IsSupportedReGammaSRGB(self) -> bool:
        """Checks if re-gamma sRGB is supported."""
        pass

    def ResetGammaRamp(self) -> ADLX_RESULT:
        """Resets the gamma ramp to default."""
        pass

    def SetDeGammaRampMemory(self, gamma_ramp: List[int]) -> ADLX_RESULT:
        """Sets the de-gamma ramp from memory array."""
        pass

    def SetDeGammaRampFile(self, path: str) -> ADLX_RESULT:
        """Sets the de-gamma ramp from file."""
        pass

    def SetReGammaRampMemory(self, gamma_ramp: List[int]) -> ADLX_RESULT:
        """Sets the re-gamma ramp from memory array."""
        pass

    def SetReGammaRampFile(self, path: str) -> ADLX_RESULT:
        """Sets the re-gamma ramp from file."""
        pass

    def SetReGamma36(self) -> ADLX_RESULT:
        """Sets re-gamma to 3.6."""
        pass

    def SetReGammaBT709(self) -> ADLX_RESULT:
        """Sets re-gamma to BT709."""
        pass

    def SetReGammaCoefficient(self, coeff: ADLX_RegammaCoeff) -> ADLX_RESULT:
        """Sets re-gamma coefficient."""
        pass

    def SetReGammaPQ(self) -> ADLX_RESULT:
        """Sets re-gamma to PQ."""
        pass

    def SetReGammaPQ2084Interim(self) -> ADLX_RESULT:
        """Sets re-gamma to PQ2084 interim."""
        pass

    def SetReGammaSRGB(self) -> ADLX_RESULT:
        """Sets re-gamma to sRGB."""
        pass

    def QueryInterface(self, interfaceId: str) -> 'IADLXDisplayGamma':
        """Queries for an interface."""
        pass

class IADLXDisplayGamut(IADLXInterface):
    """The IADLXDisplayGamut interface provides methods for display gamut control."""

    def IsSupportedCCIR709ColorSpace(self) -> bool:
        """Checks if CCIR709 color space is supported."""
        pass

    def IsSupportedCCIR601ColorSpace(self) -> bool:
        """Checks if CCIR601 color space is supported."""
        pass

    def IsSupportedAdobeRgbColorSpace(self) -> bool:
        """Checks if Adobe RGB color space is supported."""
        pass

    def IsSupportedCIERgbColorSpace(self) -> bool:
        """Checks if CIE RGB color space is supported."""
        pass

    def IsSupportedCCIR2020ColorSpace(self) -> bool:
        """Checks if CCIR2020 color space is supported."""
        pass

    def IsSupportedCustomColorSpace(self) -> bool:
        """Checks if custom color space is supported."""
        pass

    def IsCurrentCCIR709ColorSpace(self) -> bool | None:
        """Checks if current color space is CCIR709."""
        pass

    def IsCurrentCCIR601ColorSpace(self) -> bool | None:
        """Checks if current color space is CCIR601."""
        pass

    def IsCurrentAdobeRgbColorSpace(self) -> bool | None:
        """Checks if current color space is Adobe RGB."""
        pass

    def IsCurrentCIERgbColorSpace(self) -> bool | None:
        """Checks if current color space is CIE RGB."""
        pass

    def IsCurrentCCIR2020ColorSpace(self) -> bool | None:
        """Checks if current color space is CCIR2020."""
        pass

    def IsCurrentCustomColorSpace(self) -> bool | None:
        """Checks if current color space is custom."""
        pass

    def SetColorSpace(self, colorSpace: ADLX_GAMUT_SPACE) -> ADLX_RESULT:
        """Sets the color space."""
        pass

    def GetGamutColorSpace(self) -> ADLX_GamutColorSpace:
        """Gets the current gamut color space."""
        pass

    def SetGamut(self, gamut: ADLX_GamutColorSpace) -> ADLX_RESULT:
        """Sets the gamut."""
        pass

    def GetWhitePoint(self) -> ADLX_Point:
        """Gets the white point."""
        pass

    def SetWhitePoint(self, whitePoint: ADLX_Point) -> ADLX_RESULT:
        """Sets the white point."""
        pass

    def IsCurrent5000kWhitePoint(self) -> bool | None:
        """Checks if current white point is 5000K."""
        pass

    def IsCurrent6500kWhitePoint(self) -> bool | None:
        """Checks if current white point is 6500K."""
        pass

    def IsCurrent7500kWhitePoint(self) -> bool | None:
        """Checks if current white point is 7500K."""
        pass

    def IsCurrent9300kWhitePoint(self) -> bool | None:
        """Checks if current white point is 9300K."""
        pass

    def IsCurrentCustomWhitePoint(self) -> bool | None:
        """Checks if current white point is custom."""
        pass

    def IsSupported5000kWhitePoint(self) -> bool:
        """Checks if 5000K white point is supported."""
        pass

    def IsSupported6500kWhitePoint(self) -> bool:
        """Checks if 6500K white point is supported."""
        pass

    def IsSupported7500kWhitePoint(self) -> bool:
        """Checks if 7500K white point is supported."""
        pass

    def IsSupported9300kWhitePoint(self) -> bool:
        """Checks if 9300K white point is supported."""
        pass

class IADLXDisplayGPUScaling(IADLXInterface):
    """The IADLXDisplayGPUScaling interface provides methods for display GPU scaling control."""

    def IsSupported(self) -> bool:
        """Checks if GPU scaling is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if GPU scaling is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets GPU scaling enabled state."""
        pass

class IADLXDisplayScalingMode(IADLXInterface):
    """The IADLXDisplayScalingMode interface provides methods for display scaling mode control."""

    def IsSupported(self) -> bool:
        """Checks if scaling mode is supported."""
        pass

    def GetMode(self) -> ADLX_SCALE_MODE:
        """Gets the current scaling mode."""
        pass

    def SetMode(self, mode: ADLX_SCALE_MODE) -> ADLX_RESULT:
        """Sets the scaling mode."""
        pass

class IADLXDisplayIntegerScaling(IADLXInterface):
    """The IADLXDisplayIntegerScaling interface provides methods for display integer scaling control."""

    def IsSupported(self) -> bool:
        """Checks if integer scaling is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if integer scaling is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets integer scaling enabled state."""
        pass

class IADLXDisplayHDCP(IADLXInterface):
    """The IADLXDisplayHDCP interface provides methods for display HDCP control."""

    def IsSupported(self) -> bool:
        """Checks if HDCP is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if HDCP is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets HDCP enabled state."""
        pass

class IADLXDisplayVariBright(IADLXInterface):
    """The IADLXDisplayVariBright interface provides methods for display Vari-Bright control."""

    def IsSupported(self) -> bool:
        """Checks if Vari-Bright is supported."""
        pass

    def IsEnabled(self) -> bool | None:
        """Checks if Vari-Bright is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets Vari-Bright enabled state."""
        pass

    def IsCurrentBalanced(self) -> bool | None:
        """Checks if current mode is balanced."""
        pass

    def IsCurrentMaximizeBattery(self) -> bool | None:
        """Checks if current mode is maximize battery."""
        pass

    def IsCurrentMaximizeBrightness(self) -> bool | None:
        """Checks if current mode is maximize brightness."""
        pass

    def IsCurrentOptimizeBattery(self) -> bool | None:
        """Checks if current mode is optimize battery."""
        pass

    def IsCurrentOptimizeBrightness(self) -> bool | None:
        """Checks if current mode is optimize brightness."""
        pass

    def SetBalanced(self) -> ADLX_RESULT:
        """Sets balanced mode."""
        pass

    def SetMaximizeBattery(self) -> ADLX_RESULT:
        """Sets maximize battery mode."""
        pass

    def SetMaximizeBrightness(self) -> ADLX_RESULT:
        """Sets maximize brightness mode."""
        pass

    def SetOptimizeBattery(self) -> ADLX_RESULT:
        """Sets optimize battery mode."""
        pass

    def SetOptimizeBrightness(self) -> ADLX_RESULT:
        """Sets optimize brightness mode."""
        pass

    def IsBacklightAdaptiveSupported(self) -> bool:
        """Checks if Backlight Adaptive Vari-Bright Scaling mode is supported (IADLXDisplayVariBright1)."""
        pass

    def IsBacklightAdaptiveEnabled(self) -> bool:
        """Checks if Backlight Adaptive Vari-Bright Scaling mode is enabled (IADLXDisplayVariBright1)."""
        pass

    def SetBacklightAdaptiveEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets Backlight Adaptive Vari-Bright Scaling mode (IADLXDisplayVariBright1)."""
        pass

    def IsBatteryLifeSupported(self) -> bool:
        """Checks if Battery Life Vari-Bright Scaling mode is supported (IADLXDisplayVariBright1)."""
        pass

    def IsBatteryLifeEnabled(self) -> bool:
        """Checks if Battery Life Vari-Bright Scaling mode is enabled (IADLXDisplayVariBright1)."""
        pass

    def SetBatteryLifeEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets Battery Life Vari-Bright Scaling mode (IADLXDisplayVariBright1)."""
        pass

    def IsWindowsPowerModeSupported(self) -> bool:
        """Checks if Windows Power Mode Vari-Bright Scaling mode is supported (IADLXDisplayVariBright1)."""
        pass

    def IsWindowsPowerModeEnabled(self) -> bool:
        """Checks if Windows Power Mode Vari-Bright Scaling mode is enabled (IADLXDisplayVariBright1)."""
        pass

    def SetWindowsPowerModeEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets Windows Power Mode Vari-Bright Scaling mode (IADLXDisplayVariBright1)."""
        pass

    def IsFullScreenVideoSupported(self) -> bool:
        """Checks if Full Screen Video Vari-Bright Scaling mode is supported (IADLXDisplayVariBright1)."""
        pass

    def IsFullScreenVideoEnabled(self) -> bool:
        """Checks if Full Screen Video Vari-Bright Scaling mode is enabled (IADLXDisplayVariBright1)."""
        pass

    def SetFullScreenVideoEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets Full Screen Video Vari-Bright Scaling mode (IADLXDisplayVariBright1)."""
        pass

class IADLXDisplayVSR(IADLXInterface):
    """The IADLXDisplayVSR interface provides methods for Virtual Super Resolution control."""

    def IsSupported(self) -> bool:
        """Checks if VSR is supported."""
        pass

    def IsEnabled(self) -> bool:
        """Checks if VSR is enabled."""
        pass

    def SetEnabled(self, enable: bool) -> ADLX_RESULT:
        """Sets VSR enabled state."""
        pass

class IADLXDisplayChangedHandling(IADLXInterface):
    """The IADLXDisplayChangedHandling interface provides methods for registering and unregistering for display change notifications."""

    def AddChangedListener(self, listener) -> ADLX_RESULT:
        """Adds a listener for display changes."""
        pass

    def RemoveChangedListener(self, listener) -> ADLX_RESULT:
        """Removes a listener for display changes."""
        pass

class IADLX3DSettingsServices(IADLXInterface):
    """The IADLX3DSettingsServices interface is the main interface for the 3D Graphics domain.
        It provides access to interfaces that control specific 3D Graphics settings features, such as
        AMD Radeon™ Anti-Lag, AMD Radeon™ Chill, AMD Radeon™ Boost, and AMD Radeon Image Sharpening.

        More info at: https://gpuopen.com/manuals/adlx/adlx-_d_o_x__i_a_d_l_x3_d_settings_services/

        How to get:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        three_d_settings_services = system.Get3DSettingsServices()
        ...
    """

    def __init__(self):
        """**Warning this class should not be instantiated**

        Instead get it as follow:

        ```python
        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        three_d_settings_services = system.Get3DSettingsServices()
        ...
        ```
        """
    def Get3DSettingsChangedHandling(self) -> IADLX3DSettingsChangedHandling:
        """Gets the reference-counted interface that allows registering and unregistering for notifications when 3D Graphics settings change.

        :return: IADLX3DSettingsChangedHandling interface, None if method fails
        :rtype: IADLX3DSettingsChangedHandling
        """
        pass
    def GetAMDFluidMotionFrames(self) -> IADLX3DAMDFluidMotionFrames:
        """Gets the reference-counted AMD Fluid Motion Frames interface.

        :return: IADLX3DAMDFluidMotionFrames interface, None if method fails
        :rtype: IADLX3DAMDFluidMotionFrames
        """
        pass
    def GetAnisotropicFiltering(self, pGPU: IADLXGPU) -> IADLX3DAnisotropicFiltering:
        """Gets the reference-counted Anisotropic Filtering interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DAnisotropicFiltering interface, None if method fails
        :rtype: IADLX3DAnisotropicFiltering
        """
        pass
    def GetAntiAliasing(self, pGPU: IADLXGPU) -> IADLX3DAntiAliasing:
        """Gets the reference-counted Anti-Aliasing interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DAntiAliasing interface, None if method fails
        :rtype: IADLX3DAntiAliasing
        """
        pass
    def GetAntiLag(self, pGPU: IADLXGPU) -> IADLX3DAntiLag:
        """Gets the reference-counted AMD Radeon™ Anti-Lag interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DAntiLag interface, None if method fails
        :rtype: IADLX3DAntiLag
        """
        pass
    def GetBoost(self, pGPU: IADLXGPU) -> IADLX3DBoost:
        """Gets the reference-counted AMD Radeon™ Boost interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DBoost interface, None if method fails
        :rtype: IADLX3DBoost
        """
        pass
    def GetChill(self, pGPU: IADLXGPU) -> IADLX3DChill:
        """Gets the reference-counted AMD Radeon™ Chill interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DChill interface, None if method fails
        :rtype: IADLX3DChill
        """
        pass
    def GetEnhancedSync(self, pGPU: IADLXGPU) -> IADLX3DEnhancedSync:
        """Gets the reference-counted AMD Radeon™ Enhanced Sync interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DEnhancedSync interface, None if method fails
        :rtype: IADLX3DEnhancedSync
        """
        pass
    def GetFrameRateTargetControl(self, pGPU: IADLXGPU) -> IADLX3DFrameRateTargetControl:
        """Gets the reference-counted AMD Frame Rate Target Control interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DFrameRateTargetControl interface, None if method fails
        :rtype: IADLX3DFrameRateTargetControl
        """
        pass
    def GetImageSharpening(self, pGPU: IADLXGPU) -> IADLX3DImageSharpening:
        """Gets the reference-counted AMD Radeon Image Sharpening interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DImageSharpening interface, None if method fails
        :rtype: IADLX3DImageSharpening
        """
        pass
    def GetMorphologicalAntiAliasing(self, pGPU: IADLXGPU) -> IADLX3DMorphologicalAntiAliasing:
        """Gets the reference-counted Morphological Anti-Aliasing interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DMorphologicalAntiAliasing interface, None if method fails
        :rtype: IADLX3DMorphologicalAntiAliasing
        """
        pass
    def GetRadeonSuperResolution(self) -> IADLX3DRadeonSuperResolution:
        """Gets the reference-counted Radeon™ Super Resolution interface.

        :return: IADLX3DRadeonSuperResolution interface, None if method fails
        :rtype: IADLX3DRadeonSuperResolution
        """
        pass
    def GetResetShaderCache(self, pGPU: IADLXGPU) -> IADLX3DResetShaderCache:
        """Gets the reference-counted Reset Shader Cache interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DResetShaderCache interface, None if method fails
        :rtype: IADLX3DResetShaderCache
        """
        pass
    def GetTessellation(self, pGPU: IADLXGPU) -> IADLX3DTessellation:
        """Gets the reference-counted Tessellation interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DTessellation interface, None if method fails
        :rtype: IADLX3DTessellation
        """
        pass
    def GetWaitForVerticalRefresh(self, pGPU: IADLXGPU) -> IADLX3DWaitForVerticalRefresh:
        """Gets the reference-counted Wait for Vertical Refresh interface of a GPU.

        :param pGPU: The pointer to the GPU interface
        :type pGPU: IADLXGPU
        :return: IADLX3DWaitForVerticalRefresh interface, None if method fails
        :rtype: IADLX3DWaitForVerticalRefresh
        """
        pass

class IADLXDesktopServices(IADLXInterface):
    """The IADLXDesktopServices is the main interface for the Desktop domain and
        provides control to desktop specific functionality.
        The IADLXDesktopServices interface provides:

        * The list of desktops instantiated on the AMD GPUs.
        * The interface for registering and unregistering for notifications when the desktops are changed.
        * The interface for creating and destroying AMD Eyefinity desktops.

        More info at: https://gpuopen.com/manuals/adlx/adlx-_d_o_x__i_a_d_l_x_desktop_services/

        How to get:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        desktop_services = system.GetDesktopsServices()
        ...
    """

    def __init__(self):
        """**Warning this class should not be instantiated**

        Instead get it as follow:

        ```python
        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        desktop_services = system.GetDesktopsServices()
        ...
        ```
        """
    def GetDesktopChangedHandling(self) -> IADLXDesktopChangedHandling:
        """Gets the reference counted interface that allows registering and unregistering for notifications when desktop settings change.

        :return: IADLXDesktopChangedHandling interface, None if method fails
        :rtype: IADLXDesktopChangedHandling
        """
        pass
    def GetDesktops(self) -> List[IADLXDesktop]:
        """Gets the reference counted list of desktops instantiated on the AMD GPUs.

        :return: Python list of IADLXDesktop interface
        :rtype: List[IADLXDesktop]
        """
        pass
    def GetNumberOfDesktops(self) -> int:
        """Gets the number of desktops instantiated on the AMD GPUs.

        :return: Number of desktops instantiated on the AMD GPUs.
        :rtype: int
        """
        pass
    def GetSimpleEyefinity(self) -> IADLXSimpleEyefinity:
        """Gets the reference counted interface to create and destroy AMD Eyefinity desktops.

        :return: IADLXSimpleEyefinity interface, None if method fails
        :rtype: IADLXSimpleEyefinity
        """
        pass

class IADLXDisplayServices(IADLXInterface):
    """The IADLXDisplayServices is the main interface of the Display domain
        and provides control to the display-specific functionality.
        The IADLXDesktopServices interface provides:

        * The list of displays connected to the AMD GPUs.
        * The interface for registering and unregistering for notifications when the displays are changed.
        * Access to gamut, gamma, 3D LUT, and display settings functionality for a given display.

        More info at: https://gpuopen.com/manuals/adlx/adlx-_d_o_x__i_a_d_l_x_display_services/

        How to get:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        display_services = system.GetDisplaysServices()
        ...
    """

    def __init__(self):
        """**Warning this class should not be instantiated**

        Instead get it as follow:

        ```python
        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        display_services = system.GetDisplaysServices()
        ...
        ```
        """
    def Get3DLUT(self, pDisplay: IADLXDisplay) -> IADLXDisplay3DLUT:
        """Gets the reference counted 3D LUT interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplay3DLUT interface, None if method fails
        :rtype: IADLXDisplay3DLUT
        """
        pass
    def GetColorDepth(self, pDisplay: IADLXDisplay) -> IADLXDisplayColorDepth:
        """Gets the reference counted color depth interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayColorDepth interface, None if method fails
        :rtype: IADLXDisplayColorDepth
        """
        pass
    def GetCustomColor(self, pDisplay: IADLXDisplay) -> IADLXDisplayCustomColor:
        """Gets the reference counted custom color interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayCustomColor interface, None if method fails
        :rtype: IADLXDisplayCustomColor
        """
        pass
    def GetCustomResolution(self, pDisplay: IADLXDisplay) -> IADLXDisplayCustomResolution:
        """Gets the reference counted custom resolution interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayCustomResolution interface, None if method fails
        :rtype: IADLXDisplayCustomResolution
        """
        pass
    def GetDisplayChangedHandling(self) -> IADLXDisplayChangedHandling:
        """Gets the reference counted interface that allows registering and unregistering for notifications when display change.

        :return: IADLXDisplayChangedHandling interface, None if method fails
        :rtype: IADLXDisplayChangedHandling
        """
        pass
    def GetDisplays(self) -> List[IADLXDisplay]:
        """Gets the reference counted list of display instantiated on the AMD GPUs.

        :return: Python list of IADLXDisplay interface
        :rtype: List[IADLXDisplay]
        """
        pass
    def GetDisplaysListRaw(self) -> IADLXDisplayList:
        """Gets the reference counted list of display instantiated on the AMD GPUs.

        .. note::
            This returns a CPPlike Object, if you want a python list consider using **GetDisplays()**

        :return: IADLXDisplayList interface, None if method fails
        :rtype: IADLXDisplayList
        """
        pass
    def GetFreeSync(self, pDisplay: IADLXDisplay) -> IADLXDisplayFreeSync:
        """Gets the reference counted AMD FreeSync™ Technology interface.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayFreeSync interface, None if method fails
        :rtype: IADLXDisplayFreeSync
        """
        pass
    def GetGamma(self, pDisplay: IADLXDisplay) -> IADLXDisplayGamma:
        """Gets the reference counted gamma interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayGamma interface, None if method fails
        :rtype: IADLXDisplayGamma
        """
        pass
    def GetGamut(self, pDisplay: IADLXDisplay) -> IADLXDisplayGamut:
        """Gets the reference counted gamut interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayGamut interface, None if method fails
        :rtype: IADLXDisplayGamut
        """
        pass
    def GetGPUScaling(self, pDisplay: IADLXDisplay) -> IADLXDisplayGPUScaling:
        """Gets the reference counted GPU scaling interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayGPUScaling interface, None if method fails
        :rtype: IADLXDisplayGPUScaling
        """
        pass
    def GetHDCP(self, pDisplay: IADLXDisplay) -> IADLXDisplayHDCP:
        """Gets the reference counted HDCP interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayHDCP interface, None if method fails
        :rtype: IADLXDisplayHDCP
        """
        pass
    def GetIntegerScaling(self, pDisplay: IADLXDisplay) -> IADLXDisplayIntegerScaling:
        """Gets the reference counted integer scaling interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayIntegerScaling interface, None if method fails
        :rtype: IADLXDisplayIntegerScaling
        """
        pass
    def GetNumberOfDisplays(self) -> int:
        """Gets the number of displays connected to the AMD GPUs.

        :return: Number of displays connected to the AMD GPUs.
        :rtype: int
        """
        pass
    def GetPixelFormat(self, pDisplay: IADLXDisplay) -> IADLXDisplayPixelFormat:
        """Gets the reference counted pixel format interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayPixelFormat interface, None if method fails
        :rtype: IADLXDisplayPixelFormat
        """
        pass
    def GetScalingMode(self, pDisplay: IADLXDisplay) -> IADLXDisplayScalingMode:
        """Gets the reference counted scaling mode interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayScalingMode interface, None if method fails
        :rtype: IADLXDisplayScalingMode
        """
        pass
    def GetVariBright(self, pDisplay: IADLXDisplay) -> IADLXDisplayVariBright:
        """Gets the reference counted Vari-Bright interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayVariBright interface, None if method fails
        :rtype: IADLXDisplayVariBright
        """
        pass
    def GetVirtualSuperResolution(self, pDisplay: IADLXDisplay) -> IADLXDisplayVSR:
        """Gets the reference counted virtual super resolution interface for a display.

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayVSR interface, None if method fails
        :rtype: IADLXDisplayVSR
        """
        pass
    def GetDisplayBlanking(self, pDisplay: IADLXDisplay) -> IADLXDisplayBlanking:
        """Gets the reference counted display blanking interface for a display (IADLXDisplayServices1).

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        :return: IADLXDisplayBlanking interface, None if method fails
        :rtype: IADLXDisplayBlanking
        """
        pass
    def GetDisplayConnectivityExperience(self, pDisplay: IADLXDisplay):
        """Gets the reference counted display connectivity experience interface for a display (IADLXDisplayServices2).

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        """
        pass
    def GetDynamicRefreshRateControl(self, pDisplay: IADLXDisplay):
        """Gets the reference counted dynamic refresh rate control interface for a display (IADLXDisplayServices3).

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        """
        pass
    def GetFreeSyncColorAccuracy(self, pDisplay: IADLXDisplay):
        """Gets the reference counted FreeSync color accuracy interface for a display (IADLXDisplayServices3).

        :param pDisplay:  The pointer to the display interface.
        :type pDisplay: IADLXDisplay
        """
        pass

class IADLXGPU(IADLXInterface):
    """The IADLXGPU interface provides properties of a GPU, such as name and type.

        More info at: https://gpuopen.com/manuals/adlx/adlx-_d_o_x__i_a_d_l_x_g_p_u/

        How to get:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        gpus = system.GetGPUs()
        ...
    """

    def __init__(self):
        """**Warning this class should not be instantiated**

        Instead get it as follow:

        ```python
        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        gpus = system.GetGPUs()
        ...
        ```
        """
    def ASICFamilyType(self) -> ADLX_ASIC_FAMILY_TYPE:
        """Gets the ASIC family type of a GPU.

        :return: ASIC family type
        :rtype: ADLX_ASIC_FAMILY_TYPE
        """
        pass
    def BIOSInfo(self) -> Tuple[str, str, str]:
        """Gets the BIOS info of a GPU.

        :return: (partNumber, version, date)
        :rtype: Tuple[str,str,str]
        """
        pass
    def DeviceId(self) -> str:
        """Gets the device id of a GPU.

        :return: Device id
        :rtype: str
        """
        pass
    def DriverPath(self) -> str:
        """Gets the driver registry path of a GPU.

        :return: Driver registry path of a GPU.
        :rtype: str
        """
        pass
    def HasDesktops(self) -> bool:
        """Checks if a GPU drives any desktops.

        :return: True if GPPU drives any desktops otherwise False
        :rtype: bool
        """
        pass
    def IsExternal(self) -> bool:
        """Checks if a GPU is an external or internal GPU.

        :return: True if the GPU is external, False if the GPU is internal
        :rtype: bool
        """
        pass
    def Name(self) -> str:
        """Gets the name of a GPU.

        :return: Name of GPU
        :rtype: str
        """
        pass
    def PNPString(self) -> str:
        """Gets the PNP string of a GPU.

        :return: PNP string of a GPU.
        :rtype: str
        """
        pass
    def RevisionId(self) -> str:
        """Gets the revision id of a GPU.

        :return: Revision id
        :rtype: str
        """
        pass
    def SubSystemId(self) -> str:
        """Gets the subsystem id of a GPU.

        :return: Subsystem id
        :rtype: str
        """
        pass
    def SubSystemVendorId(self) -> str:
        """Gets the subsystem vendor id of a GPU.

        :return: Subsystem vendor id
        :rtype: str
        """
        pass
    def TotalVRAM(self) -> int:
        """Gets the total VRAM size(MB) of a GPU.

        :return: VRAM size(MB)
        :rtype: int
        """
        pass
    def Type(self) -> ADLX_GPU_TYPE:
        """Gets the type of a GPU.

        :return: GPU type
        :rtype: ADLX_GPU_TYPE
        """
        pass
    def UniqueId(self) -> int:
        """Gets the unique id of a GPU.

        :return: Unique id
        :rtype: int
        """
        pass
    def VendorId(self) -> str:
        """Gets the vendor id of a GPU.

        :return: Vendor id
        :rtype: str
        """
        pass
    def VRAMType(self) -> str:
        """Gets the VRAM type of a GPU.

        :return: VRAM type
        :rtype: str
        """
        pass
    def PCIBusType(self) -> ADLX_PCI_BUS_TYPE:
        """Gets the PCI bus type of a GPU.

        :return: PCI bus type
        :rtype: ADLX_PCI_BUS_TYPE
        """
        pass
    def PCIBusLaneWidth(self) -> int:
        """Gets the PCI bus lane width of a GPU.

        :return: PCI bus lane width
        :rtype: int
        """
        pass
    def MultiGPUMode(self) -> ADLX_MGPU_MODE:
        """Gets the mGPU mode of a GPU.

        :return: mGPU mode
        :rtype: ADLX_MGPU_MODE
        """
        pass
    def ProductName(self) -> str:
        """Gets the product name of a GPU.

        :return: Product name
        :rtype: str
        """
        pass
    def IsSupportedApplicationList(self) -> bool:
        """Checks if support get application list on a GPU.

        :return: True if the GPU supports get application list, False if the GPU does not support it
        :rtype: bool
        """
        pass
    def LUID(self) -> ADLX_LUID:
        """Gets the LUID of a GPU.

        :return: LUID
        :rtype: ADLX_LUID
        """
        pass
    def GetApplications(self) -> List:
        """Gets the list of applications running on a GPU (IADLXGPU2).

        :return: List of applications
        :rtype: List
        """
        pass
    def AMDSoftwareReleaseDate(self) -> Tuple[int, int, int]:
        """Gets the AMD software release date of a GPU (IADLXGPU2).

        :return: (year, month, day)
        :rtype: Tuple[int, int, int]
        """
        pass
    def AMDSoftwareEdition(self) -> str:
        """Gets the AMD software edition of a GPU (IADLXGPU2).

        :return: AMD software edition
        :rtype: str
        """
        pass
    def AMDSoftwareVersion(self) -> str:
        """Gets the AMD software version of a GPU (IADLXGPU2).

        :return: AMD software version
        :rtype: str
        """
        pass
    def DriverVersion(self) -> str:
        """Gets the driver version of a GPU (IADLXGPU2).

        :return: Driver version
        :rtype: str
        """
        pass
    def AMDWindowsDriverVersion(self) -> str:
        """Gets the AMD Windows driver version of a GPU (IADLXGPU2).

        :return: AMD Windows driver version
        :rtype: str
        """
        pass
    def IsPowerOff(self) -> bool:
        """Checks if a GPU is powered off (IADLXGPU2).

        :return: True if the GPU is powered off
        :rtype: bool
        """
        pass
    def PowerOn(self) -> ADLX_RESULT:
        """Powers on a GPU (IADLXGPU2).

        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass
    def AbortPowerOff(self) -> ADLX_RESULT:
        """Aborts powering off a GPU (IADLXGPU2).

        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass
    def MicroArchitecture(self) -> str:
        """Gets the microarchitecture of a GPU (IADLXGPU3).

        :return: Microarchitecture
        :rtype: str
        """
        pass
    def HighestVRAMBandwidth(self) -> int:
        """Gets the maximum VRAM bandwidth on a GPU in Mbytes/s (IADLXGPU3).

        :return: Highest VRAM bandwidth
        :rtype: int
        """
        pass
    def InvisibleVRAM(self) -> int:
        """Gets the size of the invisible VRAM on a GPU in MB (IADLXGPU3).

        :return: Invisible VRAM size
        :rtype: int
        """
        pass
    def VisibleVRAM(self) -> int:
        """Gets the size of the visible VRAM on a GPU in MB (IADLXGPU3).

        :return: Visible VRAM size
        :rtype: int
        """
        pass
    def VRAMVendorRevId(self) -> int:
        """Gets the VRAM vendor ID (IADLXGPU3).

        :return: VRAM vendor revision ID
        :rtype: int
        """
        pass
    def VRAMBandwidth(self) -> int:
        """Gets the VRAM bandwidth on a GPU in Mbytes/s (IADLXGPU3).

        :return: VRAM bandwidth
        :rtype: int
        """
        pass
    def VRAMBitRate(self) -> int:
        """Gets the bit rate of the VRAM on a GPU in Mbps (IADLXGPU3).

        :return: VRAM bit rate
        :rtype: int
        """
        pass
    def IsSupportedStressTest(self) -> bool:
        """Checks if GPU stress testing is supported (IADLXGPU3).

        :return: True if stress test is supported
        :rtype: bool
        """
        pass
    def StartPowerOff(self, pListener: 'PyGPUConnectChangedListenerCallback', timeout: int) -> ADLX_RESULT:
        """Starts powering off a GPU (IADLXGPU2).

        :param pListener: The GPU Connect changed listener callback.
        :type pListener: PyGPUConnectChangedListenerCallback
        :param timeout: The timeout for the power off operation.
        :type timeout: int
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass
    def StartStressTest(self, pListener: 'PyGPUStressTestFinishedListenerCallback', duration: int) -> ADLX_RESULT:
        """Starts a GPU stress test (IADLXGPU3).

        :param pListener: The GPU stress test finished listener callback.
        :type pListener: PyGPUStressTestFinishedListenerCallback
        :param duration: The duration for the stress test in seconds.
        :type duration: int
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

class PyGPUsEventListenerCallback:
    """Callback interface for GPU list change events."""

    def OnGPUListChanged(self) -> bool:
        """Called when the GPU list changes."""
        pass

class IADLXGPUAutoTuning(IADLXInterface):
    """The IADLXGPUAutoTuning interface provides methods for GPU auto-tuning."""

    def IsCurrentOverclockGPU(self) -> bool:
        """Checks if GPU overclock is currently enabled."""
        pass

    def IsCurrentOverclockVRAM(self) -> bool:
        """Checks if VRAM overclock is currently enabled."""
        pass

    def IsCurrentUndervoltGPU(self) -> bool:
        """Checks if GPU undervolt is currently enabled."""
        pass

    def IsSupportedOverclockGPU(self) -> bool:
        """Checks if GPU overclock is supported."""
        pass

    def IsSupportedOverclockVRAM(self) -> bool:
        """Checks if VRAM overclock is supported."""
        pass

    def IsSupportedUndervoltGPU(self) -> bool:
        """Checks if GPU undervolt is supported."""
        pass

    def StartOverclockGPU(self, pCompleteListener: Any) -> ADLX_RESULT:
        """Starts GPU overclock with completion listener."""
        pass

    def StartOverclockVRAM(self, pCompleteListener: Any) -> ADLX_RESULT:
        """Starts VRAM overclock with completion listener."""
        pass

    def StartUndervoltGPU(self, pCompleteListener: Any) -> ADLX_RESULT:
        """Starts GPU undervolt with completion listener."""
        pass

    def QueryInterface(self, interfaceId: str) -> 'IADLXGPUAutoTuning':
        """Queries for an interface."""
        pass

class IADLXGPUTuningChangedHandling(IADLXInterface):
    """The IADLXGPUTuningChangedHandling interface provides methods for registering and unregistering for GPU tuning change notifications."""

    def AddChangedListener(self, listener) -> ADLX_RESULT:
        """Adds a listener for GPU tuning changes."""
        pass

    def RemoveChangedListener(self, listener) -> ADLX_RESULT:
        """Removes a listener for GPU tuning changes."""
        pass

class IADLXManualFanTuning(IADLXInterface):
    """The IADLXManualFanTuning interface provides methods for manual fan tuning."""

    def GetEmptyFanTuningStates(self) -> List['IADLXManualFanTuningState']:
        """Gets an empty list of fan tuning states."""
        pass

    def GetFanTuningRanges(self) -> Dict[str, Any]:
        """Gets the fan tuning ranges for temperature and speed."""
        pass

    def GetFanTuningStates(self) -> List['IADLXManualFanTuningState']:
        """Gets the current fan tuning states."""
        pass

    def GetMinAcousticLimit(self) -> int:
        """Gets the minimum acoustic limit."""
        pass

    def GetMinAcousticLimitRange(self) -> Dict[str, int]:
        """Gets the minimum acoustic limit range with max_value, min_value, and step."""
        pass

    def GetMinFanSpeed(self) -> int:
        """Gets the minimum fan speed."""
        pass

    def GetMinFanSpeedRange(self) -> Dict[str, int]:
        """Gets the minimum fan speed range with max_value, min_value, and step."""
        pass

    def GetTargetFanSpeed(self) -> int:
        """Gets the target fan speed."""
        pass

    def GetTargetFanSpeedRange(self) -> Dict[str, int]:
        """Gets the target fan speed range with max_value, min_value, and step."""
        pass

    def GetZeroRPMState(self) -> bool:
        """Gets the zero RPM state."""
        pass

    def IsSupportedMinAcousticLimit(self) -> bool:
        """Checks if minimum acoustic limit is supported."""
        pass

    def IsSupportedMinFanSpeed(self) -> bool:
        """Checks if minimum fan speed is supported."""
        pass

    def IsSupportedTargetFanSpeed(self) -> bool:
        """Checks if target fan speed is supported."""
        pass

    def IsSupportedZeroRPM(self) -> bool:
        """Checks if zero RPM is supported."""
        pass

    def IsValidFanTuningStates(self, states: List['IADLXManualFanTuningState']) -> int:
        """Validates fan tuning states and returns error index (-1 if valid)."""
        pass

    def SetFanTuningStates(self, states: List['IADLXManualFanTuningState']) -> ADLX_RESULT:
        """Sets the fan tuning states."""
        pass

    def SetMinAcousticLimit(self, value: int) -> ADLX_RESULT:
        """Sets the minimum acoustic limit."""
        pass

    def SetMinFanSpeed(self, value: int) -> ADLX_RESULT:
        """Sets the minimum fan speed."""
        pass

    def SetTargetFanSpeed(self, value: int) -> ADLX_RESULT:
        """Sets the target fan speed."""
        pass

    def SetZeroRPMState(self, value: int) -> ADLX_RESULT:
        """Sets the zero RPM state."""
        pass

    def GetDefaultFanTuningStates(self) -> List['IADLXManualFanTuningState']:
        """Gets the default fan tuning states."""
        pass

    def GetMinAcousticLimitDefault(self) -> int:
        """Gets the default minimum acoustic limit."""
        pass

    def GetMinFanSpeedDefault(self) -> int:
        """Gets the default minimum fan speed."""
        pass

    def GetTargetFanSpeedDefault(self) -> int:
        """Gets the default target fan speed."""
        pass

    def GetDefaultZeroRPMState(self) -> bool:
        """Gets the default zero RPM state."""
        pass

    def QueryInterface(self, interfaceId: str) -> 'IADLXManualFanTuning':
        """Queries for an interface."""
        pass

    def GetFanTuningStatesRaw(self) -> 'IADLXManualFanTuningStateList':
        """Gets the current fan tuning states as raw list object."""
        pass

class IADLXManualGraphicsTuning1(IADLXInterface):
    """The IADLXManualGraphicsTuning1 interface provides methods for manual graphics tuning (version 1)."""

    def GetGPUTuningRanges(self) -> Dict[str, Any]:
        """Gets the GPU tuning ranges for frequency and voltage.
        
        Returns a dictionary with 'frequency_range' and 'voltage_range' keys, 
        each containing ADLX_IntRange objects.
        """
        pass

    def GetEmptyGPUTuningStates(self) -> List['IADLXManualTuningState']:
        """Gets empty GPU tuning states list."""
        pass

    def GetGPUTuningStates(self) -> List['IADLXManualTuningState']:
        """Gets the current GPU tuning states."""
        pass

    def IsValidGPUTuningStates(self, states: List['IADLXManualTuningState']) -> int:
        """Validates GPU tuning states and returns error index or -1 if valid."""
        pass

    def SetGPUTuningStates(self, states: List['IADLXManualTuningState']) -> ADLX_RESULT:
        """Sets the GPU tuning states."""
        pass

    def QueryInterface(self, interfaceId: str) -> 'IADLXManualGraphicsTuning1':
        """Queries for an interface."""
        pass

class IADLXManualGraphicsTuning2(IADLXInterface):
    """The IADLXManualGraphicsTuning2 interface provides methods for manual graphics tuning (version 2)."""

    def GetGPUMaxFrequency(self) -> int | None:
        """Gets the current GPU maximum frequency."""
        pass

    def GetGPUMaxFrequencyRange(self) -> Dict[str, int] | None:
        """Gets the GPU maximum frequency range with max_value, min_value, and step."""
        pass

    def GetGPUMinFrequency(self) -> int | None:
        """Gets the current GPU minimum frequency."""
        pass

    def GetGPUMinFrequencyRange(self) -> Dict[str, int] | None:
        """Gets the GPU minimum frequency range with max_value, min_value, and step."""
        pass

    def GetGPUVoltage(self) -> int | None:
        """Gets the current GPU voltage."""
        pass

    def GetGPUVoltageRange(self) -> Dict[str, int] | None:
        """Gets the GPU voltage range with max_value, min_value, and step."""
        pass

    def SetGPUMaxFrequency(self, maxFreq: int) -> ADLX_RESULT:
        """Sets the GPU maximum frequency."""
        pass

    def SetGPUMinFrequency(self, minFreq: int) -> ADLX_RESULT:
        """Sets the GPU minimum frequency."""
        pass

    def SetGPUVoltage(self, voltage: int) -> ADLX_RESULT:
        """Sets the GPU voltage."""
        pass

    def GetGPUMinFrequencyDefault(self) -> int | None:
        """Gets the default GPU minimum frequency."""
        pass

    def GetGPUMaxFrequencyDefault(self) -> int | None:
        """Gets the default GPU maximum frequency."""
        pass

    def GetGPUVoltageDefault(self) -> int | None:
        """Gets the default GPU voltage."""
        pass

    def QueryInterface(self, interfaceId: str) -> 'IADLXManualGraphicsTuning2':
        """Queries for an interface."""
        pass

class IADLXManualPowerTuning(IADLXInterface):
    """The IADLXManualPowerTuning interface provides methods for manual power tuning."""

    def GetPowerLimitRange(self) -> Dict[str, int]:
        """Gets the power limit range with max_value, min_value, and step."""
        pass

    def GetPowerLimit(self) -> int | None:
        """Gets the current power limit."""
        pass

    def SetPowerLimit(self, limit: int) -> ADLX_RESULT:
        """Sets the power limit."""
        pass

    def GetTDCLimitRange(self) -> Dict[str, int]:
        """Gets the TDC limit range with max_value, min_value, and step."""
        pass

    def GetTDCLimit(self) -> int | None:
        """Gets the current TDC limit."""
        pass

    def SetTDCLimit(self, limit: int) -> ADLX_RESULT:
        """Sets the TDC limit."""
        pass

    def IsSupportedTDCLimit(self) -> bool:
        """Checks if TDC limit is supported."""
        pass

    def GetPowerLimitDefault(self) -> int | None:
        """Gets the default power limit."""
        pass

    def GetTDCLimitDefault(self) -> int | None:
        """Gets the default TDC limit."""
        pass

    def QueryInterface(self, interfaceId: str) -> 'IADLXManualPowerTuning':
        """Queries for an interface."""
        pass

class IADLXManualVRAMTuning1(IADLXInterface):
    """The IADLXManualVRAMTuning1 interface provides methods for manual VRAM tuning (version 1)."""

    def GetVRAMTuningRanges(self) -> Dict[str, Dict[str, int]]:
        """Gets the VRAM tuning ranges for frequency and voltage.
        
        Returns a dictionary with 'frequency_range' and 'voltage_range' keys,
        each containing dicts with 'max_value', 'min_value', and 'step'.
        """
        pass

    def GetEmptyVRAMTuningStates(self) -> List['IADLXManualTuningState']:
        """Gets empty VRAM tuning states list."""
        pass

    def GetVRAMTuningStates(self) -> List['IADLXManualTuningState']:
        """Gets the current VRAM tuning states."""
        pass

    def IsValidVRAMTuningStates(self, states: List['IADLXManualTuningState']) -> int:
        """Validates VRAM tuning states and returns error index or -1 if valid."""
        pass

    def SetVRAMTuningStates(self, states: List['IADLXManualTuningState']) -> ADLX_RESULT:
        """Sets the VRAM tuning states."""
        pass

    def GetMemoryTimingDescription(self) -> ADLX_MEMORYTIMING_DESCRIPTION | None:
        """Gets the memory timing description."""
        pass

    def GetSupportedMemoryTimingDescriptionList(self) -> List['IADLXMemoryTimingDescription']:
        """Gets the list of supported memory timing descriptions."""
        pass

    def IsSupportedMemoryTiming(self) -> bool:
        """Checks if memory timing is supported."""
        pass

    def SetMemoryTimingDescription(self, description: ADLX_MEMORYTIMING_DESCRIPTION) -> ADLX_RESULT:
        """Sets the memory timing description."""
        pass

    def GetVRAMTuningStatesRaw(self) -> 'IADLXManualTuningStateList':
        """Gets the raw VRAM tuning states list."""
        pass

    def QueryInterface(self, interfaceId: str) -> 'IADLXManualVRAMTuning1':
        """Queries for an interface."""
        pass

class IADLXManualVRAMTuning2(IADLXInterface):
    """The IADLXManualVRAMTuning2 interface provides methods for manual VRAM tuning (version 2)."""

    def GetMaxVRAMFrequency(self) -> int:
        """Gets the maximum VRAM frequency."""
        pass

    def GetMaxVRAMFrequencyRange(self) -> Dict[str, int]:
        """Gets the maximum VRAM frequency range with max_value, min_value, and step."""
        pass

    def GetMemoryTimingDescription(self) -> ADLX_MEMORYTIMING_DESCRIPTION:
        """Gets the memory timing description."""
        pass

    def GetSupportedMemoryTimingDescriptionList(self) -> List['IADLXMemoryTimingDescription']:
        """Gets the list of supported memory timing descriptions."""
        pass

    def IsSupportedMemoryTiming(self) -> bool:
        """Checks if memory timing is supported."""
        pass

    def SetMaxVRAMFrequency(self, freq: int) -> ADLX_RESULT:
        """Sets the maximum VRAM frequency."""
        pass

    def SetMemoryTimingDescription(self, description: ADLX_MEMORYTIMING_DESCRIPTION) -> ADLX_RESULT:
        """Sets the memory timing description."""
        pass

    def GetMaxVRAMFrequencyDefault(self) -> int:
        """Gets the default maximum VRAM frequency."""
        pass

    def QueryInterface(self, interfaceId: str) -> 'IADLXManualVRAMTuning2':
        """Queries for an interface."""
        pass

    def GetSupportedMemoryTimingDescriptionListRaw(self) -> 'IADLXMemoryTimingDescriptionList':
        """Gets the raw list object of supported memory timing descriptions."""
        pass

class IADLXGPUPresetTuning(IADLXInterface):
    """The IADLXGPUPresetTuning interface provides methods for GPU preset tuning."""

    def IsSupported(self) -> bool:
        """Checks if preset tuning is supported."""
        pass

    def IsCurrentPowerSaver(self) -> bool:
        """Checks if current preset is Power Saver."""
        pass

    def IsCurrentQuiet(self) -> bool:
        """Checks if current preset is Quiet."""
        pass

    def IsCurrentBalanced(self) -> bool:
        """Checks if current preset is Balanced."""
        pass

    def IsCurrentTurbo(self) -> bool:
        """Checks if current preset is Turbo."""
        pass

    def IsCurrentRage(self) -> bool:
        """Checks if current preset is Rage."""
        pass

    def SetPowerSaver(self) -> ADLX_RESULT:
        """Sets preset to Power Saver."""
        pass

    def SetQuiet(self) -> ADLX_RESULT:
        """Sets preset to Quiet."""
        pass

    def SetBalanced(self) -> ADLX_RESULT:
        """Sets preset to Balanced."""
        pass

    def SetTurbo(self) -> ADLX_RESULT:
        """Sets preset to Turbo."""
        pass

    def SetRage(self) -> ADLX_RESULT:
        """Sets preset to Rage."""
        pass

class IADLXGPUMetrics(IADLXInterface):
    """The IADLXGPUMetrics interface provides methods for accessing GPU performance metrics."""

    def TimeStamp(self) -> int | None:
        """Gets the timestamp of the metrics."""
        pass

    def GPUUsage(self) -> float | None:
        """Gets the GPU usage percentage."""
        pass

    def GPUClockSpeed(self) -> int | None:
        """Gets the GPU clock speed in MHz."""
        pass

    def GPUVRAMClockSpeed(self) -> int | None:
        """Gets the GPU VRAM clock speed in MHz."""
        pass

    def GPUTemperature(self) -> float | None:
        """Gets the GPU temperature in Celsius."""
        pass

    def GPUHotspotTemperature(self) -> float | None:
        """Gets the GPU hotspot temperature in Celsius."""
        pass

    def GPUPower(self) -> float | None:
        """Gets the GPU power consumption in Watts."""
        pass

    def GPUFanSpeed(self) -> int | None:
        """Gets the GPU fan speed in RPM."""
        pass

    def GPUVRAM(self) -> int | None:
        """Gets the GPU VRAM usage in MB."""
        pass

    def GPUVoltage(self) -> int | None:
        """Gets the GPU voltage in mV."""
        pass

    def GPUTotalBoardPower(self) -> float | None:
        """Gets the GPU total board power in Watts."""
        pass

    def GPUIntakeTemperature(self) -> float | None:
        """Gets the GPU intake temperature in Celsius."""
        pass

    def GPUMemoryTemperature(self) -> float | None:
        """Gets the GPU memory temperature in Celsius."""
        pass

    def NPUFrequency(self) -> int | None:
        """Gets the NPU frequency in MHz."""
        pass

    def NPUActivityLevel(self) -> int | None:
        """Gets the NPU activity level percentage."""
        pass

    def GPUSharedMemory(self) -> int | None:
        """Gets the GPU shared memory usage in MB."""
        pass

    def GPUFanDuty(self) -> int | None:
        """Gets the GPU fan duty cycle percentage."""
        pass

class IADLXSystemMetrics(IADLXInterface):
    """The IADLXSystemMetrics interface provides methods for accessing system performance metrics."""

    def TimeStamp(self) -> int | None:
        """Gets the timestamp of the metrics.
        
        Returns the timestamp in milliseconds on success, or None on failure.
        """
        pass

    def CPUUsage(self) -> float | None:
        """Gets the CPU usage percentage.
        
        Returns the CPU usage percentage on success, or None on failure.
        """
        pass

    def SystemRAM(self) -> int | None:
        """Gets the system RAM usage in MB.
        
        Returns the system RAM usage in MB on success, or None on failure.
        """
        pass

    def SmartShift(self) -> int | None:
        """Gets the SmartShift value.
        
        Returns the SmartShift value on success, or None on failure.
        """
        pass

    def PowerDistribution(self) -> Tuple[int, int, int, int, int]:
        """Gets the power distribution values.
        
        Returns a tuple of (apuShiftValue, gpuShiftValue, apuShiftLimit, gpuShiftLimit, totalShiftLimit).
        """
        pass

class IADLXFPS(IADLXInterface):
    """The IADLXFPS interface provides methods for accessing FPS (frames per second) metrics."""

    def TimeStamp(self) -> int | None:
        """Gets the timestamp of the FPS measurement.
        
        Returns the timestamp in milliseconds on success, or None on failure.
        """
        pass

    def FPS(self) -> int | None:
        """Gets the FPS value.
        
        Returns the FPS value on success, or None on failure.
        """
        pass

class IADLXAllMetrics(IADLXInterface):
    """The IADLXAllMetrics interface provides methods for accessing all performance metrics."""

    def TimeStamp(self) -> int | None:
        """Gets the timestamp of the metrics."""
        pass

    def GetGPUMetrics(self, gpu: IADLXGPU) -> IADLXGPUMetrics:
        """Gets GPU metrics for a specific GPU."""
        pass

    def GetSystemMetrics(self) -> IADLXSystemMetrics:
        """Gets system metrics."""
        pass

    def GetFPS(self) -> IADLXFPS:
        """Gets FPS metrics."""
        pass

class IADLXFPSList(IADLXList):
    """The IADLXFPSList interface provides methods for managing a list of FPS metrics."""

    def Add_Back(self, item: IADLXFPS) -> ADLX_RESULT:
        """Adds FPS metrics to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last FPS metrics from the list."""
        pass

class IADLXAllMetricsList(IADLXList):
    """The IADLXAllMetricsList interface provides methods for managing a list of all metrics."""

    def Add_Back(self, item: IADLXAllMetrics) -> ADLX_RESULT:
        """Adds all metrics to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last all metrics from the list."""
        pass

class IADLXGPUMetricsList(IADLXList):
    """The IADLXGPUMetricsList interface provides methods for managing a list of GPU metrics."""

    def Add_Back(self, item: IADLXGPUMetrics) -> ADLX_RESULT:
        """Adds GPU metrics to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last GPU metrics from the list."""
        pass

class IADLXSystemMetricsList(IADLXList):
    """The IADLXSystemMetricsList interface provides methods for managing a list of system metrics."""

    def Add_Back(self, item: IADLXSystemMetrics) -> ADLX_RESULT:
        """Adds system metrics to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last system metrics from the list."""
        pass

class IADLXGPUMetricsSupport(IADLXInterface):
    """The IADLXGPUMetricsSupport interface provides methods for checking which GPU metrics are supported."""

    def IsSupportedGPUUsage(self) -> bool:
        """Checks if GPU usage metric is supported."""
        pass

    def IsSupportedGPUClockSpeed(self) -> bool:
        """Checks if GPU clock speed metric is supported."""
        pass

    def IsSupportedGPUVRAMClockSpeed(self) -> bool:
        """Checks if GPU VRAM clock speed metric is supported."""
        pass

    def IsSupportedGPUTemperature(self) -> bool:
        """Checks if GPU temperature metric is supported."""
        pass

    def IsSupportedGPUHotspotTemperature(self) -> bool:
        """Checks if GPU hotspot temperature metric is supported."""
        pass

    def IsSupportedGPUPower(self) -> bool:
        """Checks if GPU power metric is supported."""
        pass

    def IsSupportedGPUTotalBoardPower(self) -> bool:
        """Checks if GPU total board power metric is supported."""
        pass

    def IsSupportedGPUFanSpeed(self) -> bool:
        """Checks if GPU fan speed metric is supported."""
        pass

    def IsSupportedGPUVRAM(self) -> bool:
        """Checks if GPU VRAM metric is supported."""
        pass

    def IsSupportedGPUVoltage(self) -> bool:
        """Checks if GPU voltage metric is supported."""
        pass

    def IsSupportedGPUIntakeTemperature(self) -> bool:
        """Checks if GPU intake temperature metric is supported."""
        pass

    def IsSupportedGPUMemoryTemperature(self) -> bool:
        """Checks if GPU memory temperature metric is supported."""
        pass

    def IsSupportedNPUFrequency(self) -> bool:
        """Checks if NPU frequency metric is supported."""
        pass

    def IsSupportedNPUActivityLevel(self) -> bool:
        """Checks if NPU activity level metric is supported."""
        pass

    def IsSupportedGPUSharedMemory(self) -> bool:
        """Checks if GPU shared memory metric is supported."""
        pass

    def IsSupportedGPUFanDuty(self) -> bool:
        """Checks if GPU fan duty metric is supported."""
        pass

    def GetGPUUsageRange(self) -> Tuple[int, int]:
        """Gets the GPU usage range as (minValue, maxValue)."""
        pass

    def GetGPUClockSpeedRange(self) -> Tuple[int, int]:
        """Gets the GPU clock speed range as (minValue, maxValue)."""
        pass

    def GetGPUVRAMClockSpeedRange(self) -> Tuple[int, int]:
        """Gets the GPU VRAM clock speed range as (minValue, maxValue)."""
        pass

    def GetGPUTemperatureRange(self) -> Tuple[int, int]:
        """Gets the GPU temperature range as (minValue, maxValue)."""
        pass

    def GetGPUHotspotTemperatureRange(self) -> Tuple[int, int]:
        """Gets the GPU hotspot temperature range as (minValue, maxValue)."""
        pass

    def GetGPUPowerRange(self) -> Tuple[int, int]:
        """Gets the GPU power range as (minValue, maxValue)."""
        pass

    def GetGPUFanSpeedRange(self) -> Tuple[int, int]:
        """Gets the GPU fan speed range as (minValue, maxValue)."""
        pass

    def GetGPUVRAMRange(self) -> Tuple[int, int]:
        """Gets the GPU VRAM range as (minValue, maxValue)."""
        pass

    def GetGPUVoltageRange(self) -> Tuple[int, int]:
        """Gets the GPU voltage range as (minValue, maxValue)."""
        pass

    def GetGPUTotalBoardPowerRange(self) -> Tuple[int, int]:
        """Gets the GPU total board power range as (minValue, maxValue)."""
        pass

    def GetGPUIntakeTemperatureRange(self) -> Tuple[int, int]:
        """Gets the GPU intake temperature range as (minValue, maxValue)."""
        pass

    def GetGPUMemoryTemperatureRange(self) -> Tuple[int, int]:
        """Gets the GPU memory temperature range as (minValue, maxValue)."""
        pass

    def GetNPUFrequencyRange(self) -> Tuple[int, int]:
        """Gets the NPU frequency range as (minValue, maxValue)."""
        pass

    def GetNPUActivityLevelRange(self) -> Tuple[int, int]:
        """Gets the NPU activity level range as (minValue, maxValue)."""
        pass

    def GetGPUSharedMemoryRange(self) -> Tuple[int, int]:
        """Gets the GPU shared memory range as (minValue, maxValue)."""
        pass

    def GetGPUFanDutyRange(self) -> Tuple[int, int]:
        """Gets the GPU fan duty range as (minValue, maxValue)."""
        pass

class IADLXSystemMetricsSupport(IADLXInterface):
    """The IADLXSystemMetricsSupport interface provides methods for checking which system metrics are supported."""

    def IsSupportedCPUUsage(self) -> bool:
        """Checks if CPU usage metric is supported."""
        pass

    def IsSupportedSystemRAM(self) -> bool:
        """Checks if system RAM metric is supported."""
        pass

    def IsSupportedSmartShift(self) -> bool:
        """Checks if SmartShift metric is supported."""
        pass

    def IsSupportedPowerDistribution(self) -> bool:
        """Checks if power distribution metric is supported."""
        pass

    def GetCPUUsageRange(self) -> Tuple[int, int]:
        """Gets the CPU usage range as (minValue, maxValue)."""
        pass

    def GetSystemRAMRange(self) -> Tuple[int, int]:
        """Gets the system RAM range as (minValue, maxValue)."""
        pass

    def GetSmartShiftRange(self) -> Tuple[int, int]:
        """Gets the SmartShift range as (minValue, maxValue)."""
        pass

class IADLXGPUList(IADLXList):
    """The IADLXGPUList interface provides methods for managing a list of GPUs."""

    def Add_Back(self, item: IADLXGPU) -> ADLX_RESULT:
        """Adds a GPU to the end of the list."""
        pass

    def Remove_Back(self) -> ADLX_RESULT:
        """Removes the last GPU from the list."""
        pass

class IADLXApplicationList(IADLXList):
    """The IADLXApplicationList interface provides methods for managing a list of applications."""

    def At(self, location: int) -> IADLXApplication:
        """Returns the application at the requested location.

        :param location: The location of the requested interface.
        :type location: int
        :return: IADLXApplication interface
        :rtype: IADLXApplication
        """
        pass

    def Add_Back(self, item: IADLXApplication) -> ADLX_RESULT:
        """Adds an application to the end of the list.

        :param item: The application to add.
        :type item: IADLXApplication
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

class IADLXGPU2List(IADLXList):
    """The IADLXGPU2List interface provides methods for managing a list of GPU2 interfaces."""

    def At(self, location: int) -> IADLXGPU:
        """Returns the GPU at the requested location.

        :param location: The location of the requested interface.
        :type location: int
        :return: IADLXGPU interface (as IADLXGPU2)
        :rtype: IADLXGPU
        """
        pass

    def Add_Back(self, item: IADLXGPU) -> ADLX_RESULT:
        """Adds a GPU to the end of the list.

        :param item: The GPU to add.
        :type item: IADLXGPU
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

class IADLXGPUAppsListChangedHandling(IADLXInterface):
    """The IADLXGPUAppsListChangedHandling interface allows registering/unregistering for notifications when GPU app lists change."""

    def AddGPUAppsListEventListener(self, pListener: 'PyGPUAppsListEventListenerCallback') -> ADLX_RESULT:
        """Registers an event listener for GPU app list change notifications.

        :param pListener: The event listener callback.
        :type pListener: PyGPUAppsListEventListenerCallback
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

    def RemoveGPUAppsListEventListener(self, pListener: 'PyGPUAppsListEventListenerCallback') -> ADLX_RESULT:
        """Unregisters an event listener from GPU app list change notifications.

        :param pListener: The event listener callback.
        :type pListener: PyGPUAppsListEventListenerCallback
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

class PyGPUAppsListEventListenerCallback:
    """Callback interface for GPU application list change events."""

    call: object
    """Set to a callable that receives (IADLXGPU, IADLXApplicationList) and returns bool."""

class PyGPUStressTestFinishedListenerCallback:
    """Callback interface for GPU stress test finished events."""

    call: object
    """Set to a callable that receives (IADLXGPU, bool) and returns bool."""

class PyLogCallback:
    """Callback interface for ADLX logging."""

    def OnLog(self, message: str) -> None:
        """Called when a log message is generated."""
        pass

class IADLXGPUsChangedHandling(IADLXInterface):
    """The IADLXGPUsChangedHandling interface allows registering and unregistering for notifications when the GPU list changes.

        More info at: https://gpuopen.com/manuals/adlx/adlx-_d_o_x__i_a_d_l_x_g_p_us_changed_handling/#doxid-d-o-x-i-a-d-l-x-g-p-us-changed-handling

        How to get:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        gpus_changed_handling = system.GetGPUsChangedHandling()
        ...
    """

    def __init__(self):
        """**Warning this class should not be instantiated**

        Instead get it as follow:

        ```python
        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        gpus_changed_handling = system.GetGPUsChangedHandling()
        ...
        ```
        """
    def AddGPUsListEventListener(self, pListener: PyGPUsEventListenerCallback) -> ADLX_RESULT:
        """Registers an event listener for notifications when the GPU list changes.

        :param pListener: Event listener interface to register for receiving the GPU list change notifications.
        :type pListener: PyGPUsEventListenerCallback
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

    def RemoveGPUsListEventListener(self, pListener: PyGPUsEventListenerCallback) -> ADLX_RESULT:
        """Unregisters  an event listener for notifications when the GPU list changes.

        :param pListener: Event listener interface to register for receiving the GPU list change notifications.
        :type pListener: PyGPUsEventListenerCallback
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

class IADLXGPUTuningServices(IADLXInterface):
    """The IADLXGPUTuningServices is the main interface for the GPU tuning domain and provides control to GPU tuning specific functionality.

        The IADLXGPUTuningServices interface provides:

        * Information if a tuning functionality, such as automated tuning or preset tuning is available for a GPU.
        * The interfaces for controlling a tuning aspect, such as automated tuning or preset tuning on a GPU.
        * The interface for registering and unregistering for notifications when the GPU tuning settings are changed.
        * Resetting the tuning settings to factory values on a GPU.

        More info at: https://gpuopen.com/manuals/adlx/adlx-_d_o_x__i_a_d_l_x_g_p_u_tuning_services/

        How to get:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        gpu_tuning_services = system.GetGPUTuningServices()
        ...
    """

    def __init__(self):
        """**Warning this class should not be instantiated**

        Instead get it as follow:

        ```python
        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        gpu_tuning_services = system.GetGPUTuningServices()
        ...
        ```
        """
    def GetAutoTuning(self, pGPU: IADLXGPU) -> IADLXGPUAutoTuning:
        """Gets the reference counted automatic tuning interface of a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXGPUAutoTuning interface, None if method fails
        :rtype: IADLXGPUAutoTuning
        """
        pass
    def GetGPUTuningChangedHandling(self, pGPU: IADLXGPU) -> IADLXGPUTuningChangedHandling:
        """Gets the reference counted interface that allows registering and unregistering for notifications when GPU tuning changes.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXGPUTuningChangedHandling interface, None if method fails
        :rtype: IADLXGPUTuningChangedHandling
        """
        pass
    def GetManualFanTuning(self, pGPU: IADLXGPU) -> IADLXManualFanTuning:
        """Gets the reference counted manual fan tuning interface of a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXManualFanTuning interface, None if method fails
        :rtype: IADLXManualFanTuning
        """
        pass
    def GetManualGFXTuning1(self, pGPU: IADLXGPU) -> IADLXManualGraphicsTuning1:
        """Gets the reference counted manual graphics tuning interface of a GPU for pre-RDNA ASIC family.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXManualGraphicsTuning1 interface, None if method fails
        :rtype: IADLXManualGraphicsTuning1
        """
        pass
    def GetManualGFXTuning2(self, pGPU: IADLXGPU) -> IADLXManualGraphicsTuning2:
        """Gets the reference counted manual graphics tuning interface of a GPU for post-RDNA ASIC family.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXManualGraphicsTuning2 interface, None if method fails
        :rtype: IADLXManualGraphicsTuning2
        """
        pass
    def GetManualPowerTuning(self, pGPU: IADLXGPU) -> IADLXManualPowerTuning:
        """Gets the reference counted manual power tuning interface of a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXManualPowerTuning interface, None if method fails
        :rtype: IADLXManualPowerTuning
        """
        pass
    def GetManualVRAMTuning1(self, pGPU: IADLXGPU) -> IADLXManualVRAMTuning1:
        """Gets the reference counted manual VRAM tuning interface of a GPU for pre-RDNA ASIC family.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXManualVRAMTuning1 interface, None if method fails
        :rtype: IADLXManualVRAMTuning1
        """
        pass
    def GetManualVRAMTuning2(self, pGPU: IADLXGPU) -> IADLXManualVRAMTuning2:
        """Gets the reference counted manual VRAM tuning interface of a GPU for post-RDNA ASIC family.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXManualVRAMTuning2 interface, None if method fails
        :rtype: IADLXManualVRAMTuning2
        """
        pass
    def GetPresetTuning(self, pGPU: IADLXGPU) -> IADLXGPUPresetTuning:
        """Gets the reference counted preset tuning interface of a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXGPUPresetTuning interface, None if method fails
        :rtype: IADLXGPUPresetTuning
        """
        pass
    def IsAtFactory(self, pGPU: IADLXGPU) -> bool:
        """Checks if the GPU tuning on a GPU is set to factory settings.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: True if GPU is set to factory settings
        :rtype: bool
        """
        pass
    def IsSupportedAutoTuning(self, pGPU: IADLXGPU) -> bool:
        """Checks if the automatic tuning is supported on a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: True if the automatic tuning is supported on a GPU.
        :rtype: bool
        """
        pass
    def IsSupportedManualFanTuning(self, pGPU: IADLXGPU) -> bool:
        """Checks if the manual fan tuning is supported on a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: True if the manual fan tuning is supported on a GPU.
        :rtype: bool
        """
        pass
    def IsSupportedManualGFXTuning(self, pGPU: IADLXGPU) -> bool:
        """Checks if the manual graphic tuning is supported on a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: True if the manual graphic tuning is supported on a GPU.
        :rtype: bool
        """
        pass
    def IsSupportedManualPowerTuning(self, pGPU: IADLXGPU) -> bool:
        """Checks if the manual power tuning is supported on a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: True if the manual power tuning is supported on a GPU.
        :rtype: bool
        """
        pass
    def IsSupportedManualVRAMTuning(self, pGPU: IADLXGPU) -> bool:
        """Checks if the manual VRAM Tuning is supported on a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: True if the manual VRAM Tuning is supported on a GPU.
        :rtype: bool
        """
        pass
    def IsSupportedPresetTuning(self, pGPU: IADLXGPU) -> bool:
        """Checks if the preset tuning is supported on a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: True if the preset tuning is supported on a GPU.
        :rtype: bool
        """
        pass
    def ResetToFactory(self, pGPU: IADLXGPU) -> ADLX_RESULT:
        """Reset the GPU tuning to factory settings.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass
    def GetSmartAccessMemory(self, pGPU: IADLXGPU) -> 'IADLXSmartAccessMemory':
        """Gets the Smart Access Memory interface for a GPU (QI-fold from IADLXGPUTuningServices1).

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXSmartAccessMemory interface, None if not supported
        :rtype: IADLXSmartAccessMemory
        """
        pass

class IADLXI2C(IADLXInterface):
    """The IADLXI2C interface provides methods to read data from, and write data to OEM devices through the I2C bus.

        More info at: https://gpuopen.com/manuals/adlx/adlx-_d_o_x__i_a_d_l_x_i2_c/

        How to get:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        i2c = system.GetI2C()
        ...
    """

    def __init__(self):
        """**Warning this class should not be instantiated**

        Instead get it as follow:

        ```python
        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        i2c = system.GetI2C()
        ...
        ```
        """
    def IsSupported(self, line: ADLX_I2C_LINE, address: int) -> bool:
        """Checks if the OEM device data can be read and written through the I2C bus on a GPU.

        :param line: The I2C line
        :type line: ADLX_I2C_LINE
        :param address: The 7-bit I2C slave device address which is shifted one bit to the left.
        :type address: int
        :return: True if the OEM device data can be read and written through the I2C bus on a GPU.
        :rtype: bool
        """
        pass
    # fmt:off
    def Read(self, line: ADLX_I2C_LINE, speed: int, address: int, offset: int, dataSize: int) -> Tuple[ADLX_RESULT, List[int]]:
        """Reads the OEM device data through the I2C bus of a GPU.

        :param line: The I2C line.
        :type line: ADLX_I2C_LINE
        :param speed: The I2C clock speed (in KHz).
        :type speed: int
        :param address: The 7-bit I2C slave device address which is shifted one bit to the left.
        :type address: int
        :param offset: The offset of the data from the address.
        :type offset: int
        :param dataSize: The size (in bytes) of the buffer for the OEM device data.
        :type dataSize: int
        :return: the buffer with the OEM data.
        :rtype: Tuple[ADLX_RESULT, List[int]]
        """
        pass
    def RepeatedStartRead(self, line: ADLX_I2C_LINE, speed: int, address: int, offset: int, dataSize: int) -> Tuple[ADLX_RESULT, List[int]]:
        """Repeat start reads the OEM device data through the I2C bus of a GPU.

        :param line: The I2C line.
        :type line: ADLX_I2C_LINE
        :param speed: The I2C clock speed (in KHz).
        :type speed: int
        :param address: The 7-bit I2C slave device address which is shifted one bit to the left.
        :type address: int
        :param offset: The offset of the data from the address.
        :type offset: int
        :param dataSize: The size (in bytes) of the buffer for the OEM device data.
        :type dataSize: int
        :return: the buffer with the OEM data.
        :rtype: Tuple[ADLX_RESULT, List[int]]
        """
        pass
    def Version(self) -> str:
        """Retrieves the major and minor software version of I2C interface on a GPU.

        :return: "Major.minor"
        :rtype: str
        """
        pass
    def Write(self, line: ADLX_I2C_LINE, speed: int, address: int, offset: int, dataSize: int, data: List[int]) -> ADLX_RESULT:
        """Writes the OEM device data through the I2C bus of a GPU.

        :param line: The I2C line.
        :type line: ADLX_I2C_LINE
        :param speed: The I2C clock speed (in KHz).
        :type speed: int
        :param address: The 7-bit I2C slave device address which is shifted one bit to the left.
        :type address: int
        :param offset: The offset of the data from the address.
        :type offset: int
        :param dataSize: The size (in bytes) of the buffer for the OEM device data.
        :type dataSize: int
        :param data:  The buffer with the new OEM data.
        :type data: List[int]
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass
    # fmt:on

class IADLXPerformanceMonitoringServices(IADLXInterface):
    """The IADLXPerformanceMonitoringServices interface provides methods to configure the performance monitoring functionality 
        and to obtain the performance data.

        The IADLXPerformanceMonitoringServices interface provides:

        * The configuration for the performance metric sampling.
        * The methods to start and stop the performance metric sampling.
        * Access to the data from the performance metric buffer.

        More info at: https://gpuopen.com/manuals/adlx/adlx-_d_o_x__i_a_d_l_x_performance_monitoring_services/#doxid-d-o-x-i-a-d-l-x-performance-monitoring-services

        How to get:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        perf_mon_services = system.GetPerformanceMonitoringServices()
        ...
    """

    def __init__(self):
        """**Warning this class should not be instantiated**

        Instead get it as follow:

        ```python
        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        perf_mon_services = system.GetPerformanceMonitoringServices()
        ...
        ```
        """
    def ClearPerformanceMetricsHistory(self) -> ADLX_RESULT:
        """Clears the buffer for performance monitoring.

        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

    def GetAllMetricsHistory(self, startMs: int, stopMs: int) -> List[IADLXAllMetrics]:
        """Gets the reference counted list of all the metrics in a time interval.

        :param startMs: The start time of the time interval (in millisecond).
        :type startMs: int
        :param stopMs: The stop time of the time interval (in millisecond).
        :type stopMs: int
        :return: Python list of IADLXAllMetrics
        :rtype: List[IADLXAllMetrics]
        """
        pass

    def GetAllMetricsHistoryRaw(self, startMs: int, stopMs: int) -> IADLXAllMetricsList:
        """Gets the reference counted list of all the metrics in a time interval.

        .. note::
            This returns a CPPlike Object, if you want a python list consider using **GetAllMetricsHistory()**

        :param startMs: The start time of the time interval (in millisecond).
        :type startMs: int
        :param stopMs: The stop time of the time interval (in millisecond).
        :type stopMs: int
        :return: IADLXAllMetricsList interface, None if method fails
        :rtype: IADLXAllMetricsList
        """
        pass

    def GetCurrentAllMetrics(self) -> IADLXAllMetrics:
        """Gets the reference counted IADLXAllMetrics interface for the current metric set.

        :return: IADLXAllMetrics interface, None if method fails
        :rtype: IADLXAllMetrics
        """
        pass

    def GetCurrentFPS(self) -> IADLXFPS:
        """Gets the reference counted IADLXFPS interface for the current FPS metric.

        :return: IADLXFPS interface, None if method fails
        :rtype: IADLXFPS
        """
        pass

    def GetCurrentGPUMetrics(self, pGPU: IADLXGPU) -> IADLXGPUMetrics:
        """Gets the reference counted IADLXGPUMetrics interface for the current metric set of a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXGPUMetrics interface, None if method fails
        :rtype: IADLXGPUMetrics
        """
        pass

    def GetCurrentPerformanceMetricsHistorySize(self) -> int:
        """Gets the duration of the metrics history from the performance monitoring buffer.

        :return: Duration (in seconds)
        :rtype: int
        """
        pass

    def GetCurrentSystemMetrics(self) -> IADLXSystemMetrics:
        """Gets the reference counted IADLXSystemMetrics interface for the current metric set.

        :return: IADLXGPUMetrics interface, None if method fails
        :rtype: IADLXSystemMetrics
        """
        pass

    def GetFPSHistory(self, startMs: int, stopMs: int) -> List[IADLXFPS]:
        """Gets the reference counted list of FPS metrics in a time interval.

        :param startMs: The start time of the time interval (in millisecond).
        :type startMs: int
        :param stopMs: The stop time of the time interval (in millisecond).
        :type stopMs: int
        :return: Python list of IADLXFPS
        :rtype: List[IADLXFPS]
        """
        pass

    def GetFPSHistoryRaw(self, startMs: int, stopMs: int) -> IADLXFPSList:
        """Gets the reference counted list of FPS metrics in a time interval.

        .. note::
            This returns a CPPlike Object, if you want a python list consider using **GetFPSHistory()**

        :param startMs: The start time of the time interval (in millisecond).
        :type startMs: int
        :param stopMs: The stop time of the time interval (in millisecond).
        :type stopMs: int
        :return: IADLXAllMetricsList interface, None if method fails
        :rtype: IADLXFPSList
        """
        pass

    def GetGPUMetricsHistory(self, pGPU: IADLXGPU, startMs: int, stopMs: int) -> List[IADLXGPUMetrics]:
        """Gets the reference counted list of GPU metrics in a time interval of a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :param startMs: The start time of the time interval (in millisecond).
        :type startMs: int
        :param stopMs: The stop time of the time interval (in millisecond).
        :type stopMs: int
        :return: Python list of IADLXGPUMetrics
        :rtype: List[IADLXGPUMetrics]
        """
        pass

    def GetGPUMetricsHistoryRaw(self, pGPU: IADLXGPU, startMs: int, stopMs: int) -> IADLXGPUMetricsList:
        """Gets the reference counted list of GPU metrics in a time interval of a GPU.

        .. note::
            This returns a CPPlike Object, if you want a python list consider using **GetGPUMetricsHistory()**

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :param startMs: The start time of the time interval (in millisecond).
        :type startMs: int
        :param stopMs: The stop time of the time interval (in millisecond).
        :type stopMs: int
        :return: IADLXGPUMetricsList interface, None if method fails
        :rtype: IADLXGPUMetricsList
        """
        pass

    def GetMaxPerformanceMetricsHistorySize(self) -> int:
        """Gets the duration of the performance monitoring buffer.

        :return: The buffer duration (in second)
        :rtype: int
        """
        pass

    def GetMaxPerformanceMetricsHistorySizeRange(self) -> ADLX_IntRange:
        """Gets the maximum size, minimum size, and step size for the performance monitoring buffer.

        :return: ADLX_IntRange interface, None if method fails
        :rtype: ADLX_IntRange (in second)
        """
        pass

    def GetSamplingInterval(self) -> int:
        """Gets the sampling interval for performance monitoring.

        :return: The sampling interval (in millisecond)
        :rtype: int
        """
        pass

    def GetSamplingIntervalRange(self) -> ADLX_IntRange:
        """Gets the maximum sampling interval, minimum sampling interval, and step sampling interval for the performance monitoring.

        :return: ADLX_IntRange (in millisecond), None if method fails
        :rtype: ADLX_IntRange
        """
        pass

    def GetSupportedGPUMetrics(self, pGPU: IADLXGPU) -> IADLXGPUMetricsSupport:
        """Gets the reference counted interface for discovering what performance metrics are supported on a GPU.

        :param pGPU: The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXGPUMetricsSupport interface, None if method fails
        :rtype: IADLXGPUMetricsSupport
        """
        pass

    def GetSupportedSystemMetrics(self) -> IADLXSystemMetricsSupport:
        """Gets the reference counted interface for discovering what performance metrics are supported on the system.

        :return: IADLXSystemMetricsSupport interface, None if method fails
        :rtype: IADLXSystemMetricsSupport
        """
        pass

    def GetSystemMetricsHistory(self, startMs: int, stopMs: int) -> List[IADLXSystemMetrics]:
        """Gets the reference counted list of system metrics in a time interval.

        :param startMs: The start time of the time interval (in millisecond).
        :type startMs: int
        :param stopMs: The stop time of the time interval (in millisecond).
        :type stopMs: int
        :return: Python list of IADLXSystemMetrics
        :rtype: List[IADLXSystemMetrics]
        """
        pass

    def GetSystemMetricsHistoryRaw(self, startMs: int, stopMs: int) -> IADLXSystemMetricsList:
        """Gets the reference counted list of system metrics in a time interval.

        .. note::
            This returns a CPPlike Object, if you want a python list consider using **GetSystemMetricsHistory()**

        :param startMs: The start time of the time interval (in millisecond).
        :type startMs: int
        :param stopMs: The stop time of the time interval (in millisecond).
        :type stopMs: int
        :return: IADLXGPUMetricsList interface, None if method fails
        :rtype: IADLXSystemMetricsList
        """
        pass

    def SetMaxPerformanceMetricsHistorySize(self, sizeSec : int) -> ADLX_RESULT:
        """Sets the duration of the performance monitoring buffer.

        :param sizeSec: The buffer duration (in second).
        :type sizeSec: int
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

    def SetSamplingInterval(self, intervalMs : int) -> ADLX_RESULT:
        """Sets the sampling interval for the performance monitoring.

        :param intervalMs: The sampling interval (in millisecond).
        :type intervalMs: int
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

    def StartPerformanceMetricsTracking(self) -> ADLX_RESULT:
        """Increases the count for the performance metrics tracking.

        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

    def StopPerformanceMetricsTracking(self) -> ADLX_RESULT:
        """Decreases the count for the performance metrics tracking.

        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass

class IADLXSystem:
    """The IADLXSystem is the main interface to ADLX and provides platform-specific functionality.

        More info at: https://gpuopen.com/manuals/adlx/adlx-_d_o_x__i_a_d_l_x_system/#iadlxsystem

        How to get:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        ...
    """

    def __init__(self):
        """**Warning this class should not be instantiated**

        Instead get it as follow:

        ```python
        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret != ADLX.ADLX_RESULT.ADLX_OK:
            sys.exit(1)
        system = adlx_helper.GetSystemServices()
        ...
        ```
        """
        pass
    def EnableLog(
        self, mode: ADLX_LOG_DESTINATION, severity: ADLX_LOG_SEVERITY, pLogger: PyLogCallback, fileName: str
    ) -> ADLX_RESULT:
        """Enables logging in ADLX.

        :param mode: The log destination.
        :type mode: ADLX_LOG_DESTINATION
        :param severity: The logging severity.
        :type severity: ADLX_LOG_SEVERITY
        :param pLogger:  The pointer to the log interface to receive log messages from ADLX can be None
        :type pLogger: PyLogCallback
        :param fileName: Specifies the path of the log file.
        :type fileName: str
        :return: ADLX_RESULT
        :rtype: ADLX_RESULT
        """
        pass
    def Get3DSettingsServices(self) -> IADLX3DSettingsServices:
        """Gets the reference counted main interface to the 3D Graphics domain.

        :return: IADLX3DSettingsServices interface, None if method fails
        :rtype: IADLX3DSettingsServices
        """
        pass
    def GetDesktopsServices(self) -> IADLXDesktopServices:
        """Gets the reference counted main interface to the Desktop domain.

        :return: IADLXDesktopServices interface, None if method fails
        :rtype: IADLXDesktopServices
        """
        pass
    def GetDisplaysServices(self) -> IADLXDisplayServices:
        """Gets the reference counted main interface to the Display domain.

        :return: IADLXDisplayServices interface, None if method fails
        :rtype: IADLXDisplayServices
        """
        pass
    def GetGPUs(self) -> List[IADLXGPU]:
        """Gets a python list of AMD GPUs.

        :return: Python list of IADLXGPU interfaces
        :rtype: List[IADLXGPU]
        """
        pass
    def GetGPUsChangedHandling(self) -> IADLXGPUsChangedHandling:
        """Gets the reference counted interface to allow registering and unregistering for notifications when the GPU list changes.

        :return: IADLXGPUsChangedHandling interface, None if method fails
        :rtype: IADLXGPUsChangedHandling
        """
        pass
    def GetGPUsRaw(self) -> IADLXGPUList:
        """Gets the reference counted list of AMD GPUs

        .. note::
            This returns a CPPlike Object, if you want a python list consider using **GetGPUs()**

        :return: IADLXGPUList interface, None if method fails
        :rtype: IADLXGPUList
        """
        pass
    def GetGPUTuningServices(self) -> IADLXGPUTuningServices:
        """Gets the reference counted main interface to the GPU Tuning domain.

        :return: IADLXGPUTuningServices interface, None if method fails
        :rtype: IADLXGPUTuningServices
        """
        pass
    def GetI2C(self, pGPU: IADLXGPU) -> IADLXI2C:
        """Gets the reference counted I2C interface of a GPU.

        :param pGPU:  The pointer to the GPU interface.
        :type pGPU: IADLXGPU
        :return: IADLXI2C
        :rtype: IADLXI2C
        """
        pass
    def GetPerformanceMonitoringServices(self) -> IADLXPerformanceMonitoringServices:
        """Gets the reference counted main interface to the Performance Monitoring domain.

        :return: IADLXPerformanceMonitoringServices interface, None if method fails
        :rtype: IADLXPerformanceMonitoringServices
        """
        pass
    def HybridGraphicsType(self) -> ADLX_HG_TYPE:
        """Gets the hybrid graphics type of the system.

        :return: ADLX_HG_TYPE
        :rtype: ADLX_HG_TYPE
        """
        pass
    def QueryInterface(self, interfaceId):
        """Gets reference counted extension interfaces to IADLXSystem .

        :param interfaceId: The identifier of the interface being requested.
        :type interfaceId: str
        """
        pass
    def TotalSystemRAM(self) -> int:
        """Gets the size of the total RAM on this system.

        :return:  The total system RAM size is returned, in MB
        :rtype: int
        """
        pass
    def GetPowerTuningServices(self) -> 'IADLXPowerTuningServices':
        """Gets the reference counted main interface to the Power Tuning domain (via IADLXSystem1).

        :return: IADLXPowerTuningServices interface, None if not supported
        :rtype: IADLXPowerTuningServices
        """
        pass
    def GetMultimediaServices(self) -> 'IADLXMultimediaServices':
        """Gets the reference counted main interface to the Multimedia domain (via IADLXSystem2).

        :return: IADLXMultimediaServices interface, None if not supported
        :rtype: IADLXMultimediaServices
        """
        pass
    def GetVariableGraphicsMemory(self) -> 'IADLXVariableGraphicsMemory':
        """Gets the reference counted interface to Variable Graphics Memory (via IADLXSystem3).

        :return: IADLXVariableGraphicsMemory interface, None if not supported
        :rtype: IADLXVariableGraphicsMemory
        """
        pass
    def GetGPUAppsListChangedHandling(self) -> 'IADLXGPUAppsListChangedHandling':
        """Gets the reference counted interface for registering/unregistering GPU app list change notifications (via IADLXSystem2).

        :return: IADLXGPUAppsListChangedHandling interface, None if not supported
        :rtype: IADLXGPUAppsListChangedHandling
        """
        pass

class PyADLIdsFromADLX:
    """Data class representing ADL IDs from ADLX."""

    VidPnSourceId: int
    adapterIndex: int
    bus: int
    device: int
    function: int

class PyBdfFromADLXGPU:
    """Data class representing BDF (Bus, Device, Function) from ADLX GPU."""

    bus: int
    device: int
    function: int

class ADLXHelper:
    """ADLXHelper class are methods to initialize ADLX in Python programs.

    More info at: https://gpuopen.com/manuals/adlx/adlx-page__a_d_l_x_cpp_help/#adlxhelper-class

    Example:

    .. code-block:: python

        import sys
        from adlx import ADLX
        adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
        ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
        if ret == ADLX.ADLX_RESULT.ADLX_OK:
            adlx_version: str = adlx_helper.QueryVersion()
            print(f"ADLX Version: {adlx_version}")
            adlx_helper.Terminate()

    """
    def GetAdlMapping(self) -> IADLMapping:
        """Gets the ADL Mapping interface.
        Remarks
        GetAdlMapping is used to convert data between ADL and ADLX in applications where ADLX was initialized with Initialize.

        :return: If ADLX was successfully initialized with ADL, a valid pointer of the IADLMapping interface is returned.
                If ADLX was initialized under any of the following circumstances, nullptr is returned.
                ADLX initialization was with other initialization methods.
                ADLX initialization was failed.
                ADLX initialization was not called.
        :rtype: IADLMapping
        """
        pass
    def GetSystemServices(self) -> IADLXSystem:
        """Gets the ADLX system interface.

        :return: If ADLX was successfully initialized before this method call, the IADLXSystem interface is returned.
                If ADLX was not successfully initialized, nullptr is returned.
        :rtype: IADLXSystem
        """
        pass
    def Initialize(self) -> ADLX_RESULT:
        """Initializes ADLX with default parameters.

        :return: If Initialize is successfully executed, ADLX_OK is returned.
                If Initialize is not successfully executed, an error code is returned.
                If ADLX was previously successfully initialized with any of the initialization functions, ADLX_ALREADY_INITIALIZED is returned.
        :rtype: ADLX_RESULT
        """
        pass
    
    def InitializeWithIncompatibleDriver(self) -> ADLX_RESULT:
        """Initializes ADLX with a legacy driver.
            This method is used when an application does not use the ADL library and initializes ADLX to consider AMD GPUs using legacy AMD graphics driver.

        :return: If InitializeWithIncompatibleDriver is successfully executed, ADLX_OK is returned.
                If InitializeWithIncompatibleDriver is not successfully executed, an error code is returned.
                If ADLX was previously successfully initialized with any of the Initialize versions, ADLX_ALREADY_INITIALIZED is returned.
        :rtype: ADLX_RESULT
        """
        pass
    def QueryFullVersion(self) -> int:
        """Gets the full version of ADLX.

        :return: The full version of ADLX.
        :rtype: int
        """
        pass
    def QueryVersion(self) -> str:
        """Gets the version of ADLX.

        :return: The version of ADLX.
        :rtype: str
        """
        pass
    def Terminate(self) -> ADLX_RESULT:
        """Terminates ADLX and releases ADLX library.
            Any interface obtained from ADLX that is not released becomes invalid.
            Any attempt of calling ADLX interface after termination could result in errors such as exceptions or crashes.

        :return: If Terminate is successfully executed, ADLX_OK is returned.
                If Terminate is not successfully executed, an error code is returned.
        :rtype: ADLX_RESULT
        """
        pass
    def __init__(self):
        """The constructor of the ADLXHelper class.

        More info at: https://gpuopen.com/manuals/adlx/adlx-page__a_d_l_x_cpp_help/#adlxhelper-class

        Example:

        .. code-block:: python

            import sys
            from adlx import ADLX
            adlx_helper: ADLX.ADLXHelper = ADLX.ADLXHelper()
            ret: ADLX.ADLX_RESULT = adlx_helper.Initialize()
            if ret == ADLX.ADLX_RESULT.ADLX_OK:
                adlx_version: str = adlx_helper.QueryVersion()
                print(f"ADLX Version: {adlx_version}")
                adlx_helper.Terminate()

        """
        pass


class IADLXSmartShiftMax(IADLXInterface):
    """Interface for AMD SmartShift Max."""
    def IsSupported(self) -> Optional[bool]:
        """Checks if SmartShift Max is supported."""
        pass
    def GetBiasMode(self) -> Optional[ADLX_SSM_BIAS_MODE]:
        """Gets the current bias mode."""
        pass
    def SetBiasMode(self, mode: ADLX_SSM_BIAS_MODE) -> ADLX_RESULT:
        """Sets the bias mode."""
        pass
    def GetBiasRange(self) -> dict:
        """Gets the bias range. Returns dict with 'return', 'min_value', 'max_value', 'step'."""
        pass
    def GetBias(self) -> Optional[int]:
        """Gets the current bias value."""
        pass
    def SetBias(self, bias: int) -> ADLX_RESULT:
        """Sets the bias value."""
        pass

class IADLXSmartShiftEco(IADLXInterface):
    """Interface for AMD SmartShift Eco."""
    def IsSupported(self) -> Optional[bool]:
        """Checks if SmartShift Eco is supported."""
        pass
    def IsEnabled(self) -> Optional[bool]:
        """Checks if SmartShift Eco is enabled."""
        pass
    def SetEnabled(self, enabled: bool) -> ADLX_RESULT:
        """Enables or disables SmartShift Eco."""
        pass
    def IsInactive(self) -> Optional[bool]:
        """Checks if SmartShift Eco is inactive."""
        pass
    def GetInactiveReason(self) -> Optional[ADLX_SMARTSHIFT_ECO_INACTIVE_REASON]:
        """Gets the reason SmartShift Eco is inactive."""
        pass

class IADLXPowerTuningChangedEvent(IADLXChangedEvent):
    """Interface for power tuning changed events."""
    def IsSmartShiftMaxChanged(self) -> bool:
        """Checks if SmartShift Max settings changed."""
        pass
    def IsSmartShiftEcoChanged(self) -> bool:
        """Checks if SmartShift Eco settings changed (QI-fold from Event1)."""
        pass

class PyPowerTuningChangedListenerCallback:
    """Callback wrapper for power tuning changed events."""
    call: Any
    def __init__(self): ...

class IADLXPowerTuningChangedHandling(IADLXInterface):
    """Interface for managing power tuning event listeners."""
    def AddPowerTuningEventListener(self, pListener: PyPowerTuningChangedListenerCallback) -> ADLX_RESULT:
        """Registers an event listener for power tuning changes."""
        pass
    def RemovePowerTuningEventListener(self, pListener: PyPowerTuningChangedListenerCallback) -> ADLX_RESULT:
        """Unregisters an event listener for power tuning changes."""
        pass

class IADLXPowerTuningServices(IADLXInterface):
    """Interface for power tuning services."""
    def GetPowerTuningChangedHandling(self) -> IADLXPowerTuningChangedHandling:
        """Gets the changed handling interface."""
        pass
    def GetSmartShiftMax(self) -> IADLXSmartShiftMax:
        """Gets the SmartShift Max interface."""
        pass
    def GetSmartShiftEco(self) -> IADLXSmartShiftEco:
        """Gets the SmartShift Eco interface (QI-fold from Services1)."""
        pass
    def IsGPUConnectSupported(self) -> Optional[bool]:
        """Checks if GPU Connect is supported (QI-fold from Services1)."""
        pass
    def GetGPUConnectGPUs(self) -> Any:
        """Gets the list of GPU Connect GPUs (QI-fold from Services1)."""
        pass

class IADLXGPUConnectChangedEvent(IADLXChangedEvent):
    """Interface for GPU Connect changed events."""
    def GetGPU(self) -> IADLXGPU:
        """Gets the GPU associated with the event."""
        pass
    def IsGPUAppsListChanged(self) -> bool:
        """Checks if GPU apps list changed."""
        pass
    def IsGPUPowerChanged(self) -> bool:
        """Checks if GPU power changed."""
        pass
    def IsGPUPowerChangeError(self) -> tuple[bool, ADLX_RESULT]:
        """Checks if there was a GPU power change error. Returns (hasError, errorResult)."""
        pass

class PyGPUConnectChangedListenerCallback:
    """Callback wrapper for GPU Connect changed events."""
    call: Any
    def __init__(self): ...

class IADLXVideoUpscale(IADLXInterface):
    """Interface for Video Upscale settings."""
    def IsSupported(self) -> Optional[bool]:
        """Checks if Video Upscale is supported."""
        pass
    def IsEnabled(self) -> Optional[bool]:
        """Checks if Video Upscale is enabled."""
        pass
    def GetSharpnessRange(self) -> dict:
        """Gets the sharpness range. Returns dict with 'return', 'min_value', 'max_value', 'step'."""
        pass
    def GetSharpness(self) -> Optional[int]:
        """Gets the current sharpness value."""
        pass
    def SetEnabled(self, enabled: bool) -> ADLX_RESULT:
        """Enables or disables Video Upscale."""
        pass
    def SetSharpness(self, sharpness: int) -> ADLX_RESULT:
        """Sets the Video Upscale sharpness value."""
        pass

class IADLXVideoSuperResolution(IADLXInterface):
    """Interface for Video Super Resolution settings."""
    def IsSupported(self) -> Optional[bool]:
        """Checks if Video Super Resolution is supported."""
        pass
    def IsEnabled(self) -> Optional[bool]:
        """Checks if Video Super Resolution is enabled."""
        pass
    def SetEnabled(self, enabled: bool) -> ADLX_RESULT:
        """Enables or disables Video Super Resolution."""
        pass

class IADLXMultimediaChangedEvent(IADLXInterface):
    """Interface for multimedia changed events."""
    def GetGPU(self) -> IADLXGPU:
        """Gets the GPU associated with the event."""
        pass
    def IsVideoUpscaleChanged(self) -> bool:
        """Checks if Video Upscale settings changed."""
        pass
    def IsVideoSuperResolutionChanged(self) -> bool:
        """Checks if Video Super Resolution settings changed."""
        pass

class PyMultimediaChangedListenerCallback:
    """Callback wrapper for multimedia changed events."""
    call: Any
    def __init__(self): ...

class IADLXMultimediaChangedHandling(IADLXInterface):
    """Interface for managing multimedia event listeners."""
    def AddMultimediaEventListener(self, pListener: PyMultimediaChangedListenerCallback) -> ADLX_RESULT:
        """Registers an event listener for multimedia changes."""
        pass
    def RemoveMultimediaEventListener(self, pListener: PyMultimediaChangedListenerCallback) -> ADLX_RESULT:
        """Unregisters an event listener for multimedia changes."""
        pass

class IADLXMultimediaServices(IADLXInterface):
    """Interface for multimedia services."""
    def GetMultimediaChangedHandling(self) -> IADLXMultimediaChangedHandling:
        """Gets the changed handling interface."""
        pass
    def GetVideoUpscale(self, gpu: IADLXGPU) -> IADLXVideoUpscale:
        """Gets the Video Upscale interface for a GPU."""
        pass
    def GetVideoSuperResolution(self, gpu: IADLXGPU) -> IADLXVideoSuperResolution:
        """Gets the Video Super Resolution interface for a GPU."""
        pass

class IADLXSmartAccessMemory(IADLXInterface):
    """Interface for Smart Access Memory settings."""
    def IsSupported(self) -> Optional[bool]:
        """Checks if Smart Access Memory is supported."""
        pass
    def IsEnabled(self) -> Optional[bool]:
        """Checks if Smart Access Memory is enabled."""
        pass
    def SetEnabled(self, enabled: bool) -> ADLX_RESULT:
        """Enables or disables Smart Access Memory."""
        pass

class IADLXVariableGraphicsMemoryOption(IADLXInterface):
    """Interface for a Variable Graphics Memory option."""
    def Name(self) -> Optional[str]:
        """Gets the name of the option."""
        pass
    def Mode(self) -> Optional[ADLX_VARIABLE_GRAPHICS_MEMORY_MODE]:
        """Gets the mode of the option."""
        pass
    def MemoryCarved(self) -> Optional[float]:
        """Gets the system RAM dedicated to graphics memory (in GB)."""
        pass
    def MemoryRemaining(self) -> Optional[float]:
        """Gets the remaining system RAM (in GB)."""
        pass

class IADLXVariableGraphicsMemoryOptionList(IADLXList):
    """List of Variable Graphics Memory options."""
    def At(self, location: int) -> IADLXVariableGraphicsMemoryOption:
        """Gets the option at the specified location."""
        pass
    def Add_Back(self, pItem: IADLXVariableGraphicsMemoryOption) -> ADLX_RESULT:
        """Adds an option to the back of the list."""
        pass

class IADLXVariableGraphicsMemory(IADLXInterface):
    """Interface for Variable Graphics Memory settings."""
    def IsSupported(self) -> Optional[bool]:
        """Checks if Variable Graphics Memory is supported."""
        pass
    def GetDefaultOption(self) -> IADLXVariableGraphicsMemoryOption:
        """Gets the default option."""
        pass
    def GetOption(self) -> IADLXVariableGraphicsMemoryOption:
        """Gets the current option."""
        pass
    def GetAvailableOptions(self) -> IADLXVariableGraphicsMemoryOptionList:
        """Gets the list of available options."""
        pass
    def SetOption(self, opt: IADLXVariableGraphicsMemoryOption) -> ADLX_RESULT:
        """Sets the option."""
        pass
