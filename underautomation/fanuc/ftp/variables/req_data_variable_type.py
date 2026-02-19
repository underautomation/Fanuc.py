import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ReqDataVariableType as req_data_variable_type

class ReqDataVariableType(GenericVariableType):
	'''Describes the Fanuc type REQ_DATA_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = req_data_variable_type()
		else:
			self._instance = _internal

	@property
	def err_type(self) -> int:
		'''Value of variable $ERR_TYPE'''
		return self._instance.ErrType

	@property
	def err_grp(self) -> int:
		'''Value of variable $ERR_GRP'''
		return self._instance.ErrGrp

	@property
	def err_axis(self) -> int:
		'''Value of variable $ERR_AXIS'''
		return self._instance.ErrAxis

	@property
	def axis_type(self) -> bool:
		'''Value of variable $AXIS_TYPE'''
		return self._instance.AxisType

	@property
	def error_dist(self) -> float:
		'''Value of variable $ERROR_DIST'''
		return self._instance.ErrorDist

	@property
	def err_time(self) -> int:
		'''Value of variable $ERR_TIME'''
		return self._instance.ErrTime

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ReqDataVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
