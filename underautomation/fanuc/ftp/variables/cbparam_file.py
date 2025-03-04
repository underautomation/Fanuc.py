import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CbparamFile as cbparam_file

class CbparamFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cbparam_file()
		else:
			self._instance = _internal
	@property
	def payload1(self) -> float:
		return self._instance.Payload1
	@property
	def payload1_x(self) -> float:
		return self._instance.Payload1X
	@property
	def payload1_y(self) -> float:
		return self._instance.Payload1Y
	@property
	def payload1_z(self) -> float:
		return self._instance.Payload1Z
	@property
	def payload1_ix(self) -> float:
		return self._instance.Payload1Ix
	@property
	def payload1_iy(self) -> float:
		return self._instance.Payload1Iy
	@property
	def payload1_iz(self) -> float:
		return self._instance.Payload1Iz
	@property
	def payload2(self) -> float:
		return self._instance.Payload2
	@property
	def payload2_x(self) -> float:
		return self._instance.Payload2X
	@property
	def payload2_y(self) -> float:
		return self._instance.Payload2Y
	@property
	def payload2_z(self) -> float:
		return self._instance.Payload2Z
	@property
	def payload2_ix(self) -> float:
		return self._instance.Payload2Ix
	@property
	def payload2_iy(self) -> float:
		return self._instance.Payload2Iy
	@property
	def payload2_iz(self) -> float:
		return self._instance.Payload2Iz
	@property
	def tframe_x(self) -> typing.List[float]:
		return self._instance.TframeX
	@property
	def tframe_y(self) -> typing.List[float]:
		return self._instance.TframeY
	@property
	def tframe_z(self) -> typing.List[float]:
		return self._instance.TframeZ
	@property
	def se_ctrlmode(self) -> int:
		return self._instance.SeCtrlmode
	@property
	def data_c1(self) -> typing.List[float]:
		return self._instance.DataC1
	@property
	def data_c2(self) -> typing.List[float]:
		return self._instance.DataC2
	@property
	def data_c3(self) -> typing.List[float]:
		return self._instance.DataC3
	@property
	def data_c4(self) -> typing.List[float]:
		return self._instance.DataC4
	@property
	def data_c5(self) -> typing.List[float]:
		return self._instance.DataC5
	@property
	def data_c6(self) -> typing.List[float]:
		return self._instance.DataC6
	@property
	def data_c7(self) -> typing.List[float]:
		return self._instance.DataC7
	@property
	def data_c8(self) -> typing.List[float]:
		return self._instance.DataC8
	@property
	def data_c9(self) -> typing.List[float]:
		return self._instance.DataC9
	@property
	def data_c10(self) -> typing.List[float]:
		return self._instance.DataC10
