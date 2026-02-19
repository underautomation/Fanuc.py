import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PlstGrpVariableType as plst_grp_variable_type

class PlstGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type PLST_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plst_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def comment(self) -> str:
		'''Value of variable $COMMENT'''
		return self._instance.Comment

	@property
	def payload(self) -> float:
		'''Value of variable $PAYLOAD'''
		return self._instance.Payload

	@property
	def payload_x(self) -> float:
		'''Value of variable $PAYLOAD_X'''
		return self._instance.PayloadX

	@property
	def payload_y(self) -> float:
		'''Value of variable $PAYLOAD_Y'''
		return self._instance.PayloadY

	@property
	def payload_z(self) -> float:
		'''Value of variable $PAYLOAD_Z'''
		return self._instance.PayloadZ

	@property
	def payload_ix(self) -> float:
		'''Value of variable $PAYLOAD_IX'''
		return self._instance.PayloadIx

	@property
	def payload_iy(self) -> float:
		'''Value of variable $PAYLOAD_IY'''
		return self._instance.PayloadIy

	@property
	def payload_iz(self) -> float:
		'''Value of variable $PAYLOAD_IZ'''
		return self._instance.PayloadIz

	@property
	def icondisp(self) -> int:
		'''Value of variable $ICONDISP'''
		return self._instance.Icondisp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PlstGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
