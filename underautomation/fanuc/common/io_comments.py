from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Common import IOComments as io_comments

class IOComments:
	'''Contains input and output comment arrays for an I/O type.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_comments()
		else:
			self._instance = _internal

	@property
	def inputs(self) -> typing.List[str]:
		'''Array of input comments. Index 0 corresponds to Fanuc port 1.'''
		return self._instance.Inputs

	@inputs.setter
	def inputs(self, value: typing.List[str]):
		self._instance.Inputs = value

	@property
	def outputs(self) -> typing.List[str]:
		'''Array of output comments. Index 0 corresponds to Fanuc port 1.'''
		return self._instance.Outputs

	@outputs.setter
	def outputs(self, value: typing.List[str]):
		self._instance.Outputs = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IOComments):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
