import typing
from underautomation.fanuc.ftp.variables.generic_field import GenericField
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import Utils as utils

T = typing.TypeVar('T')
class Utils:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = utils()
		else:
			self._instance = _internal
	@staticmethod
	def set_name(field: GenericField, name: str) -> None:
		utils.SetName(field._instance, name)
