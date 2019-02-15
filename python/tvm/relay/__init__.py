# pylint: disable=wildcard-import, redefined-builtin, invalid-name
"""The Relay IR namespace containing the IR definition and compiler."""
from __future__ import absolute_import
from ..api import register_func
from . import base
from . import ty
from . import expr
from . import expr_functor
from . import module
from . import ir_pass
from .build_module import build, build_config, create_executor, optimize
from . import parser
from . import debug

# Root operators
from .op import Op
from .op.reduce import *
from .op.tensor import *
from .op.transform import *
from . import nn
from . import annotation
from . import vision
from . import image
from . import frontend
from . import backend
from . import quantize

from .scope_builder import ScopeBuilder

# Span
Span = base.Span

# Env
Module = module.Module

# Type
Type = ty.Type
TupleType = ty.TupleType
TensorType = ty.TensorType
Kind = ty.Kind
TypeVar = ty.TypeVar
TypeConstraint = ty.TypeConstraint
FuncType = ty.FuncType
TypeRelation = ty.TypeRelation
IncompleteType = ty.IncompleteType
scalar_type = ty.scalar_type
RefType = ty.RefType

# Expr
Expr = expr.Expr
Constant = expr.Constant
Tuple = expr.Tuple
Var = expr.Var
GlobalVar = expr.GlobalVar
Function = expr.Function
Call = expr.Call
Let = expr.Let
If = expr.If
TupleGetItem = expr.TupleGetItem
RefCreate = expr.RefCreate
RefRead = expr.RefRead
RefWrite = expr.RefWrite

# helper functions
var = expr.var
const = expr.const
bind = expr.bind

# ExprFunctor
ExprFunctor = expr_functor.ExprFunctor
ExprMutator = expr_functor.ExprMutator

# Parser
fromtext = parser.fromtext
