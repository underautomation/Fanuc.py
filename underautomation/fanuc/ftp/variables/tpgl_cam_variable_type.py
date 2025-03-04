import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpglCamVariableType as tpgl_cam_variable_type

class TpglCamVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpgl_cam_variable_type()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def id(self) -> str:
		return self._instance.Id
	@property
	def fid(self) -> str:
		return self._instance.Fid
	@property
	def gif(self) -> str:
		return self._instance.Gif
	@property
	def nearplane(self) -> float:
		return self._instance.Nearplane
	@property
	def farplane(self) -> float:
		return self._instance.Farplane
	@property
	def distance(self) -> float:
		return self._instance.Distance
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
