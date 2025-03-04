import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ErNoalmVariableType as er_noalm_variable_type

class ErNoalmVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = er_noalm_variable_type()
		else:
			self._instance = _internal
	@property
	def noalmenble(self) -> int:
		return self._instance.Noalmenble
	@property
	def noalm_num(self) -> int:
		return self._instance.NoalmNum
	@property
	def er_code1(self) -> int:
		return self._instance.ErCode1
	@property
	def er_code2(self) -> int:
		return self._instance.ErCode2
	@property
	def er_code3(self) -> int:
		return self._instance.ErCode3
	@property
	def er_code4(self) -> int:
		return self._instance.ErCode4
	@property
	def er_code5(self) -> int:
		return self._instance.ErCode5
	@property
	def er_code6(self) -> int:
		return self._instance.ErCode6
	@property
	def er_code7(self) -> int:
		return self._instance.ErCode7
	@property
	def er_code8(self) -> int:
		return self._instance.ErCode8
	@property
	def er_code9(self) -> int:
		return self._instance.ErCode9
	@property
	def er_code10(self) -> int:
		return self._instance.ErCode10
	@property
	def er_code11(self) -> int:
		return self._instance.ErCode11
	@property
	def er_code12(self) -> int:
		return self._instance.ErCode12
	@property
	def er_code13(self) -> int:
		return self._instance.ErCode13
	@property
	def er_code14(self) -> int:
		return self._instance.ErCode14
	@property
	def er_code15(self) -> int:
		return self._instance.ErCode15
	@property
	def er_code16(self) -> int:
		return self._instance.ErCode16
	@property
	def er_code17(self) -> int:
		return self._instance.ErCode17
	@property
	def er_code18(self) -> int:
		return self._instance.ErCode18
	@property
	def er_code19(self) -> int:
		return self._instance.ErCode19
	@property
	def er_code20(self) -> int:
		return self._instance.ErCode20
	@property
	def er_code21(self) -> int:
		return self._instance.ErCode21
	@property
	def er_code22(self) -> int:
		return self._instance.ErCode22
	@property
	def er_code23(self) -> int:
		return self._instance.ErCode23
	@property
	def er_code24(self) -> int:
		return self._instance.ErCode24
	@property
	def er_code25(self) -> int:
		return self._instance.ErCode25
	@property
	def er_code26(self) -> int:
		return self._instance.ErCode26
	@property
	def er_code27(self) -> int:
		return self._instance.ErCode27
	@property
	def er_code28(self) -> int:
		return self._instance.ErCode28
	@property
	def er_code29(self) -> int:
		return self._instance.ErCode29
	@property
	def er_code30(self) -> int:
		return self._instance.ErCode30
	@property
	def er_code31(self) -> int:
		return self._instance.ErCode31
	@property
	def er_code32(self) -> int:
		return self._instance.ErCode32
	@property
	def er_code33(self) -> int:
		return self._instance.ErCode33
	@property
	def er_code34(self) -> int:
		return self._instance.ErCode34
	@property
	def er_code35(self) -> int:
		return self._instance.ErCode35
	@property
	def er_code36(self) -> int:
		return self._instance.ErCode36
	@property
	def er_code37(self) -> int:
		return self._instance.ErCode37
	@property
	def er_code38(self) -> int:
		return self._instance.ErCode38
	@property
	def er_code39(self) -> int:
		return self._instance.ErCode39
	@property
	def er_code40(self) -> int:
		return self._instance.ErCode40
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
