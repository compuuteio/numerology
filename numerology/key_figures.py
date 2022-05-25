from dataclasses import dataclass
from typing import Dict, List, Union


class KeyFigures:
    _key_figures: Dict[str, Union[None, int, List[int], str, List[str]]] = {}

    def __iter__(self):
        for k, v in self._key_figures.items():
            yield (k, v)

    def set(self, key: str, value: Union[None, int, List[int], str, List[str]]):
        self._key_figures[key] = value

    @property
    def all(self) -> Dict:
        return self._key_figures

    @property
    def get(self, key: str) -> Union[None, int, List[int], str, List[str]]:
        return self._key_figures.get(key=key)


if __name__ == "__main__":
    ...
    # test = KeyFigures()
    # test.set("a_key", "a_value")
    # print(f"{[t for t in test]}")
