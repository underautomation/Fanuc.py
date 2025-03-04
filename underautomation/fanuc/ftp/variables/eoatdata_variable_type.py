import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import EoatdataVariableType as eoatdata_variable_type

class EoatdataVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = eoatdata_variable_type()
		else:
			self._instance = _internal
	@property
	def id(self) -> int:
		return self._instance.Id
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def zone(self) -> int:
		return self._instance.Zone
	@property
	def type(self) -> int:
		return self._instance.Type
	@property
	def io_ugrp_typ(self) -> int:
		return self._instance.IoUgrpTyp
	@property
	def io_ugrp_prt(self) -> int:
		return self._instance.IoUgrpPrt
	@property
	def io_ugrp_cnd(self) -> int:
		return self._instance.IoUgrpCnd
	@property
	def io_grp_typ(self) -> int:
		return self._instance.IoGrpTyp
	@property
	def io_grp_prt(self) -> int:
		return self._instance.IoGrpPrt
	@property
	def io_grp_cnd(self) -> int:
		return self._instance.IoGrpCnd
	@property
	def group_num(self) -> int:
		return self._instance.GroupNum
	@property
	def axis_num(self) -> int:
		return self._instance.AxisNum
	@property
	def sv_sched(self) -> int:
		return self._instance.SvSched
	@property
	def mn_ugrp_typ(self) -> int:
		return self._instance.MnUgrpTyp
	@property
	def mn_ugrp_prt(self) -> int:
		return self._instance.MnUgrpPrt
	@property
	def mn_ugrp_cnd(self) -> int:
		return self._instance.MnUgrpCnd
	@property
	def mn_grp_typ(self) -> int:
		return self._instance.MnGrpTyp
	@property
	def mn_grp_prt(self) -> int:
		return self._instance.MnGrpPrt
	@property
	def mn_grp_cnd(self) -> int:
		return self._instance.MnGrpCnd
	@property
	def ugrp_thrsh(self) -> float:
		return self._instance.UgrpThrsh
	@property
	def grp_thrsh(self) -> float:
		return self._instance.GrpThrsh
	@property
	def maint_cycle(self) -> int:
		return self._instance.MaintCycle
	@property
	def maint_thrsh(self) -> float:
		return self._instance.MaintThrsh
	@property
	def ugrp_time(self) -> float:
		return self._instance.UgrpTime
	@property
	def grp_time(self) -> float:
		return self._instance.GrpTime
	@property
	def detect_dly(self) -> int:
		return self._instance.DetectDly
	@property
	def drop_cnt(self) -> int:
		return self._instance.DropCnt
	@property
	def cycle_cnt(self) -> int:
		return self._instance.CycleCnt
	@property
	def day_thrsh(self) -> int:
		return self._instance.DayThrsh
	@property
	def hour_thrsh(self) -> int:
		return self._instance.HourThrsh
	@property
	def total_thrsh(self) -> int:
		return self._instance.TotalThrsh
	@property
	def grp_timout(self) -> bool:
		return self._instance.GrpTimout
	@property
	def ugrp_timout(self) -> bool:
		return self._instance.UgrpTimout
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
