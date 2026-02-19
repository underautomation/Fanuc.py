import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TscfgVariableType as tscfg_variable_type

class TscfgVariableType(GenericVariableType):
	'''Describes the Fanuc type TSCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tscfg_variable_type()
		else:
			self._instance = _internal

	@property
	def grp_mask(self) -> int:
		'''Value of variable $GRP_MASK'''
		return self._instance.GrpMask

	@property
	def mode_mask(self) -> int:
		'''Value of variable $MODE_MASK'''
		return self._instance.ModeMask

	@property
	def status(self) -> int:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def opt_val(self) -> float:
		'''Value of variable $OPT_VAL'''
		return self._instance.OptVal

	@property
	def size(self) -> int:
		'''Value of variable $SIZE'''
		return self._instance.Size

	@property
	def fname_type(self) -> int:
		'''Value of variable $FNAME_TYPE'''
		return self._instance.FnameType

	@property
	def proc(self) -> bool:
		'''Value of variable $PROC'''
		return self._instance.Proc

	@property
	def output(self) -> bool:
		'''Value of variable $OUTPUT'''
		return self._instance.Output

	@property
	def output_done(self) -> bool:
		'''Value of variable $OUTPUT_DONE'''
		return self._instance.OutputDone

	@property
	def axs_msk_enb(self) -> bool:
		'''Value of variable $AXS_MSK_ENB'''
		return self._instance.AxsMskEnb

	@property
	def axis_mask(self) -> typing.List[int]:
		'''Value of variable $AXIS_MASK'''
		return self._instance.AxisMask

	@property
	def cur_rectime(self) -> int:
		'''Value of variable $CUR_RECTIME'''
		return self._instance.CurRectime

	@property
	def tot_chn_num(self) -> int:
		'''Value of variable $TOT_CHN_NUM'''
		return self._instance.TotChnNum

	@property
	def minfreq_us(self) -> int:
		'''Value of variable $MINFREQ_US'''
		return self._instance.MinfreqUs

	@property
	def setfreq_pow(self) -> int:
		'''Value of variable $SETFREQ_POW'''
		return self._instance.SetfreqPow

	@property
	def lparam(self) -> typing.List[int]:
		'''Value of variable $LPARAM'''
		return self._instance.Lparam

	@property
	def fparam(self) -> typing.List[float]:
		'''Value of variable $FPARAM'''
		return self._instance.Fparam

	@property
	def path_nam(self) -> str:
		'''Value of variable $PATH_NAM'''
		return self._instance.PathNam

	@property
	def dummy19(self) -> int:
		'''Value of variable $DUMMY19'''
		return self._instance.Dummy19

	@property
	def dummy20(self) -> int:
		'''Value of variable $DUMMY20'''
		return self._instance.Dummy20

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TscfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
