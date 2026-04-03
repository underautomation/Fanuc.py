from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Cgtp import CgtpFileItem as cgtp_file_item

class CgtpFileItem:
	'''Represents a file entry returned by the controller's index pages.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_file_item()
		else:
			self._instance = _internal

	@property
	def file(self) -> str:
		'''File name on the controller.'''
		return self._instance.File

	@property
	def comment(self) -> str:
		'''Comment associated with the file, if any.'''
		return self._instance.Comment

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpFileItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
