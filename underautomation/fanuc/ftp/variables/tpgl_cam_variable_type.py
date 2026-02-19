import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TpglCamVariableType as tpgl_cam_variable_type

class TpglCamVariableType(GenericVariableType):
	'''Describes the Fanuc type TPGL_CAM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpgl_cam_variable_type()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Value of variable $NAME'''
		return self._instance.Name

	@property
	def id(self) -> str:
		'''Value of variable $ID'''
		return self._instance.Id

	@property
	def fid(self) -> str:
		'''Value of variable $FID'''
		return self._instance.Fid

	@property
	def gif(self) -> str:
		'''Value of variable $GIF'''
		return self._instance.Gif

	@property
	def nearplane(self) -> float:
		'''Value of variable $NEARPLANE'''
		return self._instance.Nearplane

	@property
	def farplane(self) -> float:
		'''Value of variable $FARPLANE'''
		return self._instance.Farplane

	@property
	def distance(self) -> float:
		'''Value of variable $DISTANCE'''
		return self._instance.Distance

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpglCamVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
