from __future__ import annotations
import typing
from underautomation.fanuc.rmi.tp_instructions.motion_tp_instruction_base import MotionTpInstructionBase
from underautomation.fanuc.rmi.data.rmi_port_type import RmiPortType
from underautomation.fanuc.rmi.data.rmi_on_off import RmiOnOff
from UnderAutomation.Fanuc.Rmi.TpInstructions import FullMotionTpInstructionBase as full_motion_tp_instruction_base
from UnderAutomation.Fanuc.Rmi.Data import RmiPortType as rmi_port_type
from UnderAutomation.Fanuc.Rmi.Data import RmiOnOff as rmi_on_off

class FullMotionTpInstructionBase(MotionTpInstructionBase):
	'''Extends MotionTpInstructionBase with the full set of optional motion modifiers shared by all non-simplified instruction types.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = full_motion_tp_instruction_base()
		else:
			self._instance = _internal

	@property
	def acc(self) -> int | None:
		'''Optional acceleration override (1-100 %). null uses the controller default.'''
		return self._instance.Acc

	@acc.setter
	def acc(self, value: int | None):
		self._instance.Acc = value

	@property
	def offset_pr_number(self) -> int | None:
		'''Offset position register number. null disables offset.'''
		return self._instance.OffsetPrNumber

	@offset_pr_number.setter
	def offset_pr_number(self, value: int | None):
		self._instance.OffsetPrNumber = value

	@property
	def vision_pr_number(self) -> int | None:
		'''Vision offset position register number. null disables vision offset.'''
		return self._instance.VisionPrNumber

	@vision_pr_number.setter
	def vision_pr_number(self, value: int | None):
		self._instance.VisionPrNumber = value

	@property
	def lcb_type(self) -> str:
		'''Lock-and-continue (LCB) condition type string. null disables LCB.'''
		return self._instance.LcbType

	@lcb_type.setter
	def lcb_type(self, value: str):
		self._instance.LcbType = value

	@property
	def lcb_value(self) -> int | None:
		'''Lock-and-continue (LCB) condition value. Required when LcbType is set.'''
		return self._instance.LcbValue

	@lcb_value.setter
	def lcb_value(self, value: int | None):
		self._instance.LcbValue = value

	@property
	def port_type(self) -> RmiPortType | None:
		'''Digital output port type to trigger at the end of this motion. null disables output.'''
		return RmiPortType(int(self._instance.PortType))

	@port_type.setter
	def port_type(self, value: RmiPortType | None):
		self._instance.PortType = value

	@property
	def port_number(self) -> int | None:
		'''Digital output port number. Required when PortType is set.'''
		return self._instance.PortNumber

	@port_number.setter
	def port_number(self, value: int | None):
		self._instance.PortNumber = value

	@property
	def port_value(self) -> RmiOnOff | None:
		'''Digital output port value. Required when PortType is set.'''
		return RmiOnOff(int(self._instance.PortValue))

	@port_value.setter
	def port_value(self, value: RmiOnOff | None):
		self._instance.PortValue = value

	@property
	def tool_offset_pr_number(self) -> int | None:
		'''Tool-offset position register number. null disables tool offset. Requires MajorVersion >= 4.'''
		return self._instance.ToolOffsetPrNumber

	@tool_offset_pr_number.setter
	def tool_offset_pr_number(self, value: int | None):
		self._instance.ToolOffsetPrNumber = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FullMotionTpInstructionBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
