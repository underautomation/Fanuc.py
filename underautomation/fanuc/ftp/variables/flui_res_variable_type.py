import typing
from underautomation.fanuc.ftp.variables.vector_variable import VectorVariable
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FluiResVariableType as flui_res_variable_type

class FluiResVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = flui_res_variable_type()
		else:
			self._instance = _internal
	@property
	def navid(self) -> str:
		return self._instance.Navid
	@property
	def text(self) -> str:
		return self._instance.Text
	@property
	def result_type(self) -> int:
		return self._instance.ResultType
	@property
	def visited(self) -> int:
		return self._instance.Visited
	@property
	def scid(self) -> int:
		return self._instance.Scid
	@property
	def select_mask(self) -> int:
		return self._instance.SelectMask
	@property
	def vector(self) -> VectorVariable:
		return VectorVariable(self._instance.Vector)
	@property
	def number(self) -> int:
		return self._instance.Number
	@property
	def real_number(self) -> float:
		return self._instance.RealNumber
	@property
	def position(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Position)
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
