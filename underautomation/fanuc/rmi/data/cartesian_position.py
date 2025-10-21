import typing
from underautomation.fanuc.rmi.data.motion_configuration import MotionConfiguration
from underautomation.fanuc.rmi.data.frame import Frame
from underautomation.fanuc.rmi.data.rmi_timed_response import RmiTimedResponse
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import CartesianPosition as cartesian_position

class CartesianPosition(RmiTimedResponse):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_position()
		else:
			self._instance = _internal
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
