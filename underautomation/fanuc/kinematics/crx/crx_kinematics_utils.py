import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.kinematics.dh_parameters import DhParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics.Crx import CrxKinematicsUtils as crx_kinematics_utils

class CrxKinematicsUtils:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = crx_kinematics_utils()
		else:
			self._instance = _internal
	@staticmethod
	def inverse_kinematics(pose: CartesianPosition, parameters: DhParameters, includeDuals: bool=True, seedJoints: typing.List[float]=None) -> typing.List[JointsPosition]:
		return [JointsPosition(x) for x in crx_kinematics_utils.InverseKinematics(pose._instance if pose else None, parameters._instance if parameters else None, includeDuals, seedJoints)]
