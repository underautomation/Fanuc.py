import typing
from underautomation.fanuc.ftp.variables.pinfo_variable_type import PinfoVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RcmcfgVariableType as rcmcfg_variable_type

class RcmcfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rcmcfg_variable_type()
		else:
			self._instance = _internal
	@property
	def rcm_enable(self) -> bool:
		return self._instance.RcmEnable
	@property
	def qsize(self) -> int:
		return self._instance.Qsize
	@property
	def timer(self) -> int:
		return self._instance.Timer
	@property
	def status_time(self) -> int:
		return self._instance.StatusTime
	@property
	def mailserv(self) -> str:
		return self._instance.Mailserv
	@property
	def plant(self) -> str:
		return self._instance.Plant
	@property
	def line(self) -> str:
		return self._instance.Line
	@property
	def cluster(self) -> str:
		return self._instance.Cluster
	@property
	def toaddr(self) -> str:
		return self._instance.Toaddr
	@property
	def ccaddr(self) -> str:
		return self._instance.Ccaddr
	@property
	def fraddr(self) -> str:
		return self._instance.Fraddr
	@property
	def subject(self) -> str:
		return self._instance.Subject
	@property
	def status_enb(self) -> bool:
		return self._instance.StatusEnb
	@property
	def alarm_enb(self) -> bool:
		return self._instance.AlarmEnb
	@property
	def tplog_enb(self) -> bool:
		return self._instance.TplogEnb
	@property
	def varlog_enb(self) -> bool:
		return self._instance.VarlogEnb
	@property
	def motion_enb(self) -> bool:
		return self._instance.MotionEnb
	@property
	def system_enb(self) -> bool:
		return self._instance.SystemEnb
	@property
	def appl_enb(self) -> bool:
		return self._instance.ApplEnb
	@property
	def pass_enb(self) -> bool:
		return self._instance.PassEnb
	@property
	def comm_enb(self) -> bool:
		return self._instance.CommEnb
	@property
	def port(self) -> int:
		return self._instance.Port
	@property
	def stat_subj(self) -> str:
		return self._instance.StatSubj
	@property
	def alertaddr(self) -> str:
		return self._instance.Alertaddr
	@property
	def alerturl(self) -> str:
		return self._instance.Alerturl
	@property
	def stat_attach(self) -> str:
		return self._instance.StatAttach
	@property
	def err_throt(self) -> int:
		return self._instance.ErrThrot
	@property
	def usr_throt(self) -> int:
		return self._instance.UsrThrot
	@property
	def size_throt(self) -> int:
		return self._instance.SizeThrot
	@property
	def varchg_time(self) -> int:
		return self._instance.VarchgTime
	@property
	def varchg_max(self) -> int:
		return self._instance.VarchgMax
	@property
	def ws_url(self) -> str:
		return self._instance.WsUrl
	@property
	def ws_mode(self) -> bool:
		return self._instance.WsMode
	@property
	def ws_uid(self) -> str:
		return self._instance.WsUid
	@property
	def ws_user(self) -> str:
		return self._instance.WsUser
	@property
	def last_err(self) -> int:
		return self._instance.LastErr
	@property
	def snd_maxtry(self) -> int:
		return self._instance.SndMaxtry
	@property
	def snd_delay(self) -> int:
		return self._instance.SndDelay
	@property
	def ws_qsize(self) -> int:
		return self._instance.WsQsize
	@property
	def ws_persist(self) -> bool:
		return self._instance.WsPersist
	@property
	def ws_timer(self) -> int:
		return self._instance.WsTimer
	@property
	def ros_qsize(self) -> int:
		return self._instance.RosQsize
	@property
	def clk_timer(self) -> int:
		return self._instance.ClkTimer
	@property
	def mem_timer(self) -> int:
		return self._instance.MemTimer
	@property
	def usexmlcfg(self) -> bool:
		return self._instance.Usexmlcfg
	@property
	def msgfrmt(self) -> int:
		return self._instance.Msgfrmt
	@property
	def tcp_timeout(self) -> int:
		return self._instance.TcpTimeout
	@property
	def ping_retry(self) -> int:
		return self._instance.PingRetry
	@property
	def option(self) -> int:
		return self._instance.Option
	@property
	def ping(self) -> bool:
		return self._instance.Ping
	@property
	def ping_timer(self) -> int:
		return self._instance.PingTimer
	@property
	def cstat_enb(self) -> bool:
		return self._instance.CstatEnb
	@property
	def retry_auth(self) -> bool:
		return self._instance.RetryAuth
	@property
	def tp_updtime(self) -> int:
		return self._instance.TpUpdtime
	@property
	def pcount(self) -> int:
		return self._instance.Pcount
	@property
	def pinfo(self) -> typing.List[PinfoVariableType]:
		return [PinfoVariableType(x) for x in self._instance.Pinfo]
	@property
	def vcount(self) -> int:
		return self._instance.Vcount
	@property
	def tp_rmtime(self) -> int:
		return self._instance.TpRmtime
	@property
	def acc_timer(self) -> int:
		return self._instance.AccTimer
	@property
	def acc_snap(self) -> int:
		return self._instance.AccSnap
	@property
	def dummy1(self) -> int:
		return self._instance.Dummy1
	@property
	def dummy2(self) -> int:
		return self._instance.Dummy2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
