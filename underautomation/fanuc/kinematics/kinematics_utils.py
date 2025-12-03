import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.kinematics.dh_parameters import DhParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics import KinematicsUtils as kinematics_utils

class KinematicsUtils:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kinematics_utils()
		else:
			self._instance = _internal
	@staticmethod
	def forward_kinematics(jointAnglesRad: typing.List[float], dhParameters: DhParameters) -> CartesianPosition:
		return CartesianPosition(None, None, None, None, None, None, None, kinematics_utils.ForwardKinematics(jointAnglesRad, dhParameters._instance if dhParameters else None))
	@staticmethod
	def inverse_kinematics(position: CartesianPosition, parameters: DhParameters) -> typing.List[JointsPosition]:
		return [JointsPosition(x) for x in kinematics_utils.InverseKinematics(position._instance if position else None, parameters._instance if parameters else None)]
	@staticmethod
	def mul(A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
		return kinematics_utils.Mul(A, B)
