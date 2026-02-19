import typing
from underautomation.fanuc.ftp.variables.tpgl_uview_variable_type import TpglUviewVariableType
from underautomation.fanuc.ftp.variables.tpgl_cam_variable_type import TpglCamVariableType
from underautomation.fanuc.ftp.variables.tpgl_view_variable_type import TpglViewVariableType
from underautomation.fanuc.ftp.variables.jog_rad_variable_type import JogRadVariableType
from underautomation.fanuc.ftp.variables.tpgl_mset_variable_type import TpglMsetVariableType
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TpglConfVariableType as tpgl_conf_variable_type

class TpglConfVariableType(GenericVariableType):
	'''Describes the Fanuc type TPGL_CONF_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpgl_conf_variable_type()
		else:
			self._instance = _internal

	@property
	def mount(self) -> typing.List[str]:
		'''Value of variable $MOUNT'''
		return self._instance.Mount

	@property
	def lock_follow(self) -> bool:
		'''Value of variable $LOCK_FOLLOW'''
		return self._instance.LockFollow

	@property
	def dbglvl(self) -> int:
		'''Value of variable $DBGLVL'''
		return self._instance.Dbglvl

	@property
	def gldbglvl(self) -> int:
		'''Value of variable $GLDBGLVL'''
		return self._instance.Gldbglvl

	@property
	def test_xml(self) -> str:
		'''Value of variable $TEST_XML'''
		return self._instance.TestXml

	@property
	def tempint(self) -> typing.List[int]:
		'''Value of variable $TEMPINT'''
		return self._instance.Tempint

	@property
	def tempstr(self) -> typing.List[str]:
		'''Value of variable $TEMPSTR'''
		return self._instance.Tempstr

	@property
	def user_views(self) -> typing.List[TpglUviewVariableType]:
		'''Value of variable $USER_VIEWS'''
		return [TpglUviewVariableType(x) for x in self._instance.UserViews]

	@property
	def cameras(self) -> typing.List[TpglCamVariableType]:
		'''Value of variable $CAMERAS'''
		return [TpglCamVariableType(x) for x in self._instance.Cameras]

	@property
	def temp_locs(self) -> typing.List[TpglViewVariableType]:
		'''Value of variable $TEMP_LOCS'''
		return [TpglViewVariableType(x) for x in self._instance.TempLocs]

	@property
	def scene_view(self) -> typing.List[TpglViewVariableType]:
		'''Value of variable $SCENE_VIEW'''
		return [TpglViewVariableType(x) for x in self._instance.SceneView]

	@property
	def karel_tmo(self) -> int:
		'''Value of variable $KAREL_TMO'''
		return self._instance.KarelTmo

	@property
	def tpdraw_tmo(self) -> int:
		'''Value of variable $TPDRAW_TMO'''
		return self._instance.TpdrawTmo

	@property
	def jog_veclen(self) -> int:
		'''Value of variable $JOG_VECLEN'''
		return self._instance.JogVeclen

	@property
	def jog_radius(self) -> typing.List[JogRadVariableType]:
		'''Value of variable $JOG_RADIUS'''
		return [JogRadVariableType(x) for x in self._instance.JogRadius]

	@property
	def check_tools(self) -> int:
		'''Value of variable $CHECK_TOOLS'''
		return self._instance.CheckTools

	@property
	def check_vis(self) -> int:
		'''Value of variable $CHECK_VIS'''
		return self._instance.CheckVis

	@property
	def reg_vis32(self) -> int:
		'''Value of variable $REG_VIS32'''
		return self._instance.RegVis32

	@property
	def reg_vis64(self) -> int:
		'''Value of variable $REG_VIS64'''
		return self._instance.RegVis64

	@property
	def machset(self) -> typing.List[TpglMsetVariableType]:
		'''Value of variable $MACHSET'''
		return [TpglMsetVariableType(x) for x in self._instance.Machset]

	@property
	def cont_idx(self) -> int:
		'''Value of variable $CONT_IDX'''
		return self._instance.ContIdx

	@property
	def dummy31(self) -> int:
		'''Value of variable $DUMMY31'''
		return self._instance.Dummy31

	@property
	def visible(self) -> typing.List[int]:
		'''Value of variable $VISIBLE'''
		return self._instance.Visible

	@property
	def rail_boxes(self) -> typing.List[int]:
		'''Value of variable $RAIL_BOXES'''
		return self._instance.RailBoxes

	@property
	def robot_xml(self) -> typing.List[str]:
		'''Value of variable $ROBOT_XML'''
		return self._instance.RobotXml

	@property
	def showwarn(self) -> typing.List[int]:
		'''Value of variable $SHOWWARN'''
		return self._instance.Showwarn

	@property
	def controlmax(self) -> int:
		'''Value of variable $CONTROLMAX'''
		return self._instance.Controlmax

	@property
	def controlmask(self) -> typing.List[int]:
		'''Value of variable $CONTROLMASK'''
		return self._instance.Controlmask

	@property
	def fp_to_fk(self) -> typing.List[CartesianPositionVariable]:
		'''Value of variable $FP_TO_FK'''
		return [CartesianPositionVariable(x) for x in self._instance.FpToFk]

	@property
	def html5_enbl(self) -> bool:
		'''Value of variable $HTML5_ENBL'''
		return self._instance.Html5Enbl

	@property
	def update_mint(self) -> int:
		'''Value of variable $UPDATE_MINT'''
		return self._instance.UpdateMint

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpglConfVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
