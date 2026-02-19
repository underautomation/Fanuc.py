import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.ftp.diagnosis.group_position import GroupPosition
from UnderAutomation.Fanuc.Ftp.Diagnosis import CurrentPosition as current_position

class CurrentPosition(IFanucContent):
	'''Contains the position for each robots'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_position()
		else:
			self._instance = _internal

	@property
	def groups_position(self) -> typing.List[GroupPosition]:
		'''Position of each robots handled by this controller'''
		return [GroupPosition(x) for x in self._instance.GroupsPosition]

	@property
	def name(self) -> str:
		'''File name : curpos.dg'''
		return self._instance.Name

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CurrentPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
