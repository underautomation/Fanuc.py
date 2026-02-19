import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import HscdMngVariableType as hscd_mng_variable_type

class HscdMngVariableType(GenericVariableType):
	'''Describes the Fanuc type HSCD_MNG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hscd_mng_variable_type()
		else:
			self._instance = _internal

	@property
	def coll_mode(self) -> bool:
		'''Value of variable $COLL_MODE'''
		return self._instance.CollMode

	@property
	def threshold(self) -> int:
		'''Value of variable $THRESHOLD'''
		return self._instance.Threshold

	@property
	def do_err(self) -> int:
		'''Value of variable $DO_ERR'''
		return self._instance.DoErr

	@property
	def do_enable(self) -> int:
		'''Value of variable $DO_ENABLE'''
		return self._instance.DoEnable

	@property
	def macro_reg(self) -> int:
		'''Value of variable $MACRO_REG'''
		return self._instance.MacroReg

	@property
	def stnd_cd(self) -> int:
		'''Value of variable $STND_CD'''
		return self._instance.StndCd

	@property
	def auto_reset(self) -> int:
		'''Value of variable $AUTO_RESET'''
		return self._instance.AutoReset

	@property
	def upd_groups(self) -> int:
		'''Value of variable $UPD_GROUPS'''
		return self._instance.UpdGroups

	@property
	def param_verid(self) -> str:
		'''Value of variable $PARAM_VERID'''
		return self._instance.ParamVerid

	@property
	def param119(self) -> typing.List[int]:
		'''Value of variable $PARAM119'''
		return self._instance.Param119

	@property
	def param120(self) -> typing.List[int]:
		'''Value of variable $PARAM120'''
		return self._instance.Param120

	@property
	def param121(self) -> typing.List[int]:
		'''Value of variable $PARAM121'''
		return self._instance.Param121

	@property
	def param122(self) -> typing.List[int]:
		'''Value of variable $PARAM122'''
		return self._instance.Param122

	@property
	def param123(self) -> typing.List[int]:
		'''Value of variable $PARAM123'''
		return self._instance.Param123

	@property
	def param124(self) -> typing.List[int]:
		'''Value of variable $PARAM124'''
		return self._instance.Param124

	@property
	def param125(self) -> typing.List[int]:
		'''Value of variable $PARAM125'''
		return self._instance.Param125

	@property
	def act_ratio(self) -> int:
		'''Value of variable $ACT_RATIO'''
		return self._instance.ActRatio

	@property
	def saved119(self) -> typing.List[int]:
		'''Value of variable $SAVED119'''
		return self._instance.Saved119

	@property
	def saved120(self) -> typing.List[int]:
		'''Value of variable $SAVED120'''
		return self._instance.Saved120

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HscdMngVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
