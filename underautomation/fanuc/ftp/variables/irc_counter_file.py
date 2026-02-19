import typing
from underautomation.fanuc.ftp.variables.irc_gnrc_variable_type import IrcGnrcVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import IrcCounterFile as irc_counter_file

class IrcCounterFile(GenericVariableFile):
	'''Describes the Fanuc variable file irc_counter.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = irc_counter_file()
		else:
			self._instance = _internal

	@property
	def attach_files(self) -> typing.List[str]:
		'''Value of variable ATTACH_FILES'''
		return self._instance.AttachFiles

	@property
	def counter_mode(self) -> int:
		'''Value of variable COUNTER_MODE'''
		return self._instance.CounterMode

	@property
	def cur_time(self) -> int:
		'''Value of variable CUR_TIME'''
		return self._instance.CurTime

	@property
	def cur_time_str(self) -> str:
		'''Value of variable CUR_TIME_STR'''
		return self._instance.CurTimeStr

	@property
	def dbg_rc(self) -> bool:
		'''Value of variable DBG_RC'''
		return self._instance.DbgRc

	@property
	def file_name(self) -> str:
		'''Value of variable FILE_NAME'''
		return self._instance.FileName

	@property
	def irc_gnrc(self) -> IrcGnrcVariableType:
		'''Value of variable IRC_GNRC'''
		return IrcGnrcVariableType(self._instance.IrcGnrc)

	@property
	def pkrcxmlfile(self) -> str:
		'''Value of variable PKRCXMLFILE'''
		return self._instance.Pkrcxmlfile

	@property
	def send_email(self) -> bool:
		'''Value of variable SEND_EMAIL'''
		return self._instance.SendEmail

	@property
	def snd_priority(self) -> int:
		'''Value of variable SND_PRIORITY'''
		return self._instance.SndPriority

	@property
	def status(self) -> int:
		'''Value of variable STATUS'''
		return self._instance.Status

	@property
	def thr_duration(self) -> int:
		'''Value of variable THR_DURATION'''
		return self._instance.ThrDuration

	@property
	def thr_prvtime(self) -> int:
		'''Value of variable THR_PRVTIME'''
		return self._instance.ThrPrvtime

	@property
	def tpp_gencall(self) -> bool:
		'''Value of variable TPP_GENCALL'''
		return self._instance.TppGencall

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IrcCounterFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
