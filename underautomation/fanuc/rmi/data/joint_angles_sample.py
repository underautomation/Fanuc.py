import typing
from underautomation.fanuc.rmi.data.joint_angles import JointAngles
from underautomation.fanuc.rmi.data.rmi_timed_response import RmiTimedResponse
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import JointAnglesSample as joint_angles_sample

class JointAnglesSample(RmiTimedResponse):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_angles_sample()
		else:
			self._instance = _internal
	@property
	def joint_angle(self) -> JointAngles:
		return JointAngles(self._instance.JointAngle)
	@joint_angle.setter
	def joint_angle(self, value: JointAngles):
		self._instance.JointAngle = value
