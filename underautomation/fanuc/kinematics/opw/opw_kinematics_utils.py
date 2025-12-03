import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.kinematics.dh_parameters import DhParameters
from underautomation.fanuc.common.joints_position import JointsPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics.Opw import OpwKinematicsUtils as opw_kinematics_utils

class OpwKinematicsUtils:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = opw_kinematics_utils()
		else:
			self._instance = _internal
	@staticmethod
	def forward_kinematics(jointAnglesRad: typing.List[float], dhParameters: DhParameters) -> CartesianPosition:
		return CartesianPosition(None, None, None, None, None, None, None, opw_kinematics_utils.ForwardKinematics(jointAnglesRad, dhParameters._instance if dhParameters else None))
	@staticmethod
	def inverse_kinematics(pose: CartesianPosition, dhParameters: DhParameters) -> typing.List[JointsPosition]:
		return [JointsPosition(x) for x in opw_kinematics_utils.InverseKinematics(pose._instance if pose else None, dhParameters._instance if dhParameters else None)]
