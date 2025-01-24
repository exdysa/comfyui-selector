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

MAX_RECOURSE_INPUTS = 8
SELECTOR_DESC = "Directs flow. Coordinated by model type output from RecourseCheckpoint."
RECOURSE_DESC = "Ensures connection. Output first active input by type."
SELECTOR_CATEGORY = "utils/Selector_Recourse"
TYPE_DESC = "SD1, SDXL, FLUX, AURAFLOW, HUNYUANDIT, SD3, STABLE_CASCADE"

MODEL_1 = "This port requires MODEL to send the MODEL_TYPE to other nodes."
MODEL_2 = "This port is activated in case MODEL_1 has no signal."
UNITE_PORT = "An input port is activated based on the model_type number."
FORK_PORT = "An output port is activated based on the model_type number."
RECOURSE_PORT = "The lowest number port with an active signal is sent to output."

OUTPUT_0 = "Active when Stable Diffusion 1 is detected"
OUTPUT_1 = "Active when Stable Diffusion XL/Refiner/P2P is detected"
OUTPUT_2 = "Active when Flux is detected"
OUTPUT_3 = "Active when Auraflow is detected"
OUTPUT_4 = "Active when HunyuanDIT is detected"
OUTPUT_5 = "Active when Stable Diffusion 3 is detected"
OUTPUT_6 = "Active when Stable Cascade C is detected"
OUTPUT_6 = "Active when Stable Cascade B is detected"


class selectah:
    # dimensions sourced from: https://arxiv.org/abs/2307.01952
    # & https://github.com/Stability-AI/generative-models
    RATIO = [
        ("1:1___SD 512x512", 512, 512),
        ("4:3___SD 682x512", 682, 512),
        ("3:2___SD 768x512", 768, 512),
        ("16:9__SD 910x512", 910, 512),
        ("1:85:1 SD 952x512", 952, 512),
        ("2:1___SD 1024x512", 1024, 512),
        ("1:1_SV3D 576x576", 576, 576),
        ("16:9_SVD 1024X576", 1024, 576),
        ("1:1__SD2 768x768", 768, 768),
        ("1:1___XL 1024x1024", 1024, 1024),
        ("16:15_XL 1024x960", 1024, 960),
        ("17:15_XL 1088x960", 1088, 960),
        ("17:14_XL 1088x896", 1088, 896),
        ("4:3___XL 1152x896", 1152, 896),
        ("18:13_XL 1152x832", 1152, 832),
        ("3:2___XL 1216x832", 1216, 832),
        ("72:32_XL 1232x832", 1232, 832),
        ("5:3___XL 1280x768", 1280, 768),
        ("7:4___XL 1344x768", 1344, 768),
        ("21:11_XL 1344x704", 1344, 704),
        ("2:1___XL 1408x704", 1408, 704),
        ("23:11_XL 1472x704", 1472, 704),
        ("21:9__XL 1536x640", 1536, 640),
        ("2:1)__XL 1536x768", 1536, 768),
        ("5:2___XL 1600x640", 1600, 640),
        ("26:9__XL 1664x576", 1664, 576),
        ("3:1___XL 1728x576", 1728, 576),
        ("28:9__XL 1792x576", 1792, 576),
        ("29:8__XL 1856x512", 1856, 512),
        ("15:4__XL 1920x512", 1920, 512),
        ("31:8__XL 1984x512", 1984, 512),
        ("4:1___XL 2048x512", 2048, 512),
    ]

    @classmethod
    def INPUT_TYPES(cls):
        aspect_ratio_titles = [title for title, res1, res2 in cls.RATIO]
        rotation = ("landscape", "portrait")

        return {
            "required": {
                "aR": (aspect_ratio_titles, {"default": ("1:1___XL 1024x1024")}),
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
                "scale_factor": (
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
        "SCALE_FACTOR",
        "VARIATION_STR",
        "SAMPLER",
        "SCHEDULER",
    )
    FUNCTION = "selectah"
    CATEGORY = "image"

    def selectah(self, aR, rotation, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale_factor, variation_str, sampler, scheduler):
        for title, width, height in self.RATIO:
            if title == aR:
                if rotation == "portrait":
                    width, height = height, width  # Swap for portrait orientation
                return (
                    width,
                    height,
                    batch,
                    steps,
                    refiner_steps,
                    cfg,
                    refiner_cfg,
                    str_denoise,
                    scale_factor,
                    variation_str,
                    sampler,
                    scheduler,
                )
        return (
            None,
            None,
            batch,
            steps,
            refiner_steps,
            cfg,
            refiner_cfg,
            str_denoise,
            scale_factor,
            variation_str,
            sampler,
            scheduler,
        )  # In case the aspect ratio is not found


# pythongossss 🤍
class ne_ting(str):
    def __ne__(self, __value: object) -> bool:
        return False


anyting = ne_ting("*")


# ltdrdata 🤍
class recourse:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "input": (anyting,),
                "fallback": (anyting,),
            },
            "required": {},
        }

    RETURN_TYPES = (
        anyting,
        "BOOLEAN",
    )
    RETURN_NAMES = (
        "OUTPUT",
        "BOOL",
    )
    FUNCTION = "checkit"
    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = RECOURSE_DESC

    def checkit(self, input=None, fallback=None):
        if input is None:
            return (
                fallback,
                False,
            )
        else:
            return (
                input,
                True,
            )


