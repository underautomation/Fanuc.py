import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ErrMaskVariableType as err_mask_variable_type

class ErrMaskVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = err_mask_variable_type()
		else:
			self._instance = _internal
	@property
	def ssc_mask1(self) -> int:
		return self._instance.SscMask1
	@property
	def ssc_mask2(self) -> int:
		return self._instance.SscMask2
	@property
	def ssc_mask3(self) -> int:
		return self._instance.SscMask3
	@property
	def ssc_mask4(self) -> int:
		return self._instance.SscMask4
	@property
	def sev_mask(self) -> int:
		return self._instance.SevMask
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
