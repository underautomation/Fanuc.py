import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.fdot_variable_type import FdotVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VcalVdVariableType as vcal_vd_variable_type

class VcalVdVariableType(GenericVariableType):
	'''Describes the Fanuc type VCAL_VD_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcal_vd_variable_type()
		else:
			self._instance = _internal

	@property
	def vprog_name(self) -> str:
		'''Value of variable VPROG_NAME'''
		return self._instance.VprogName

	@property
	def camera_name(self) -> str:
		'''Value of variable CAMERA_NAME'''
		return self._instance.CameraName

	@property
	def tool_type(self) -> int:
		'''Value of variable TOOL_TYPE'''
		return self._instance.ToolType

	@property
	def detect_type(self) -> int:
		'''Value of variable DETECT_TYPE'''
		return self._instance.DetectType

	@property
	def expo_time(self) -> int:
		'''Value of variable EXPO_TIME'''
		return self._instance.ExpoTime

	@property
	def num_mul_expo(self) -> int:
		'''Value of variable NUM_MUL_EXPO'''
		return self._instance.NumMulExpo

	@property
	def num_mep_usb(self) -> int:
		'''Value of variable NUM_MEP_USB'''
		return self._instance.NumMepUsb

	@property
	def vis_xyz(self) -> CartesianPositionVariable:
		'''Value of variable VIS_XYZ'''
		return CartesianPositionVariable(self._instance.VisXyz)

	@property
	def log_port(self) -> int:
		'''Value of variable LOG_PORT'''
		return self._instance.LogPort

	@property
	def focal_dist(self) -> float:
		'''Value of variable FOCAL_DIST'''
		return self._instance.FocalDist

	@property
	def grid_spacing(self) -> float:
		'''Value of variable GRID_SPACING'''
		return self._instance.GridSpacing

	@property
	def distort(self) -> typing.List[float]:
		'''Value of variable DISTORT'''
		return self._instance.Distort

	@property
	def ovrrd_focus(self) -> bool:
		'''Value of variable OVRRD_FOCUS'''
		return self._instance.OvrrdFocus

	@property
	def num_retry(self) -> int:
		'''Value of variable NUM_RETRY'''
		return self._instance.NumRetry

	@property
	def trim_ratio(self) -> float:
		'''Value of variable TRIM_RATIO'''
		return self._instance.TrimRatio

	@property
	def fdot_t(self) -> FdotVariableType:
		'''Value of variable FDOT_T'''
		return FdotVariableType(self._instance.FdotT)

	@property
	def led_type(self) -> int:
		'''Value of variable LED_TYPE'''
		return self._instance.LedType

	@property
	def led_intensit(self) -> int:
		'''Value of variable LED_INTENSIT'''
		return self._instance.LedIntensit

	@property
	def dummy18(self) -> int:
		'''Value of variable $DUMMY18'''
		return self._instance.Dummy18

	@property
	def dummy19(self) -> int:
		'''Value of variable $DUMMY19'''
		return self._instance.Dummy19

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VcalVdVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
