import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ClhistVariableType as clhist_variable_type

class ClhistVariableType(GenericVariableType):
	'''Describes the Fanuc type CLHIST_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = clhist_variable_type()
		else:
			self._instance = _internal

	@property
	def cldet_axs(self) -> int:
		'''Value of variable $CLDET_AXS'''
		return self._instance.CldetAxs

	@property
	def ps_cldet_ti(self) -> int:
		'''Value of variable $PS_CLDET_TI'''
		return self._instance.PsCldetTi

	@property
	def cldet_time(self) -> int:
		'''Value of variable $CLDET_TIME'''
		return self._instance.CldetTime

	@property
	def jpos_cmd(self) -> typing.List[float]:
		'''Value of variable $JPOS_CMD'''
		return self._instance.JposCmd

	@property
	def jpos_fb(self) -> typing.List[float]:
		'''Value of variable $JPOS_FB'''
		return self._instance.JposFb

	@property
	def vel_fb(self) -> typing.List[float]:
		'''Value of variable $VEL_FB'''
		return self._instance.VelFb

	@property
	def cl_ovr(self) -> int:
		'''Value of variable $CL_OVR'''
		return self._instance.ClOvr

	@property
	def cl_frmz(self) -> int:
		'''Value of variable $CL_FRMZ'''
		return self._instance.ClFrmz

	@property
	def cldept_idx(self) -> int:
		'''Value of variable $CLDEPT_IDX'''
		return self._instance.CldeptIdx

	@property
	def clname(self) -> str:
		'''Value of variable $CLNAME'''
		return self._instance.Clname

	@property
	def clcurline(self) -> int:
		'''Value of variable $CLCURLINE'''
		return self._instance.Clcurline

	@property
	def wnt_cnt(self) -> int:
		'''Value of variable $WNT_CNT'''
		return self._instance.WntCnt

	@property
	def stck_cnt(self) -> int:
		'''Value of variable $STCK_CNT'''
		return self._instance.StckCnt

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ClhistVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
