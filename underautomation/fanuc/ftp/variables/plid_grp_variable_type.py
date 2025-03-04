import typing
from underautomation.fanuc.ftp.variables.max_pld_cal_variable_type import MaxPldCalVariableType
from underautomation.fanuc.ftp.variables.j3d_pld_cal_variable_type import J3dPldCalVariableType
from underautomation.fanuc.ftp.variables.calc_result_variable_type import CalcResultVariableType
from underautomation.fanuc.ftp.variables.armld_pos_variable_type import ArmldPosVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PlidGrpVariableType as plid_grp_variable_type

class PlidGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plid_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def pi_enb(self) -> int:
		return self._instance.PiEnb
	@property
	def payload(self) -> float:
		return self._instance.Payload
	@property
	def payload_x(self) -> float:
		return self._instance.PayloadX
	@property
	def payload_y(self) -> float:
		return self._instance.PayloadY
	@property
	def payload_z(self) -> float:
		return self._instance.PayloadZ
	@property
	def payload_ix(self) -> float:
		return self._instance.PayloadIx
	@property
	def payload_iy(self) -> float:
		return self._instance.PayloadIy
	@property
	def payload_iz(self) -> float:
		return self._instance.PayloadIz
	@property
	def armload1(self) -> float:
		return self._instance.Armload1
	@property
	def armload2(self) -> float:
		return self._instance.Armload2
	@property
	def armload3(self) -> float:
		return self._instance.Armload3
	@property
	def rob_type(self) -> int:
		return self._instance.RobType
	@property
	def data_num(self) -> int:
		return self._instance.DataNum
	@property
	def speed_high(self) -> int:
		return self._instance.SpeedHigh
	@property
	def speed_low(self) -> int:
		return self._instance.SpeedLow
	@property
	def defspd_high(self) -> int:
		return self._instance.DefspdHigh
	@property
	def defspd_low(self) -> int:
		return self._instance.DefspdLow
	@property
	def accel_high(self) -> int:
		return self._instance.AccelHigh
	@property
	def accel_low(self) -> int:
		return self._instance.AccelLow
	@property
	def defacc_high(self) -> int:
		return self._instance.DefaccHigh
	@property
	def defacc_low(self) -> int:
		return self._instance.DefaccLow
	@property
	def sample_time(self) -> int:
		return self._instance.SampleTime
	@property
	def sample_high(self) -> int:
		return self._instance.SampleHigh
	@property
	def sample_low(self) -> int:
		return self._instance.SampleLow
	@property
	def mov_axis(self) -> typing.List[bool]:
		return self._instance.MovAxis
	@property
	def mov_pos1(self) -> typing.List[float]:
		return self._instance.MovPos1
	@property
	def mov_pos2(self) -> typing.List[float]:
		return self._instance.MovPos2
	@property
	def mov_def1(self) -> typing.List[float]:
		return self._instance.MovDef1
	@property
	def mov_def2(self) -> typing.List[float]:
		return self._instance.MovDef2
	@property
	def rot_inertia(self) -> typing.List[float]:
		return self._instance.RotInertia
	@property
	def max_vel_hi(self) -> typing.List[float]:
		return self._instance.MaxVelHi
	@property
	def min_vel_hi(self) -> typing.List[float]:
		return self._instance.MinVelHi
	@property
	def max_acc_hi(self) -> typing.List[float]:
		return self._instance.MaxAccHi
	@property
	def min_acc_hi(self) -> typing.List[float]:
		return self._instance.MinAccHi
	@property
	def max_vel_low(self) -> typing.List[float]:
		return self._instance.MaxVelLow
	@property
	def min_vel_low(self) -> typing.List[float]:
		return self._instance.MinVelLow
	@property
	def max_acc_low(self) -> typing.List[float]:
		return self._instance.MaxAccLow
	@property
	def min_acc_low(self) -> typing.List[float]:
		return self._instance.MinAccLow
	@property
	def gamma(self) -> typing.List[float]:
		return self._instance.Gamma
	@property
	def stop_data(self) -> int:
		return self._instance.StopData
	@property
	def getdata_fin(self) -> int:
		return self._instance.GetdataFin
	@property
	def id_result(self) -> typing.List[float]:
		return self._instance.IdResult
	@property
	def calibrate(self) -> int:
		return self._instance.Calibrate
	@property
	def pi_debug(self) -> int:
		return self._instance.PiDebug
	@property
	def hidat_v_max(self) -> typing.List[float]:
		return self._instance.HidatVMax
	@property
	def hidat_v_mea(self) -> typing.List[float]:
		return self._instance.HidatVMea
	@property
	def hidat_a_max(self) -> typing.List[float]:
		return self._instance.HidatAMax
	@property
	def hidat_a_mea(self) -> typing.List[float]:
		return self._instance.HidatAMea
	@property
	def lwdat_v_max(self) -> typing.List[float]:
		return self._instance.LwdatVMax
	@property
	def lwdat_v_mea(self) -> typing.List[float]:
		return self._instance.LwdatVMea
	@property
	def lwdat_a_max(self) -> typing.List[float]:
		return self._instance.LwdatAMax
	@property
	def lwdat_a_mea(self) -> typing.List[float]:
		return self._instance.LwdatAMea
	@property
	def calc_type(self) -> int:
		return self._instance.CalcType
	@property
	def mtn_calctyp(self) -> int:
		return self._instance.MtnCalctyp
	@property
	def chker_ver(self) -> str:
		return self._instance.ChkerVer
	@property
	def pdck_rb_typ(self) -> int:
		return self._instance.PdckRbTyp
	@property
	def i_factor(self) -> typing.List[float]:
		return self._instance.IFactor
	@property
	def max_payload(self) -> float:
		return self._instance.MaxPayload
	@property
	def max_inertia(self) -> typing.List[float]:
		return self._instance.MaxInertia
	@property
	def max_moment(self) -> typing.List[float]:
		return self._instance.MaxMoment
	@property
	def comb_load(self) -> typing.List[float]:
		return self._instance.CombLoad
	@property
	def max_pld_cal(self) -> MaxPldCalVariableType:
		return MaxPldCalVariableType(self._instance.MaxPldCal)
	@property
	def j3d_pld_cal(self) -> typing.List[J3dPldCalVariableType]:
		return [J3dPldCalVariableType(x) for x in self._instance.J3dPldCal]
	@property
	def im_srch_dt(self) -> float:
		return self._instance.ImSrchDt
	@property
	def warn_disp(self) -> int:
		return self._instance.WarnDisp
	@property
	def warn_level(self) -> float:
		return self._instance.WarnLevel
	@property
	def over_level(self) -> float:
		return self._instance.OverLevel
	@property
	def calc_result(self) -> CalcResultVariableType:
		return CalcResultVariableType(self._instance.CalcResult)
	@property
	def pamswflg(self) -> int:
		return self._instance.Pamswflg
	@property
	def amld_scrn(self) -> int:
		return self._instance.AmldScrn
	@property
	def dummy100(self) -> int:
		return self._instance.Dummy100
	@property
	def mov_pos3(self) -> typing.List[float]:
		return self._instance.MovPos3
	@property
	def mov_pos4(self) -> typing.List[float]:
		return self._instance.MovPos4
	@property
	def mov_def3(self) -> typing.List[float]:
		return self._instance.MovDef3
	@property
	def mov_def4(self) -> typing.List[float]:
		return self._instance.MovDef4
	@property
	def pi3a_enb(self) -> int:
		return self._instance.Pi3aEnb
	@property
	def method(self) -> int:
		return self._instance.Method
	@property
	def pi3a_typ(self) -> int:
		return self._instance.Pi3aTyp
	@property
	def pi3a_axs(self) -> typing.List[int]:
		return self._instance.Pi3aAxs
	@property
	def fixed_ax(self) -> int:
		return self._instance.FixedAx
	@property
	def period(self) -> int:
		return self._instance.Period
	@property
	def sample3a(self) -> int:
		return self._instance.Sample3a
	@property
	def ref_pos(self) -> typing.List[float]:
		return self._instance.RefPos
	@property
	def def_ref(self) -> typing.List[float]:
		return self._instance.DefRef
	@property
	def ampl1(self) -> typing.List[float]:
		return self._instance.Ampl1
	@property
	def ampl2(self) -> typing.List[float]:
		return self._instance.Ampl2
	@property
	def def_ampl2(self) -> typing.List[float]:
		return self._instance.DefAmpl2
	@property
	def lim_ampl(self) -> typing.List[float]:
		return self._instance.LimAmpl
	@property
	def loop1(self) -> typing.List[int]:
		return self._instance.Loop1
	@property
	def loop2(self) -> typing.List[int]:
		return self._instance.Loop2
	@property
	def appr_len(self) -> int:
		return self._instance.ApprLen
	@property
	def flt_len1(self) -> typing.List[int]:
		return self._instance.FltLen1
	@property
	def flt_len2(self) -> typing.List[int]:
		return self._instance.FltLen2
	@property
	def rot_inrt3a(self) -> typing.List[float]:
		return self._instance.RotInrt3a
	@property
	def cond_def(self) -> typing.List[float]:
		return self._instance.CondDef
	@property
	def cond_num(self) -> typing.List[float]:
		return self._instance.CondNum
	@property
	def armload_x(self) -> typing.List[ArmldPosVariableType]:
		return [ArmldPosVariableType(x) for x in self._instance.ArmloadX]
	@property
	def armload_y(self) -> typing.List[ArmldPosVariableType]:
		return [ArmldPosVariableType(x) for x in self._instance.ArmloadY]
	@property
	def armload_z(self) -> typing.List[ArmldPosVariableType]:
		return [ArmldPosVariableType(x) for x in self._instance.ArmloadZ]
	@property
	def rang_mgn(self) -> float:
		return self._instance.RangMgn
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
