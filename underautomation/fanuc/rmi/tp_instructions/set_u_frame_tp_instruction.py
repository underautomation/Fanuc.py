from __future__ import annotations
import typing
from underautomation.fanuc.rmi.tp_instructions.rmi_instruction_base import RmiInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import SetUFrameTpInstruction as set_u_frame_tp_instruction

class SetUFrameTpInstruction(RmiInstructionBase):
	'''Instruction for a UFRAME_NUM = n assignment. Pass to RmiInstructionBase).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = set_u_frame_tp_instruction()
		else:
			self._instance = _internal

	@property
	def frame_number(self) -> int:
		'''User frame number to activate.'''
		return self._instance.FrameNumber

	@frame_number.setter
	def frame_number(self, value: int):
		self._instance.FrameNumber = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SetUFrameTpInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
