from facefusion import state_manager
from facefusion.core.ui import get_ui_layouts_modules

def load():
    layouts = state_manager.get_item("ui_layouts") or ["default"]
    return get_ui_layouts_modules(layouts)