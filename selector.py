class selector:
    # dimensions as sourced from: https://arxiv.org/abs/2307.01952, https://github.com/Stability-AI/generative-models
    RATIO = [
        ("1:1______512x512", 512, 512),
        ("4:3______682x512", 682, 512),
        ("3:2______768x512", 768, 512),
        ("16:9_____910x512", 910, 512),
        ("1:85:1___952x512", 952, 512),
        ("2:1______1024x512", 1024, 512),
        ("1:1_SV3D_576x576", 576, 576),
        ("16:9_SVD_576x1024", 1024, 576),
        ("1:1___2__768x768", 768, 768),
        ("1:1___XL_1024x1024", 1024, 1024),
        ("16:15_XL_1024x960", 1024, 960),
        ("17:15_XL_1088x960", 1088, 960),
        ("17:14_XL_1088x896", 1088, 896),
        ("4:3___XL_1152x896", 1152, 896),
        ("18:13_XL_1152x832", 1152, 832),
        ("3:2___XL_1216x832", 1216, 832),
        ("5:3___XL_1280x768", 1280, 768),
        ("7:4___XL_1344x768", 1344, 768),
        ("21:11_XL_1344x704", 1344, 704),
        ("2:1___XL_1408x704", 1408, 704),
        ("23:11_XL_1472x704", 1472, 704),
        ("21:9__XL_1536x640", 1536, 640),
        ("5:2___XL_1600x640", 1600, 640),
        ("26:9__XL_1664x576", 1664, 576),
        ("3:1___XL_1728x576", 1728, 576),
        ("28:9__XL_1792x576", 1792, 576),
        ("29:8__XL_1856x512", 1856, 512),
        ("15:4__XL_1920x512", 1920, 512),
        ("31:8__XL_1984x512", 1984, 512),
        ("4:1___XL_2048x512", 2048, 512),
    ]

    @classmethod
    def INPUT_TYPES(cls):
        aspect_ratio_titles = [title for title, res1, res2 in cls.RATIO]
        rotation = ("landscape", "portrait")
        
        return {
            "required": {
                "aspectRatio": (aspect_ratio_titles,),
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
                         "default": 1.0,
                         "min": -10.0,
                         "max": 10.0,
                         "step": 0.1,
                         "round": 0.1,
                }),
                "refiner_cfg": ("FLOAT", {
                        "default": 1.0,
                        "min": -10.0,
                        "max": 10.0,
                        "step": 0.1,
                        "round": 0.1,
                }),
                "str_denoise": ("FLOAT", {
                        "default": 1.000,
                        "min": -10.000,
                        "max": 10.000,
                        "step": 0.001,
                        "round": 0.01,
                 }),
                "upscale_factor": ("FLOAT", {
                        "default": 2.0,
                        "min": 1.0,
                        "max": 10.0,
                        "step": 0.1,
                        "round": 0.1,
                }),
            }
        }   
    RETURN_TYPES = (
        "INT", "INT", "INT", "INT", "INT", "FLOAT", "FLOAT", "FLOAT", "FLOAT",
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
        "UPSCALE",
    )
    FUNCTION = "selectah"
    CATEGORY = "image"

    def selectah(self, aspectRatio, rotation, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, upscale_factor):
        for title, width, height in self.RATIO:
            if title == aspectRatio:
                if rotation == "portrait":
                    width, height = height, width  # Swap for portrait orientation
                return (width, height, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, upscale_factor)
        return (None, None, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, upscale_factor)  # In case the aspect ratio is not found

NODE_CLASS_MAPPINGS = { "Selector": selector, }
NODE_DISPLAY_NAME_MAPPINGS = { "Selector": "Selector" }
