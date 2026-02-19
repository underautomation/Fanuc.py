import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PssaveVariableType as pssave_variable_type

class PssaveVariableType(GenericVariableType):
	'''Describes the Fanuc type PSSAVE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pssave_variable_type()
		else:
			self._instance = _internal

	@property
	def mc_folder(self) -> str:
		'''Value of variable $MC_FOLDER'''
		return self._instance.McFolder

	@property
	def slave_save(self) -> bool:
		'''Value of variable $SLAVE_SAVE'''
		return self._instance.SlaveSave

	@property
	def start_multi(self) -> bool:
		'''Value of variable $START_MULTI'''
		return self._instance.StartMulti

	@property
	def slave_load(self) -> typing.List[bool]:
		'''Value of variable $SLAVE_LOAD'''
		return self._instance.SlaveLoad

	@property
	def load_dev(self) -> int:
		'''Value of variable $LOAD_DEV'''
		return self._instance.LoadDev

	@property
	def keep_hnaddr(self) -> str:
		'''Value of variable $KEEP_HNADDR'''
		return self._instance.KeepHnaddr

	@property
	def keep_hraddr(self) -> str:
		'''Value of variable $KEEP_HRADDR'''
		return self._instance.KeepHraddr

	@property
	def keep_ccomm(self) -> str:
		'''Value of variable $KEEP_CCOMM'''
		return self._instance.KeepCcomm

	@property
	def keep_cprot(self) -> str:
		'''Value of variable $KEEP_CPROT'''
		return self._instance.KeepCprot

	@property
	def ps_keep_cop(self) -> int:
		'''Value of variable $PS_KEEP_COP'''
		return self._instance.PsKeepCop

	@property
	def keep_coper(self) -> int:
		'''Value of variable $KEEP_COPER'''
		return self._instance.KeepCoper

	@property
	def keep_cstate(self) -> int:
		'''Value of variable $KEEP_CSTATE'''
		return self._instance.KeepCstate

	@property
	def keep_cremot(self) -> str:
		'''Value of variable $KEEP_CREMOT'''
		return self._instance.KeepCremot

	@property
	def keep_ctimeo(self) -> int:
		'''Value of variable $KEEP_CTIMEO'''
		return self._instance.KeepCtimeo

	@property
	def keep_csremo(self) -> str:
		'''Value of variable $KEEP_CSREMO'''
		return self._instance.KeepCsremo

	@property
	def keep_cuname(self) -> str:
		'''Value of variable $KEEP_CUNAME'''
		return self._instance.KeepCuname

	@property
	def keep_chpwd(self) -> str:
		'''Value of variable $KEEP_CHPWD'''
		return self._instance.KeepChpwd

	@property
	def keep_sbmsk(self) -> str:
		'''Value of variable $KEEP_SBMSK'''
		return self._instance.KeepSbmsk

	@property
	def collabmode(self) -> bool:
		'''Value of variable $COLLABMODE'''
		return self._instance.Collabmode

	@property
	def ps_started(self) -> bool:
		'''Value of variable $PS_STARTED'''
		return self._instance.PsStarted

	@property
	def inits_comp(self) -> bool:
		'''Value of variable $INITS_COMP'''
		return self._instance.InitsComp

	@property
	def noloadfcalb(self) -> bool:
		'''Value of variable $NOLOADFCALB'''
		return self._instance.Noloadfcalb

	@property
	def start_done(self) -> bool:
		'''Value of variable $START_DONE'''
		return self._instance.StartDone

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PssaveVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
