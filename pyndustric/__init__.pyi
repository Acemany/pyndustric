"""
A compiler from Python to Mindustry's assembly (logic programming language).

The language **is** Python, so all simple programs you can imagine are possible.
Beyond that, the supported "system calls" are documented in the `pyndustri.pyi` file.

To learn about the possible compiler errors, refer to the `ERR_` and `ERROR_DESCRIPTIONS`
constants in the `constants.py` file.
"""

from .constants import (ERR_COMPLEX_ASSIGN, ERR_COMPLEX_VALUE, ERR_UNSUPPORTED_OP, ERR_UNSUPPORTED_ITER, ERR_BAD_ITER_ARGS, ERR_UNSUPPORTED_IMPORT,
                        ERR_UNSUPPORTED_EXPR, ERR_UNSUPPORTED_SYSCALL, ERR_BAD_SYSCALL_ARGS, ERR_NESTED_DEF, ERR_INVALID_DEF, ERR_REDEF,
                        ERR_NO_DEF, ERR_ARGC_MISMATCH, ERR_TOO_LONG, ERR_INVALID_SOURCE, ERR_BAD_TUPLE_ASSIGN, INTERNAL_COMPILER_ERR,
                        ERROR_DESCRIPTIONS,
                        BIN_CMP, NEGATED_BIN_CMP, BIN_OPS, BUILTIN_DEFS, RADAR_ORDERS, ENV_MAP, RES_MAP,
                        ALLOWED_DECORATORS,
                        REG_STACK, REG_RET, REG_RET_COUNTER_PREFIX, REG_IT_FMT, REG_TMP_FMT,
                        MAX_INSTRUCTIONS)
from .compiler import Compiler, CompilerError
from .version import __version__

__all__ = [
    "ERR_COMPLEX_ASSIGN", "ERR_COMPLEX_VALUE", "ERR_UNSUPPORTED_OP", "ERR_UNSUPPORTED_ITER", "ERR_BAD_ITER_ARGS", "ERR_UNSUPPORTED_IMPORT",
    "ERR_UNSUPPORTED_EXPR", "ERR_UNSUPPORTED_SYSCALL", "ERR_BAD_SYSCALL_ARGS", "ERR_NESTED_DEF", "ERR_INVALID_DEF", "ERR_REDEF",
    "ERR_NO_DEF", "ERR_ARGC_MISMATCH", "ERR_TOO_LONG", "ERR_INVALID_SOURCE", "ERR_BAD_TUPLE_ASSIGN", "INTERNAL_COMPILER_ERR",
    "ERROR_DESCRIPTIONS",
    "BIN_CMP", "NEGATED_BIN_CMP", "BIN_OPS", "BUILTIN_DEFS", "RADAR_ORDERS", "ENV_MAP", "RES_MAP",
    "ALLOWED_DECORATORS",
    "REG_STACK", "REG_RET", "REG_RET_COUNTER_PREFIX", "REG_IT_FMT", "REG_TMP_FMT",
    "MAX_INSTRUCTIONS",
    "Compiler", "CompilerError",
    "__version__"
]
