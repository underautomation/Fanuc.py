import typing
from underautomation.fanuc.common.joints_position import JointsPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import JointPositionVariable as joint_position_variable

class JointPositionVariable(JointsPosition):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_position_variable()
		else:
			self._instance = _internal
	@staticmethod
	def parse(value: str) -> 'JointPositionVariable':
		return JointPositionVariable(joint_position_variable.Parse(value))
	@property
	def group(self) -> int:
		return self._instance.Group
	@group.setter
	def group(self, value: int):
		self._instance.Group = value
