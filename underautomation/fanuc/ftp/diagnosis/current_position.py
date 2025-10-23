import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.ftp.diagnosis.group_position import GroupPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import CurrentPosition as current_position

class CurrentPosition(IFanucContent):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_position()
		else:
			self._instance = _internal
	@property
	def groups_position(self) -> typing.List[GroupPosition]:
		return [GroupPosition(x) for x in self._instance.GroupsPosition]
	@property
	def name(self) -> str:
		return self._instance.Name
