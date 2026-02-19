import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SnpxParamVariableType as snpx_param_variable_type

class SnpxParamVariableType(GenericVariableType):
	'''Describes the Fanuc type SNPX_PARAM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_param_variable_type()
		else:
			self._instance = _internal

	@property
	def timeout(self) -> int:
		'''Value of variable $TIMEOUT'''
		return self._instance.Timeout

	@property
	def snp_id(self) -> str:
		'''Value of variable $SNP_ID'''
		return self._instance.SnpId

	@property
	def num_asg(self) -> int:
		'''Value of variable $NUM_ASG'''
		return self._instance.NumAsg

	@property
	def num_cimp(self) -> int:
		'''Value of variable $NUM_CIMP'''
		return self._instance.NumCimp

	@property
	def num_frif(self) -> int:
		'''Value of variable $NUM_FRIF'''
		return self._instance.NumFrif

	@property
	def version(self) -> int:
		'''Value of variable $VERSION'''
		return self._instance.Version

	@property
	def status(self) -> int:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def disp_info(self) -> int:
		'''Value of variable $DISP_INFO'''
		return self._instance.DispInfo

	@property
	def modbus_adr(self) -> int:
		'''Value of variable $MODBUS_ADR'''
		return self._instance.ModbusAdr

	@property
	def num_modbus(self) -> int:
		'''Value of variable $NUM_MODBUS'''
		return self._instance.NumModbus

	@property
	def modbus_port(self) -> int:
		'''Value of variable $MODBUS_PORT'''
		return self._instance.ModbusPort

	@property
	def cmd_endian(self) -> int:
		'''Value of variable $CMD_ENDIAN'''
		return self._instance.CmdEndian

	@property
	def comp_flag(self) -> int:
		'''Value of variable $COMP_FLAG'''
		return self._instance.CompFlag

	@property
	def dummy13(self) -> int:
		'''Value of variable $DUMMY13'''
		return self._instance.Dummy13

	@property
	def dummy14(self) -> int:
		'''Value of variable $DUMMY14'''
		return self._instance.Dummy14

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SnpxParamVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
