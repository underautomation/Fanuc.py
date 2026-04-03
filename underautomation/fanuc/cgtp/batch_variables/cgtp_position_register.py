from __future__ import annotations
import typing
from underautomation.fanuc.cgtp.batch_variables.i_cgtp_batch_variable import ICgtpBatchVariable
from underautomation.fanuc.common.position_register_with_comment import PositionRegisterWithComment
from UnderAutomation.Fanuc.Cgtp.BatchVariables import CgtpPositionRegister as cgtp_position_register

class CgtpPositionRegister(PositionRegisterWithComment, ICgtpBatchVariable):
	'''Represents a position register (PR[]) for batch read/write operations.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_position_register()
		else:
			self._instance = _internal

	@property
	def index(self) -> int:
		'''1-based index of the position register (second dimension of POSREG[group,index])'''
		return self._instance.Index

	@index.setter
	def index(self, value: int):
		self._instance.Index = value

	@property
	def group(self) -> int:
		'''Motion group number (first dimension of POSREG[group,index])'''
		return self._instance.Group

	@group.setter
	def group(self, value: int):
		self._instance.Group = value

	@property
	def u_tool(self) -> int:
		'''User tool number. -1 means unset (stored as 255 on the controller).'''
		return self._instance.UTool

	@u_tool.setter
	def u_tool(self, value: int):
		self._instance.UTool = value

	@property
	def u_frame(self) -> int:
		'''User frame number. -1 means unset (stored as 255 on the controller).'''
		return self._instance.UFrame

	@u_frame.setter
	def u_frame(self, value: int):
		self._instance.UFrame = value

	@property
	def axes(self) -> int:
		'''Number of axes'''
		return self._instance.Axes

	@axes.setter
	def axes(self, value: int):
		self._instance.Axes = value

	@property
	def name(self) -> str:
		return self._instance.Name

	@property
	def program(self) -> str:
		return self._instance.Program

	@property
	def string_value(self) -> str:
		return self._instance.StringValue

	@property
	def exists(self) -> bool:
		return self._instance.Exists

	@property
	def is_uninitialized(self) -> bool:
		return self._instance.IsUninitialized

	@property
	def is_read_only(self) -> bool:
		return self._instance.IsReadOnly

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpPositionRegister):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
