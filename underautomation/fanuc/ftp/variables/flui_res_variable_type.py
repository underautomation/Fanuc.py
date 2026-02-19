import typing
from underautomation.fanuc.ftp.variables.vector_variable import VectorVariable
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FluiResVariableType as flui_res_variable_type

class FluiResVariableType(GenericVariableType):
	'''Describes the Fanuc type FLUI_RES_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = flui_res_variable_type()
		else:
			self._instance = _internal

	@property
	def navid(self) -> str:
		'''Value of variable $NAVID'''
		return self._instance.Navid

	@property
	def text(self) -> str:
		'''Value of variable $TEXT'''
		return self._instance.Text

	@property
	def result_type(self) -> int:
		'''Value of variable $RESULT_TYPE'''
		return self._instance.ResultType

	@property
	def visited(self) -> int:
		'''Value of variable $VISITED'''
		return self._instance.Visited

	@property
	def scid(self) -> int:
		'''Value of variable $SCID'''
		return self._instance.Scid

	@property
	def select_mask(self) -> int:
		'''Value of variable $SELECT_MASK'''
		return self._instance.SelectMask

	@property
	def vector(self) -> VectorVariable:
		'''Value of variable $VECTOR'''
		return VectorVariable(self._instance.Vector)

	@property
	def number(self) -> int:
		'''Value of variable $NUMBER'''
		return self._instance.Number

	@property
	def real_number(self) -> float:
		'''Value of variable $REAL_NUMBER'''
		return self._instance.RealNumber

	@property
	def position(self) -> CartesianPositionVariable:
		'''Value of variable $POSITION'''
		return CartesianPositionVariable(self._instance.Position)

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FluiResVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
