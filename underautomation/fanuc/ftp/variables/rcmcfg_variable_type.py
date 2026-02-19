import typing
from underautomation.fanuc.ftp.variables.pinfo_variable_type import PinfoVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RcmcfgVariableType as rcmcfg_variable_type

class RcmcfgVariableType(GenericVariableType):
	'''Describes the Fanuc type RCMCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rcmcfg_variable_type()
		else:
			self._instance = _internal

	@property
	def rcm_enable(self) -> bool:
		'''Value of variable $RCM_ENABLE'''
		return self._instance.RcmEnable

	@property
	def qsize(self) -> int:
		'''Value of variable $QSIZE'''
		return self._instance.Qsize

	@property
	def timer(self) -> int:
		'''Value of variable $TIMER'''
		return self._instance.Timer

	@property
	def status_time(self) -> int:
		'''Value of variable $STATUS_TIME'''
		return self._instance.StatusTime

	@property
	def mailserv(self) -> str:
		'''Value of variable $MAILSERV'''
		return self._instance.Mailserv

	@property
	def plant(self) -> str:
		'''Value of variable $PLANT'''
		return self._instance.Plant

	@property
	def line(self) -> str:
		'''Value of variable $LINE'''
		return self._instance.Line

	@property
	def cluster(self) -> str:
		'''Value of variable $CLUSTER'''
		return self._instance.Cluster

	@property
	def toaddr(self) -> str:
		'''Value of variable $TOADDR'''
		return self._instance.Toaddr

	@property
	def ccaddr(self) -> str:
		'''Value of variable $CCADDR'''
		return self._instance.Ccaddr

	@property
	def fraddr(self) -> str:
		'''Value of variable $FRADDR'''
		return self._instance.Fraddr

	@property
	def subject(self) -> str:
		'''Value of variable $SUBJECT'''
		return self._instance.Subject

	@property
	def status_enb(self) -> bool:
		'''Value of variable $STATUS_ENB'''
		return self._instance.StatusEnb

	@property
	def alarm_enb(self) -> bool:
		'''Value of variable $ALARM_ENB'''
		return self._instance.AlarmEnb

	@property
	def tplog_enb(self) -> bool:
		'''Value of variable $TPLOG_ENB'''
		return self._instance.TplogEnb

	@property
	def varlog_enb(self) -> bool:
		'''Value of variable $VARLOG_ENB'''
		return self._instance.VarlogEnb

	@property
	def motion_enb(self) -> bool:
		'''Value of variable $MOTION_ENB'''
		return self._instance.MotionEnb

	@property
	def system_enb(self) -> bool:
		'''Value of variable $SYSTEM_ENB'''
		return self._instance.SystemEnb

	@property
	def appl_enb(self) -> bool:
		'''Value of variable $APPL_ENB'''
		return self._instance.ApplEnb

	@property
	def pass_enb(self) -> bool:
		'''Value of variable $PASS_ENB'''
		return self._instance.PassEnb

	@property
	def comm_enb(self) -> bool:
		'''Value of variable $COMM_ENB'''
		return self._instance.CommEnb

	@property
	def port(self) -> int:
		'''Value of variable $PORT'''
		return self._instance.Port

	@property
	def stat_subj(self) -> str:
		'''Value of variable $STAT_SUBJ'''
		return self._instance.StatSubj

	@property
	def alertaddr(self) -> str:
		'''Value of variable $ALERTADDR'''
		return self._instance.Alertaddr

	@property
	def alerturl(self) -> str:
		'''Value of variable $ALERTURL'''
		return self._instance.Alerturl

	@property
	def stat_attach(self) -> str:
		'''Value of variable $STAT_ATTACH'''
		return self._instance.StatAttach

	@property
	def err_throt(self) -> int:
		'''Value of variable $ERR_THROT'''
		return self._instance.ErrThrot

	@property
	def usr_throt(self) -> int:
		'''Value of variable $USR_THROT'''
		return self._instance.UsrThrot

	@property
	def size_throt(self) -> int:
		'''Value of variable $SIZE_THROT'''
		return self._instance.SizeThrot

	@property
	def varchg_time(self) -> int:
		'''Value of variable $VARCHG_TIME'''
		return self._instance.VarchgTime

	@property
	def varchg_max(self) -> int:
		'''Value of variable $VARCHG_MAX'''
		return self._instance.VarchgMax

	@property
	def ws_url(self) -> str:
		'''Value of variable $WS_URL'''
		return self._instance.WsUrl

	@property
	def ws_mode(self) -> bool:
		'''Value of variable $WS_MODE'''
		return self._instance.WsMode

	@property
	def ws_uid(self) -> str:
		'''Value of variable $WS_UID'''
		return self._instance.WsUid

	@property
	def ws_user(self) -> str:
		'''Value of variable $WS_USER'''
		return self._instance.WsUser

	@property
	def last_err(self) -> int:
		'''Value of variable $LAST_ERR'''
		return self._instance.LastErr

	@property
	def snd_maxtry(self) -> int:
		'''Value of variable $SND_MAXTRY'''
		return self._instance.SndMaxtry

	@property
	def snd_delay(self) -> int:
		'''Value of variable $SND_DELAY'''
		return self._instance.SndDelay

	@property
	def ws_qsize(self) -> int:
		'''Value of variable $WS_QSIZE'''
		return self._instance.WsQsize

	@property
	def ws_persist(self) -> bool:
		'''Value of variable $WS_PERSIST'''
		return self._instance.WsPersist

	@property
	def ws_timer(self) -> int:
		'''Value of variable $WS_TIMER'''
		return self._instance.WsTimer

	@property
	def ros_qsize(self) -> int:
		'''Value of variable $ROS_QSIZE'''
		return self._instance.RosQsize

	@property
	def clk_timer(self) -> int:
		'''Value of variable $CLK_TIMER'''
		return self._instance.ClkTimer

	@property
	def mem_timer(self) -> int:
		'''Value of variable $MEM_TIMER'''
		return self._instance.MemTimer

	@property
	def usexmlcfg(self) -> bool:
		'''Value of variable $USEXMLCFG'''
		return self._instance.Usexmlcfg

	@property
	def msgfrmt(self) -> int:
		'''Value of variable $MSGFRMT'''
		return self._instance.Msgfrmt

	@property
	def tcp_timeout(self) -> int:
		'''Value of variable $TCP_TIMEOUT'''
		return self._instance.TcpTimeout

	@property
	def ping_retry(self) -> int:
		'''Value of variable $PING_RETRY'''
		return self._instance.PingRetry

	@property
	def option(self) -> int:
		'''Value of variable $OPTION'''
		return self._instance.Option

	@property
	def ping(self) -> bool:
		'''Value of variable $PING'''
		return self._instance.Ping

	@property
	def ping_timer(self) -> int:
		'''Value of variable $PING_TIMER'''
		return self._instance.PingTimer

	@property
	def cstat_enb(self) -> bool:
		'''Value of variable $CSTAT_ENB'''
		return self._instance.CstatEnb

	@property
	def retry_auth(self) -> bool:
		'''Value of variable $RETRY_AUTH'''
		return self._instance.RetryAuth

	@property
	def tp_updtime(self) -> int:
		'''Value of variable $TP_UPDTIME'''
		return self._instance.TpUpdtime

	@property
	def pcount(self) -> int:
		'''Value of variable $PCOUNT'''
		return self._instance.Pcount

	@property
	def pinfo(self) -> typing.List[PinfoVariableType]:
		'''Value of variable $PINFO'''
		return [PinfoVariableType(x) for x in self._instance.Pinfo]

	@property
	def vcount(self) -> int:
		'''Value of variable $VCOUNT'''
		return self._instance.Vcount

	@property
	def tp_rmtime(self) -> int:
		'''Value of variable $TP_RMTIME'''
		return self._instance.TpRmtime

	@property
	def acc_timer(self) -> int:
		'''Value of variable $ACC_TIMER'''
		return self._instance.AccTimer

	@property
	def acc_snap(self) -> int:
		'''Value of variable $ACC_SNAP'''
		return self._instance.AccSnap

	@property
	def dummy1(self) -> int:
		'''Value of variable $DUMMY1'''
		return self._instance.Dummy1

	@property
	def dummy2(self) -> int:
		'''Value of variable $DUMMY2'''
		return self._instance.Dummy2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RcmcfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
