import functools
from typing import Any, Callable


################################################################################
# Cashes
class Cashes(object):
    def __init__(self):
        self._cashes = dict()

    @property
    def cashes(self) -> dict:
        return self._cashes

    def put(self, key: str, value: Any) -> None:
        self._cashes[key] = value

    def get(self, key: str) -> Any:
        return self._cashes.get(key)

    def clear(self):
        self._cashes = dict()


################################################################################
# LRU cashes
class LRUCashes(Cashes):
    def __init__(self, max_size: int = 128):
        super().__init__()
        self._max_size = max_size

    def put(self, key: str, value: Any) -> None:
        self._cashes[key] = value
        if len(self._cashes) > self._max_size:
            # remove first element (last) in the dictionary
            self._cashes.pop(list(self._cashes.keys())[0])

    def get(self, key: str) -> Any:
        value = self._cashes.get(key)
        if value is not None:
            # move item at the end of dictionary
            self._cashes[key] = self._cashes.pop(key)
        return value


def lru_cashes(max_size: int = 128) -> Callable:
    def inner(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = "key_" + "_".join(map(str, args)) + "_" + "_".join(map(str, kwargs.items()))
            result = inner.cashes.get(key)
            if result is None:
                result = func(*args, **kwargs)
                inner.cashes.put(key, result)
            return result

        return wrapper

    inner.cashes = LRUCashes(max_size=max_size)
    return inner


################################################################################
# LFU cashes
class LFUCashes(Cashes):
    def __init__(self, max_size: int = 128):
        super().__init__()
        self._max_size = max_size

    def put(self, key: str, value: Any) -> None:
        self._cashes[key] = value
        if len(self._cashes) > self._max_size:
            # remove first element (last) in the dictionary
            self._cashes.pop(list(self._cashes.keys())[0])

    def get(self, key: str) -> Any:
        # TODO: finish it later
        pass


################################################################################

