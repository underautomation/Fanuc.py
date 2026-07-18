from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.generic_field import GenericField
from UnderAutomation.Fanuc.Common import Utils as utils

class Utils:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = utils()
		else:
			self._instance = _internal

	@staticmethod
	def set_name(field: GenericField, name: str) -> None:
		'''Trick for code generation'''
		utils.SetName(field._instance if field else None, name)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Utils):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
