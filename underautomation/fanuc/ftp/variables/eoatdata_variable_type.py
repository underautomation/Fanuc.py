import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import EoatdataVariableType as eoatdata_variable_type

class EoatdataVariableType(GenericVariableType):
	'''Describes the Fanuc type EOATDATA_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = eoatdata_variable_type()
		else:
			self._instance = _internal

	@property
	def id(self) -> int:
		'''Value of variable $ID'''
		return self._instance.Id

	@property
	def name(self) -> str:
		'''Value of variable $NAME'''
		return self._instance.Name

	@property
	def zone(self) -> int:
		'''Value of variable $ZONE'''
		return self._instance.Zone

	@property
	def type(self) -> int:
		'''Value of variable $TYPE'''
		return self._instance.Type

	@property
	def io_ugrp_typ(self) -> int:
		'''Value of variable $IO_UGRP_TYP'''
		return self._instance.IoUgrpTyp

	@property
	def io_ugrp_prt(self) -> int:
		'''Value of variable $IO_UGRP_PRT'''
		return self._instance.IoUgrpPrt

	@property
	def io_ugrp_cnd(self) -> int:
		'''Value of variable $IO_UGRP_CND'''
		return self._instance.IoUgrpCnd

	@property
	def io_grp_typ(self) -> int:
		'''Value of variable $IO_GRP_TYP'''
		return self._instance.IoGrpTyp

	@property
	def io_grp_prt(self) -> int:
		'''Value of variable $IO_GRP_PRT'''
		return self._instance.IoGrpPrt

	@property
	def io_grp_cnd(self) -> int:
		'''Value of variable $IO_GRP_CND'''
		return self._instance.IoGrpCnd

	@property
	def group_num(self) -> int:
		'''Value of variable $GROUP_NUM'''
		return self._instance.GroupNum

	@property
	def axis_num(self) -> int:
		'''Value of variable $AXIS_NUM'''
		return self._instance.AxisNum

	@property
	def sv_sched(self) -> int:
		'''Value of variable $SV_SCHED'''
		return self._instance.SvSched

	@property
	def mn_ugrp_typ(self) -> int:
		'''Value of variable $MN_UGRP_TYP'''
		return self._instance.MnUgrpTyp

	@property
	def mn_ugrp_prt(self) -> int:
		'''Value of variable $MN_UGRP_PRT'''
		return self._instance.MnUgrpPrt

	@property
	def mn_ugrp_cnd(self) -> int:
		'''Value of variable $MN_UGRP_CND'''
		return self._instance.MnUgrpCnd

	@property
	def mn_grp_typ(self) -> int:
		'''Value of variable $MN_GRP_TYP'''
		return self._instance.MnGrpTyp

	@property
	def mn_grp_prt(self) -> int:
		'''Value of variable $MN_GRP_PRT'''
		return self._instance.MnGrpPrt

	@property
	def mn_grp_cnd(self) -> int:
		'''Value of variable $MN_GRP_CND'''
		return self._instance.MnGrpCnd

	@property
	def ugrp_thrsh(self) -> float:
		'''Value of variable $UGRP_THRSH'''
		return self._instance.UgrpThrsh

	@property
	def grp_thrsh(self) -> float:
		'''Value of variable $GRP_THRSH'''
		return self._instance.GrpThrsh

	@property
	def maint_cycle(self) -> int:
		'''Value of variable $MAINT_CYCLE'''
		return self._instance.MaintCycle

	@property
	def maint_thrsh(self) -> float:
		'''Value of variable $MAINT_THRSH'''
		return self._instance.MaintThrsh

	@property
	def ugrp_time(self) -> float:
		'''Value of variable $UGRP_TIME'''
		return self._instance.UgrpTime

	@property
	def grp_time(self) -> float:
		'''Value of variable $GRP_TIME'''
		return self._instance.GrpTime

	@property
	def detect_dly(self) -> int:
		'''Value of variable $DETECT_DLY'''
		return self._instance.DetectDly

	@property
	def drop_cnt(self) -> int:
		'''Value of variable $DROP_CNT'''
		return self._instance.DropCnt

	@property
	def cycle_cnt(self) -> int:
		'''Value of variable $CYCLE_CNT'''
		return self._instance.CycleCnt

	@property
	def day_thrsh(self) -> int:
		'''Value of variable $DAY_THRSH'''
		return self._instance.DayThrsh

	@property
	def hour_thrsh(self) -> int:
		'''Value of variable $HOUR_THRSH'''
		return self._instance.HourThrsh

	@property
	def total_thrsh(self) -> int:
		'''Value of variable $TOTAL_THRSH'''
		return self._instance.TotalThrsh

	@property
	def grp_timout(self) -> bool:
		'''Value of variable $GRP_TIMOUT'''
		return self._instance.GrpTimout

	@property
	def ugrp_timout(self) -> bool:
		'''Value of variable $UGRP_TIMOUT'''
		return self._instance.UgrpTimout

	@property
	def enabled(self) -> bool:
		'''Value of variable $ENABLED'''
		return self._instance.Enabled

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, EoatdataVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
