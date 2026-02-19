import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import IoDefAsgVariableType as io_def_asg_variable_type

class IoDefAsgVariableType(GenericVariableType):
	'''Describes the Fanuc type IO_DEF_ASG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_def_asg_variable_type()
		else:
			self._instance = _internal

	@property
	def log_type(self) -> int:
		'''Value of variable $LOG_TYPE'''
		return self._instance.LogType

	@property
	def log_no(self) -> int:
		'''Value of variable $LOG_NO'''
		return self._instance.LogNo

	@property
	def num_ports(self) -> int:
		'''Value of variable $NUM_PORTS'''
		return self._instance.NumPorts

	@property
	def rack(self) -> int:
		'''Value of variable $RACK'''
		return self._instance.Rack

	@property
	def slot(self) -> int:
		'''Value of variable $SLOT'''
		return self._instance.Slot

	@property
	def phy_type(self) -> int:
		'''Value of variable $PHY_TYPE'''
		return self._instance.PhyType

	@property
	def phy_no(self) -> int:
		'''Value of variable $PHY_NO'''
		return self._instance.PhyNo

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoDefAsgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
