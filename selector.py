#

"""
@author:"˶𝞢⤬⫒ⵖsᐼ˶"
@title: "Selector"
@nickname: "Selector"
@version: "4.0.0"
@project: "https://github.com/exdysa/comfyui-selector",
@description: "EXDYSA. Selector and Recourse. Presets & failsafes. Work flow."
"""

import comfy.samplers
import comfy.sd
import comfy.utils
import comfy.model_base
import comfy.model_management
import comfy.model_sampling

MODEL_TO_TYPE = {
    "SD3": 6,
    "HunyuanDiT": 5,
    "AuraFlow": 4,
    "Flux": 3,
    "SDXL": 2,
    "SDXL_instructpix2pix": 2,
    "SDXLRefiner": 2,
    "BaseModel": 1,
}
TYPE_DESC = "SD1, SDXL, FLUX, AURAFLOW, HUNYUANDIT, SD3, STABLE_CASCADE_C, STABLE_CASCADE_B"
RECOURSE_CHECK_DESC = f"Ensure connection of first active input by type, then signal type as integer based on MODEL. {MODEL_TO_TYPE}"
SELECTOR_CATEGORY_PATH = "Selector_Recourse"

MODEL_1 = "This port requires MODEL to send the MODEL_TYPE to other nodes."
MODEL_2 = "This port is activated in case MODEL_1 has no signal."
RECOURSE_PORT = "The lowest number port with an active signal is used."
STRING_PORT = "A single string to send"
LINK_PORT = "All strings are joined together and sent as one"


SD_RES = 8
XL_RES = 9
MAX_RES = 24
SD_SAMPLERS = {}
XL_SAMPLERS = {}
FLUX_SAMPLERS = {}
AURAFLOW_SAMPLERS = {}
HUNYUANDIT_SAMPLERS = {}
SD3_SAMPLERS = {}


