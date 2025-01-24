#

"""
@author:"˶𝞢⤬⫒ⵖsᐼ˶"
@title: "Selector"
@nickname: "Selector"
@version: "3.1.0"
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
    "StableCascade_B": 8,
    "StableCascade_C": 7,
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
        ("4:3___1152x896", 1152, 896),
        ("18:13_1152x832", 1152, 832),
        ("3:2___1216x832", 1216, 832),
        ("72:32_1232x832", 1232, 832),
        ("5:3___1280x768", 1280, 768),
        ("7:4___1344x768", 1344, 768),
        ("21:11_1344x704", 1344, 704),
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
        ("4:3___V_832x624", 832, 624),
        ("22:15_V_704x480", 704, 480),
        ("9:5___V_720x400", 720, 400),
        ("3:2___V_720x480", 720, 480),
        ("5:4___V_720x576", 720, 576),
        ("3:2___V_768x512", 768, 512),
        ("4:3___V 960x704", 960, 704),
        ("1:1___V_960x960", 960, 960),
        ("20:11_V_1280x704", 1280, 704),
        ("16:9__V_1024X576", 1024, 576),
        ("1:1__SV3D_576x576", 576, 576),
        ("1:1____SD_512x512", 512, 512),
        ("4:3____SD_682x512", 682, 512),
        ("3:2____SD_768x512", 768, 512),
        ("16:9___SD_910x512", 910, 512),
        ("1:85:1_SD_952x512", 952, 512),
        ("1:1___SD2_768x768", 768, 768),
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
                "sampler": (comfy.samplers.KSampler.SAMPLERS,),
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
        "STRENGTH",
        "VARIATION_STR",
        "SCALE",
        "SAMPLER",
        "SCHEDULER",
    )
    FUNCTION = "selectah"
    CATEGORY = SELECTOR_CATEGORY_PATH

    def selectah(self, aspect_ratio, rotation, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale, variation_str, sampler, scheduler):
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
                return (width, height, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale, variation_str, sampler, scheduler)

        # If aspect ratio is not found, return None for width and height
        return (None, None, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale, variation_str, sampler, scheduler)


class RecourseCheckpoint:
    """Redirect flow by first active and model type"""

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "model_opta": ("MODEL",),
                "model_optb": ("MODEL",),
                "clip_opta": ("CLIP",),
                "clip_optb": ("CLIP",),
                "clip_optc": ("CLIP",),
                "vae_opta": ("VAE",),
                "vae_optb": ("VAE",),
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

    def checkckpt(self, model_opta=None, model_optb=None, clip_opta=None, clip_optb=None, clip_optc=None, vae_opta=None, vae_optb=None, model_type=1):
        model_out = next((model for model in [model_opta, model_optb] if model), None)
        clip_out = next((clip for clip in [clip_opta, clip_optb, clip_optc] if clip), None)
        vae_out = next((vae for vae in [vae_opta, vae_optb] if vae), None)

        model_id = type(model_out.model).__name__
        model_type = MODEL_TO_TYPE.get(model_id)
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
                "model_1": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "dynamicPrompts": True,
                    },
                ),
            },
            "optional": {
                "model_2": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "dynamicPrompts": True,
                    },
                ),
                "model_3": (
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
        "STRING",
        "INT",
        "INT",
    )
    RETURN_NAMES = (
        "LINKED_STRINGS",
        "MODEL_1",
        "MODEL_2",
        "MODEL_3",
        "SEED",
        "NOISE_SEED",
    )
    FUNCTION = "recourse_string"

    CATEGORY = SELECTOR_CATEGORY_PATH

    def recourse_string(
        self,
        seed,
        noise_seed,
        model_1,
        model_2="",
        model_3="",
    ):
        data = [model_1, model_2, model_3]
        full_out = "".join(data)

        return (
            full_out,
            model_1,
            model_2,
            model_3,
            seed,
            noise_seed,
        )


NODE_CLASS_MAPPINGS = {
    "Selector": Selectah,
    "RecourseCkpt": RecourseCheckpoint,
    "RecourseStrings": RecourseStrings,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Selector": "Selector...",
    "RecourseCkpt": "RecourseCheck...",
    "RecourseStrings": "RecourseStrings...",
}
