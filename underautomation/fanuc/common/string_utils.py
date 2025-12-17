import typing
from underautomation.fanuc.common.languages import Languages
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import StringUtils as string_utils

class StringUtils:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_utils()
		else:
			self._instance = _internal
	@staticmethod
	def get_encoding(language: Languages) -> typing.Any:
		return string_utils.GetEncoding(language)
