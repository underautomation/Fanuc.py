import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import OpworkVariableType as opwork_variable_type

class OpworkVariableType(GenericVariableType):
	'''Describes the Fanuc type OPWORK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = opwork_variable_type()
		else:
			self._instance = _internal

	@property
	def sysbusy(self) -> int:
		'''Value of variable $SYSBUSY'''
		return self._instance.Sysbusy

	@property
	def sopbusymsk(self) -> int:
		'''Value of variable $SOPBUSYMSK'''
		return self._instance.Sopbusymsk

	@property
	def tpbusymsk(self) -> int:
		'''Value of variable $TPBUSYMSK'''
		return self._instance.Tpbusymsk

	@property
	def uopbusymsk(self) -> int:
		'''Value of variable $UOPBUSYMSK'''
		return self._instance.Uopbusymsk

	@property
	def intprunning(self) -> int:
		'''Value of variable $INTPRUNNING'''
		return self._instance.Intprunning

	@property
	def intppaused(self) -> int:
		'''Value of variable $INTPPAUSED'''
		return self._instance.Intppaused

	@property
	def intpmask(self) -> int:
		'''Value of variable $INTPMASK'''
		return self._instance.Intpmask

	@property
	def opt_out(self) -> int:
		'''Value of variable $OPT_OUT'''
		return self._instance.OptOut

	@property
	def uop_disable(self) -> int:
		'''Value of variable $UOP_DISABLE'''
		return self._instance.UopDisable

	@property
	def outimage(self) -> typing.List[int]:
		'''Value of variable $OUTIMAGE'''
		return self._instance.Outimage

	@property
	def op_prev_img(self) -> typing.List[int]:
		'''Value of variable $OP_PREV_IMG'''
		return self._instance.OpPrevImg

	@property
	def op_inv_mask(self) -> typing.List[int]:
		'''Value of variable $OP_INV_MASK'''
		return self._instance.OpInvMask

	@property
	def orgovrdval(self) -> int:
		'''Value of variable $ORGOVRDVAL'''
		return self._instance.Orgovrdval

	@property
	def user_output(self) -> typing.List[int]:
		'''Value of variable $USER_OUTPUT'''
		return self._instance.UserOutput

	@property
	def enbl_on(self) -> int:
		'''Value of variable $ENBL_ON'''
		return self._instance.EnblOn

	@property
	def mlt_rbt_enb(self) -> int:
		'''Value of variable $MLT_RBT_ENB'''
		return self._instance.MltRbtEnb

	@property
	def noalm_msk(self) -> int:
		'''Value of variable $NOALM_MSK'''
		return self._instance.NoalmMsk

	@property
	def dummy19(self) -> int:
		'''Value of variable $DUMMY19'''
		return self._instance.Dummy19

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, OpworkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
