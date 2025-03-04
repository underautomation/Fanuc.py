import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PlstGrpVariableType as plst_grp_variable_type

class PlstGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plst_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def comment(self) -> str:
		return self._instance.Comment
	@property
	def payload(self) -> float:
		return self._instance.Payload
	@property
	def payload_x(self) -> float:
		return self._instance.PayloadX
	@property
	def payload_y(self) -> float:
		return self._instance.PayloadY
	@property
	def payload_z(self) -> float:
		return self._instance.PayloadZ
	@property
	def payload_ix(self) -> float:
		return self._instance.PayloadIx
	@property
	def payload_iy(self) -> float:
		return self._instance.PayloadIy
	@property
	def payload_iz(self) -> float:
		return self._instance.PayloadIz
	@property
	def icondisp(self) -> int:
		return self._instance.Icondisp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
