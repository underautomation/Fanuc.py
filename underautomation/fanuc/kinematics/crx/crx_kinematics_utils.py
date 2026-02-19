import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.kinematics.dh_parameters import DhParameters
from UnderAutomation.Fanuc.Kinematics.Crx import CrxKinematicsUtils as crx_kinematics_utils

class CrxKinematicsUtils:
	'''Utility methods implementing CRX collaborative robot inverse kinematics using a geometric approach.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = crx_kinematics_utils()
		else:
			self._instance = _internal

	@staticmethod
	def inverse_kinematics(pose: CartesianPosition, parameters: DhParameters, includeDuals: bool=True, seedJoints: typing.List[float]=None) -> typing.List[JointsPosition]:
		'''Solve IK for a desired tool pose (WPR). Returns up to 16 solutions (including duals, Eq. (23)). This implements Steps 1..7 from paper §2.6 with references to Eqs. (13–23).

		:param pose: Target pose in WPR (deg) and XYZ (mm).
		:param parameters: DH Parameters
		:param includeDuals: Whether to add dual solutions per Eq. (23).
		:param seedJoints: Optional seed [J1..J6] (deg) to bias q-search near source.
		'''
		return [JointsPosition(None, None, None, None, None, None, None, None, None, x) for x in crx_kinematics_utils.InverseKinematics(pose._instance if pose else None, parameters._instance if parameters else None, includeDuals, seedJoints)]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CrxKinematicsUtils):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
