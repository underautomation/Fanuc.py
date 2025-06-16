import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import Feature as feature

class Feature:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = feature()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
	@name.setter
	def name(self, value: str):
		self._instance.Name = value
	@property
	def order_no(self) -> str:
		return self._instance.OrderNo
	@order_no.setter
	def order_no(self, value: str):
		self._instance.OrderNo = value
