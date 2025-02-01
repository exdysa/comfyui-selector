"""
@author:"˶𝞢⤬⫒ⵖsᐼ˶"
@title: "Selector"
@nickname: "Selector"
@version: "4.0.1"
@project: "https://github.com/exdysa/comfyui-selector",
@description: "EXDYSA. Selector and Recourse. Presets & failsafes. Work flow."
"""

MAX_RECOURSE_INPUTS = 8

SELECTOR_IN_CATEGORY_PATH = "Selector_Recourse/In"
SELECTOR_DESC = "Directs flow. Coordinated by model type output from RecourseCheckpoint."
TYPE_DESC = "SD1, SDXL, FLUX, AURAFLOW, HUNYUANDIT, SD3, STABLE_CASCADE_C, STABLE_CASCADE_B"
SELECTOR_PORT = "An input port is activated based on the model_type number."

OUTPUT_0 = "Active when Stable Diffusion 1 is detected"
OUTPUT_1 = "Active when Stable Diffusion XL/Refiner/P2P is detected"
OUTPUT_2 = "Active when Flux is detected"
OUTPUT_3 = "Active when Auraflow is detected"
OUTPUT_4 = "Active when HunyuanDIT is detected"
OUTPUT_5 = "Active when Stable Diffusion 3 is detected"
OUTPUT_6 = ""
OUTPUT_7 = ""


class SelInLatent:
    def __init__(self):
        pass

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

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"latent{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class SelInModel:
    def __init__(self):
        pass

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

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"model{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class SelInClip:
    def __init__(self):
        pass

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

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"clip{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class SelInPolar:
    def __init__(self):
        pass

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

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"conditioning{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class SelInSigmas:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "sigmas1": ("SIGMAS", {"lazy": True}),
                "sigmas2": ("SIGMAS", {"lazy": True}),
                "sigmas3": ("SIGMAS", {"lazy": True}),
                "sigmas4": ("SIGMAS", {"lazy": True}),
                "sigmas5": ("SIGMAS", {"lazy": True}),
                "sigmas6": ("SIGMAS", {"lazy": True}),
                "sigmas7": ("SIGMAS", {"lazy": True}),
                "sigmas8": ("SIGMAS", {"lazy": True}),
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
        live_output = f"sigmas{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = ("SIGMAS",)
    RETURN_NAMES = ("SIGMAS",)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"sigmas{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class SelInSampler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "sampler1": ("SAMPLER", {"lazy": True}),
                "sampler2": ("SAMPLER", {"lazy": True}),
                "sampler3": ("SAMPLER", {"lazy": True}),
                "sampler4": ("SAMPLER", {"lazy": True}),
                "sampler5": ("SAMPLER", {"lazy": True}),
                "sampler6": ("SAMPLER", {"lazy": True}),
                "sampler7": ("SAMPLER", {"lazy": True}),
                "sampler8": ("SAMPLER", {"lazy": True}),
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
        live_output = f"sampler{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = ("SAMPLER",)
    RETURN_NAMES = ("SAMPLER",)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"sampler{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class SelInGuider:
    def __init__(self):
        pass

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

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"guider{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class SelInFloat:
    def __init__(self):
        pass

    field_name = "cfg"
    node_type = "FLOAT"

    @classmethod
    def INPUT_TYPES(s):
        node_type = "FLOAT"
        return {
            "optional": {
                "float1": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "float2": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "float3": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "float4": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "float5": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "float6": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "float7": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "float8": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
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
        live_output = f"{self.field_name}{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = (node_type,)
    RETURN_NAMES = (node_type,)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"float{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class SelInInt:
    def __init__(self):
        pass

    field_name = "int"
    node_type = "INT"

    @classmethod
    def INPUT_TYPES(s):
        node_type = "INT"
        return {
            "optional": {
                "int1": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "int2": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "int3": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "int4": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "int5": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "int6": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "int7": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
                "int8": (
                    node_type,
                    {
                        "lazy": True,
                    },
                ),
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
        live_output = f"{self.field_name}{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return [live_output]
        else:
            return []

    RETURN_TYPES = (node_type,)
    RETURN_NAMES = (node_type,)
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"int{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


class SelInVae:
    def __init__(self):
        pass

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

    CATEGORY = SELECTOR_IN_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    @staticmethod
    def select_model(**kwargs):
        live_output = f"vae{int(kwargs['model_type'])}"
        if live_output in kwargs:
            return (kwargs[live_output],)
        return (None,)


NODE_CLASS_MAPPINGS = {
    "SelInLatent": SelInLatent,
    "SelInModel": SelInModel,
    "SelInClip": SelInClip,
    "SelInPolar": SelInPolar,
    "SelInGuider": SelInGuider,
    "SelInVae": SelInVae,
    "SelInSigmas": SelInSigmas,
    "SelInSampler": SelInSampler,
    "SelInFloat": SelInFloat,
    "SelInInt": SelInInt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SelInLatent": "Selector In (LATENT)...",
    "SelInModel": "Selector In (MODEL)...",
    "SelInClip": "Selector In (CLIP)...",
    "SelInPolar": "Selector In (Polarity)...",
    "SelInGuider": "Selector In (GUIDER)...",
    "SelInVae": "Selector In (VAE)...",
    "SelInSigmas": "Selector In (SIGMAS)",
    "SelInSampler": "Selector In (SAMPLER)",
    "SelInFloat": "Selector In (FLOAT)",
    "SelInInt": "Selector In (INT)",
}
