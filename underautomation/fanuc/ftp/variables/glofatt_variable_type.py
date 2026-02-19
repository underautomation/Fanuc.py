import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import GlofattVariableType as glofatt_variable_type

class GlofattVariableType(GenericVariableType):
	'''Describes the Fanuc type GLOFATT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = glofatt_variable_type()
		else:
			self._instance = _internal

	@property
	def device(self) -> str:
		'''Value of variable $DEVICE'''
		return self._instance.Device

	@property
	def name(self) -> str:
		'''Value of variable $NAME'''
		return self._instance.Name

	@property
	def ext(self) -> str:
		'''Value of variable $EXT'''
		return self._instance.Ext

	@property
	def taskid(self) -> int:
		'''Value of variable $TASKID'''
		return self._instance.Taskid

	@property
	def mode(self) -> int:
		'''Value of variable $MODE'''
		return self._instance.Mode

	@property
	def tskfnum(self) -> int:
		'''Value of variable $TSKFNUM'''
		return self._instance.Tskfnum

	@property
	def fileptr(self) -> int:
		'''Value of variable $FILEPTR'''
		return self._instance.Fileptr

	@property
	def kfile(self) -> int:
		'''Value of variable $KFILE'''
		return self._instance.Kfile

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GlofattVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
