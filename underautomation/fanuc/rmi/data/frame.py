import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import Frame as frame

class Frame:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = frame()
		else:
			self._instance = _internal
	@property
	def x(self) -> float:
		return self._instance.X
	@x.setter
	def x(self, value: float):
		self._instance.X = value
	@property
	def y(self) -> float:
		return self._instance.Y
	@y.setter
	def y(self, value: float):
		self._instance.Y = value
	@property
	def z(self) -> float:
		return self._instance.Z
	@z.setter
	def z(self, value: float):
		self._instance.Z = value
	@property
	def w(self) -> float:
		return self._instance.W
	@w.setter
	def w(self, value: float):
		self._instance.W = value
	@property
	def p(self) -> float:
		return self._instance.P
	@p.setter
	def p(self, value: float):
		self._instance.P = value
	@property
	def r(self) -> float:
		return self._instance.R
	@r.setter
	def r(self, value: float):
		self._instance.R = value
	@property
	def ext1(self) -> float:
		return self._instance.Ext1
	@ext1.setter
	def ext1(self, value: float):
		self._instance.Ext1 = value
	@property
	def ext2(self) -> float:
		return self._instance.Ext2
	@ext2.setter
	def ext2(self, value: float):
		self._instance.Ext2 = value
	@property
	def ext3(self) -> float:
		return self._instance.Ext3
	@ext3.setter
	def ext3(self, value: float):
		self._instance.Ext3 = value
