import typing
from underautomation.fanuc.common.languages import Languages
from UnderAutomation.Fanuc.Common import StringUtils as string_utils
from UnderAutomation.Fanuc.Common import Languages as languages

class StringUtils:
	'''Contains string related utility methods'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_utils()
		else:
			self._instance = _internal

	@staticmethod
	def get_encoding(language: Languages) -> typing.Any:
		'''Gets the encoding for the specified controller language'''
		return string_utils.GetEncoding(languages(int(language)))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StringUtils):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
