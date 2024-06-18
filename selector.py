#

"""
@author:"˶𝞢⤬⫒ⵖsᐼ˶"
@title: "Selector"
@nickname: "Selector"
@version: "2.0.0"
@project: "https://github.com/exdysa/comfyui-selector",
@description: "EXDYSA. Selector and Recourse. Presets & failsafes. Work flow."
"""

import comfy.samplers
import comfy.sd
import comfy.utils
import comfy.model_base
import comfy.model_management
import comfy.model_sampling

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
        ("5:3___XL 1280x768", 1280, 768),
        ("7:4___XL 1344x768", 1344, 768),
        ("21:11_XL 1344x704", 1344, 704),
        ("2:1___XL 1408x704", 1408, 704),
        ("23:11_XL 1472x704", 1472, 704),
        ("21:9__XL 1536x640", 1536, 640),
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
                "aR": (aspect_ratio_titles,
                    {"default": ("1:1___XL 1024x1024")}),
                "rotation": (rotation,),
            },
            "optional": {
                "batch": 
                    ("INT", {"default": 1, "min": 1, "max": 10000,}),
                "steps": 
                    ("INT", {"default": 20, "min": 1, "max": 10000,}),
                "refiner_steps":
                    ("INT", {"default": 20, "min": 1, "max": 10000,}),
                "cfg": ("FLOAT",{
                         "default": 1.00,
                         "min": 0.00,
                         "max": 100.00,
                         "step": 0.01,
                         "round": 0.01,
                }),
                "refiner_cfg": ("FLOAT", {
                        "default": 1.00,
                        "min": 0.00,
                        "max": 100.00,
                        "step": 0.01,
                        "round": 0.01,
                }),
                "str_denoise": ("FLOAT", {
                        "default": 0.500,
                        "min": 0.00,
                        "max": 1000.00,
                        "step": 0.01,
                        "round": 0.01,
                 }),
                "scale_factor": ("FLOAT", {
                        "default": 2.00,
                        "min": 0.00,
                        "max": 1000.00,
                        "step": 0.01,
                        "round": 0.01,
                }),
                "variation_str": ("FLOAT", {
                        "default": 0.000,
                        "min": 0.000,
                        "max": 1000.000,
                        "step": 0.001,
                        "round": 0.001,
                }),
                "sampler": (comfy.samplers.KSampler.SAMPLERS,),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS,)
            }
        }   
    RETURN_TYPES = (
        "INT", "INT", "INT", "INT", "INT", "FLOAT",
        "FLOAT", "FLOAT", "FLOAT", "FLOAT", comfy.samplers.KSampler.SAMPLERS,
        comfy.samplers.KSampler.SCHEDULERS,)
        
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
                return (width, height, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale_factor, variation_str, sampler, scheduler)
        return (None, None, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale_factor, variation_str, sampler, scheduler)  # In case the aspect ratio is not found

# pythongossss 🤍
class ne_ting(str):
    def __ne__(self, __value: object) -> bool:
        return False

anyting = ne_ting("*")

# ltdrdata 🤍
class re_korz:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {"input": (anyting,), "fallback": (anyting,),},
            "required": {}
        }

    RETURN_TYPES = (anyting, "BOOLEAN", )
    RETURN_NAMES = ("OUTPUT", "BOO")
    FUNCTION = "checkit"

    CATEGORY = "utils/Recourse"

    def checkit(self, input=None, fallback=None):
        if input is None:
            return (fallback, False, )
        else:
            return (input, True, )

class re_korz_ckpt:
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
            "required": {}
        }

    RETURN_TYPES = (
        "MODEL","CLIP", "VAE", "INT"
        )
    RETURN_NAMES = (
        "MODEL", "CLIP", "VAE", "M_TYPE(1-5)"

    )
    FUNCTION = "checkckpt"
    CATEGORY = "utils/Recourse"

    def checkckpt(self, model_opta=None, model_optb=None, clip_opta=None, clip_optb=None, clip_optc=None, vae_opta=None, vae_optb=None,m_type=1):
        
        model_out = next((model for model in [model_opta, model_optb] if getattr(model, 'model_options', None) is not None), None)
        
        if clip_opta is not None or clip_optb is not None or clip_optc is not None:
            clip_out = next((clip for clip in [clip_opta, clip_optb, clip_optc] if clip), None)
        else:
            clip_out = None

        if vae_opta is not None or vae_optb is not None:
            vae_out = next((vae for vae in [vae_opta, vae_optb] if vae), None)
        else:
            vae_out = None

        if model_out is not None :
            if isinstance(model_out, comfy.model_base.SDXL) or isinstance(model_out, comfy.model_base.SDXL_instructpix2pix):
                m_type=2
            elif isinstance(model_out, comfy.model_base.SDXLRefiner):
                m_type=4
            elif isinstance(model_out, comfy.model_base.SD3):
                m_type=3
            else:
                m_type=5
        
        return (model_out,clip_out,vae_out,m_type)

