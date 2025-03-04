import typing
from underautomation.fanuc.ftp.variables.tpgl_uview_variable_type import TpglUviewVariableType
from underautomation.fanuc.ftp.variables.tpgl_cam_variable_type import TpglCamVariableType
from underautomation.fanuc.ftp.variables.tpgl_view_variable_type import TpglViewVariableType
from underautomation.fanuc.ftp.variables.jog_rad_variable_type import JogRadVariableType
from underautomation.fanuc.ftp.variables.tpgl_mset_variable_type import TpglMsetVariableType
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpglConfVariableType as tpgl_conf_variable_type

class TpglConfVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpgl_conf_variable_type()
		else:
			self._instance = _internal
	@property
	def mount(self) -> typing.List[str]:
		return self._instance.Mount
	@property
	def lock_follow(self) -> bool:
		return self._instance.LockFollow
	@property
	def dbglvl(self) -> int:
		return self._instance.Dbglvl
	@property
	def gldbglvl(self) -> int:
		return self._instance.Gldbglvl
	@property
	def test_xml(self) -> str:
		return self._instance.TestXml
	@property
	def tempint(self) -> typing.List[int]:
		return self._instance.Tempint
	@property
	def tempstr(self) -> typing.List[str]:
		return self._instance.Tempstr
	@property
	def user_views(self) -> typing.List[TpglUviewVariableType]:
		return [TpglUviewVariableType(x) for x in self._instance.UserViews]
	@property
	def cameras(self) -> typing.List[TpglCamVariableType]:
		return [TpglCamVariableType(x) for x in self._instance.Cameras]
	@property
	def temp_locs(self) -> typing.List[TpglViewVariableType]:
		return [TpglViewVariableType(x) for x in self._instance.TempLocs]
	@property
	def scene_view(self) -> typing.List[TpglViewVariableType]:
		return [TpglViewVariableType(x) for x in self._instance.SceneView]
	@property
	def karel_tmo(self) -> int:
		return self._instance.KarelTmo
	@property
	def tpdraw_tmo(self) -> int:
		return self._instance.TpdrawTmo
	@property
	def jog_veclen(self) -> int:
		return self._instance.JogVeclen
	@property
	def jog_radius(self) -> typing.List[JogRadVariableType]:
		return [JogRadVariableType(x) for x in self._instance.JogRadius]
	@property
	def check_tools(self) -> int:
		return self._instance.CheckTools
	@property
	def check_vis(self) -> int:
		return self._instance.CheckVis
	@property
	def reg_vis32(self) -> int:
		return self._instance.RegVis32
	@property
	def reg_vis64(self) -> int:
		return self._instance.RegVis64
	@property
	def machset(self) -> typing.List[TpglMsetVariableType]:
		return [TpglMsetVariableType(x) for x in self._instance.Machset]
	@property
	def cont_idx(self) -> int:
		return self._instance.ContIdx
	@property
	def dummy31(self) -> int:
		return self._instance.Dummy31
	@property
	def visible(self) -> typing.List[int]:
		return self._instance.Visible
	@property
	def rail_boxes(self) -> typing.List[int]:
		return self._instance.RailBoxes
	@property
	def robot_xml(self) -> typing.List[str]:
		return self._instance.RobotXml
	@property
	def showwarn(self) -> typing.List[int]:
		return self._instance.Showwarn
	@property
	def controlmax(self) -> int:
		return self._instance.Controlmax
	@property
	def controlmask(self) -> typing.List[int]:
		return self._instance.Controlmask
	@property
	def fp_to_fk(self) -> typing.List[CartesianPositionVariable]:
		return [CartesianPositionVariable(x) for x in self._instance.FpToFk]
	@property
	def html5_enbl(self) -> bool:
		return self._instance.Html5Enbl
	@property
	def update_mint(self) -> int:
		return self._instance.UpdateMint
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
