"""
Wraps module
============
    This module provides several tools for wrapping the result around the return.
    This part is inspired by Rust's `Result` wraps, which does a lot of interesting
    thins like is_ok or is_err. So, this is implemented here too

Classes
-------
1. Result
2. Ok
3. Err
"""


from typing import Any, Union, TypeVar, Type


Value         = TypeVar('Value')
GoodValueType = TypeVar('GoodValueType')
BadValueType  = TypeVar('BadValueType')


__all__ = (
    "Err",
    "Ok",
    "Result"
)


class Result(object):
    """

    """


    result: bool = False


    def __init__(self): ...


    def is_good(self) -> bool:
        return False


    def is_bad(self) -> bool:
        return False


    def unwrap(self) -> Union[Value: GoodValueType, Value: BadValueType]:
        ...


    def if_err(self, f: function, *args) -> Any:
        if not self.result:
            f(args)


    def __getitem__(self, good: Type, bad: Type) -> Union[GoodValueType, BadValueType]:
        ...


class Ok(Result):
    value: Any = None
    result: bool = True


    def __init__(self, value: Any):
        self.value = value


    def is_good(self) -> bool:
        return True


    def unwrap(self) -> Value:
        return self.value


class Err(Result):
    value: Any = None
    result: bool = True


    def __init__(self, value: Any):
        self.value = value


    def is_err(self) -> bool:
        return False


    def unwrap(self) -> Value:
        return self.value
