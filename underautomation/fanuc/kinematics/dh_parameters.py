import typing
from underautomation.fanuc.kinematics.i_dh_parameters import IDhParameters
from underautomation.fanuc.kinematics.kinematics_category import KinematicsCategory
from underautomation.fanuc.kinematics.arm_kinematic_models import ArmKinematicModels
from underautomation.fanuc.ftp.variables.symotn_file import SymotnFile
from underautomation.fanuc.ftp.variables.mrr_grp_variable_type import MrrGrpVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics import DhParameters as dh_parameters

class DhParameters(IDhParameters):
	def __init__(self, d4: float, d5: float, d6: float, a1: float, a2: float, a3: float, _internal = 0):
		if(_internal == 0):
			self._instance = dh_parameters(d4, d5, d6, a1, a2, a3)
		else:
			self._instance = _internal
	@staticmethod
	def from_arm_kinematic_model(model: ArmKinematicModels) -> 'DhParameters':
		return DhParameters(None, None, None, None, None, None, dh_parameters.FromArmKinematicModel(model))
	@staticmethod
	def from_opw_parameters(a1: float, a2: float, c2: float, c3: float, c4: float) -> 'DhParameters':
		return DhParameters(None, None, None, None, None, None, dh_parameters.FromOpwParameters(a1, a2, c2, c3, c4))
	@staticmethod
	def from_def_file(doc: typing.Any) -> typing.List['DhParameters']:
		return [DhParameters(x) for x in dh_parameters.FromDefFile(doc)]
	@staticmethod
	def from_symotn_file(file: SymotnFile) -> typing.List['DhParameters']:
		return [DhParameters(x) for x in dh_parameters.FromSymotnFile(file._instance if file else None)]
	@staticmethod
	def from_mrr_grp(mrrGrp: MrrGrpVariableType) -> 'DhParameters':
		return DhParameters(None, None, None, None, None, None, dh_parameters.FromMrrGrp(mrrGrp._instance if mrrGrp else None))
	@property
	def d4(self) -> float:
		return self._instance.D4
	@d4.setter
	def d4(self, value: float):
		self._instance.D4 = value
	@property
	def d5(self) -> float:
		return self._instance.D5
	@d5.setter
	def d5(self, value: float):
		self._instance.D5 = value
	@property
	def d6(self) -> float:
		return self._instance.D6
	@d6.setter
	def d6(self, value: float):
		self._instance.D6 = value
	@property
	def a1(self) -> float:
		return self._instance.A1
	@a1.setter
	def a1(self, value: float):
		self._instance.A1 = value
	@property
	def a2(self) -> float:
		return self._instance.A2
	@a2.setter
	def a2(self, value: float):
		self._instance.A2 = value
	@property
	def a3(self) -> float:
		return self._instance.A3
	@a3.setter
	def a3(self, value: float):
		self._instance.A3 = value
	@property
	def kinematics_category(self) -> KinematicsCategory:
		return KinematicsCategory(self._instance.KinematicsCategory)
	@property
	def tag(self) -> typing.Any:
		return self._instance.Tag
	@tag.setter
	def tag(self, value: typing.Any):
		self._instance.Tag = value
