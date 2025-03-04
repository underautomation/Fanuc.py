import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SvdtGrpVariableType as svdt_grp_variable_type

class SvdtGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = svdt_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def data00(self) -> typing.List[int]:
		return self._instance.Data00
	@property
	def data01(self) -> typing.List[int]:
		return self._instance.Data01
	@property
	def data02(self) -> typing.List[int]:
		return self._instance.Data02
	@property
	def data03(self) -> typing.List[int]:
		return self._instance.Data03
	@property
	def data04(self) -> typing.List[int]:
		return self._instance.Data04
	@property
	def data05(self) -> typing.List[int]:
		return self._instance.Data05
	@property
	def data06(self) -> typing.List[int]:
		return self._instance.Data06
	@property
	def data07(self) -> typing.List[int]:
		return self._instance.Data07
	@property
	def data08(self) -> typing.List[int]:
		return self._instance.Data08
	@property
	def data09(self) -> typing.List[int]:
		return self._instance.Data09
	@property
	def data0a(self) -> typing.List[int]:
		return self._instance.Data0a
	@property
	def data0b(self) -> typing.List[int]:
		return self._instance.Data0b
	@property
	def data0c(self) -> typing.List[int]:
		return self._instance.Data0c
	@property
	def data0d(self) -> typing.List[int]:
		return self._instance.Data0d
	@property
	def data0e(self) -> typing.List[int]:
		return self._instance.Data0e
	@property
	def data0f(self) -> typing.List[int]:
		return self._instance.Data0f
	@property
	def data10(self) -> typing.List[int]:
		return self._instance.Data10
	@property
	def data11(self) -> typing.List[int]:
		return self._instance.Data11
	@property
	def data12(self) -> typing.List[int]:
		return self._instance.Data12
	@property
	def data13(self) -> typing.List[int]:
		return self._instance.Data13
	@property
	def data14(self) -> typing.List[int]:
		return self._instance.Data14
	@property
	def data15(self) -> typing.List[int]:
		return self._instance.Data15
	@property
	def data16(self) -> typing.List[int]:
		return self._instance.Data16
	@property
	def data17(self) -> typing.List[int]:
		return self._instance.Data17
	@property
	def data18(self) -> typing.List[int]:
		return self._instance.Data18
	@property
	def data19(self) -> typing.List[int]:
		return self._instance.Data19
	@property
	def data1a(self) -> typing.List[int]:
		return self._instance.Data1a
	@property
	def data1b(self) -> typing.List[int]:
		return self._instance.Data1b
	@property
	def data1c(self) -> typing.List[int]:
		return self._instance.Data1c
	@property
	def data1d(self) -> typing.List[int]:
		return self._instance.Data1d
	@property
	def data1e(self) -> typing.List[int]:
		return self._instance.Data1e
	@property
	def data1f(self) -> typing.List[int]:
		return self._instance.Data1f
	@property
	def data20(self) -> typing.List[int]:
		return self._instance.Data20
	@property
	def data21(self) -> typing.List[int]:
		return self._instance.Data21
	@property
	def data22(self) -> typing.List[int]:
		return self._instance.Data22
	@property
	def data23(self) -> typing.List[int]:
		return self._instance.Data23
	@property
	def data24(self) -> typing.List[int]:
		return self._instance.Data24
	@property
	def data25(self) -> typing.List[int]:
		return self._instance.Data25
	@property
	def data26(self) -> typing.List[int]:
		return self._instance.Data26
	@property
	def data27(self) -> typing.List[int]:
		return self._instance.Data27
	@property
	def data28(self) -> typing.List[int]:
		return self._instance.Data28
	@property
	def data29(self) -> typing.List[int]:
		return self._instance.Data29
	@property
	def data2a(self) -> typing.List[int]:
		return self._instance.Data2a
	@property
	def data2b(self) -> typing.List[int]:
		return self._instance.Data2b
	@property
	def data2c(self) -> typing.List[int]:
		return self._instance.Data2c
	@property
	def data2d(self) -> typing.List[int]:
		return self._instance.Data2d
	@property
	def data2e(self) -> typing.List[int]:
		return self._instance.Data2e
	@property
	def data2f(self) -> typing.List[int]:
		return self._instance.Data2f
	@property
	def data30(self) -> typing.List[int]:
		return self._instance.Data30
	@property
	def data31(self) -> typing.List[int]:
		return self._instance.Data31
	@property
	def data32(self) -> typing.List[int]:
		return self._instance.Data32
	@property
	def data33(self) -> typing.List[int]:
		return self._instance.Data33
	@property
	def data34(self) -> typing.List[int]:
		return self._instance.Data34
	@property
	def data35(self) -> typing.List[int]:
		return self._instance.Data35
	@property
	def data36(self) -> typing.List[int]:
		return self._instance.Data36
	@property
	def data37(self) -> typing.List[int]:
		return self._instance.Data37
	@property
	def data38(self) -> typing.List[int]:
		return self._instance.Data38
	@property
	def data39(self) -> typing.List[int]:
		return self._instance.Data39
	@property
	def data3a(self) -> typing.List[int]:
		return self._instance.Data3a
	@property
	def data3b(self) -> typing.List[int]:
		return self._instance.Data3b
	@property
	def data3c(self) -> typing.List[int]:
		return self._instance.Data3c
	@property
	def data3d(self) -> typing.List[int]:
		return self._instance.Data3d
	@property
	def data3e(self) -> typing.List[int]:
		return self._instance.Data3e
	@property
	def data3f(self) -> typing.List[int]:
		return self._instance.Data3f
	@property
	def data40(self) -> typing.List[int]:
		return self._instance.Data40
	@property
	def data41(self) -> typing.List[int]:
		return self._instance.Data41
	@property
	def data42(self) -> typing.List[int]:
		return self._instance.Data42
	@property
	def data43(self) -> typing.List[int]:
		return self._instance.Data43
	@property
	def data44(self) -> typing.List[int]:
		return self._instance.Data44
	@property
	def data45(self) -> typing.List[int]:
		return self._instance.Data45
	@property
	def data46(self) -> typing.List[int]:
		return self._instance.Data46
	@property
	def data47(self) -> typing.List[int]:
		return self._instance.Data47
	@property
	def data48(self) -> typing.List[int]:
		return self._instance.Data48
	@property
	def data49(self) -> typing.List[int]:
		return self._instance.Data49
	@property
	def data4a(self) -> typing.List[int]:
		return self._instance.Data4a
	@property
	def data4b(self) -> typing.List[int]:
		return self._instance.Data4b
	@property
	def data4c(self) -> typing.List[int]:
		return self._instance.Data4c
	@property
	def data4d(self) -> typing.List[int]:
		return self._instance.Data4d
	@property
	def data4e(self) -> typing.List[int]:
		return self._instance.Data4e
	@property
	def data4f(self) -> typing.List[int]:
		return self._instance.Data4f
	@property
	def data50(self) -> typing.List[int]:
		return self._instance.Data50
	@property
	def data51(self) -> typing.List[int]:
		return self._instance.Data51
	@property
	def data52(self) -> typing.List[int]:
		return self._instance.Data52
	@property
	def data53(self) -> typing.List[int]:
		return self._instance.Data53
	@property
	def data54(self) -> typing.List[int]:
		return self._instance.Data54
	@property
	def data55(self) -> typing.List[int]:
		return self._instance.Data55
	@property
	def data56(self) -> typing.List[int]:
		return self._instance.Data56
	@property
	def data57(self) -> typing.List[int]:
		return self._instance.Data57
	@property
	def data58(self) -> typing.List[int]:
		return self._instance.Data58
	@property
	def data59(self) -> typing.List[int]:
		return self._instance.Data59
	@property
	def data5a(self) -> typing.List[int]:
		return self._instance.Data5a
	@property
	def data5b(self) -> typing.List[int]:
		return self._instance.Data5b
	@property
	def data5c(self) -> typing.List[int]:
		return self._instance.Data5c
	@property
	def data5d(self) -> typing.List[int]:
		return self._instance.Data5d
	@property
	def data5e(self) -> typing.List[int]:
		return self._instance.Data5e
	@property
	def data5f(self) -> typing.List[int]:
		return self._instance.Data5f
	@property
	def data60(self) -> typing.List[int]:
		return self._instance.Data60
	@property
	def data61(self) -> typing.List[int]:
		return self._instance.Data61
	@property
	def data62(self) -> typing.List[int]:
		return self._instance.Data62
	@property
	def data63(self) -> typing.List[int]:
		return self._instance.Data63
	@property
	def data64(self) -> typing.List[int]:
		return self._instance.Data64
	@property
	def data65(self) -> typing.List[int]:
		return self._instance.Data65
	@property
	def data66(self) -> typing.List[int]:
		return self._instance.Data66
	@property
	def data67(self) -> typing.List[int]:
		return self._instance.Data67
	@property
	def data68(self) -> typing.List[int]:
		return self._instance.Data68
	@property
	def data69(self) -> typing.List[int]:
		return self._instance.Data69
	@property
	def data6a(self) -> typing.List[int]:
		return self._instance.Data6a
	@property
	def data6b(self) -> typing.List[int]:
		return self._instance.Data6b
	@property
	def data6c(self) -> typing.List[int]:
		return self._instance.Data6c
	@property
	def data6d(self) -> typing.List[int]:
		return self._instance.Data6d
	@property
	def data6e(self) -> typing.List[int]:
		return self._instance.Data6e
	@property
	def data6f(self) -> typing.List[int]:
		return self._instance.Data6f
	@property
	def data70(self) -> typing.List[int]:
		return self._instance.Data70
	@property
	def data71(self) -> typing.List[int]:
		return self._instance.Data71
	@property
	def data72(self) -> typing.List[int]:
		return self._instance.Data72
	@property
	def data73(self) -> typing.List[int]:
		return self._instance.Data73
	@property
	def data74(self) -> typing.List[int]:
		return self._instance.Data74
	@property
	def data75(self) -> typing.List[int]:
		return self._instance.Data75
	@property
	def data76(self) -> typing.List[int]:
		return self._instance.Data76
	@property
	def data77(self) -> typing.List[int]:
		return self._instance.Data77
	@property
	def data78(self) -> typing.List[int]:
		return self._instance.Data78
	@property
	def data79(self) -> typing.List[int]:
		return self._instance.Data79
	@property
	def data7a(self) -> typing.List[int]:
		return self._instance.Data7a
	@property
	def data7b(self) -> typing.List[int]:
		return self._instance.Data7b
	@property
	def data7c(self) -> typing.List[int]:
		return self._instance.Data7c
	@property
	def data7d(self) -> typing.List[int]:
		return self._instance.Data7d
	@property
	def data7e(self) -> typing.List[int]:
		return self._instance.Data7e
	@property
	def data7f(self) -> typing.List[int]:
		return self._instance.Data7f
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