class re_korz_polarity:
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
            "required": {}
        }

    RETURN_TYPES = (
        "CONDITIONING","CONDITIONING",
        )
    RETURN_NAMES = (
        "CONDITION+", "CONDITION-", 

    )
    FUNCTION = "checkcond"
    CATEGORY = "utils/Recourse"

    def checkcond(self, pos_opta=0, pos_optb=0, pos_optc=0, pos_optd=0, neg_opta=0, neg_optb=0, neg_optc=0, neg_optd=0):

        if pos_opta is not None or pos_optb is not None or pos_optc is not None or pos_optd is not None:
            pos_out = next((pos for pos in [pos_opta, pos_optb, pos_optc, pos_optd] if pos), None)
        else:
            pos_out = None

        if neg_opta is not None or neg_optb is not None or neg_optc is not None or neg_optd is not None:
            neg_out = next((neg for neg in [neg_opta, neg_optb, neg_optc, neg_optd] if neg), None)
        else:
            neg_out = None

        return (pos_out,neg_out)

class re_korz_image:
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
            "required": {}
        }

    RETURN_TYPES = (
        "IMAGE",
        )
    RETURN_NAMES = (
        "IMAGE", 

    )
    FUNCTION = "checkimg"
    CATEGORY = "utils/Recourse"

    def checkimg(self,img_opta=0, img_optb=0, img_optc=0, img_optd=0, ):

        if img_opta is not None:
                img_out = img_opta
        elif img_optb is not None:
                img_out = img_optb
        elif img_optc is not None:
                img_out = img_optc
        elif img_optd is not None:
                img_out = img_optd
        else:
            img_out = None

        return (img_out,)


# ltdrdata 🤍
class fork:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "switch": 
                    ("INT", {"default": 1, "min": 1, "max": 10000,}),
                "model": ("MODEL",),
            },
            "required": {}
        }

    RETURN_TYPES = "MODEL", "MODEL", "MODEL", "MODEL",
    RETURN_NAMES = "OUT_A", "OUT_B", "OUT_C", "OUT_D", 
    FUNCTION = "forkd"

    CATEGORY = "utils/Recourse"

    def forkd(switch, model):

        if switch == 1:
            return (model, None, None, None)
        elif switch == 2:
            return (None, model, None, None)
        elif switch == 3:
            return (None, None, model, None)
        elif switch == 4 or 5:
            return (None, None, None, model)
        else:
            return (None, None, None, None)

class fork_clip:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "switch": 
                    ("INT", {"default": 1, "min": 1, "max": 10000,}),
                "clip": ("CLIP",),
            },
            "required": {}
        }

    RETURN_TYPES = "CLIP", "CLIP", "CLIP", "CLIP",
    RETURN_NAMES = "OUT_A", "OUT_B", "OUT_C", "OUT_D", 
    FUNCTION = "forkd"

    CATEGORY = "utils/Recourse"

    def forkd(switch, clip):

        if switch == 1:
            return (clip, None, None, None)
        elif switch == 2:
            return (None, clip, None, None)
        elif switch == 3:
            return (None, None, clip, None)
        elif switch == 4 or 5:
            return (None, None, None, clip)
        else:
            return (None, None, None, None)

class unite:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "latent_opta": ("LATENT",),
                "latent_optb": ("LATENT",),
                "latent_optc": ("LATENT",),
                "latent_optd": ("LATENT",),
            },
            "required": {
                "switch": 
                    ("INT", {"default": 1, "min": 1, "max": 10000,}),
            }
        }

    RETURN_TYPES = "LATENT",
    RETURN_NAMES = "LATENT", 
    FUNCTION = "unity"

    CATEGORY = "utils/Recourse"

    def unity(switch, latent_opta,latent_optb,latent_optc,latent_optd):

        if switch == 1:
            return latent_opta
        elif switch == 2:
            return latent_optb
        elif switch == 3:
            return latent_optc
        elif switch == 4 or 5:
            return latent_optd
        else:
            return None

NODE_CLASS_MAPPINGS = { "Selector": selectah,
                        "Recourse": re_korz,
                        "RecourseCkpt": re_korz_ckpt,
                        "Recourse+/-": re_korz_polarity,
                        "RecourseImage": re_korz_image,
                        "Fork": fork,
                        "ForkClip": fork_clip,
                        "Unite": unite,
                      }

NODE_DISPLAY_NAME_MAPPINGS = { "Selector": "Selector...       ⠑⠭⠙⠽⠎⠁",
                                "Recourse": "Recourse...       ⠑⠭⠙⠽⠎⠁", 
                                "RecourseCkpt": "RecourseCheck...  ⠑⠭⠙⠽⠎⠁",
                                "Recourse+/-": "RecoursePolar...  ⠑⠭⠙⠽⠎⠁",
                                "RecourseImage": "RecourseImage...  ⠑⠭⠙⠽⠎⠁",
                                "Fork": "Fork (Model)...   ⠑⠭⠙⠽⠎⠁",
                                "ForkClip": "Fork (Clip)...    ⠑⠭⠙⠽⠎⠁",
                                "Unite": "Unite (Latent)...  ⠑⠭⠙⠽⠎⠁",
                            }