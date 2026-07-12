from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_on_off import RmiOnOff
from underautomation.fanuc.rmi.tp_instructions.rmi_instruction_base import RmiInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import WaitDinTpInstruction as wait_din_tp_instruction
from UnderAutomation.Fanuc.Rmi.Data import RmiOnOff as rmi_on_off

class WaitDinTpInstruction(RmiInstructionBase):
	'''Instruction for a WAIT DI[n] = value condition. Pass to RmiInstructionBase).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = wait_din_tp_instruction()
		else:
			self._instance = _internal

	@property
	def port_number(self) -> int:
		'''Digital input port number to wait on.'''
		return self._instance.PortNumber

	@port_number.setter
	def port_number(self, value: int):
		self._instance.PortNumber = value

	@property
	def value(self) -> RmiOnOff:
		'''Expected port state that releases the wait.'''
		return RmiOnOff(int(self._instance.Value))

	@value.setter
	def value(self, value: RmiOnOff):
		self._instance.Value = rmi_on_off(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, WaitDinTpInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
