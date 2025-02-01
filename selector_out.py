"""
@author:"˶𝞢⤬⫒ⵖsᐼ˶"
@title: "Selector"
@nickname: "Selector"
@version: "4.0.1"
@project: "https://github.com/exdysa/comfyui-selector",
@description: "EXDYSA. Selector and Recourse. Presets & failsafes. Work flow."
"""

MAX_RECOURSE_INPUTS = 8

SELECTOR_OUT_CATEGORY_PATH = "Selector_Recourse/Out"
SELECTOR_DESC = "Directs flow. Coordinated by model type output from RecourseCheckpoint."
TYPE_DESC = "SD1, SDXL, FLUX, AURAFLOW, HUNYUANDIT, SD3, STABLE_CASCADE_C, STABLE_CASCADE_B"
SELECTOR_PORT = "An output port is activated based on the model_type number."
SELECTOR_OUT_RETURN_NAMES = (
    "OUT_1",
    "OUT_2",
    "OUT_3",
    "OUT_4",
    "OUT_5",
    "OUT_6",
    "OUT_7",
    "OUT_8",
)

OUTPUT_0 = "Active when Stable Diffusion 1 is detected"
OUTPUT_1 = "Active when Stable Diffusion XL/Refiner/P2P is detected"
OUTPUT_2 = "Active when Flux is detected"
OUTPUT_3 = "Active when Auraflow is detected"
OUTPUT_4 = "Active when HunyuanDIT is detected"
OUTPUT_5 = "Active when Stable Diffusion 3 is detected"
OUTPUT_6 = ""
OUTPUT_7 = ""


# ltdrdata 🤍
class SelOutModel:
    def __init__(self):
        pass

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
    RETURN_NAMES = SELECTOR_OUT_RETURN_NAMES
    FUNCTION = "select_model"

    CATEGORY = SELECTOR_OUT_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    def select_model(self, model_type, model):
        result = [None] * MAX_RECOURSE_INPUTS
        if 1 <= model_type <= MAX_RECOURSE_INPUTS:
            result[model_type - 1] = model
        return tuple(
            result,
        )


class SelOutClip:
    def __init__(self):
        pass

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
    RETURN_NAMES = SELECTOR_OUT_RETURN_NAMES
    FUNCTION = "select_clip"

    CATEGORY = SELECTOR_OUT_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    def select_clip(self, model_type, clip):
        result = [None] * MAX_RECOURSE_INPUTS
        if 1 <= model_type <= MAX_RECOURSE_INPUTS:
            result[model_type - 1] = clip
        return tuple(
            result,
        )


class SelOutPolar:
    def __init__(self):
        pass

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
    RETURN_NAMES = SELECTOR_OUT_RETURN_NAMES
    FUNCTION = "select_condition"

    CATEGORY = SELECTOR_OUT_CATEGORY_PATH
    DESCRIPTION = SELECTOR_DESC

    def select_condition(self, model_type, conditioning=None):
        result = [None] * MAX_RECOURSE_INPUTS
        if 1 <= model_type <= MAX_RECOURSE_INPUTS:
            result[model_type - 1] = conditioning
        return tuple(
            result,
        )


NODE_CLASS_MAPPINGS = {
    "SelOutModel": SelOutModel,
    "SelOutCLIP": SelOutClip,
    "SelOutPolar": SelOutPolar,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SelOutModel": "Selector Out (MODEL)...",
    "SelOutCLIP": "Selector Out (CLIP)...",
    "SelOutPolar": "Selector Out (Polarity)...",
}
