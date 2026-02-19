import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PslgtempVariableType as pslgtemp_variable_type

class PslgtempVariableType(GenericVariableType):
	'''Describes the Fanuc type PSLGTEMP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pslgtemp_variable_type()
		else:
			self._instance = _internal

	@property
	def dat_typ(self) -> int:
		'''Value of variable $DAT_TYP'''
		return self._instance.DatTyp

	@property
	def jnum(self) -> int:
		'''Value of variable $JNUM'''
		return self._instance.Jnum

	@property
	def do_rec(self) -> int:
		'''Value of variable $DO_REC'''
		return self._instance.DoRec

	@property
	def fil_mp(self) -> int:
		'''Value of variable $FIL_MP'''
		return self._instance.FilMp

	@property
	def fil_vel(self) -> int:
		'''Value of variable $FIL_VEL'''
		return self._instance.FilVel

	@property
	def rst_tqmon(self) -> int:
		'''Value of variable $RST_TQMON'''
		return self._instance.RstTqmon

	@property
	def pno(self) -> str:
		'''Value of variable $PNO'''
		return self._instance.Pno

	@property
	def c_result(self) -> typing.List[int]:
		'''Value of variable $C_RESULT'''
		return self._instance.CResult

	@property
	def v_result(self) -> typing.List[int]:
		'''Value of variable $V_RESULT'''
		return self._instance.VResult

	@property
	def cv_result(self) -> typing.List[int]:
		'''Value of variable $CV_RESULT'''
		return self._instance.CvResult

	@property
	def cp_file(self) -> typing.List[int]:
		'''Value of variable $CP_FILE'''
		return self._instance.CpFile

	@property
	def cm_file(self) -> typing.List[int]:
		'''Value of variable $CM_FILE'''
		return self._instance.CmFile

	@property
	def v1p_file(self) -> typing.List[int]:
		'''Value of variable $V1P_FILE'''
		return self._instance.V1pFile

	@property
	def v1m_file(self) -> typing.List[int]:
		'''Value of variable $V1M_FILE'''
		return self._instance.V1mFile

	@property
	def v2p_file(self) -> typing.List[int]:
		'''Value of variable $V2P_FILE'''
		return self._instance.V2pFile

	@property
	def v2m_file(self) -> typing.List[int]:
		'''Value of variable $V2M_FILE'''
		return self._instance.V2mFile

	@property
	def v3p_file(self) -> typing.List[int]:
		'''Value of variable $V3P_FILE'''
		return self._instance.V3pFile

	@property
	def v3m_file(self) -> typing.List[int]:
		'''Value of variable $V3M_FILE'''
		return self._instance.V3mFile

	@property
	def v4p_file(self) -> typing.List[int]:
		'''Value of variable $V4P_FILE'''
		return self._instance.V4pFile

	@property
	def v4m_file(self) -> typing.List[int]:
		'''Value of variable $V4M_FILE'''
		return self._instance.V4mFile

	@property
	def cur1(self) -> typing.List[float]:
		'''Value of variable $CUR_1'''
		return self._instance.Cur1

	@property
	def cur2(self) -> typing.List[float]:
		'''Value of variable $CUR_2'''
		return self._instance.Cur2

	@property
	def cur_t(self) -> typing.List[float]:
		'''Value of variable $CUR_T'''
		return self._instance.CurT

	@property
	def mincur_t(self) -> typing.List[float]:
		'''Value of variable $MINCUR_T'''
		return self._instance.MincurT

	@property
	def vib11(self) -> typing.List[int]:
		'''Value of variable $VIB11'''
		return self._instance.Vib11

	@property
	def vib12(self) -> typing.List[int]:
		'''Value of variable $VIB12'''
		return self._instance.Vib12

	@property
	def vib21(self) -> typing.List[int]:
		'''Value of variable $VIB21'''
		return self._instance.Vib21

	@property
	def vib22(self) -> typing.List[int]:
		'''Value of variable $VIB22'''
		return self._instance.Vib22

	@property
	def vib31(self) -> typing.List[int]:
		'''Value of variable $VIB31'''
		return self._instance.Vib31

	@property
	def vib32(self) -> typing.List[int]:
		'''Value of variable $VIB32'''
		return self._instance.Vib32

	@property
	def vib41(self) -> typing.List[int]:
		'''Value of variable $VIB41'''
		return self._instance.Vib41

	@property
	def vib42(self) -> typing.List[int]:
		'''Value of variable $VIB42'''
		return self._instance.Vib42

	@property
	def vib_t(self) -> typing.List[int]:
		'''Value of variable $VIB_T'''
		return self._instance.VibT

	@property
	def cl_result(self) -> typing.List[int]:
		'''Value of variable $CL_RESULT'''
		return self._instance.ClResult

	@property
	def cur3(self) -> typing.List[float]:
		'''Value of variable $CUR_3'''
		return self._instance.Cur3

	@property
	def cur4(self) -> typing.List[float]:
		'''Value of variable $CUR_4'''
		return self._instance.Cur4

	@property
	def cur_t2(self) -> typing.List[float]:
		'''Value of variable $CUR_T2'''
		return self._instance.CurT2

	@property
	def mincur_t2(self) -> typing.List[float]:
		'''Value of variable $MINCUR_T2'''
		return self._instance.MincurT2

	@property
	def plus_torque(self) -> typing.List[float]:
		'''Value of variable $PLUS_TORQUE'''
		return self._instance.PlusTorque

	@property
	def minus_torqu(self) -> typing.List[float]:
		'''Value of variable $MINUS_TORQU'''
		return self._instance.MinusTorqu

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PslgtempVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
