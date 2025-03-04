import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ApcureqVariableType as apcureq_variable_type

class ApcureqVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = apcureq_variable_type()
		else:
			self._instance = _internal
	@property
	def softpart_id(self) -> int:
		return self._instance.SoftpartId
	@property
	def total_eq(self) -> int:
		return self._instance.TotalEq
	@property
	def cur_eqno(self) -> int:
		return self._instance.CurEqno
	@property
	def spi_index(self) -> int:
		return self._instance.SpiIndex
	@property
	def screen_name(self) -> str:
		return self._instance.ScreenName
	@property
	def app_sign(self) -> str:
		return self._instance.AppSign
	@property
	def app_proces0(self) -> int:
		return self._instance.AppProces0
	@property
	def app_proces1(self) -> int:
		return self._instance.AppProces1
	@property
	def topk_file(self) -> str:
		return self._instance.TopkFile
	@property
	def thky_file(self) -> str:
		return self._instance.ThkyFile
	@property
	def pane_eqno(self) -> typing.List[int]:
		return self._instance.PaneEqno
	@property
	def dummy12(self) -> int:
		return self._instance.Dummy12
	@property
	def dummy13(self) -> int:
		return self._instance.Dummy13
	@property
	def dummy14(self) -> int:
		return self._instance.Dummy14
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
