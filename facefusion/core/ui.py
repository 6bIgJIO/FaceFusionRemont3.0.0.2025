import importlib
from facefusion import logger
import traceback

def load_ui_layout_module(name: str):
    try:
        return importlib.import_module(f"facefusion.uis.layouts.{name}")
    except Exception as e:
        logger.error(f"Failed to load UI layout '{name}': {e}")
        logger.error(traceback.format_exc())
        return None


def get_ui_layouts_modules(layouts: list[str]):
    modules = []
    for name in layouts:
        module = load_ui_layout_module(name)
        if module:
            modules.append(module)
    return modules