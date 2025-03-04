import typing
from underautomation.fanuc.ftp.variables.irc_gnrc_variable_type import IrcGnrcVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import IrcStatusFile as irc_status_file

class IrcStatusFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = irc_status_file()
		else:
			self._instance = _internal
	@property
	def attach_files(self) -> typing.List[str]:
		return self._instance.AttachFiles
	@property
	def cur_time(self) -> int:
		return self._instance.CurTime
	@property
	def cur_time_str(self) -> str:
		return self._instance.CurTimeStr
	@property
	def dbg_rc(self) -> bool:
		return self._instance.DbgRc
	@property
	def file_name(self) -> str:
		return self._instance.FileName
	@property
	def irc_gnrc(self) -> IrcGnrcVariableType:
		return IrcGnrcVariableType(self._instance.IrcGnrc)
	@property
	def pkrcxmlfile(self) -> str:
		return self._instance.Pkrcxmlfile
	@property
	def send_email(self) -> bool:
		return self._instance.SendEmail
	@property
	def snd_priority(self) -> int:
		return self._instance.SndPriority
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def thr_duration(self) -> int:
		return self._instance.ThrDuration
	@property
	def thr_prvtime(self) -> int:
		return self._instance.ThrPrvtime
	@property
	def tpp_gencall(self) -> bool:
		return self._instance.TppGencall
