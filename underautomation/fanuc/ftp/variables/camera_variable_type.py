import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CameraVariableType as camera_variable_type

class CameraVariableType(GenericVariableType):
	'''Describes the Fanuc type $CAMERA'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = camera_variable_type()
		else:
			self._instance = _internal

	@property
	def vision_type(self) -> int:
		'''Value of variable $VISION_TYPE'''
		return self._instance.VisionType

	@property
	def camera_type(self) -> int:
		'''Value of variable $CAMERA_TYPE'''
		return self._instance.CameraType

	@property
	def camera_port(self) -> int:
		'''Value of variable $CAMERA_PORT'''
		return self._instance.CameraPort

	@property
	def detect_type(self) -> int:
		'''Value of variable $DETECT_TYPE'''
		return self._instance.DetectType

	@property
	def drive_type(self) -> int:
		'''Value of variable $DRIVE_TYPE'''
		return self._instance.DriveType

	@property
	def set_vtcp(self) -> int:
		'''Value of variable $SET_VTCP'''
		return self._instance.SetVtcp

	@property
	def debug_code(self) -> int:
		'''Value of variable $DEBUG_CODE'''
		return self._instance.DebugCode

	@property
	def dmy_ubyte(self) -> int:
		'''Value of variable $DMY_UBYTE'''
		return self._instance.DmyUbyte

	@property
	def camera_name(self) -> str:
		'''Value of variable $CAMERA_NAME'''
		return self._instance.CameraName

	@property
	def tool_type(self) -> int:
		'''Value of variable $TOOL_TYPE'''
		return self._instance.ToolType

	@property
	def distortion1(self) -> float:
		'''Value of variable $DISTORTION1'''
		return self._instance.Distortion1

	@property
	def distortion2(self) -> float:
		'''Value of variable $DISTORTION2'''
		return self._instance.Distortion2

	@property
	def disp_scale(self) -> int:
		'''Value of variable $DISP_SCALE'''
		return self._instance.DispScale

	@property
	def disp_lut(self) -> bool:
		'''Value of variable $DISP_LUT'''
		return self._instance.DispLut

	@property
	def output_bmp(self) -> bool:
		'''Value of variable $OUTPUT_BMP'''
		return self._instance.OutputBmp

	@property
	def handeye(self) -> bool:
		'''Value of variable $HANDEYE'''
		return self._instance.Handeye

	@property
	def expos_time(self) -> int:
		'''Value of variable $EXPOS_TIME'''
		return self._instance.ExposTime

	@property
	def num_mul_exp(self) -> int:
		'''Value of variable $NUM_MUL_EXP'''
		return self._instance.NumMulExp

	@property
	def num_mep_usb(self) -> int:
		'''Value of variable $NUM_MEP_USB'''
		return self._instance.NumMepUsb

	@property
	def trim_ratio(self) -> float:
		'''Value of variable $TRIM_RATIO'''
		return self._instance.TrimRatio

	@property
	def focal_dist(self) -> float:
		'''Value of variable $FOCAL_DIST'''
		return self._instance.FocalDist

	@property
	def gd_spacing(self) -> float:
		'''Value of variable $GD_SPACING'''
		return self._instance.GdSpacing

	@property
	def trgt_dist(self) -> float:
		'''Value of variable $TRGT_DIST'''
		return self._instance.TrgtDist

	@property
	def trgt_w(self) -> float:
		'''Value of variable $TRGT_W'''
		return self._instance.TrgtW

	@property
	def trgt_p(self) -> float:
		'''Value of variable $TRGT_P'''
		return self._instance.TrgtP

	@property
	def trgt_r(self) -> float:
		'''Value of variable $TRGT_R'''
		return self._instance.TrgtR

	@property
	def num_retry(self) -> int:
		'''Value of variable $NUM_RETRY'''
		return self._instance.NumRetry

	@property
	def utool(self) -> typing.List[float]:
		'''Value of variable $UTOOL'''
		return self._instance.Utool

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CameraVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
