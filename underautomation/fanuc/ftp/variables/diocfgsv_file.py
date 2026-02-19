import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import DiocfgsvFile as diocfgsv_file

class DiocfgsvFile(GenericVariableFile):
	'''Describes the Fanuc variable file diocfgsv.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = diocfgsv_file()
		else:
			self._instance = _internal

	@property
	def cfg_file_ver(self) -> int:
		'''Value of variable CFG_FILE_VER'''
		return self._instance.CfgFileVer

	@property
	def asg_log_pt(self) -> typing.List[int]:
		'''Value of variable ASG_LOG_PT'''
		return self._instance.AsgLogPt

	@property
	def asg_log_pn(self) -> typing.List[int]:
		'''Value of variable ASG_LOG_PN'''
		return self._instance.AsgLogPn

	@property
	def asg_n_pts(self) -> typing.List[int]:
		'''Value of variable ASG_N_PTS'''
		return self._instance.AsgNPts

	@property
	def asg_rack_no(self) -> typing.List[int]:
		'''Value of variable ASG_RACK_NO'''
		return self._instance.AsgRackNo

	@property
	def asg_slot_no(self) -> typing.List[int]:
		'''Value of variable ASG_SLOT_NO'''
		return self._instance.AsgSlotNo

	@property
	def asg_phy_pt(self) -> typing.List[int]:
		'''Value of variable ASG_PHY_PT'''
		return self._instance.AsgPhyPt

	@property
	def asg_phy_pn(self) -> typing.List[int]:
		'''Value of variable ASG_PHY_PN'''
		return self._instance.AsgPhyPn

	@property
	def name_log_pt(self) -> typing.List[int]:
		'''Value of variable NAME_LOG_PT'''
		return self._instance.NameLogPt

	@property
	def name_log_pn(self) -> typing.List[int]:
		'''Value of variable NAME_LOG_PN'''
		return self._instance.NameLogPn

	@property
	def name_name(self) -> typing.List[str]:
		'''Value of variable NAME_NAME'''
		return self._instance.NameName

	@property
	def name_name2(self) -> typing.List[str]:
		'''Value of variable NAME_NAME2'''
		return self._instance.NameName2

	@property
	def mode_log_pt(self) -> typing.List[int]:
		'''Value of variable MODE_LOG_PT'''
		return self._instance.ModeLogPt

	@property
	def mode_frst_pn(self) -> typing.List[int]:
		'''Value of variable MODE_FRST_PN'''
		return self._instance.ModeFrstPn

	@property
	def mode_last_pn(self) -> typing.List[int]:
		'''Value of variable MODE_LAST_PN'''
		return self._instance.ModeLastPn

	@property
	def mode_mode(self) -> typing.List[int]:
		'''Value of variable MODE_MODE'''
		return self._instance.ModeMode

	@property
	def ais_rack_no(self) -> typing.List[int]:
		'''Value of variable AIS_RACK_NO'''
		return self._instance.AisRackNo

	@property
	def ais_slot_no(self) -> typing.List[int]:
		'''Value of variable AIS_SLOT_NO'''
		return self._instance.AisSlotNo

	@property
	def ais_sequence(self) -> typing.List[str]:
		'''Value of variable AIS_SEQUENCE'''
		return self._instance.AisSequence

	@property
	def dev_rack(self) -> typing.List[int]:
		'''Value of variable DEV_RACK'''
		return self._instance.DevRack

	@property
	def dev_slot(self) -> typing.List[int]:
		'''Value of variable DEV_SLOT'''
		return self._instance.DevSlot

	@property
	def dev_mod_id(self) -> typing.List[int]:
		'''Value of variable DEV_MOD_ID'''
		return self._instance.DevModId

	@property
	def dev_data_type(self) -> typing.List[int]:
		'''Value of variable DEV_DATA_TYPE'''
		return self._instance.DevDataType

	@property
	def dev_param1(self) -> typing.List[int]:
		'''Value of variable DEV_PARAM1'''
		return self._instance.DevParam1

	@property
	def dev_param2(self) -> typing.List[int]:
		'''Value of variable DEV_PARAM2'''
		return self._instance.DevParam2

	@property
	def dev_comment(self) -> typing.List[str]:
		'''Value of variable DEV_COMMENT'''
		return self._instance.DevComment

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DiocfgsvFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
