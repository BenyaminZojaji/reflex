"""Progress."""

from __future__ import annotations

from types import SimpleNamespace
from typing import Optional

from reflex.components.component import Component
from reflex.components.radix.primitives.accordion import DEFAULT_ANIMATION_DURATION
from reflex.components.radix.primitives.base import RadixPrimitiveComponentWithClassName
from reflex.style import Style
from reflex.vars import Var


class ProgressComponent(RadixPrimitiveComponentWithClassName):
    """A Progress component."""

    library = "@radix-ui/react-progress@^1.0.3"


class ProgressRoot(ProgressComponent):
    """The Progress Root component."""

    tag = "Root"
    alias = "RadixProgressRoot"

    # The current progress value.
    value: Var[Optional[int]]

    # The maximum progress value.
    max: Var[int]

    def _apply_theme(self, theme: Component):
        self.style = Style(
            {
                "position": "relative",
                "overflow": "hidden",
                "background": "var(--gray-a3)",
                "border_radius": "99999px",
                "width": "100%",
                "height": "20px",
                "boxShadow": "inset 0 0 0 1px var(--gray-a5)",
                **self.style,
            }
        )


class ProgressIndicator(ProgressComponent):
    """The Progress bar indicator."""

    tag = "Indicator"

    alias = "RadixProgressIndicator"

    # The current progress value.
    value: Var[Optional[int]]

    def _apply_theme(self, theme: Component):
        self.style = Style(
            {
                "background-color": "var(--accent-9)",
                "width": "100%",
                "height": "100%",
                f"transition": f"transform {DEFAULT_ANIMATION_DURATION}ms linear",
                "&[data_state='loading']": {
                    "transition": f"transform {DEFAULT_ANIMATION_DURATION}ms linear",
                },
                "transform": f"translateX(calc(-100% + {self.value}%))",  # type: ignore
                "boxShadow": "inset 0 0 0 1px var(--gray-a5)",
            }
        )


class Progress(SimpleNamespace):
    """High level API for progress bar."""

    root = staticmethod(ProgressRoot.create)
    indicator = staticmethod(ProgressIndicator.create)

    @staticmethod
    def __call__(width: Optional[str] = "100%", **props) -> Component:
        """High level API for progress bar.

        Args:
            **props: The props of the progress bar

        Returns:
            The progress bar.
        """
        return ProgressRoot.create(
            ProgressIndicator.create(width=width, value=props.get("value")),
            **props,
        )


progress = Progress()
