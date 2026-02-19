import typing
from underautomation.fanuc.ftp.variables.det_io_variable_type import DetIoVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CondetIoVariableType as condet_io_variable_type

class CondetIoVariableType(GenericVariableType):
	'''Describes the Fanuc type CONDET_IO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = condet_io_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> int:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def req_mask(self) -> int:
		'''Value of variable $REQ_MASK'''
		return self._instance.ReqMask

	@property
	def used_msk(self) -> int:
		'''Value of variable $USED_MSK'''
		return self._instance.UsedMsk

	@property
	def io_data(self) -> typing.List[DetIoVariableType]:
		'''Value of variable $IO_DATA'''
		return [DetIoVariableType(x) for x in self._instance.IoData]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CondetIoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
