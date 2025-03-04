import typing
from underautomation.fanuc.ftp.variables.tpgl_view_variable_type import TpglViewVariableType
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.tpglmach_variable_type import TpglmachVariableType
from underautomation.fanuc.ftp.variables.recloc_variable_type import ReclocVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpglOutVariableType as tpgl_out_variable_type

class TpglOutVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpgl_out_variable_type()
		else:
			self._instance = _internal
	@property
	def views(self) -> typing.List[TpglViewVariableType]:
		return [TpglViewVariableType(x) for x in self._instance.Views]
	@property
	def selected(self) -> typing.List[str]:
		return self._instance.Selected
	@property
	def selpos(self) -> typing.List[CartesianPositionVariable]:
		return [CartesianPositionVariable(x) for x in self._instance.Selpos]
	@property
	def pip_xml(self) -> str:
		return self._instance.PipXml
	@property
	def nodevis(self) -> typing.List[int]:
		return self._instance.Nodevis
	@property
	def machines(self) -> typing.List[TpglmachVariableType]:
		return [TpglmachVariableType(x) for x in self._instance.Machines]
	@property
	def recordedloc(self) -> typing.List[ReclocVariableType]:
		return [ReclocVariableType(x) for x in self._instance.Recordedloc]
	@property
	def nextpipe(self) -> str:
		return self._instance.Nextpipe
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
