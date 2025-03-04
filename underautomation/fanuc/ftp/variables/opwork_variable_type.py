import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import OpworkVariableType as opwork_variable_type

class OpworkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = opwork_variable_type()
		else:
			self._instance = _internal
	@property
	def sysbusy(self) -> int:
		return self._instance.Sysbusy
	@property
	def sopbusymsk(self) -> int:
		return self._instance.Sopbusymsk
	@property
	def tpbusymsk(self) -> int:
		return self._instance.Tpbusymsk
	@property
	def uopbusymsk(self) -> int:
		return self._instance.Uopbusymsk
	@property
	def intprunning(self) -> int:
		return self._instance.Intprunning
	@property
	def intppaused(self) -> int:
		return self._instance.Intppaused
	@property
	def intpmask(self) -> int:
		return self._instance.Intpmask
	@property
	def opt_out(self) -> int:
		return self._instance.OptOut
	@property
	def uop_disable(self) -> int:
		return self._instance.UopDisable
	@property
	def outimage(self) -> typing.List[int]:
		return self._instance.Outimage
	@property
	def op_prev_img(self) -> typing.List[int]:
		return self._instance.OpPrevImg
	@property
	def op_inv_mask(self) -> typing.List[int]:
		return self._instance.OpInvMask
	@property
	def orgovrdval(self) -> int:
		return self._instance.Orgovrdval
	@property
	def user_output(self) -> typing.List[int]:
		return self._instance.UserOutput
	@property
	def enbl_on(self) -> int:
		return self._instance.EnblOn
	@property
	def mlt_rbt_enb(self) -> int:
		return self._instance.MltRbtEnb
	@property
	def noalm_msk(self) -> int:
		return self._instance.NoalmMsk
	@property
	def dummy19(self) -> int:
		return self._instance.Dummy19
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
