"""
@author:"˶𝞢⤬⫒ⵖsᐼ˶"
@title: "Selector"
@nickname: "Selector"
@version: "4.0.1"
@project: "https://github.com/exdysa/comfyui-selector",
@description: "EXDYSA. Selector and Recourse. Presets & failsafes. Work flow."
"""

RECOURSE_DESC = "Ensures connection. Output first active input by type."
RECOURSE_CATEGORY_PATH = "Selector_Recourse/Recourse"
RECOURSE_PORT = "The lowest number port with an active signal is used."


# pyhongossss 🤍
class AnyThingType(str):
    def __ne__(self, __value: object) -> bool:
        return False


anythingtype = AnyThingType("*")


# ltdrdata 🤍
class Recourse:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "input_signal": (
                    anythingtype,
                    {"tooltip": RECOURSE_PORT},
                ),
                "fallback_signal": (
                    anythingtype,
                    {"tooltip": RECOURSE_PORT},
                ),
            },
            "required": {},
        }

    RETURN_TYPES = (
        anythingtype,
        "BOOLEAN",
    )
    RETURN_NAMES = (
        "OUTPUT",
        "BOOL",
    )
    FUNCTION = "checkit"
    CATEGORY = RECOURSE_CATEGORY_PATH
    DESCRIPTION = RECOURSE_DESC

    def checkit(self, input_signal=None, fallback_signal=None):
        if input_signal is None:
            return (
                fallback_signal,
                False,
            )
        else:
            return (
                input_signal,
                True,
            )


class RecoursePolar:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "pos_a": (
                    "CONDITIONING",
                    {"tooltip": RECOURSE_PORT},
                ),
                "pos_b": (
                    "CONDITIONING",
                    {"tooltip": RECOURSE_PORT},
                ),
                "pos_c": (
                    "CONDITIONING",
                    {"tooltip": RECOURSE_PORT},
                ),
                "pos_d": (
                    "CONDITIONING",
                    {"tooltip": RECOURSE_PORT},
                ),
                "neg_a": (
                    "CONDITIONING",
                    {"tooltip": RECOURSE_PORT},
                ),
                "neg_b": (
                    "CONDITIONING",
                    {"tooltip": RECOURSE_PORT},
                ),
                "neg_c": (
                    "CONDITIONING",
                    {"tooltip": RECOURSE_PORT},
                ),
                "neg_d": (
                    "CONDITIONING",
                    {"tooltip": RECOURSE_PORT},
                ),
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
    CATEGORY = RECOURSE_CATEGORY_PATH
    DESCRIPTION = RECOURSE_DESC
    FUNCTION = "checkcond"

    def checkcond(self, pos_a, pos_b, pos_c, pos_d, neg_a, neg_b, neg_c, neg_d):
        pos_kwargs = [pos_a, pos_b, pos_c, pos_d]
        neg_kwargs = [neg_a, neg_b, neg_c, neg_d]
        pos_out = next((pos for pos in pos_kwargs if pos), None)
        neg_out = next((neg for neg in neg_kwargs if neg), None)

        return (
            pos_out,
            neg_out,
        )


class RecourseImage:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "img_opt_a": (
                    "IMAGE",
                    {"tooltip": RECOURSE_PORT},
                ),
                "img_opt_b": (
                    "IMAGE",
                    {"tooltip": RECOURSE_PORT},
                ),
                "img_opt_c": (
                    "IMAGE",
                    {"tooltip": RECOURSE_PORT},
                ),
                "img_opt_d": (
                    "IMAGE",
                    {"tooltip": RECOURSE_PORT},
                ),
                "img_opt_e": (
                    "IMAGE",
                    {"tooltip": RECOURSE_PORT},
                ),
                "img_opt_f": (
                    "IMAGE",
                    {"tooltip": RECOURSE_PORT},
                ),
                "img_opt_g": (
                    "IMAGE",
                    {"tooltip": RECOURSE_PORT},
                ),
                "img_opt_h": (
                    "IMAGE",
                    {"tooltip": RECOURSE_PORT},
                ),
            },
            "required": {},
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    FUNCTION = "checkimg"
    CATEGORY = RECOURSE_CATEGORY_PATH
    DESCRIPTION = RECOURSE_DESC

    def checkimg(self, **kwargs):
        image_out = next(kwargs[x] for x in kwargs if x is not None)
        return (image_out,)


NODE_CLASS_MAPPINGS = {
    "RecourseAny": Recourse,
    "RecoursePolar": RecoursePolar,
    "RecourseImage": RecourseImage,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Recourse": "Recourse (ANY)...",
    "RecoursePolar": "Recourse (Polarity)...",
    "RecourseImage": "Recourse (IMAGE)...",
}
