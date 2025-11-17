import gradio as gr

class RangeSlider(gr.Slider):
    def __init__(
        self,
        minimum=0,
        maximum=100,
        value=(0, 100),
        step=1,
        label=None,
        info=None,
        interactive=True,
        **kwargs,
    ):
        super().__init__(
            minimum=minimum,
            maximum=maximum,
            value=value,
            step=step,
            label=label,
            info=info,
            interactive=interactive,
            **kwargs
        )

    def get_block_name(self):
        return "slider"