import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UiConfigVariableType as ui_config_variable_type

class UiConfigVariableType(GenericVariableType):
	'''Describes the Fanuc type UI_CONFIG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_config_variable_type()
		else:
			self._instance = _internal

	@property
	def num_menus(self) -> int:
		'''Value of variable $NUM_MENUS'''
		return self._instance.NumMenus

	@property
	def num_connect(self) -> int:
		'''Value of variable $NUM_CONNECT'''
		return self._instance.NumConnect

	@property
	def recovermenu(self) -> int:
		'''Value of variable $RECOVERMENU'''
		return self._instance.Recovermenu

	@property
	def color_crt(self) -> int:
		'''Value of variable $COLOR_CRT'''
		return self._instance.ColorCrt

	@property
	def topmenu_idx(self) -> int:
		'''Value of variable $TOPMENU_IDX'''
		return self._instance.TopmenuIdx

	@property
	def mem_limit(self) -> int:
		'''Value of variable $MEM_LIMIT'''
		return self._instance.MemLimit

	@property
	def dbglvl(self) -> int:
		'''Value of variable $DBGLVL'''
		return self._instance.Dbglvl

	@property
	def popup_mask(self) -> int:
		'''Value of variable $POPUP_MASK'''
		return self._instance.PopupMask

	@property
	def extstatus(self) -> typing.List[int]:
		'''Value of variable $EXTSTATUS'''
		return self._instance.Extstatus

	@property
	def dummy73(self) -> int:
		'''Value of variable $DUMMY73'''
		return self._instance.Dummy73

	@property
	def mode(self) -> typing.List[int]:
		'''Value of variable $MODE'''
		return self._instance.Mode

	@property
	def dummy74(self) -> int:
		'''Value of variable $DUMMY74'''
		return self._instance.Dummy74

	@property
	def focus(self) -> typing.List[int]:
		'''Value of variable $FOCUS'''
		return self._instance.Focus

	@property
	def dummy75(self) -> int:
		'''Value of variable $DUMMY75'''
		return self._instance.Dummy75

	@property
	def config_chan(self) -> typing.List[int]:
		'''Value of variable $CONFIG_CHAN'''
		return self._instance.ConfigChan

	@property
	def timeout(self) -> int:
		'''Value of variable $TIMEOUT'''
		return self._instance.Timeout

	@property
	def pipesize(self) -> int:
		'''Value of variable $PIPESIZE'''
		return self._instance.Pipesize

	@property
	def mwin_limit(self) -> int:
		'''Value of variable $MWIN_LIMIT'''
		return self._instance.MwinLimit

	@property
	def panemap(self) -> typing.List[int]:
		'''Value of variable $PANEMAP'''
		return self._instance.Panemap

	@property
	def menu_favs(self) -> typing.List[str]:
		'''Value of variable $MENU_FAVS'''
		return self._instance.MenuFavs

	@property
	def hlpmen_dict(self) -> typing.List[str]:
		'''Value of variable $HLPMEN_DICT'''
		return self._instance.HlpmenDict

	@property
	def hlpmen_elem(self) -> typing.List[int]:
		'''Value of variable $HLPMEN_ELEM'''
		return self._instance.HlpmenElem

	@property
	def hlpmen_url(self) -> typing.List[str]:
		'''Value of variable $HLPMEN_URL'''
		return self._instance.HlpmenUrl

	@property
	def dspmen_mask(self) -> int:
		'''Value of variable $DSPMEN_MASK'''
		return self._instance.DspmenMask

	@property
	def hmi_mask(self) -> int:
		'''Value of variable $HMI_MASK'''
		return self._instance.HmiMask

	@property
	def rotimeout(self) -> typing.List[int]:
		'''Value of variable $ROTIMEOUT'''
		return self._instance.Rotimeout

	@property
	def readonly(self) -> typing.List[bool]:
		'''Value of variable $READONLY'''
		return self._instance.Readonly

	@property
	def touch_mask(self) -> int:
		'''Value of variable $TOUCH_MASK'''
		return self._instance.TouchMask

	@property
	def prog_common(self) -> typing.List[str]:
		'''Value of variable $PROG_COMMON'''
		return self._instance.ProgCommon

	@property
	def alarm_mask(self) -> int:
		'''Value of variable $ALARM_MASK'''
		return self._instance.AlarmMask

	@property
	def filvew_mask(self) -> int:
		'''Value of variable $FILVEW_MASK'''
		return self._instance.FilvewMask

	@property
	def enb_menufav(self) -> bool:
		'''Value of variable $ENB_MENUFAV'''
		return self._instance.EnbMenufav

	@property
	def enb_userfav(self) -> bool:
		'''Value of variable $ENB_USERFAV'''
		return self._instance.EnbUserfav

	@property
	def enb_fctnfav(self) -> bool:
		'''Value of variable $ENB_FCTNFAV'''
		return self._instance.EnbFctnfav

	@property
	def enb_wide(self) -> typing.List[bool]:
		'''Value of variable $ENB_WIDE'''
		return self._instance.EnbWide

	@property
	def icon_edit(self) -> typing.List[bool]:
		'''Value of variable $ICON_EDIT'''
		return self._instance.IconEdit

	@property
	def fctn_title(self) -> str:
		'''Value of variable $FCTN_TITLE'''
		return self._instance.FctnTitle

	@property
	def enb_coordfv(self) -> bool:
		'''Value of variable $ENB_COORDFV'''
		return self._instance.EnbCoordfv

	@property
	def lockmenufav(self) -> bool:
		'''Value of variable $LOCKMENUFAV'''
		return self._instance.Lockmenufav

	@property
	def lockuserfav(self) -> bool:
		'''Value of variable $LOCKUSERFAV'''
		return self._instance.Lockuserfav

	@property
	def enb_webform(self) -> bool:
		'''Value of variable $ENB_WEBFORM'''
		return self._instance.EnbWebform

	@property
	def coord_favs(self) -> typing.List[int]:
		'''Value of variable $COORD_FAVS'''
		return self._instance.CoordFavs

	@property
	def lockcoordfv(self) -> bool:
		'''Value of variable $LOCKCOORDFV'''
		return self._instance.Lockcoordfv

	@property
	def backcolor(self) -> int:
		'''Value of variable $BACKCOLOR'''
		return self._instance.Backcolor

	@property
	def lockbgcolor(self) -> bool:
		'''Value of variable $LOCKBGCOLOR'''
		return self._instance.Lockbgcolor

	@property
	def color_inst(self) -> bool:
		'''Value of variable $COLOR_INST'''
		return self._instance.ColorInst

	@property
	def iostat_inst(self) -> bool:
		'''Value of variable $IOSTAT_INST'''
		return self._instance.IostatInst

	@property
	def pmn_max_pkt(self) -> int:
		'''Value of variable $PMN_MAX_PKT'''
		return self._instance.PmnMaxPkt

	@property
	def ihelp_timer(self) -> int:
		'''Value of variable $IHELP_TIMER'''
		return self._instance.IhelpTimer

	@property
	def blnk_timer(self) -> int:
		'''Value of variable $BLNK_TIMER'''
		return self._instance.BlnkTimer

	@property
	def blnk_enable(self) -> bool:
		'''Value of variable $BLNK_ENABLE'''
		return self._instance.BlnkEnable

	@property
	def sipmanual(self) -> int:
		'''Value of variable $SIPMANUAL'''
		return self._instance.Sipmanual

	@property
	def blnk_alarm(self) -> bool:
		'''Value of variable $BLNK_ALARM'''
		return self._instance.BlnkAlarm

	@property
	def touch_beep(self) -> bool:
		'''Value of variable $TOUCH_BEEP'''
		return self._instance.TouchBeep

	@property
	def enb_topmenu(self) -> bool:
		'''Value of variable $ENB_TOPMENU'''
		return self._instance.EnbTopmenu

	@property
	def enb_iconedt(self) -> typing.List[bool]:
		'''Value of variable $ENB_ICONEDT'''
		return self._instance.EnbIconedt

	@property
	def blink_icon(self) -> int:
		'''Value of variable $BLINK_ICON'''
		return self._instance.BlinkIcon

	@property
	def jwdog_timer(self) -> int:
		'''Value of variable $JWDOG_TIMER'''
		return self._instance.JwdogTimer

	@property
	def touch_dsbl(self) -> bool:
		'''Value of variable $TOUCH_DSBL'''
		return self._instance.TouchDsbl

	@property
	def cgtp_timer(self) -> int:
		'''Value of variable $CGTP_TIMER'''
		return self._instance.CgtpTimer

	@property
	def itp_timer(self) -> int:
		'''Value of variable $ITP_TIMER'''
		return self._instance.ItpTimer

	@property
	def jcgtp_timer(self) -> int:
		'''Value of variable $JCGTP_TIMER'''
		return self._instance.JcgtpTimer

	@property
	def style(self) -> int:
		'''Value of variable $STYLE'''
		return self._instance.Style

	@property
	def iedit_style(self) -> int:
		'''Value of variable $IEDIT_STYLE'''
		return self._instance.IeditStyle

	@property
	def editor_fkey(self) -> int:
		'''Value of variable $EDITOR_FKEY'''
		return self._instance.EditorFkey

	@property
	def iedit_html5(self) -> int:
		'''Value of variable $IEDIT_HTML5'''
		return self._instance.IeditHtml5

	@property
	def dsp_name(self) -> str:
		'''Value of variable $DSP_NAME'''
		return self._instance.DspName

	@property
	def dim_timer(self) -> int:
		'''Value of variable $DIM_TIMER'''
		return self._instance.DimTimer

	@property
	def dim_bright(self) -> int:
		'''Value of variable $DIM_BRIGHT'''
		return self._instance.DimBright

	@property
	def on_bright(self) -> int:
		'''Value of variable $ON_BRIGHT'''
		return self._instance.OnBright

	@property
	def blnk_tch(self) -> int:
		'''Value of variable $BLNK_TCH'''
		return self._instance.BlnkTch

	@property
	def enb_html5(self) -> int:
		'''Value of variable $ENB_HTML5'''
		return self._instance.EnbHtml5

	@property
	def bt_device(self) -> int:
		'''Value of variable $BT_DEVICE'''
		return self._instance.BtDevice

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UiConfigVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
