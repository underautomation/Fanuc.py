import typing
from underautomation.fanuc.kinematics.i_dh_parameters import IDhParameters
from underautomation.fanuc.kinematics.kinematics_category import KinematicsCategory
from underautomation.fanuc.kinematics.arm_kinematic_models import ArmKinematicModels
from underautomation.fanuc.ftp.variables.symotn_file import SymotnFile
from underautomation.fanuc.ftp.variables.mrr_grp_variable_type import MrrGrpVariableType
from UnderAutomation.Fanuc.Kinematics import DhParameters as dh_parameters
from UnderAutomation.Fanuc.Kinematics import KinematicsCategory as kinematics_category
from UnderAutomation.Fanuc.Kinematics import ArmKinematicModels as arm_kinematic_models

class DhParameters(IDhParameters):
	'''Denavit-Hartenberg parameters for a 6-axis robot arm.'''
	def __init__(self, d4: float, d5: float, d6: float, a1: float, a2: float, a3: float, _internal = 0):
		'''Initializes a new instance of DhParameters with the specified values.

		:param d4: DH parameter D4 (mm).
		:param d5: DH parameter D5 (mm).
		:param d6: DH parameter D6 (mm).
		:param a1: DH parameter A1 (mm).
		:param a2: DH parameter A2 (mm).
		:param a3: DH parameter A3 (mm).
		'''
		if(_internal == 0):
			self._instance = dh_parameters(d4, d5, d6, a1, a2, a3)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@staticmethod
	def from_arm_kinematic_model(model: ArmKinematicModels) -> 'DhParameters':
		'''Returns DH parameters from a known Arm Kinematic Model.'''
		return DhParameters(None, None, None, None, None, None, dh_parameters.FromArmKinematicModel(arm_kinematic_models(int(model))))

	@staticmethod
	def from_opw_parameters(a1: float, a2: float, c2: float, c3: float, c4: float) -> 'DhParameters':
		'''Creates DH parameters from OPW parameters (in meters) C1 and B are ignored because B is always 0 and C1 is not used in the DH representation.

		:param a1: OPW A1 parameter in meters
		:param a2: OPW A2 parameter in meters
		:param c2: OPW C2 parameter in meters
		:param c3: OPW C3 parameter in meters
		:param c4: OPW C4 parameter in meters
		'''
		return DhParameters(None, None, None, None, None, None, dh_parameters.FromOpwParameters(a1, a2, c2, c3, c4))

	@staticmethod
	def from_def_file(doc: typing.Any) -> typing.List['DhParameters']:
		'''Loads DH parameters of each robots described in a ROBOGUIDE definition file (*.def). By default, this file is located in "C:\ProgramData\FANUC\ROBOGUIDE\Robot Library".'''
		return [DhParameters(None, None, None, None, None, None, x) for x in dh_parameters.FromDefFile(doc)]

	@staticmethod
	def from_symotn_file(file: SymotnFile) -> typing.List['DhParameters']:
		'''Loads DH parameters of each group from a parsed symotn.va file.'''
		return [DhParameters(None, None, None, None, None, None, x) for x in dh_parameters.FromSymotnFile(file._instance if file else None)]

	@staticmethod
	def from_mrr_grp(mrrGrp: MrrGrpVariableType) -> 'DhParameters':
		'''Loads DH parameters from parsed variable $MRR_GRP located in symotn.va.'''
		return DhParameters(None, None, None, None, None, None, dh_parameters.FromMrrGrp(mrrGrp._instance if mrrGrp else None))

	@property
	def d4(self) -> float:
		'''DH parameter D4 (mm).'''
		return self._instance.D4

	@d4.setter
	def d4(self, value: float):
		self._instance.D4 = value

	@property
	def d5(self) -> float:
		'''DH parameter D5 (mm).'''
		return self._instance.D5

	@d5.setter
	def d5(self, value: float):
		self._instance.D5 = value

	@property
	def d6(self) -> float:
		'''DH parameter D6 (mm).'''
		return self._instance.D6

	@d6.setter
	def d6(self, value: float):
		self._instance.D6 = value

	@property
	def a1(self) -> float:
		'''DH parameter A1 (mm).'''
		return self._instance.A1

	@a1.setter
	def a1(self, value: float):
		self._instance.A1 = value

	@property
	def a2(self) -> float:
		'''DH parameter A2 (mm).'''
		return self._instance.A2

	@a2.setter
	def a2(self, value: float):
		self._instance.A2 = value

	@property
	def a3(self) -> float:
		'''DH parameter A3 (mm).'''
		return self._instance.A3

	@a3.setter
	def a3(self, value: float):
		self._instance.A3 = value

	@property
	def kinematics_category(self) -> KinematicsCategory:
		'''Gets the kinematics category determined from the DH parameter values.'''
		return KinematicsCategory(int(self._instance.KinematicsCategory))

	@property
	def tag(self) -> typing.Any:
		'''User-defined tag for associating additional data with this instance.'''
		return self._instance.Tag

	@tag.setter
	def tag(self, value: typing.Any):
		self._instance.Tag = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
