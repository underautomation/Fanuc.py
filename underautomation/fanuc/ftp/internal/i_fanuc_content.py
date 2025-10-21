import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import IFanucContent as i_fanuc_content

class IFanucContent:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_fanuc_content()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
