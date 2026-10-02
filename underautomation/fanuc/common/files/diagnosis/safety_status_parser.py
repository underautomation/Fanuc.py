from __future__ import annotations
import typing
from underautomation.fanuc.common.files.section_parser_1 import SectionParser1
from underautomation.fanuc.common.files.diagnosis.safety_status import SafetyStatus
from UnderAutomation.Fanuc.Common.Files.Diagnosis import SafetyStatusParser as safety_status_parser
import System

class SafetyStatusParser(SectionParser1[SafetyStatus]):
	'''Parser for reading and interpreting safety status signals from diagnostic files.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = safety_status_parser()
		else:
			self._instance = _internal

	@typing.overload
	def parse_line(self, line: str, start: str, setValue: typing.Callable[[bool], None]) -> None: ...

	@typing.overload
	def parse_line(self, line: str) -> None: ...

	def parse_line(self, *args, **kwargs) -> None:
		'''Arguments: (line, start, setValue)
		Arguments: (line)
		'''
		__a = _bind_overload(args, kwargs, ['line', 'start', 'setValue'], {})
		if __a is not None:
			line, start, setValue = __a
			self._instance.ParseLine(line, start, (setValue._instance if hasattr(setValue, '_instance') else System.Action[System.Boolean](lambda _x0: setValue(_x0))) if setValue else None)
			return
		__a = _bind_overload(args, kwargs, ['line'], {})
		if __a is not None:
			line, = __a
			self._instance.ParseLine(line)
			return
		raise TypeError("parse_line(): no overload takes these arguments")

	@property
	def section_start(self) -> typing.List[str]:
		return self._instance.SectionStart

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SafetyStatusParser):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

def _bind_overload(args, kwargs, names, defaults):
	if len(args) > len(names) or any(k not in names[len(args):] for k in kwargs):
		return None
	values = list(args)
	for name in names[len(args):]:
		if name in kwargs:
			values.append(kwargs[name])
		elif name in defaults:
			values.append(defaults[name])
		else:
			return None
	return values
