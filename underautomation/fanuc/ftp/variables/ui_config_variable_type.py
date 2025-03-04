import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UiConfigVariableType as ui_config_variable_type

class UiConfigVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_config_variable_type()
		else:
			self._instance = _internal
	@property
	def num_menus(self) -> int:
		return self._instance.NumMenus
	@property
	def num_connect(self) -> int:
		return self._instance.NumConnect
	@property
	def recovermenu(self) -> int:
		return self._instance.Recovermenu
	@property
	def color_crt(self) -> int:
		return self._instance.ColorCrt
	@property
	def topmenu_idx(self) -> int:
		return self._instance.TopmenuIdx
	@property
	def mem_limit(self) -> int:
		return self._instance.MemLimit
	@property
	def dbglvl(self) -> int:
		return self._instance.Dbglvl
	@property
	def popup_mask(self) -> int:
		return self._instance.PopupMask
	@property
	def extstatus(self) -> typing.List[int]:
		return self._instance.Extstatus
	@property
	def dummy73(self) -> int:
		return self._instance.Dummy73
	@property
	def mode(self) -> typing.List[int]:
		return self._instance.Mode
	@property
	def dummy74(self) -> int:
		return self._instance.Dummy74
	@property
	def focus(self) -> typing.List[int]:
		return self._instance.Focus
	@property
	def dummy75(self) -> int:
		return self._instance.Dummy75
	@property
	def config_chan(self) -> typing.List[int]:
		return self._instance.ConfigChan
	@property
	def timeout(self) -> int:
		return self._instance.Timeout
	@property
	def pipesize(self) -> int:
		return self._instance.Pipesize
	@property
	def mwin_limit(self) -> int:
		return self._instance.MwinLimit
	@property
	def panemap(self) -> typing.List[int]:
		return self._instance.Panemap
	@property
	def menu_favs(self) -> typing.List[str]:
		return self._instance.MenuFavs
	@property
	def hlpmen_dict(self) -> typing.List[str]:
		return self._instance.HlpmenDict
	@property
	def hlpmen_elem(self) -> typing.List[int]:
		return self._instance.HlpmenElem
	@property
	def hlpmen_url(self) -> typing.List[str]:
		return self._instance.HlpmenUrl
	@property
	def dspmen_mask(self) -> int:
		return self._instance.DspmenMask
	@property
	def hmi_mask(self) -> int:
		return self._instance.HmiMask
	@property
	def rotimeout(self) -> typing.List[int]:
		return self._instance.Rotimeout
	@property
	def readonly(self) -> typing.List[bool]:
		return self._instance.Readonly
	@property
	def touch_mask(self) -> int:
		return self._instance.TouchMask
	@property
	def prog_common(self) -> typing.List[str]:
		return self._instance.ProgCommon
	@property
	def alarm_mask(self) -> int:
		return self._instance.AlarmMask
	@property
	def filvew_mask(self) -> int:
		return self._instance.FilvewMask
	@property
	def enb_menufav(self) -> bool:
		return self._instance.EnbMenufav
	@property
	def enb_userfav(self) -> bool:
		return self._instance.EnbUserfav
	@property
	def enb_fctnfav(self) -> bool:
		return self._instance.EnbFctnfav
	@property
	def enb_wide(self) -> typing.List[bool]:
		return self._instance.EnbWide
	@property
	def icon_edit(self) -> typing.List[bool]:
		return self._instance.IconEdit
	@property
	def fctn_title(self) -> str:
		return self._instance.FctnTitle
	@property
	def enb_coordfv(self) -> bool:
		return self._instance.EnbCoordfv
	@property
	def lockmenufav(self) -> bool:
		return self._instance.Lockmenufav
	@property
	def lockuserfav(self) -> bool:
		return self._instance.Lockuserfav
	@property
	def enb_webform(self) -> bool:
		return self._instance.EnbWebform
	@property
	def coord_favs(self) -> typing.List[int]:
		return self._instance.CoordFavs
	@property
	def lockcoordfv(self) -> bool:
		return self._instance.Lockcoordfv
	@property
	def backcolor(self) -> int:
		return self._instance.Backcolor
	@property
	def lockbgcolor(self) -> bool:
		return self._instance.Lockbgcolor
	@property
	def color_inst(self) -> bool:
		return self._instance.ColorInst
	@property
	def iostat_inst(self) -> bool:
		return self._instance.IostatInst
	@property
	def pmn_max_pkt(self) -> int:
		return self._instance.PmnMaxPkt
	@property
	def ihelp_timer(self) -> int:
		return self._instance.IhelpTimer
	@property
	def blnk_timer(self) -> int:
		return self._instance.BlnkTimer
	@property
	def blnk_enable(self) -> bool:
		return self._instance.BlnkEnable
	@property
	def sipmanual(self) -> int:
		return self._instance.Sipmanual
	@property
	def blnk_alarm(self) -> bool:
		return self._instance.BlnkAlarm
	@property
	def touch_beep(self) -> bool:
		return self._instance.TouchBeep
	@property
	def enb_topmenu(self) -> bool:
		return self._instance.EnbTopmenu
	@property
	def enb_iconedt(self) -> typing.List[bool]:
		return self._instance.EnbIconedt
	@property
	def blink_icon(self) -> int:
		return self._instance.BlinkIcon
	@property
	def jwdog_timer(self) -> int:
		return self._instance.JwdogTimer
	@property
	def touch_dsbl(self) -> bool:
		return self._instance.TouchDsbl
	@property
	def cgtp_timer(self) -> int:
		return self._instance.CgtpTimer
	@property
	def itp_timer(self) -> int:
		return self._instance.ItpTimer
	@property
	def jcgtp_timer(self) -> int:
		return self._instance.JcgtpTimer
	@property
	def style(self) -> int:
		return self._instance.Style
	@property
	def iedit_style(self) -> int:
		return self._instance.IeditStyle
	@property
	def editor_fkey(self) -> int:
		return self._instance.EditorFkey
	@property
	def iedit_html5(self) -> int:
		return self._instance.IeditHtml5
	@property
	def dsp_name(self) -> str:
		return self._instance.DspName
	@property
	def dim_timer(self) -> int:
		return self._instance.DimTimer
	@property
	def dim_bright(self) -> int:
		return self._instance.DimBright
	@property
	def on_bright(self) -> int:
		return self._instance.OnBright
	@property
	def blnk_tch(self) -> int:
		return self._instance.BlnkTch
	@property
	def enb_html5(self) -> int:
		return self._instance.EnbHtml5
	@property
	def bt_device(self) -> int:
		return self._instance.BtDevice
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