class Selectah:
    """Choose settings for multiple nodes in a single place"""

    def __init__(self):
        pass

    # dimensions sourced from: https://arxiv.org/abs/2307.01952
    # https://github.com/Stability-AI/generative-models
    # https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-7B-Text2World
    # https://huggingface.co/THUDM/CogVideoX-5b
    #
    RATIO = [
        ("1:1___1024x1024", 1024, 1024),
        ("16:15_1024x960", 1024, 960),
        ("17:15_1088x960", 1088, 960),
        ("17:14_1088x896", 1088, 896),
        ("18:13_1152x832", 1152, 832),
        ("4:3___1152x896", 1152, 896),
        ("3:2___1216x832", 1216, 832),
        # ("72:32_1232x832", 1232, 832),
        ("5:3___1280x768", 1280, 768),
        ("21:11_1344x704", 1344, 704),
        ("7:4___1344x768", 1344, 768),
        ("2:1___1408x704", 1408, 704),
        ("23:11_1472x704", 1472, 704),
        ("21:9__1536x640", 1536, 640),
        ("2:1___1536x768", 1536, 768),
        ("5:2___1600x640", 1600, 640),
        ("26:9__1664x576", 1664, 576),
        ("3:1___1728x576", 1728, 576),
        ("28:9__1792x576", 1792, 576),
        ("29:8__1856x512", 1856, 512),
        ("15:4__1920x512", 1920, 512),
        ("31:8__1984x512", 1984, 512),
        ("4:1___2048x512", 2048, 512),
        ("1:1___V_256x256", 256, 256),
        ("4:3___V_320x240", 320, 240),
        ("32:27_V_576x486", 576, 486),
        ("22:15_V_704x480", 704, 480),
        ("9:5___V_720x400", 720, 400),
        ("3:2___V_720x480", 720, 480),
        ("5:4___V_720x576", 720, 576),
        ("3:2___V_768x512", 768, 512),
        ("4:3___V_832x624", 832, 624),
        ("53:30_V_848x480", 848, 480),
        ("4:3___V 960x704", 960, 704),
        ("1:1___V_960x960", 960, 960),
        ("20:11_V_1280x704", 1280, 704),
        ("16:9__V_1024X576", 1024, 576),
        ("1:1__SV3D_576x576", 576, 576),
        ("1:1____SD_512x512", 512, 512),
        ("4:3____SD_682x512", 682, 512),
        ("3:2____SD_768x512", 768, 512),
        ("1:1____SD_768x768", 768, 768),
        ("16:9___SD_910x512", 910, 512),
        ("1:85:1_SD_952x512", 952, 512),
        ("2:1____SD_1024x512", 1024, 512),
    ]

    @classmethod
    def INPUT_TYPES(cls):
        """User inputs"""
        aspect_ratio_titles = [title for title, res1, res2 in cls.RATIO]
        rotation = ("landscape", "portrait")

        return {
            "required": {
                "aspect_ratio": (
                    aspect_ratio_titles,
                    {
                        "default": ("1:1___1024x1024"),
                    },
                ),
                "rotation": (rotation,),
            },
            "optional": {
                "batch": (
                    "INT",
                    {
                        "default": 1,
                        "min": -10000,
                        "max": 10000,
                    },
                ),
                "steps": (
                    "INT",
                    {
                        "default": 20,
                        "min": -10000,
                        "max": 10000,
                    },
                ),
                "refiner_steps": (
                    "INT",
                    {
                        "default": 0,
                        "min": -10000,
                        "max": 10000,
                    },
                ),
                "cfg": (
                    "FLOAT",
                    {
                        "default": 1.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "refiner_cfg": (
                    "FLOAT",
                    {
                        "default": 1.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "str_denoise": (
                    "FLOAT",
                    {
                        "default": 1.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "scale": (
                    "FLOAT",
                    {
                        "default": 2.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "variation_str": (
                    "FLOAT",
                    {
                        "default": 0.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS,),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS,),
            },
        }

    RETURN_TYPES = (
        "INT",
        "INT",
        "INT",
        "INT",
        "INT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        comfy.samplers.KSampler.SAMPLERS,
        comfy.samplers.KSampler.SCHEDULERS,
    )

    RETURN_NAMES = (
        "WIDTH",
        "HEIGHT",
        "BATCH_SIZE",
        "STEPS",
        "REFINER_STEPS",
        "CFG",
        "REFINER_CFG",
        "DENOISE",
        "VARIATION_STR",
        "SCALE",
        "SAMPLER_NAME",
        "SCHEDULER",
    )
    FUNCTION = "selectah"
    CATEGORY = SELECTOR_CATEGORY_PATH

    def selectah(
        self,
        aspect_ratio,
        rotation,
        batch=None,
        steps=None,
        refiner_steps=None,
        cfg=None,
        refiner_cfg=None,
        str_denoise=None,
        scale=None,
        variation_str=None,
        sampler_name=None,
        scheduler=None,
    ):
        """
        Choose universal settings for multiple repeat settings workflows\n
        :param aR: Desired aspect ratio of image
        :type aR: tuple
        :param rotation: Orientation of the desired image
        :type rotation: str
        :param args: The remaining arguments of the node
        :type args: tuple
        :return: A tuple of the settings, or None for width/height if aspect ratio is not found
        """
        for title, width, height in self.RATIO:
            if title == aspect_ratio:
                if rotation == "portrait":
                    width, height = height, width  # Swap for portrait orientation
                return (width, height, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale, variation_str, sampler_name, scheduler)

        # If aspect ratio is not found, return None for width and height
        return (None, None, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale, variation_str, sampler_name, scheduler)


class SelectahAdv:
    """Choose settings for advanced nodes in a single place"""

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """User inputs"""
        return {
            "required": {},
            "optional": {
                "clip_skip": (
                    "INT",
                    {
                        "default": -2,
                        "min": -10000,
                        "max": -1,
                    },
                ),
                "str_1": (
                    "FLOAT",
                    {
                        "default": 1.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "str_2": (
                    "FLOAT",
                    {
                        "default": 1.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "str_3": (
                    "FLOAT",
                    {
                        "default": 1.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "str_4": (
                    "FLOAT",
                    {
                        "default": 1.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "shift_1": (
                    "FLOAT",
                    {
                        "default": 1.150,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "shift_2": (
                    "FLOAT",
                    {
                        "default": 1.730,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "shift_3": (
                    "FLOAT",
                    {
                        "default": 3.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "shift_4": (
                    "FLOAT",
                    {
                        "default": 0.500,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
                "alt_scale": (
                    "FLOAT",
                    {
                        "default": 1.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                    },
                ),
            },
        }

    RETURN_TYPES = (
        "INT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
    )

    RETURN_NAMES = (
        "CLIP_SKIP",
        "STR_1",
        "STR_2",
        "STR_3",
        "STR_4",
        "SHIFT_1",
        "SHIFT_2",
        "SHIFT_3",
        "SHIFT_4",
        "ALT_SCALE",
    )
    FUNCTION = "selectah_adv"
    CATEGORY = SELECTOR_CATEGORY_PATH

    def selectah_adv(
        self,
        clip_skip=None,
        str_1=None,
        str_2=None,
        str_3=None,
        str_4=None,
        shift_1=None,
        shift_2=None,
        shift_3=None,
        shift_4=None,
        alt_scale=None,
    ):
        """
        Choose advanced workflow settings from a central place\n
        """
        return (
            clip_skip,
            str_1,
            str_2,
            str_3,
            str_4,
            shift_1,
            shift_2,
            shift_3,
            shift_4,
            alt_scale,
        )


class RecourseCheckpoint:
    """Redirect flow by first active and model type"""

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "model_opta": (
                    "MODEL",
                    {"tooltip": MODEL_1},
                ),
                "model_optb": (
                    "MODEL",
                    {"tooltip": MODEL_2},
                ),
                "clip_opta": (
                    "CLIP",
                    {"tooltip": RECOURSE_PORT},
                ),
                "clip_optb": (
                    "CLIP",
                    {"tooltip": RECOURSE_PORT},
                ),
                "clip_optc": (
                    "CLIP",
                    {"tooltip": RECOURSE_PORT},
                ),
                "vae_opta": (
                    "VAE",
                    {"tooltip": RECOURSE_PORT},
                ),
                "vae_optb": (
                    "VAE",
                    {"tooltip": RECOURSE_PORT},
                ),
            },
            "required": {},
        }

    RETURN_TYPES = (
        "MODEL",
        "CLIP",
        "VAE",
        "INT",
    )
    RETURN_NAMES = (
        "MODEL",
        "CLIP",
        "VAE",
        "MODEL_TYPE",
    )
    FUNCTION = "checkckpt"
    CATEGORY = SELECTOR_CATEGORY_PATH
    DESCRIPTION = RECOURSE_CHECK_DESC
    OUTPUT_TOOLTIPS = (RECOURSE_PORT, RECOURSE_PORT, RECOURSE_PORT)

    def checkckpt(self, model_opta=None, model_optb=None, clip_opta=None, clip_optb=None, clip_optc=None, vae_opta=None, vae_optb=None, model_type=1):
        model_out = next((model for model in [model_opta, model_optb] if model), None)
        clip_out = next((clip for clip in [clip_opta, clip_optb, clip_optc] if clip), None)
        vae_out = next((vae for vae in [vae_opta, vae_optb] if vae), None)

        model_id = type(model_out.model).__name__
        model_type = MODEL_TO_TYPE.get(model_id, 7)
        print(f"Model configuration {model_id}, Selected output {model_type}")
        return (
            model_out,
            clip_out,
            vae_out,
            model_type,
        )


class RecourseStrings:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_1": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "dynamicPrompts": True,
                    },
                ),
            },
            "optional": {
                "text_2": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "dynamicPrompts": True,
                    },
                ),
                "text_3": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "dynamicPrompts": True,
                    },
                ),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFE}),
                "noise_seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = (
        "STRING",
        "STRING",
        "STRING",
        "INT",
        "INT",
    )
    RETURN_NAMES = (
        "TEXT_1",
        "TEXT_2",
        "TEXT_3",
        "SEED",
        "NOISE_SEED",
    )
    OUTPUT_TOOLTIPS = (LINK_PORT, STRING_PORT, STRING_PORT, STRING_PORT, None, None)
    FUNCTION = "recourse_string"

    CATEGORY = SELECTOR_CATEGORY_PATH

    def recourse_string(self, text_1, seed=0, noise_seed=0, text_2="", text_3=""):
        """
        Send text to different locations in a workflow\n
        :return: Tuple of strings and seeds
        """
        # data = [string_1, string_2, string_3]
        # full_out = "".join(data)

        return (text_1, text_2, text_3, seed, noise_seed)


NODE_CLASS_MAPPINGS = {
    "Selector": Selectah,
    "Selector Advanced": SelectahAdv,
    "RecourseCkpt": RecourseCheckpoint,
    "RecourseStrings": RecourseStrings,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Selector": "Selector...",
    "Selector Advanced": "Selector Advanced...",
    "RecourseCkpt": "RecourseCheck...",
    "RecourseStrings": "RecourseStrings...",
}
