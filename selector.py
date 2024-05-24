#

class selector:
    RATIO = [
        ("1:1 x512", 512, 512),
        ("2:3 x768", 768, 512),
        ("3:4 x682", 682, 512),
        ("9:16 x910", 910, 512),
        ("1:1.85 x952", 952, 512),
        ("1:2 x1024", 1024, 512),
        ("1:1 x768 2.0", 768, 768),
        ("1:1 1024 XL", 1024, 1024),
        ("3:2 832x1216 XL", 1216, 832),
        ("3:4 896x1152 XL", 1152, 896),
        ("9:16 768x1344 XL", 1344,768 ),
        ("9:21 640x1536 XL", 1536, 640)
    ]

    @classmethod
    def INPUT_TYPES(cls):
        aspect_ratio_titles = [title for title, _, _ in cls.RATIO]
        ROTATION = ["landscape" , "portrait"]

        return {
            "required": {
                "aspectRatio": (aspect_ratio_titles,),
                "rotation": (ROTATION,),
            }
        }
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "aspector"
    CATEGORY = "image"

    def aspector(self, aspectRatio, rotation):
        for title, width, height in self.RATIO:
            if title == aspectRatio:
                if rotation == "portrait":
                    width, height = height, width  # Swap for portrait orientation
                return (width, height)
        return (None, None)  # In case the aspect ratio is not found


NODE_CLASS_MAPPINGS = { "Selector": selector, }
NODE_DISPLAY_NAME_MAPPINGS = { "Selector": "Selector" }


