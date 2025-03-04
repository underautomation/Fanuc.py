import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VtcpsetVariableType as vtcpset_variable_type

class VtcpsetVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vtcpset_variable_type()
		else:
			self._instance = _internal
	@property
	def move_dist_xy(self) -> float:
		return self._instance.MoveDistXy
	@property
	def move_dist_z(self) -> float:
		return self._instance.MoveDistZ
	@property
	def move_dist_r(self) -> float:
		return self._instance.MoveDistR
	@property
	def move_dist_w(self) -> float:
		return self._instance.MoveDistW
	@property
	def move_dist_p(self) -> float:
		return self._instance.MoveDistP
	@property
	def move_dist_fw(self) -> float:
		return self._instance.MoveDistFw
	@property
	def move_dist_fp(self) -> float:
		return self._instance.MoveDistFp
	@property
	def div_num_z(self) -> int:
		return self._instance.DivNumZ
	@property
	def div_num_r(self) -> int:
		return self._instance.DivNumR
	@property
	def div_num_wp(self) -> int:
		return self._instance.DivNumWp
	@property
	def div_num_fwp(self) -> int:
		return self._instance.DivNumFwp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
