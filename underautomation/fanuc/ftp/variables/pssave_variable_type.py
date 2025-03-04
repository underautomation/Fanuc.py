import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PssaveVariableType as pssave_variable_type

class PssaveVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pssave_variable_type()
		else:
			self._instance = _internal
	@property
	def mc_folder(self) -> str:
		return self._instance.McFolder
	@property
	def slave_save(self) -> bool:
		return self._instance.SlaveSave
	@property
	def start_multi(self) -> bool:
		return self._instance.StartMulti
	@property
	def slave_load(self) -> typing.List[bool]:
		return self._instance.SlaveLoad
	@property
	def load_dev(self) -> int:
		return self._instance.LoadDev
	@property
	def keep_hnaddr(self) -> str:
		return self._instance.KeepHnaddr
	@property
	def keep_hraddr(self) -> str:
		return self._instance.KeepHraddr
	@property
	def keep_ccomm(self) -> str:
		return self._instance.KeepCcomm
	@property
	def keep_cprot(self) -> str:
		return self._instance.KeepCprot
	@property
	def ps_keep_cop(self) -> int:
		return self._instance.PsKeepCop
	@property
	def keep_coper(self) -> int:
		return self._instance.KeepCoper
	@property
	def keep_cstate(self) -> int:
		return self._instance.KeepCstate
	@property
	def keep_cremot(self) -> str:
		return self._instance.KeepCremot
	@property
	def keep_ctimeo(self) -> int:
		return self._instance.KeepCtimeo
	@property
	def keep_csremo(self) -> str:
		return self._instance.KeepCsremo
	@property
	def keep_cuname(self) -> str:
		return self._instance.KeepCuname
	@property
	def keep_chpwd(self) -> str:
		return self._instance.KeepChpwd
	@property
	def keep_sbmsk(self) -> str:
		return self._instance.KeepSbmsk
	@property
	def collabmode(self) -> bool:
		return self._instance.Collabmode
	@property
	def ps_started(self) -> bool:
		return self._instance.PsStarted
	@property
	def inits_comp(self) -> bool:
		return self._instance.InitsComp
	@property
	def noloadfcalb(self) -> bool:
		return self._instance.Noloadfcalb
	@property
	def start_done(self) -> bool:
		return self._instance.StartDone
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
