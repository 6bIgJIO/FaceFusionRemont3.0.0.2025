# Shim: redirect import gradio_rangeslider to internal facefusion component
from facefusion.gradio_rangeslider.rangeslider import RangeSlider

__all__ = ["RangeSlider"]