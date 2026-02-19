import typing
from underautomation.fanuc.ftp.variables.cf_paramgp_variable_type import CfParamgpVariableType
from underautomation.fanuc.ftp.variables.crcfg_variable_type import CrcfgVariableType
from underautomation.fanuc.ftp.variables.enc_stat_variable_type import EncStatVariableType
from underautomation.fanuc.ftp.variables.fmr2_grp_variable_type import Fmr2GrpVariableType
from underautomation.fanuc.ftp.variables.upr_variable_type import UprVariableType
from underautomation.fanuc.ftp.variables.hscd_grp_variable_type import HscdGrpVariableType
from underautomation.fanuc.ftp.variables.ujr_grp_variable_type import UjrGrpVariableType
from underautomation.fanuc.ftp.variables.misc_grp_variable_type import MiscGrpVariableType
from underautomation.fanuc.ftp.variables.mrr2_grp_variable_type import Mrr2GrpVariableType
from underautomation.fanuc.ftp.variables.mrr_grp_variable_type import MrrGrpVariableType
from underautomation.fanuc.ftp.variables.plid_grp_variable_type import PlidGrpVariableType
from underautomation.fanuc.ftp.variables.plid_sv_variable_type import PlidSvVariableType
from underautomation.fanuc.ftp.variables.plst_grp_variable_type import PlstGrpVariableType
from underautomation.fanuc.ftp.variables.podata_variable_type import PodataVariableType
from underautomation.fanuc.ftp.variables.poinfo_variable_type import PoinfoVariableType
from underautomation.fanuc.ftp.variables.poio_variable_type import PoioVariableType
from underautomation.fanuc.ftp.variables.pssave_grp_variable_type import PssaveGrpVariableType
from underautomation.fanuc.ftp.variables.scr_variable_type import ScrVariableType
from underautomation.fanuc.ftp.variables.scr_grp_variable_type import ScrGrpVariableType
from underautomation.fanuc.ftp.variables.tbccfg_variable_type import TbccfgVariableType
from underautomation.fanuc.ftp.variables.tbc_grp_variable_type import TbcGrpVariableType
from underautomation.fanuc.ftp.variables.tbjcfg_variable_type import TbjcfgVariableType
from underautomation.fanuc.ftp.variables.tbj_grp_variable_type import TbjGrpVariableType
from underautomation.fanuc.ftp.variables.torqctrl_variable_type import TorqctrlVariableType
from underautomation.fanuc.ftp.variables.tsr_grp_variable_type import TsrGrpVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import SymotnFile as symotn_file

