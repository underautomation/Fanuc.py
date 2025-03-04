import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CameraVariableType as camera_variable_type

class CameraVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = camera_variable_type()
		else:
			self._instance = _internal
	@property
	def vision_type(self) -> int:
		return self._instance.VisionType
	@property
	def camera_type(self) -> int:
		return self._instance.CameraType
	@property
	def camera_port(self) -> int:
		return self._instance.CameraPort
	@property
	def detect_type(self) -> int:
		return self._instance.DetectType
	@property
	def drive_type(self) -> int:
		return self._instance.DriveType
	@property
	def set_vtcp(self) -> int:
		return self._instance.SetVtcp
	@property
	def debug_code(self) -> int:
		return self._instance.DebugCode
	@property
	def dmy_ubyte(self) -> int:
		return self._instance.DmyUbyte
	@property
	def camera_name(self) -> str:
		return self._instance.CameraName
	@property
	def tool_type(self) -> int:
		return self._instance.ToolType
	@property
	def distortion1(self) -> float:
		return self._instance.Distortion1
	@property
	def distortion2(self) -> float:
		return self._instance.Distortion2
	@property
	def disp_scale(self) -> int:
		return self._instance.DispScale
	@property
	def disp_lut(self) -> bool:
		return self._instance.DispLut
	@property
	def output_bmp(self) -> bool:
		return self._instance.OutputBmp
	@property
	def handeye(self) -> bool:
		return self._instance.Handeye
	@property
	def expos_time(self) -> int:
		return self._instance.ExposTime
	@property
	def num_mul_exp(self) -> int:
		return self._instance.NumMulExp
	@property
	def num_mep_usb(self) -> int:
		return self._instance.NumMepUsb
	@property
	def trim_ratio(self) -> float:
		return self._instance.TrimRatio
	@property
	def focal_dist(self) -> float:
		return self._instance.FocalDist
	@property
	def gd_spacing(self) -> float:
		return self._instance.GdSpacing
	@property
	def trgt_dist(self) -> float:
		return self._instance.TrgtDist
	@property
	def trgt_w(self) -> float:
		return self._instance.TrgtW
	@property
	def trgt_p(self) -> float:
		return self._instance.TrgtP
	@property
	def trgt_r(self) -> float:
		return self._instance.TrgtR
	@property
	def num_retry(self) -> int:
		return self._instance.NumRetry
	@property
	def utool(self) -> typing.List[float]:
		return self._instance.Utool
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
