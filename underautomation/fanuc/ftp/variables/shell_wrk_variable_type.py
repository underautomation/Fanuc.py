import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ShellWrkVariableType as shell_wrk_variable_type

class ShellWrkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell_wrk_variable_type()
		else:
			self._instance = _internal
	@property
	def rout_name(self) -> str:
		return self._instance.RoutName
	@property
	def curr_line(self) -> int:
		return self._instance.CurrLine
	@property
	def task_num(self) -> int:
		return self._instance.TaskNum
	@property
	def by_manual(self) -> bool:
		return self._instance.ByManual
	@property
	def wrk_busy(self) -> bool:
		return self._instance.WrkBusy
	@property
	def shell_start(self) -> bool:
		return self._instance.ShellStart
	@property
	def karel_uop(self) -> bool:
		return self._instance.KarelUop
	@property
	def karel_sop(self) -> bool:
		return self._instance.KarelSop
	@property
	def rsr_stat_p(self) -> int:
		return self._instance.RsrStatP
	@property
	def isol_mode(self) -> bool:
		return self._instance.IsolMode
	@property
	def cur_style(self) -> int:
		return self._instance.CurStyle
	@property
	def cur_option(self) -> int:
		return self._instance.CurOption
	@property
	def cur_opta(self) -> int:
		return self._instance.CurOpta
	@property
	def cur_optb(self) -> int:
		return self._instance.CurOptb
	@property
	def cur_optc(self) -> int:
		return self._instance.CurOptc
	@property
	def cur_decsn(self) -> int:
		return self._instance.CurDecsn
	@property
	def man_style(self) -> int:
		return self._instance.ManStyle
	@property
	def man_option(self) -> int:
		return self._instance.ManOption
	@property
	def man_opta(self) -> int:
		return self._instance.ManOpta
	@property
	def man_optb(self) -> int:
		return self._instance.ManOptb
	@property
	def man_optc(self) -> int:
		return self._instance.ManOptc
	@property
	def man_decsn(self) -> int:
		return self._instance.ManDecsn
	@property
	def chk_raw(self) -> int:
		return self._instance.ChkRaw
	@property
	def chk_stat(self) -> int:
		return self._instance.ChkStat
	@property
	def chk_force(self) -> int:
		return self._instance.ChkForce
	@property
	def chk_ignore(self) -> int:
		return self._instance.ChkIgnore
	@property
	def karel_iouop(self) -> bool:
		return self._instance.KarelIouop
	@property
	def cust_name(self) -> str:
		return self._instance.CustName
	@property
	def cell_mode(self) -> int:
		return self._instance.CellMode
	@property
	def tryout_mode(self) -> bool:
		return self._instance.TryoutMode
	@property
	def cust_start(self) -> bool:
		return self._instance.CustStart
	@property
	def remote_key(self) -> bool:
		return self._instance.RemoteKey
	@property
	def strtchk_ept(self) -> int:
		return self._instance.StrtchkEpt
	@property
	def ps_strtchk(self) -> int:
		return self._instance.PsStrtchk
	@property
	def strtchk_lin(self) -> int:
		return self._instance.StrtchkLin
	@property
	def cyctsk_num(self) -> int:
		return self._instance.CyctskNum
	@property
	def activeprog(self) -> str:
		return self._instance.Activeprog
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
