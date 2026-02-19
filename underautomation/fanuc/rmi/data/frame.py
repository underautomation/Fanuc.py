import typing
from UnderAutomation.Fanuc.Rmi.Data import Frame as frame

class Frame:
	'''Cartesian frame representation: position (X/Y/Z in mm) and orientation (W/P/R in degrees). Extended axes Ext1..Ext3 are optional and default to 0.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = frame()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def x(self) -> float:
		'''X coordinate in millimeters.'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y coordinate in millimeters.'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z coordinate in millimeters.'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	@property
	def w(self) -> float:
		'''W (Yaw) in degrees.'''
		return self._instance.W

	@w.setter
	def w(self, value: float):
		self._instance.W = value

	@property
	def p(self) -> float:
		'''P (Pitch) in degrees.'''
		return self._instance.P

	@p.setter
	def p(self, value: float):
		self._instance.P = value

	@property
	def r(self) -> float:
		'''R (Roll) in degrees.'''
		return self._instance.R

	@r.setter
	def r(self, value: float):
		self._instance.R = value

	@property
	def ext1(self) -> float:
		'''Extended axis 1 (optional).'''
		return self._instance.Ext1

	@ext1.setter
	def ext1(self, value: float):
		self._instance.Ext1 = value

	@property
	def ext2(self) -> float:
		'''Extended axis 2 (optional).'''
		return self._instance.Ext2

	@ext2.setter
	def ext2(self, value: float):
		self._instance.Ext2 = value

	@property
	def ext3(self) -> float:
		'''Extended axis 3 (optional).'''
		return self._instance.Ext3

	@ext3.setter
	def ext3(self, value: float):
		self._instance.Ext3 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Frame):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
