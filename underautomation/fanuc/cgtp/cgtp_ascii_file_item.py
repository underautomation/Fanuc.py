from __future__ import annotations
import typing
from underautomation.fanuc.cgtp.cgtp_file_item import CgtpFileItem
from UnderAutomation.Fanuc.Cgtp import CgtpAsciiFileItem as cgtp_ascii_file_item

class CgtpAsciiFileItem(CgtpFileItem):
	'''Represents a file entry that has both a binary and an ASCII format.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_ascii_file_item()
		else:
			self._instance = _internal

	@property
	def ascii_file(self) -> str:
		'''ASCII format file name, or null if not available.'''
		return self._instance.AsciiFile

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpAsciiFileItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
