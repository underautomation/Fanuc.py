import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics import KinematicsCategory as kinematics_category

class KinematicsCategory(int):
	Invalid = int(kinematics_category.Invalid)
	Crx = int(kinematics_category.Crx)
	Opw = int(kinematics_category.Opw)

	def __repr__(self):
		for name, value in vars(KinematicsCategory).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
