import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PslgtempVariableType as pslgtemp_variable_type

class PslgtempVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pslgtemp_variable_type()
		else:
			self._instance = _internal
	@property
	def dat_typ(self) -> int:
		return self._instance.DatTyp
	@property
	def jnum(self) -> int:
		return self._instance.Jnum
	@property
	def do_rec(self) -> int:
		return self._instance.DoRec
	@property
	def fil_mp(self) -> int:
		return self._instance.FilMp
	@property
	def fil_vel(self) -> int:
		return self._instance.FilVel
	@property
	def rst_tqmon(self) -> int:
		return self._instance.RstTqmon
	@property
	def pno(self) -> str:
		return self._instance.Pno
	@property
	def c_result(self) -> typing.List[int]:
		return self._instance.CResult
	@property
	def v_result(self) -> typing.List[int]:
		return self._instance.VResult
	@property
	def cv_result(self) -> typing.List[int]:
		return self._instance.CvResult
	@property
	def cp_file(self) -> typing.List[int]:
		return self._instance.CpFile
	@property
	def cm_file(self) -> typing.List[int]:
		return self._instance.CmFile
	@property
	def v1p_file(self) -> typing.List[int]:
		return self._instance.V1pFile
	@property
	def v1m_file(self) -> typing.List[int]:
		return self._instance.V1mFile
	@property
	def v2p_file(self) -> typing.List[int]:
		return self._instance.V2pFile
	@property
	def v2m_file(self) -> typing.List[int]:
		return self._instance.V2mFile
	@property
	def v3p_file(self) -> typing.List[int]:
		return self._instance.V3pFile
	@property
	def v3m_file(self) -> typing.List[int]:
		return self._instance.V3mFile
	@property
	def v4p_file(self) -> typing.List[int]:
		return self._instance.V4pFile
	@property
	def v4m_file(self) -> typing.List[int]:
		return self._instance.V4mFile
	@property
	def cur1(self) -> typing.List[float]:
		return self._instance.Cur1
	@property
	def cur2(self) -> typing.List[float]:
		return self._instance.Cur2
	@property
	def cur_t(self) -> typing.List[float]:
		return self._instance.CurT
	@property
	def mincur_t(self) -> typing.List[float]:
		return self._instance.MincurT
	@property
	def vib11(self) -> typing.List[int]:
		return self._instance.Vib11
	@property
	def vib12(self) -> typing.List[int]:
		return self._instance.Vib12
	@property
	def vib21(self) -> typing.List[int]:
		return self._instance.Vib21
	@property
	def vib22(self) -> typing.List[int]:
		return self._instance.Vib22
	@property
	def vib31(self) -> typing.List[int]:
		return self._instance.Vib31
	@property
	def vib32(self) -> typing.List[int]:
		return self._instance.Vib32
	@property
	def vib41(self) -> typing.List[int]:
		return self._instance.Vib41
	@property
	def vib42(self) -> typing.List[int]:
		return self._instance.Vib42
	@property
	def vib_t(self) -> typing.List[int]:
		return self._instance.VibT
	@property
	def cl_result(self) -> typing.List[int]:
		return self._instance.ClResult
	@property
	def cur3(self) -> typing.List[float]:
		return self._instance.Cur3
	@property
	def cur4(self) -> typing.List[float]:
		return self._instance.Cur4
	@property
	def cur_t2(self) -> typing.List[float]:
		return self._instance.CurT2
	@property
	def mincur_t2(self) -> typing.List[float]:
		return self._instance.MincurT2
	@property
	def plus_torque(self) -> typing.List[float]:
		return self._instance.PlusTorque
	@property
	def minus_torqu(self) -> typing.List[float]:
		return self._instance.MinusTorqu
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
