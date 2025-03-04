import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import IoDefAsgVariableType as io_def_asg_variable_type

class IoDefAsgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_def_asg_variable_type()
		else:
			self._instance = _internal
	@property
	def log_type(self) -> int:
		return self._instance.LogType
	@property
	def log_no(self) -> int:
		return self._instance.LogNo
	@property
	def num_ports(self) -> int:
		return self._instance.NumPorts
	@property
	def rack(self) -> int:
		return self._instance.Rack
	@property
	def slot(self) -> int:
		return self._instance.Slot
	@property
	def phy_type(self) -> int:
		return self._instance.PhyType
	@property
	def phy_no(self) -> int:
		return self._instance.PhyNo
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
