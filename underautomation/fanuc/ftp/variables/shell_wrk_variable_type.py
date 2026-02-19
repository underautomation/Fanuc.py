import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ShellWrkVariableType as shell_wrk_variable_type

class ShellWrkVariableType(GenericVariableType):
	'''Describes the Fanuc type SHELL_WRK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell_wrk_variable_type()
		else:
			self._instance = _internal

	@property
	def rout_name(self) -> str:
		'''Value of variable $ROUT_NAME'''
		return self._instance.RoutName

	@property
	def curr_line(self) -> int:
		'''Value of variable $CURR_LINE'''
		return self._instance.CurrLine

	@property
	def task_num(self) -> int:
		'''Value of variable $TASK_NUM'''
		return self._instance.TaskNum

	@property
	def by_manual(self) -> bool:
		'''Value of variable $BY_MANUAL'''
		return self._instance.ByManual

	@property
	def wrk_busy(self) -> bool:
		'''Value of variable $WRK_BUSY'''
		return self._instance.WrkBusy

	@property
	def shell_start(self) -> bool:
		'''Value of variable $SHELL_START'''
		return self._instance.ShellStart

	@property
	def karel_uop(self) -> bool:
		'''Value of variable $KAREL_UOP'''
		return self._instance.KarelUop

	@property
	def karel_sop(self) -> bool:
		'''Value of variable $KAREL_SOP'''
		return self._instance.KarelSop

	@property
	def rsr_stat_p(self) -> int:
		'''Value of variable $RSR_STAT_P'''
		return self._instance.RsrStatP

	@property
	def isol_mode(self) -> bool:
		'''Value of variable $ISOL_MODE'''
		return self._instance.IsolMode

	@property
	def cur_style(self) -> int:
		'''Value of variable $CUR_STYLE'''
		return self._instance.CurStyle

	@property
	def cur_option(self) -> int:
		'''Value of variable $CUR_OPTION'''
		return self._instance.CurOption

	@property
	def cur_opta(self) -> int:
		'''Value of variable $CUR_OPTA'''
		return self._instance.CurOpta

	@property
	def cur_optb(self) -> int:
		'''Value of variable $CUR_OPTB'''
		return self._instance.CurOptb

	@property
	def cur_optc(self) -> int:
		'''Value of variable $CUR_OPTC'''
		return self._instance.CurOptc

	@property
	def cur_decsn(self) -> int:
		'''Value of variable $CUR_DECSN'''
		return self._instance.CurDecsn

	@property
	def man_style(self) -> int:
		'''Value of variable $MAN_STYLE'''
		return self._instance.ManStyle

	@property
	def man_option(self) -> int:
		'''Value of variable $MAN_OPTION'''
		return self._instance.ManOption

	@property
	def man_opta(self) -> int:
		'''Value of variable $MAN_OPTA'''
		return self._instance.ManOpta

	@property
	def man_optb(self) -> int:
		'''Value of variable $MAN_OPTB'''
		return self._instance.ManOptb

	@property
	def man_optc(self) -> int:
		'''Value of variable $MAN_OPTC'''
		return self._instance.ManOptc

	@property
	def man_decsn(self) -> int:
		'''Value of variable $MAN_DECSN'''
		return self._instance.ManDecsn

	@property
	def chk_raw(self) -> int:
		'''Value of variable $CHK_RAW'''
		return self._instance.ChkRaw

	@property
	def chk_stat(self) -> int:
		'''Value of variable $CHK_STAT'''
		return self._instance.ChkStat

	@property
	def chk_force(self) -> int:
		'''Value of variable $CHK_FORCE'''
		return self._instance.ChkForce

	@property
	def chk_ignore(self) -> int:
		'''Value of variable $CHK_IGNORE'''
		return self._instance.ChkIgnore

	@property
	def karel_iouop(self) -> bool:
		'''Value of variable $KAREL_IOUOP'''
		return self._instance.KarelIouop

	@property
	def cust_name(self) -> str:
		'''Value of variable $CUST_NAME'''
		return self._instance.CustName

	@property
	def cell_mode(self) -> int:
		'''Value of variable $CELL_MODE'''
		return self._instance.CellMode

	@property
	def tryout_mode(self) -> bool:
		'''Value of variable $TRYOUT_MODE'''
		return self._instance.TryoutMode

	@property
	def cust_start(self) -> bool:
		'''Value of variable $CUST_START'''
		return self._instance.CustStart

	@property
	def remote_key(self) -> bool:
		'''Value of variable $REMOTE_KEY'''
		return self._instance.RemoteKey

	@property
	def strtchk_ept(self) -> int:
		'''Value of variable $STRTCHK_EPT'''
		return self._instance.StrtchkEpt

	@property
	def ps_strtchk(self) -> int:
		'''Value of variable $PS_STRTCHK_'''
		return self._instance.PsStrtchk

	@property
	def strtchk_lin(self) -> int:
		'''Value of variable $STRTCHK_LIN'''
		return self._instance.StrtchkLin

	@property
	def cyctsk_num(self) -> int:
		'''Value of variable $CYCTSK_NUM'''
		return self._instance.CyctskNum

	@property
	def activeprog(self) -> str:
		'''Value of variable $ACTIVEPROG'''
		return self._instance.Activeprog

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ShellWrkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
