import typing
from underautomation.fanuc.ftp.variables.joint_position_variable import JointPositionVariable
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PositionRegister as position_register

class PositionRegister:
	def __init__(self, jointsPosition: JointPositionVariable, cartesianPosition: CartesianPositionVariable, _internal = 0):
		if(_internal == 0):
			self._instance = position_register(jointsPosition, cartesianPosition)
		else:
			self._instance = _internal
	@staticmethod
	def parse(value: str) -> 'PositionRegister':
		return PositionRegister(None, None, position_register.Parse(value))
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def joints_position(self) -> JointPositionVariable:
		return JointPositionVariable(self._instance.JointsPosition)
	@joints_position.setter
	def joints_position(self, value: JointPositionVariable):
		self._instance.JointsPosition = value
	@property
	def cartesian_position(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.CartesianPosition)
	@cartesian_position.setter
	def cartesian_position(self, value: CartesianPositionVariable):
		self._instance.CartesianPosition = value
