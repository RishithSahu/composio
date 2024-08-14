import typing as t

from composio.tools.local.base import Action, Tool

from .actions import Notify, ScreenCapture, TakeUserInput


class SystemTools(Tool):
    """
    System Tools for LLM
    """

    def actions(self) -> list[t.Type[Action]]:
        return [ScreenCapture, Notify, TakeUserInput]

    def triggers(self) -> list:
        return []
