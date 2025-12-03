import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics import KinematicsCategory as kinematics_category

class KinematicsCategory(int):
	Invalid = kinematics_category.Invalid
	Crx = kinematics_category.Crx
	Opw = kinematics_category.Opw
