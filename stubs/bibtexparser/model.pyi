import abc
from typing import Any

from _typeshed import Incomplete

class Block(abc.ABC):
    def __init__(
        self, start_line: int | None = None, raw: str | None = None, parser_metadata: dict[str, Any] | None = None
    ) -> None: ...
    @property
    def start_line(self) -> int | None: ...
    @property
    def raw(self) -> str | None: ...
    @property
    def parser_metadata(self) -> dict[str, Any]: ...
    def get_parser_metadata(self, key: str) -> Any | None: ...
    def set_parser_metadata(self, key: str, value: Any) -> None: ...
    def __eq__(self, other: Any) -> bool: ...

class String(Block):
    def __init__(self, key: str, value: str, start_line: int | None = None, raw: str | None = None) -> None: ...
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str) -> None: ...

class Preamble(Block):
    def __init__(self, value: str, start_line: int | None = None, raw: str | None = None) -> None: ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str) -> None: ...

class ExplicitComment(Block):
    def __init__(self, comment: str, start_line: int | None = None, raw: str | None = None) -> None: ...
    @property
    def comment(self) -> str: ...
    @comment.setter
    def comment(self, value: str) -> None: ...

class ImplicitComment(Block):
    def __init__(self, comment: str, start_line: int | None = None, raw: str | None = None) -> None: ...
    @property
    def comment(self) -> str: ...
    @comment.setter
    def comment(self, value: str) -> None: ...

class Field:
    def __init__(self, key: str, value: Any, start_line: int | None = None) -> None: ...
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...
    @property
    def value(self) -> Any: ...
    @value.setter
    def value(self, value: Any) -> None: ...
    @property
    def start_line(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...

class Entry(Block):
    def __init__(
        self, entry_type: str, key: str, fields: list[Field], start_line: int | None = None, raw: str | None = None
    ) -> None: ...
    @property
    def entry_type(self) -> str: ...
    @entry_type.setter
    def entry_type(self, value: str) -> None: ...
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...
    @property
    def fields(self) -> list[Field]: ...
    @fields.setter
    def fields(self, value: list[Field]) -> None: ...
    @property
    def fields_dict(self) -> dict[str, Field]: ...
    def set_field(self, field: Field) -> None: ...
    def pop(self, key: str, default: Incomplete | None = None) -> Field | None: ...
    def get(self, key: str, default: Incomplete | None = None) -> Field | None: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def items(self) -> list[tuple[str, str | Any]]: ...

class ParsingFailedBlock(Block):
    def __init__(
        self,
        error: Exception,
        start_line: int | None = None,
        raw: str | None = None,
        ignore_error_block: Block | None = None,
    ) -> None: ...
    @property
    def error(self) -> Exception: ...
    @property
    def ignore_error_block(self) -> Block | None: ...

class MiddlewareErrorBlock(ParsingFailedBlock):
    def __init__(self, block: Block, error: Exception) -> None: ...

class DuplicateBlockKeyBlock(ParsingFailedBlock):
    def __init__(
        self,
        key: str,
        previous_block: Block,
        duplicate_block: Block,
        start_line: int | None = None,
        raw: str | None = None,
    ) -> None: ...
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...
    @property
    def previous_block(self) -> Block: ...

class DuplicateFieldKeyBlock(ParsingFailedBlock):
    def __init__(self, duplicate_keys: set[str], entry: Entry) -> None: ...
    @property
    def duplicate_keys(self) -> set[str]: ...