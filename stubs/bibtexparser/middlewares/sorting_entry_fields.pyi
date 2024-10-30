from .middleware import BlockMiddleware as BlockMiddleware
from bibtexparser.library import Library as Library
from bibtexparser.model import Block as Block, Entry as Entry
from typing import Tuple

class SortFieldsAlphabeticallyMiddleware(BlockMiddleware):
    def __init__(self, allow_inplace_modification: bool = True) -> None: ...
    def transform_entry(self, entry: Entry, library: Library) -> Block: ...
    @classmethod
    def metadata_key(cls) -> str: ...

class SortFieldsCustomMiddleware(BlockMiddleware):
    def __init__(
        self, order: Tuple[str, ...], case_sensitive: bool = False, allow_inplace_modification: bool = True
    ) -> None: ...
    def transform_entry(self, entry: Entry, library: Library) -> Block: ...
    @classmethod
    def metadata_key(cls) -> str: ...
