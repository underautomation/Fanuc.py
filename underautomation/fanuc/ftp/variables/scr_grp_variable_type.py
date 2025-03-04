import typing
from underautomation.fanuc.common.configuration import Configuration
from underautomation.fanuc.ftp.variables.ax_ofs_variable_type import AxOfsVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ScrGrpVariableType as scr_grp_variable_type

class ScrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = scr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def arm_type(self) -> int:
		return self._instance.ArmType
	@property
	def dummy127(self) -> int:
		return self._instance.Dummy127
	@property
	def arm_type_b(self) -> int:
		return self._instance.ArmTypeB
	@property
	def num_axes(self) -> int:
		return self._instance.NumAxes
	@property
	def num_rob_axs(self) -> int:
		return self._instance.NumRobAxs
	@property
	def num_red_axs(self) -> int:
		return self._instance.NumRedAxs
	@property
	def wrst_axis_s(self) -> int:
		return self._instance.WrstAxisS
	@property
	def wrst_axis_e(self) -> int:
		return self._instance.WrstAxisE
	@property
	def sync_m_axis(self) -> int:
		return self._instance.SyncMAxis
	@property
	def sync_s_axis(self) -> int:
		return self._instance.SyncSAxis
	@property
	def wrist_type(self) -> int:
		return self._instance.WristType
	@property
	def hw_strt_axs(self) -> int:
		return self._instance.HwStrtAxs
	@property
	def axisorder(self) -> typing.List[int]:
		return self._instance.Axisorder
	@property
	def dummy128(self) -> int:
		return self._instance.Dummy128
	@property
	def brk_number(self) -> typing.List[int]:
		return self._instance.BrkNumber
	@property
	def dummy129(self) -> int:
		return self._instance.Dummy129
	@property
	def dd_motor(self) -> typing.List[bool]:
		return self._instance.DdMotor
	@property
	def rotary_axs(self) -> typing.List[bool]:
		return self._instance.RotaryAxs
	@property
	def loadratio(self) -> typing.List[float]:
		return self._instance.Loadratio
	@property
	def config_mask(self) -> Configuration:
		return Configuration(None, None, None, None, None, None, None, self._instance.ConfigMask)
	@property
	def link_length(self) -> typing.List[float]:
		return self._instance.LinkLength
	@property
	def ext_order(self) -> typing.List[int]:
		return self._instance.ExtOrder
	@property
	def dummy130(self) -> int:
		return self._instance.Dummy130
	@property
	def ext_xyz_map(self) -> typing.List[int]:
		return self._instance.ExtXyzMap
	@property
	def dummy131(self) -> int:
		return self._instance.Dummy131
	@property
	def ext_offset(self) -> typing.List[float]:
		return self._instance.ExtOffset
	@property
	def ext_length(self) -> typing.List[float]:
		return self._instance.ExtLength
	@property
	def robot_id(self) -> str:
		return self._instance.RobotId
	@property
	def robot_model(self) -> str:
		return self._instance.RobotModel
	@property
	def robot_file(self) -> str:
		return self._instance.RobotFile
	@property
	def robot_int(self) -> int:
		return self._instance.RobotInt
	@property
	def sv_code_id(self) -> str:
		return self._instance.SvCodeId
	@property
	def joglim_jnt(self) -> typing.List[int]:
		return self._instance.JoglimJnt
	@property
	def coord_mask(self) -> int:
		return self._instance.CoordMask
	@property
	def op_brk_num(self) -> typing.List[int]:
		return self._instance.OpBrkNum
	@property
	def dummy132(self) -> int:
		return self._instance.Dummy132
	@property
	def use_tbjnt(self) -> bool:
		return self._instance.UseTbjnt
	@property
	def use_tbcart(self) -> bool:
		return self._instance.UseTbcart
	@property
	def num_dual(self) -> int:
		return self._instance.NumDual
	@property
	def dummy133(self) -> int:
		return self._instance.Dummy133
	@property
	def turn_axis(self) -> typing.List[int]:
		return self._instance.TurnAxis
	@property
	def axs_amp_num(self) -> typing.List[int]:
		return self._instance.AxsAmpNum
	@property
	def flextooltyp(self) -> int:
		return self._instance.Flextooltyp
	@property
	def axs_xyz_map(self) -> typing.List[int]:
		return self._instance.AxsXyzMap
	@property
	def dummy134(self) -> int:
		return self._instance.Dummy134
	@property
	def ofst(self) -> typing.List[AxOfsVariableType]:
		return [AxOfsVariableType(x) for x in self._instance.Ofst]
	@property
	def kinem_enb(self) -> int:
		return self._instance.KinemEnb
	@property
	def dummy135(self) -> int:
		return self._instance.Dummy135
	@property
	def update_map(self) -> int:
		return self._instance.UpdateMap
	@property
	def torqctrl(self) -> int:
		return self._instance.Torqctrl
	@property
	def dsp_num(self) -> typing.List[int]:
		return self._instance.DspNum
	@property
	def dummy136(self) -> int:
		return self._instance.Dummy136
	@property
	def m_pos_enb(self) -> bool:
		return self._instance.MPosEnb
	@property
	def m_dst_enb(self) -> bool:
		return self._instance.MDstEnb
	@property
	def move_dst(self) -> float:
		return self._instance.MoveDst
	@property
	def mch_pos_x(self) -> float:
		return self._instance.MchPosX
	@property
	def mch_pos_y(self) -> float:
		return self._instance.MchPosY
	@property
	def mch_pos_z(self) -> float:
		return self._instance.MchPosZ
	@property
	def mch_pos_w(self) -> float:
		return self._instance.MchPosW
	@property
	def mch_pos_p(self) -> float:
		return self._instance.MchPosP
	@property
	def mch_pos_r(self) -> float:
		return self._instance.MchPosR
	@property
	def mch_ang(self) -> typing.List[float]:
		return self._instance.MchAng
	@property
	def mch_spd(self) -> float:
		return self._instance.MchSpd
	@property
	def dst_mir_p(self) -> int:
		return self._instance.DstMirP
	@property
	def dpos_dst(self) -> float:
		return self._instance.DposDst
	@property
	def dst_pos_x(self) -> float:
		return self._instance.DstPosX
	@property
	def dst_pos_y(self) -> float:
		return self._instance.DstPosY
	@property
	def dst_pos_z(self) -> float:
		return self._instance.DstPosZ
	@property
	def dsp_ercnt(self) -> typing.List[int]:
		return self._instance.DspErcnt
	@property
	def dest_data_p(self) -> typing.List[int]:
		return self._instance.DestDataP
	@property
	def robot_func(self) -> int:
		return self._instance.RobotFunc
	@property
	def proc_axs(self) -> typing.List[bool]:
		return self._instance.ProcAxs
	@property
	def dac_mode(self) -> int:
		return self._instance.DacMode
	@property
	def dac_axmode(self) -> typing.List[int]:
		return self._instance.DacAxmode
	@property
	def dac_rate1(self) -> typing.List[float]:
		return self._instance.DacRate1
	@property
	def dac_rate2(self) -> typing.List[float]:
		return self._instance.DacRate2
	@property
	def dac_rate3(self) -> typing.List[float]:
		return self._instance.DacRate3
	@property
	def dac_rate4(self) -> typing.List[float]:
		return self._instance.DacRate4
	@property
	def dac_rate5(self) -> typing.List[float]:
		return self._instance.DacRate5
	@property
	def dac_rate6(self) -> typing.List[float]:
		return self._instance.DacRate6
	@property
	def dac_rate7(self) -> typing.List[float]:
		return self._instance.DacRate7
	@property
	def dac_rate8(self) -> typing.List[float]:
		return self._instance.DacRate8
	@property
	def dac_rate9(self) -> typing.List[float]:
		return self._instance.DacRate9
	@property
	def dac_rate10(self) -> typing.List[float]:
		return self._instance.DacRate10
	@property
	def dac_lmt1(self) -> typing.List[float]:
		return self._instance.DacLmt1
	@property
	def dac_lmt2(self) -> typing.List[float]:
		return self._instance.DacLmt2
	@property
	def dac_lmt3(self) -> typing.List[float]:
		return self._instance.DacLmt3
	@property
	def dac_lmt4(self) -> typing.List[float]:
		return self._instance.DacLmt4
	@property
	def dac_lmt5(self) -> typing.List[float]:
		return self._instance.DacLmt5
	@property
	def dac_lmt6(self) -> typing.List[float]:
		return self._instance.DacLmt6
	@property
	def dac_lmt7(self) -> typing.List[float]:
		return self._instance.DacLmt7
	@property
	def dac_lmt8(self) -> typing.List[float]:
		return self._instance.DacLmt8
	@property
	def dac_lmt9(self) -> typing.List[float]:
		return self._instance.DacLmt9
	@property
	def dac_lmt10(self) -> typing.List[float]:
		return self._instance.DacLmt10
	@property
	def dac_flt_len(self) -> int:
		return self._instance.DacFltLen
	@property
	def dac_debug(self) -> typing.List[int]:
		return self._instance.DacDebug
	@property
	def func_sw(self) -> typing.List[int]:
		return self._instance.FuncSw
	@property
	def func_val(self) -> typing.List[float]:
		return self._instance.FuncVal
	@property
	def abc_enb(self) -> bool:
		return self._instance.AbcEnb
	@property
	def hbk_enbl(self) -> bool:
		return self._instance.HbkEnbl
	@property
	def mv_diag(self) -> typing.List[float]:
		return self._instance.MvDiag
	@property
	def abc_mode1(self) -> float:
		return self._instance.AbcMode1
	@property
	def abc_mode2(self) -> float:
		return self._instance.AbcMode2
	@property
	def abc_mode3(self) -> float:
		return self._instance.AbcMode3
	@property
	def abc_mode4(self) -> float:
		return self._instance.AbcMode4
	@property
	def abc_mode5(self) -> float:
		return self._instance.AbcMode5
	@property
	def abc_mode6(self) -> float:
		return self._instance.AbcMode6
	@property
	def abc_mode7(self) -> float:
		return self._instance.AbcMode7
	@property
	def abc_mode8(self) -> float:
		return self._instance.AbcMode8
	@property
	def abc_mode9(self) -> float:
		return self._instance.AbcMode9
	@property
	def safe_jntspd(self) -> typing.List[float]:
		return self._instance.SafeJntspd
	@property
	def robot_label(self) -> str:
		return self._instance.RobotLabel
	@property
	def dsp_num_flg(self) -> int:
		return self._instance.DspNumFlg
	@property
	def group_num(self) -> int:
		return self._instance.GroupNum
	@property
	def comp_sw(self) -> typing.List[int]:
		return self._instance.CompSw
	@property
	def amb_temp(self) -> float:
		return self._instance.AmbTemp
	@property
	def dsp_strt_ax(self) -> int:
		return self._instance.DspStrtAx
	@property
	def tot_sbr_num(self) -> int:
		return self._instance.TotSbrNum
	@property
	def tot_dsp_num(self) -> int:
		return self._instance.TotDspNum
	@property
	def tot_atr_num(self) -> int:
		return self._instance.TotAtrNum
	@property
	def tandem_sub(self) -> typing.List[int]:
		return self._instance.TandemSub
	@property
	def dsp_order(self) -> typing.List[int]:
		return self._instance.DspOrder
	@property
	def atr_order(self) -> typing.List[int]:
		return self._instance.AtrOrder
	@property
	def ampinf_ordr(self) -> typing.List[int]:
		return self._instance.AmpinfOrdr
	@property
	def ampcur_ordr(self) -> typing.List[int]:
		return self._instance.AmpcurOrdr
	@property
	def fix_ornt_wr(self) -> bool:
		return self._instance.FixOrntWr
	@property
	def jnt_vel_lim(self) -> typing.List[float]:
		return self._instance.JntVelLim
	@property
	def jnt_acc_lim(self) -> typing.List[float]:
		return self._instance.JntAccLim
	@property
	def joglimrot(self) -> int:
		return self._instance.Joglimrot
	@property
	def robot_name(self) -> str:
		return self._instance.RobotName
	@property
	def axis_cat(self) -> typing.List[int]:
		return self._instance.AxisCat
	@property
	def dummy137(self) -> int:
		return self._instance.Dummy137
	@property
	def dummy138(self) -> int:
		return self._instance.Dummy138
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
