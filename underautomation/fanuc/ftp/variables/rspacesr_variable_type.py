import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RspacesrVariableType as rspacesr_variable_type

class RspacesrVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rspacesr_variable_type()
		else:
			self._instance = _internal
	@property
	def sr_enb_typ(self) -> typing.List[int]:
		return self._instance.SrEnbTyp
	@property
	def runner_axs(self) -> bool:
		return self._instance.RunnerAxs
	@property
	def hand_lngth(self) -> float:
		return self._instance.HandLngth
	@property
	def hand_thick(self) -> float:
		return self._instance.HandThick
	@property
	def flip_enb(self) -> bool:
		return self._instance.FlipEnb
	@property
	def intference(self) -> bool:
		return self._instance.Intference
	@property
	def hand_if_chk(self) -> bool:
		return self._instance.HandIfChk
	@property
	def handi_type(self) -> int:
		return self._instance.HandiType
	@property
	def handi_indx(self) -> int:
		return self._instance.HandiIndx
	@property
	def sr_g1pos(self) -> typing.List[float]:
		return self._instance.SrG1pos
	@property
	def sr_g1pos_in(self) -> typing.List[float]:
		return self._instance.SrG1posIn
	@property
	def sr_g1ang(self) -> typing.List[float]:
		return self._instance.SrG1ang
	@property
	def sr_g1ang_jf(self) -> typing.List[float]:
		return self._instance.SrG1angJf
	@property
	def sr_prm(self) -> typing.List[int]:
		return self._instance.SrPrm
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
