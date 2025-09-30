import typing
from underautomation.fanuc.rmi.data.motion_configuration import MotionConfiguration
from underautomation.fanuc.rmi.data.frame import Frame
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import PositionRegisterData as position_register_data

class PositionRegisterData(RmiResponseBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = position_register_data()
		else:
			self._instance = _internal
	@property
	def register_number(self) -> int:
		return self._instance.RegisterNumber
	@register_number.setter
	def register_number(self, value: int):
		self._instance.RegisterNumber = value
	@property
	def configuration(self) -> MotionConfiguration:
		return MotionConfiguration(self._instance.Configuration)
	@configuration.setter
	def configuration(self, value: MotionConfiguration):
		self._instance.Configuration = value
	@property
	def position(self) -> Frame:
		return Frame(self._instance.Position)
	@position.setter
	def position(self, value: Frame):
		self._instance.Position = value
