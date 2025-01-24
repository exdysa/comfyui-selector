"""
@author:"˶𝞢⤬⫒ⵖsᐼ˶"
@title: "Selector"
@nickname: "Selector"
@version: "3.2.0"
@project: "https://github.com/exdysa/comfyui-selector",
@description: "EXDYSA. Selector and Recourse. Presets & failsafes. Work flow."
"""

from . import recourse
from . import selector
from . import selector_in
from . import selector_out

NODE_CLASS_MAPPINGS = recourse.NODE_CLASS_MAPPINGS | selector.NODE_CLASS_MAPPINGS | selector_in.NODE_CLASS_MAPPINGS | selector_out.NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = recourse.NODE_DISPLAY_NAME_MAPPINGS | selector.NODE_DISPLAY_NAME_MAPPINGS | selector_in.NODE_DISPLAY_NAME_MAPPINGS | selector_out.NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