class SymotnFile(GenericVariableFile):
	'''Describes the Fanuc variable file symotn.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = symotn_file()
		else:
			self._instance = _internal

	@property
	def cf_paramgp(self) -> typing.List[CfParamgpVariableType]:
		'''Value of variable $CF_PARAMGP'''
		return [CfParamgpVariableType(x) for x in self._instance.CfParamgp]

	@property
	def crcfg(self) -> CrcfgVariableType:
		'''Value of variable $CRCFG'''
		return CrcfgVariableType(self._instance.Crcfg)

	@property
	def enc_stat(self) -> typing.List[EncStatVariableType]:
		'''Value of variable $ENC_STAT'''
		return [EncStatVariableType(x) for x in self._instance.EncStat]

	@property
	def fmr2_grp(self) -> typing.List[Fmr2GrpVariableType]:
		'''Value of variable $FMR2_GRP'''
		return [Fmr2GrpVariableType(x) for x in self._instance.Fmr2Grp]

	@property
	def group(self) -> typing.List[UprVariableType]:
		'''Value of variable $GROUP'''
		return [UprVariableType(x) for x in self._instance.Group]

	@property
	def hscd_group(self) -> typing.List[HscdGrpVariableType]:
		'''Value of variable $HSCD_GROUP'''
		return [HscdGrpVariableType(x) for x in self._instance.HscdGroup]

	@property
	def jog_group(self) -> typing.List[UjrGrpVariableType]:
		'''Value of variable $JOG_GROUP'''
		return [UjrGrpVariableType(x) for x in self._instance.JogGroup]

	@property
	def misc(self) -> typing.List[MiscGrpVariableType]:
		'''Value of variable $MISC'''
		return [MiscGrpVariableType(x) for x in self._instance.Misc]

	@property
	def motask_data(self) -> int:
		'''Value of variable $MOTASK_DATA'''
		return self._instance.MotaskData

	@property
	def mrr2_grp(self) -> typing.List[Mrr2GrpVariableType]:
		'''Value of variable $MRR2_GRP'''
		return [Mrr2GrpVariableType(x) for x in self._instance.Mrr2Grp]

	@property
	def mrr_grp(self) -> typing.List[MrrGrpVariableType]:
		'''Value of variable $MRR_GRP'''
		return [MrrGrpVariableType(x) for x in self._instance.MrrGrp]

	@property
	def param2_grp(self) -> typing.List[Mrr2GrpVariableType]:
		'''Value of variable $PARAM2_GRP'''
		return [Mrr2GrpVariableType(x) for x in self._instance.Param2Grp]

	@property
	def param_group(self) -> typing.List[MrrGrpVariableType]:
		'''Value of variable $PARAM_GROUP'''
		return [MrrGrpVariableType(x) for x in self._instance.ParamGroup]

	@property
	def plid_grp(self) -> typing.List[PlidGrpVariableType]:
		'''Value of variable $PLID_GRP'''
		return [PlidGrpVariableType(x) for x in self._instance.PlidGrp]

	@property
	def plid_sv(self) -> PlidSvVariableType:
		'''Value of variable $PLID_SV'''
		return PlidSvVariableType(self._instance.PlidSv)

	@property
	def plst_grp1(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP1'''
		return [PlstGrpVariableType(x) for x in self._instance.PlstGrp1]

	@property
	def plst_grp2(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP2'''
		return [PlstGrpVariableType(x) for x in self._instance.PlstGrp2]

	@property
	def plst_grp3(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP3'''
		return [PlstGrpVariableType(x) for x in self._instance.PlstGrp3]

	@property
	def plst_grp4(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP4'''
		return [PlstGrpVariableType(x) for x in self._instance.PlstGrp4]

	@property
	def plst_grp5(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP5'''
		return [PlstGrpVariableType(x) for x in self._instance.PlstGrp5]

	@property
	def plst_grpmad(self) -> int:
		'''Value of variable $PLST_GRPMAD'''
		return self._instance.PlstGrpmad

	@property
	def plst_parnum(self) -> typing.List[int]:
		'''Value of variable $PLST_PARNUM'''
		return self._instance.PlstParnum

	@property
	def plst_schmad(self) -> int:
		'''Value of variable $PLST_SCHMAD'''
		return self._instance.PlstSchmad

	@property
	def plst_schnum(self) -> int:
		'''Value of variable $PLST_SCHNUM'''
		return self._instance.PlstSchnum

	@property
	def plst_updnum(self) -> typing.List[int]:
		'''Value of variable $PLST_UPDNUM'''
		return self._instance.PlstUpdnum

	@property
	def podata_grp(self) -> typing.List[PodataVariableType]:
		'''Value of variable $PODATA_GRP'''
		return [PodataVariableType(x) for x in self._instance.PodataGrp]

	@property
	def poinfo_grp(self) -> typing.List[PoinfoVariableType]:
		'''Value of variable $POINFO_GRP'''
		return [PoinfoVariableType(x) for x in self._instance.PoinfoGrp]

	@property
	def poio_grp(self) -> typing.List[PoioVariableType]:
		'''Value of variable $POIO_GRP'''
		return [PoioVariableType(x) for x in self._instance.PoioGrp]

	@property
	def pssave_grp(self) -> typing.List[PssaveGrpVariableType]:
		'''Value of variable $PSSAVE_GRP'''
		return [PssaveGrpVariableType(x) for x in self._instance.PssaveGrp]

	@property
	def scr(self) -> ScrVariableType:
		'''Value of variable $SCR'''
		return ScrVariableType(self._instance.Scr)

	@property
	def scr_grp(self) -> typing.List[ScrGrpVariableType]:
		'''Value of variable $SCR_GRP'''
		return [ScrGrpVariableType(x) for x in self._instance.ScrGrp]

	@property
	def tbccfg(self) -> TbccfgVariableType:
		'''Value of variable $TBCCFG'''
		return TbccfgVariableType(self._instance.Tbccfg)

	@property
	def tbc_grp(self) -> typing.List[TbcGrpVariableType]:
		'''Value of variable $TBC_GRP'''
		return [TbcGrpVariableType(x) for x in self._instance.TbcGrp]

	@property
	def tbjcfg(self) -> TbjcfgVariableType:
		'''Value of variable $TBJCFG'''
		return TbjcfgVariableType(self._instance.Tbjcfg)

	@property
	def tbj_grp(self) -> typing.List[TbjGrpVariableType]:
		'''Value of variable $TBJ_GRP'''
		return [TbjGrpVariableType(x) for x in self._instance.TbjGrp]

	@property
	def torqctrl(self) -> TorqctrlVariableType:
		'''Value of variable $TORQCTRL'''
		return TorqctrlVariableType(self._instance.Torqctrl)

	@property
	def tsr_grp(self) -> typing.List[TsrGrpVariableType]:
		'''Value of variable $TSR_GRP'''
		return [TsrGrpVariableType(x) for x in self._instance.TsrGrp]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SymotnFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
