import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.fdot_variable_type import FdotVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VcalVdVariableType as vcal_vd_variable_type

class VcalVdVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcal_vd_variable_type()
		else:
			self._instance = _internal
	@property
	def vprog_name(self) -> str:
		return self._instance.VprogName
	@property
	def camera_name(self) -> str:
		return self._instance.CameraName
	@property
	def tool_type(self) -> int:
		return self._instance.ToolType
	@property
	def detect_type(self) -> int:
		return self._instance.DetectType
	@property
	def expo_time(self) -> int:
		return self._instance.ExpoTime
	@property
	def num_mul_expo(self) -> int:
		return self._instance.NumMulExpo
	@property
	def num_mep_usb(self) -> int:
		return self._instance.NumMepUsb
	@property
	def vis_xyz(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.VisXyz)
	@property
	def log_port(self) -> int:
		return self._instance.LogPort
	@property
	def focal_dist(self) -> float:
		return self._instance.FocalDist
	@property
	def grid_spacing(self) -> float:
		return self._instance.GridSpacing
	@property
	def distort(self) -> typing.List[float]:
		return self._instance.Distort
	@property
	def ovrrd_focus(self) -> bool:
		return self._instance.OvrrdFocus
	@property
	def num_retry(self) -> int:
		return self._instance.NumRetry
	@property
	def trim_ratio(self) -> float:
		return self._instance.TrimRatio
	@property
	def fdot_t(self) -> FdotVariableType:
		return FdotVariableType(self._instance.FdotT)
	@property
	def led_type(self) -> int:
		return self._instance.LedType
	@property
	def led_intensit(self) -> int:
		return self._instance.LedIntensit
	@property
	def dummy18(self) -> int:
		return self._instance.Dummy18
	@property
	def dummy19(self) -> int:
		return self._instance.Dummy19
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
