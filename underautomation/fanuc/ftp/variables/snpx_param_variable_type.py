import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SnpxParamVariableType as snpx_param_variable_type

class SnpxParamVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_param_variable_type()
		else:
			self._instance = _internal
	@property
	def timeout(self) -> int:
		return self._instance.Timeout
	@property
	def snp_id(self) -> str:
		return self._instance.SnpId
	@property
	def num_asg(self) -> int:
		return self._instance.NumAsg
	@property
	def num_cimp(self) -> int:
		return self._instance.NumCimp
	@property
	def num_frif(self) -> int:
		return self._instance.NumFrif
	@property
	def version(self) -> int:
		return self._instance.Version
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def disp_info(self) -> int:
		return self._instance.DispInfo
	@property
	def modbus_adr(self) -> int:
		return self._instance.ModbusAdr
	@property
	def num_modbus(self) -> int:
		return self._instance.NumModbus
	@property
	def modbus_port(self) -> int:
		return self._instance.ModbusPort
	@property
	def cmd_endian(self) -> int:
		return self._instance.CmdEndian
	@property
	def comp_flag(self) -> int:
		return self._instance.CompFlag
	@property
	def dummy13(self) -> int:
		return self._instance.Dummy13
	@property
	def dummy14(self) -> int:
		return self._instance.Dummy14
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
