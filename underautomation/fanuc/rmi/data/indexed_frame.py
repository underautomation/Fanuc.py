import typing
from underautomation.fanuc.rmi.data.frame import Frame
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import IndexedFrame as indexed_frame

class IndexedFrame(RmiResponseBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = indexed_frame()
		else:
			self._instance = _internal
	@property
	def index(self) -> int:
		return self._instance.Index
	@index.setter
	def index(self, value: int):
		self._instance.Index = value
	@property
	def frame(self) -> Frame:
		return Frame(self._instance.Frame)
	@frame.setter
	def frame(self, value: Frame):
		self._instance.Frame = value
