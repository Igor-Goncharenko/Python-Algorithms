from typing import Any


class BinNode:
    def __init__(self, val: Any) -> None:
        self.left: BinNode | None = None
        self.right: BinNode | None = None
        self.value: Any = val