class recourse_checkpoint:
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
    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = RECOURSE_DESC

    def checkckpt(self, model_opta=None, model_optb=None, clip_opta=None, clip_optb=None, clip_optc=None, vae_opta=None, vae_optb=None, model_type=1):
        model_out = next((model for model in [model_opta, model_optb] if model), None)
        clip_out = next((clip for clip in [clip_opta, clip_optb, clip_optc] if clip), None)
        vae_out = next((vae for vae in [vae_opta, vae_optb] if vae), None)

        model_id = type(model_out.model).__name__
        model_type = MODEL_TO_TYPE.get(model_id)
        print(f"Configuration : {model_id}, Aligning Outputs to: {model_type}")
        return (
            model_out,
            clip_out,
            vae_out,
            model_type,
        )


class recourse_polarity:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "pos_opta": ("CONDITIONING",),
                "pos_optb": ("CONDITIONING",),
                "pos_optc": ("CONDITIONING",),
                "pos_optd": ("CONDITIONING",),
                "neg_opta": ("CONDITIONING",),
                "neg_optb": ("CONDITIONING",),
                "neg_optc": ("CONDITIONING",),
                "neg_optd": ("CONDITIONING",),
            },
            "required": {},
        }

    RETURN_TYPES = (
        "CONDITIONING",
        "CONDITIONING",
    )
    RETURN_NAMES = (
        "CONDITION+",
        "CONDITION-",
    )
    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = RECOURSE_DESC
    FUNCTION = "checkcond"

    def checkcond(self, **kwargs):
        pos_out = next((pos for pos in kwargs if pos), None)
        neg_out = next((neg for neg in kwargs if neg), None)

        return (
            pos_out,
            neg_out,
        )


class recourse_image:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "img_opta": ("IMAGE",),
                "img_optb": ("IMAGE",),
                "img_optc": ("IMAGE",),
                "img_optd": ("IMAGE",),
            },
            "required": {},
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    FUNCTION = "checkimg"
    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = RECOURSE_DESC

    def checkimg(self, **kwargs):
        image_out = next(kwargs[x] for x in kwargs if x is not None)
        return (image_out,)


# ltdrdata 🤍
class fork_model:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "model": ("MODEL",),
            },
            "required": {
                "model_type": (
                    "INT",
                    {
                        "default": 1,
                        "min": 1,
                        "max": MAX_RECOURSE_INPUTS,
                    },
                ),
            },
        }

    RETURN_TYPES = (
        "MODEL",
        "MODEL",
        "MODEL",
        "MODEL",
        "MODEL",
        "MODEL",
        "MODEL",
        "MODEL",
    )
    RETURN_NAMES = (
        "OUT_A",
        "OUT_B",
        "OUT_C",
        "OUT_D",
        "OUT_E",
        "OUT_F",
        "OUT_G",
        "OUT_H",
    )
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = SELECTOR_DESC

    def select_model(self, model_type, model):
        result = [None] * MAX_RECOURSE_INPUTS
        if 1 <= model_type <= MAX_RECOURSE_INPUTS:
            result[model_type - 1] = model
        return tuple(
            result,
        )


