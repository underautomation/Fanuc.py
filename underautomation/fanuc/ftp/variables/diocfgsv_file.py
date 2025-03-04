import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DiocfgsvFile as diocfgsv_file

class DiocfgsvFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = diocfgsv_file()
		else:
			self._instance = _internal
	@property
	def cfg_file_ver(self) -> int:
		return self._instance.CfgFileVer
	@property
	def asg_log_pt(self) -> typing.List[int]:
		return self._instance.AsgLogPt
	@property
	def asg_log_pn(self) -> typing.List[int]:
		return self._instance.AsgLogPn
	@property
	def asg_n_pts(self) -> typing.List[int]:
		return self._instance.AsgNPts
	@property
	def asg_rack_no(self) -> typing.List[int]:
		return self._instance.AsgRackNo
	@property
	def asg_slot_no(self) -> typing.List[int]:
		return self._instance.AsgSlotNo
	@property
	def asg_phy_pt(self) -> typing.List[int]:
		return self._instance.AsgPhyPt
	@property
	def asg_phy_pn(self) -> typing.List[int]:
		return self._instance.AsgPhyPn
	@property
	def name_log_pt(self) -> typing.List[int]:
		return self._instance.NameLogPt
	@property
	def name_log_pn(self) -> typing.List[int]:
		return self._instance.NameLogPn
	@property
	def name_name(self) -> typing.List[str]:
		return self._instance.NameName
	@property
	def name_name2(self) -> typing.List[str]:
		return self._instance.NameName2
	@property
	def mode_log_pt(self) -> typing.List[int]:
		return self._instance.ModeLogPt
	@property
	def mode_frst_pn(self) -> typing.List[int]:
		return self._instance.ModeFrstPn
	@property
	def mode_last_pn(self) -> typing.List[int]:
		return self._instance.ModeLastPn
	@property
	def mode_mode(self) -> typing.List[int]:
		return self._instance.ModeMode
	@property
	def ais_rack_no(self) -> typing.List[int]:
		return self._instance.AisRackNo
	@property
	def ais_slot_no(self) -> typing.List[int]:
		return self._instance.AisSlotNo
	@property
	def ais_sequence(self) -> typing.List[str]:
		return self._instance.AisSequence
	@property
	def dev_rack(self) -> typing.List[int]:
		return self._instance.DevRack
	@property
	def dev_slot(self) -> typing.List[int]:
		return self._instance.DevSlot
	@property
	def dev_mod_id(self) -> typing.List[int]:
		return self._instance.DevModId
	@property
	def dev_data_type(self) -> typing.List[int]:
		return self._instance.DevDataType
	@property
	def dev_param1(self) -> typing.List[int]:
		return self._instance.DevParam1
	@property
	def dev_param2(self) -> typing.List[int]:
		return self._instance.DevParam2
	@property
	def dev_comment(self) -> typing.List[str]:
		return self._instance.DevComment
