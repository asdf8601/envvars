import os
from typing import Any, Type


class Var:
    __slots__ = [
        "key",
        "default",
        "dtype",
        "doc",
        "value",
    ]

    def __init__(
        self,
        key: str,
        value: Any = None,
        default: Any = None,
        dtype: Type = str,
        doc: str = "",
    ):
        self.key = key
        self.value = dtype(value)
        self.default = default
        self.dtype = dtype
        self.doc = doc

    def __str__(self) -> str:
        return f"{self.key}={self.value}, {self.doc}"

    def __hash__(self):
        return hash(self.key)


class EnvVars:
    """Class to handle environment variables.

    Examples
    --------
    >>> MYVAR = EnvVars.get("MYVAR", default="default", doc="doc")
    >>> print(EnvVars)
    === Environment variables:
        MYVAR=default, doc
    >>> EnvVars["MYVAR"]
    "default"

    """
    values: dict[str, Var] = {}
    header: str = "=== Environment variables:"

    def __init__(self, header=header):
        self.header = header

    @classmethod
    def get(
        cls,
        key: str,
        default: Any = None,
        dtype: Type = str,
        doc: str = "",
        strict: bool = False,
    ) -> Any:
        if strict and key not in os.environ:
            raise ValueError(f"Environment variable {key} is not set")
        value = os.getenv(key, default)
        value = dtype(value)
        cls.values[key] = Var(key, value, default, dtype, doc)
        return value

    @classmethod
    def str(cls) -> str:
        out = [cls.header]
        for _, value in cls.values.items():
            out += [f"    {value}"]
        return "\n".join(out)
