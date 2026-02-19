import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ErNoalmVariableType as er_noalm_variable_type

class ErNoalmVariableType(GenericVariableType):
	'''Describes the Fanuc type ER_NOALM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = er_noalm_variable_type()
		else:
			self._instance = _internal

	@property
	def noalmenble(self) -> int:
		'''Value of variable $NOALMENBLE'''
		return self._instance.Noalmenble

	@property
	def noalm_num(self) -> int:
		'''Value of variable $NOALM_NUM'''
		return self._instance.NoalmNum

	@property
	def er_code1(self) -> int:
		'''Value of variable $ER_CODE1'''
		return self._instance.ErCode1

	@property
	def er_code2(self) -> int:
		'''Value of variable $ER_CODE2'''
		return self._instance.ErCode2

	@property
	def er_code3(self) -> int:
		'''Value of variable $ER_CODE3'''
		return self._instance.ErCode3

	@property
	def er_code4(self) -> int:
		'''Value of variable $ER_CODE4'''
		return self._instance.ErCode4

	@property
	def er_code5(self) -> int:
		'''Value of variable $ER_CODE5'''
		return self._instance.ErCode5

	@property
	def er_code6(self) -> int:
		'''Value of variable $ER_CODE6'''
		return self._instance.ErCode6

	@property
	def er_code7(self) -> int:
		'''Value of variable $ER_CODE7'''
		return self._instance.ErCode7

	@property
	def er_code8(self) -> int:
		'''Value of variable $ER_CODE8'''
		return self._instance.ErCode8

	@property
	def er_code9(self) -> int:
		'''Value of variable $ER_CODE9'''
		return self._instance.ErCode9

	@property
	def er_code10(self) -> int:
		'''Value of variable $ER_CODE10'''
		return self._instance.ErCode10

	@property
	def er_code11(self) -> int:
		'''Value of variable $ER_CODE11'''
		return self._instance.ErCode11

	@property
	def er_code12(self) -> int:
		'''Value of variable $ER_CODE12'''
		return self._instance.ErCode12

	@property
	def er_code13(self) -> int:
		'''Value of variable $ER_CODE13'''
		return self._instance.ErCode13

	@property
	def er_code14(self) -> int:
		'''Value of variable $ER_CODE14'''
		return self._instance.ErCode14

	@property
	def er_code15(self) -> int:
		'''Value of variable $ER_CODE15'''
		return self._instance.ErCode15

	@property
	def er_code16(self) -> int:
		'''Value of variable $ER_CODE16'''
		return self._instance.ErCode16

	@property
	def er_code17(self) -> int:
		'''Value of variable $ER_CODE17'''
		return self._instance.ErCode17

	@property
	def er_code18(self) -> int:
		'''Value of variable $ER_CODE18'''
		return self._instance.ErCode18

	@property
	def er_code19(self) -> int:
		'''Value of variable $ER_CODE19'''
		return self._instance.ErCode19

	@property
	def er_code20(self) -> int:
		'''Value of variable $ER_CODE20'''
		return self._instance.ErCode20

	@property
	def er_code21(self) -> int:
		'''Value of variable $ER_CODE21'''
		return self._instance.ErCode21

	@property
	def er_code22(self) -> int:
		'''Value of variable $ER_CODE22'''
		return self._instance.ErCode22

	@property
	def er_code23(self) -> int:
		'''Value of variable $ER_CODE23'''
		return self._instance.ErCode23

	@property
	def er_code24(self) -> int:
		'''Value of variable $ER_CODE24'''
		return self._instance.ErCode24

	@property
	def er_code25(self) -> int:
		'''Value of variable $ER_CODE25'''
		return self._instance.ErCode25

	@property
	def er_code26(self) -> int:
		'''Value of variable $ER_CODE26'''
		return self._instance.ErCode26

	@property
	def er_code27(self) -> int:
		'''Value of variable $ER_CODE27'''
		return self._instance.ErCode27

	@property
	def er_code28(self) -> int:
		'''Value of variable $ER_CODE28'''
		return self._instance.ErCode28

	@property
	def er_code29(self) -> int:
		'''Value of variable $ER_CODE29'''
		return self._instance.ErCode29

	@property
	def er_code30(self) -> int:
		'''Value of variable $ER_CODE30'''
		return self._instance.ErCode30

	@property
	def er_code31(self) -> int:
		'''Value of variable $ER_CODE31'''
		return self._instance.ErCode31

	@property
	def er_code32(self) -> int:
		'''Value of variable $ER_CODE32'''
		return self._instance.ErCode32

	@property
	def er_code33(self) -> int:
		'''Value of variable $ER_CODE33'''
		return self._instance.ErCode33

	@property
	def er_code34(self) -> int:
		'''Value of variable $ER_CODE34'''
		return self._instance.ErCode34

	@property
	def er_code35(self) -> int:
		'''Value of variable $ER_CODE35'''
		return self._instance.ErCode35

	@property
	def er_code36(self) -> int:
		'''Value of variable $ER_CODE36'''
		return self._instance.ErCode36

	@property
	def er_code37(self) -> int:
		'''Value of variable $ER_CODE37'''
		return self._instance.ErCode37

	@property
	def er_code38(self) -> int:
		'''Value of variable $ER_CODE38'''
		return self._instance.ErCode38

	@property
	def er_code39(self) -> int:
		'''Value of variable $ER_CODE39'''
		return self._instance.ErCode39

	@property
	def er_code40(self) -> int:
		'''Value of variable $ER_CODE40'''
		return self._instance.ErCode40

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ErNoalmVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