class fork_clip:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "clip": ("CLIP",),
            },
            "required": {
                "model_type": (
                    "INT",
                    {
                        "default": 1,
                        "min": 1,
                        "max": MAX_RECOURSE_INPUTS,
                    },
                ),
            },
        }

    RETURN_TYPES = (
        "CLIP",
        "CLIP",
        "CLIP",
        "CLIP",
        "CLIP",
        "CLIP",
        "CLIP",
        "CLIP",
    )
    RETURN_NAMES = (
        "OUT_A",
        "OUT_B",
        "OUT_C",
        "OUT_D",
        "OUT_E",
        "OUT_F",
        "OUT_G",
        "OUT_H",
    )
    FUNCTION = "select_clip"

    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = SELECTOR_DESC

    def select_clip(self, model_type, clip):
        result = [None] * MAX_RECOURSE_INPUTS
        if 1 <= model_type <= MAX_RECOURSE_INPUTS:
            result[model_type - 1] = clip
        return tuple(
            result,
        )


class unite_model:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "latent1": ("LATENT", {"lazy": True}),
                "latent2": ("LATENT", {"lazy": True}),
                "latent3": ("LATENT", {"lazy": True}),
                "latent4": ("LATENT", {"lazy": True}),
                "latent5": ("LATENT", {"lazy": True}),
                "latent6": ("LATENT", {"lazy": True}),
                "latent7": ("LATENT", {"lazy": True}),
                "latent8": ("LATENT", {"lazy": True}),
            },
            "required": {
                "model_type": (
                    "INT",
                    {
                        "default": 1,
                        "min": 1,
                        "max": MAX_RECOURSE_INPUTS,
                    },
                ),
            },
        }

    def check_lazy_status(self, **kwargs):
        live_output = f"latent{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("LATENT",)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = SELECTOR_DESC

    def select_model(self, **kwargs):
        live_output = f"latent{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class unite_model:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "model1": ("MODEL", {"lazy": True}),
                "model2": ("MODEL", {"lazy": True}),
                "model3": ("MODEL", {"lazy": True}),
                "model4": ("MODEL", {"lazy": True}),
                "model5": ("MODEL", {"lazy": True}),
                "model6": ("MODEL", {"lazy": True}),
                "model7": ("MODEL", {"lazy": True}),
                "model8": ("MODEL", {"lazy": True}),
            },
            "required": {
                "model_type": (
                    "INT",
                    {
                        "default": 1,
                        "min": 1,
                        "max": MAX_RECOURSE_INPUTS,
                    },
                ),
            },
        }

    def check_lazy_status(self, **kwargs):
        live_output = f"model{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("MODEL",)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"model{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class unite_clip:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "clip1": ("CLIP", {"lazy": True}),
                "clip2": ("CLIP", {"lazy": True}),
                "clip3": ("CLIP", {"lazy": True}),
                "clip4": ("CLIP", {"lazy": True}),
                "clip5": ("CLIP", {"lazy": True}),
                "clip6": ("CLIP", {"lazy": True}),
                "clip7": ("CLIP", {"lazy": True}),
                "clip8": ("CLIP", {"lazy": True}),
            },
            "required": {
                "model_type": (
                    "INT",
                    {
                        "default": 1,
                        "min": 1,
                        "max": MAX_RECOURSE_INPUTS,
                    },
                ),
            },
        }

    def check_lazy_status(self, **kwargs):
        live_output = f"clip{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("CLIP",)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"clip{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class unite_conditioning:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "conditioning1": ("CONDITIONING", {"lazy": True}),
                "conditioning2": ("CONDITIONING", {"lazy": True}),
                "conditioning3": ("CONDITIONING", {"lazy": True}),
                "conditioning4": ("CONDITIONING", {"lazy": True}),
                "conditioning5": ("CONDITIONING", {"lazy": True}),
                "conditioning6": ("CONDITIONING", {"lazy": True}),
                "conditioning7": ("CONDITIONING", {"lazy": True}),
                "conditioning8": ("CONDITIONING", {"lazy": True}),
            },
            "required": {
                "model_type": (
                    "INT",
                    {
                        "default": 1,
                        "min": 1,
                        "max": MAX_RECOURSE_INPUTS,
                    },
                ),
            },
        }

    def check_lazy_status(self, **kwargs):
        live_output = f"conditioning{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("CONDITIONING",)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"conditioning{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class unite_guider:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "guider1": ("GUIDER", {"lazy": True}),
                "guider2": ("GUIDER", {"lazy": True}),
                "guider3": ("GUIDER", {"lazy": True}),
                "guider4": ("GUIDER", {"lazy": True}),
                "guider5": ("GUIDER", {"lazy": True}),
                "guider6": ("GUIDER", {"lazy": True}),
                "guider7": ("GUIDER", {"lazy": True}),
                "guider8": ("GUIDER", {"lazy": True}),
            },
            "required": {
                "model_type": (
                    "INT",
                    {
                        "default": 1,
                        "min": 1,
                        "max": MAX_RECOURSE_INPUTS,
                    },
                ),
            },
        }

    def check_lazy_status(self, **kwargs):
        live_output = f"guider{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = ("GUIDER",)
    RETURN_NAMES = ("GUIDER",)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"guider{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class unite_vae:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "vae1": ("VAE", {"lazy": True}),
                "vae2": ("VAE", {"lazy": True}),
                "vae3": ("VAE", {"lazy": True}),
                "vae4": ("VAE", {"lazy": True}),
                "vae5": ("VAE", {"lazy": True}),
                "vae6": ("VAE", {"lazy": True}),
                "vae7": ("VAE", {"lazy": True}),
                "vae8": ("VAE", {"lazy": True}),
            },
            "required": {
                "model_type": (
                    "INT",
                    {
                        "default": 1,
                        "min": 1,
                        "max": MAX_RECOURSE_INPUTS,
                    },
                ),
            },
        }

    def check_lazy_status(self, **kwargs):
        live_output = f"vae{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = ("VAE",)
    RETURN_NAMES = ("VAE",)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"vae{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class fork_conditioning:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "conditioning": ("CONDITIONING",),
            },
            "required": {
                "model_type": (
                    "INT",
                    {
                        "default": 1,
                        "min": 1,
                        "max": MAX_RECOURSE_INPUTS,
                    },
                ),
            },
        }

    RETURN_TYPES = (
        "CONDITIONING",
        "CONDITIONING",
        "CONDITIONING",
        "CONDITIONING",
        "CONDITIONING",
        "CONDITIONING",
        "CONDITIONING",
        "CONDITIONING",
    )
    RETURN_NAMES = (
        "OUT_A",
        "OUT_B",
        "OUT_C",
        "OUT_D",
        "OUT_E",
        "OUT_F",
        "OUT_G",
        "OUT_H",
    )
    FUNCTION = "select_condition"

    CATEGORY = SELECTOR_CATEGORY
    DESCRIPTION = SELECTOR_DESC

    def select_condition(self, model_type, conditioning=None):
        result = [None] * MAX_RECOURSE_INPUTS
        if 1 <= model_type <= MAX_RECOURSE_INPUTS:
            result[model_type - 1] = conditioning
        return tuple(
            result,
        )


NODE_CLASS_MAPPINGS = {
    "Selector": selectah,
    "Recourse": recourse,
    "RecourseCkpt": recourse_checkpoint,
    "Recourse+-": recourse_polarity,
    "RecourseImage": recourse_image,
    "Fork": fork_model,
    "ForkClip": fork_clip,
    "Unite": unite_model,
    "UniteModel": unite_model,
    "UniteClip": unite_clip,
    "Unite+-": unite_conditioning,
    "UniteGuider": unite_guider,
    "UniteVAE": unite_vae,
    "Fork+-": fork_conditioning,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Selector": "Selector...",
    "Recourse": "Recourse...",
    "RecourseCkpt": "RecourseCheck...",
    "Recourse+-": "RecoursePolar...",
    "RecourseImage": "RecourseImage...",
    "Fork": "Fork (Model)...",
    "ForkClip": "Fork (Clip)...",
    "Unite": "Unite (Latent)...",
    "UniteModel": "Unite (Model)...",
    "UniteClip": "Unite (Clip)...",
    "Unite+-": "Unite (Polarity)...",
    "UniteGuider": "Unite (Guider)...",
    "UniteVAE": "Unite (VAE)...",
    "Fork+-": "Fork (Polarity)...",
}
