import typing
from underautomation.fanuc.rmi.data.frame import Frame
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import IndexedFrame as indexed_frame

class IndexedFrame(RmiResponseBase):
	'''Frame data paired with an index (UFRAME or UTOOL).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = indexed_frame()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def index(self) -> int:
		'''Index (UFRAME or UTOOL number).'''
		return self._instance.Index

	@index.setter
	def index(self, value: int):
		self._instance.Index = value

	@property
	def frame(self) -> Frame:
		'''Frame data.'''
		return Frame(self._instance.Frame)

	@frame.setter
	def frame(self, value: Frame):
		self._instance.Frame = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IndexedFrame):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
