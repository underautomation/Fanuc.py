import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PlidSvVariableType as plid_sv_variable_type

class PlidSvVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plid_sv_variable_type()
		else:
			self._instance = _internal
	@property
	def cur_scrn(self) -> int:
		return self._instance.CurScrn
	@property
	def cur_group(self) -> int:
		return self._instance.CurGroup
	@property
	def save_done(self) -> bool:
		return self._instance.SaveDone
	@property
	def no_recover(self) -> bool:
		return self._instance.NoRecover
	@property
	def result_sav(self) -> typing.List[float]:
		return self._instance.ResultSav
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
	def do_default(self) -> bool:
		return self._instance.DoDefault
	@property
	def mov_pos1(self) -> typing.List[float]:
		return self._instance.MovPos1
	@property
	def mov_pos2(self) -> typing.List[float]:
		return self._instance.MovPos2
	@property
	def speed_high(self) -> int:
		return self._instance.SpeedHigh
	@property
	def speed_low(self) -> int:
		return self._instance.SpeedLow
	@property
	def accel_high(self) -> int:
		return self._instance.AccelHigh
	@property
	def accel_low(self) -> int:
		return self._instance.AccelLow
	@property
	def do_def_pos(self) -> bool:
		return self._instance.DoDefPos
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
