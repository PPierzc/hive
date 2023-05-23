"""
Custom spinner for the Hive project.
A bee 🐝 spinning in a circle around a honey pot 🍯.
"""
from typing import List, Optional, Union, cast

from rich.console import Console, RenderableType
from rich.live import Live
from rich.spinner import Spinner
from rich.status import Status
from rich.style import StyleType
from rich.text import Text


class BeeSpinner(Spinner):
    def __init__(
        self,
        text: "RenderableType" = "",
        *,
        style: Optional["StyleType"] = None,
        speed: float = 1.0,
    ) -> None:
        spinner = {
            "interval": 20,
            "frames": [
                "🐝  ",
                " 🐝 ",
                "  🐝",
                " 🐝 ",
            ],
        }
        self.text: "Union[RenderableType, Text]" = (
            Text.from_markup(text) if isinstance(text, str) else text
        )
        self.frames = cast(List[str], spinner["frames"])[:]
        self.interval = cast(float, spinner["interval"])
        self.start_time: Optional[float] = None
        self.style = style
        self.speed = speed
        self.frame_no_offset: float = 0.0
        self._update_speed = 0.0


class BeeStatus(Status):
    def __init__(
        self,
        status: RenderableType,
        *,
        console: Optional[Console] = None,
        spinner_style: StyleType = "status.spinner",
        speed: float = 1.0,
        refresh_per_second: float = 12.5,
    ):
        self.status = status
        self.spinner_style = spinner_style
        self.speed = speed
        self._spinner = BeeSpinner(text=status, style=spinner_style, speed=speed)
        self._live = Live(
            self.renderable,
            console=console,
            refresh_per_second=refresh_per_second,
            transient=True,
        )
