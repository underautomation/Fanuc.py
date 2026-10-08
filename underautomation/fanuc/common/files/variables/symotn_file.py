from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.cf_paramgp_variable_type import CfParamgpVariableType
from underautomation.fanuc.common.files.variables.crcfg_variable_type import CrcfgVariableType
from underautomation.fanuc.common.files.variables.enc_stat_variable_type import EncStatVariableType
from underautomation.fanuc.common.files.variables.fmr2_grp_variable_type import Fmr2GrpVariableType
from underautomation.fanuc.common.files.variables.upr_variable_type import UprVariableType
from underautomation.fanuc.common.files.variables.hscd_grp_variable_type import HscdGrpVariableType
from underautomation.fanuc.common.files.variables.ujr_grp_variable_type import UjrGrpVariableType
from underautomation.fanuc.common.files.variables.misc_grp_variable_type import MiscGrpVariableType
from underautomation.fanuc.common.files.variables.mrr2_grp_variable_type import Mrr2GrpVariableType
from underautomation.fanuc.common.files.variables.mrr_grp_variable_type import MrrGrpVariableType
from underautomation.fanuc.common.files.variables.plid_grp_variable_type import PlidGrpVariableType
from underautomation.fanuc.common.files.variables.plid_sv_variable_type import PlidSvVariableType
from underautomation.fanuc.common.files.variables.plst_grp_variable_type import PlstGrpVariableType
from underautomation.fanuc.common.files.variables.podata_variable_type import PodataVariableType
from underautomation.fanuc.common.files.variables.poinfo_variable_type import PoinfoVariableType
from underautomation.fanuc.common.files.variables.poio_variable_type import PoioVariableType
from underautomation.fanuc.common.files.variables.pssave_grp_variable_type import PssaveGrpVariableType
from underautomation.fanuc.common.files.variables.scr_variable_type import ScrVariableType
from underautomation.fanuc.common.files.variables.scr_grp_variable_type import ScrGrpVariableType
from underautomation.fanuc.common.files.variables.tbccfg_variable_type import TbccfgVariableType
from underautomation.fanuc.common.files.variables.tbc_grp_variable_type import TbcGrpVariableType
from underautomation.fanuc.common.files.variables.tbjcfg_variable_type import TbjcfgVariableType
from underautomation.fanuc.common.files.variables.tbj_grp_variable_type import TbjGrpVariableType
from underautomation.fanuc.common.files.variables.torqctrl_variable_type import TorqctrlVariableType
from underautomation.fanuc.common.files.variables.tsr_grp_variable_type import TsrGrpVariableType
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Common.Files.Variables import SymotnFile as symotn_file

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
		__r = self._instance.CfParamgp
		return None if __r is None else [None if x is None else CfParamgpVariableType(x) for x in __r]

	@property
	def crcfg(self) -> CrcfgVariableType:
		'''Value of variable $CRCFG'''
		__r = self._instance.Crcfg
		return None if __r is None else CrcfgVariableType(__r)

	@property
	def enc_stat(self) -> typing.List[EncStatVariableType]:
		'''Value of variable $ENC_STAT'''
		__r = self._instance.EncStat
		return None if __r is None else [None if x is None else EncStatVariableType(x) for x in __r]

	@property
	def fmr2_grp(self) -> typing.List[Fmr2GrpVariableType]:
		'''Value of variable $FMR2_GRP'''
		__r = self._instance.Fmr2Grp
		return None if __r is None else [None if x is None else Fmr2GrpVariableType(x) for x in __r]

	@property
	def group(self) -> typing.List[UprVariableType]:
		'''Value of variable $GROUP'''
		__r = self._instance.Group
		return None if __r is None else [None if x is None else UprVariableType(x) for x in __r]

	@property
	def hscd_group(self) -> typing.List[HscdGrpVariableType]:
		'''Value of variable $HSCD_GROUP'''
		__r = self._instance.HscdGroup
		return None if __r is None else [None if x is None else HscdGrpVariableType(x) for x in __r]

	@property
	def jog_group(self) -> typing.List[UjrGrpVariableType]:
		'''Value of variable $JOG_GROUP'''
		__r = self._instance.JogGroup
		return None if __r is None else [None if x is None else UjrGrpVariableType(x) for x in __r]

	@property
	def misc(self) -> typing.List[MiscGrpVariableType]:
		'''Value of variable $MISC'''
		__r = self._instance.Misc
		return None if __r is None else [None if x is None else MiscGrpVariableType(x) for x in __r]

	@property
	def motask_data(self) -> int:
		'''Value of variable $MOTASK_DATA'''
		return self._instance.MotaskData

	@property
	def mrr2_grp(self) -> typing.List[Mrr2GrpVariableType]:
		'''Value of variable $MRR2_GRP'''
		__r = self._instance.Mrr2Grp
		return None if __r is None else [None if x is None else Mrr2GrpVariableType(x) for x in __r]

	@property
	def mrr_grp(self) -> typing.List[MrrGrpVariableType]:
		'''Value of variable $MRR_GRP'''
		__r = self._instance.MrrGrp
		return None if __r is None else [None if x is None else MrrGrpVariableType(x) for x in __r]

	@property
	def param2_grp(self) -> typing.List[Mrr2GrpVariableType]:
		'''Value of variable $PARAM2_GRP'''
		__r = self._instance.Param2Grp
		return None if __r is None else [None if x is None else Mrr2GrpVariableType(x) for x in __r]

	@property
	def param_group(self) -> typing.List[MrrGrpVariableType]:
		'''Value of variable $PARAM_GROUP'''
		__r = self._instance.ParamGroup
		return None if __r is None else [None if x is None else MrrGrpVariableType(x) for x in __r]

	@property
	def plid_grp(self) -> typing.List[PlidGrpVariableType]:
		'''Value of variable $PLID_GRP'''
		__r = self._instance.PlidGrp
		return None if __r is None else [None if x is None else PlidGrpVariableType(x) for x in __r]

	@property
	def plid_sv(self) -> PlidSvVariableType:
		'''Value of variable $PLID_SV'''
		__r = self._instance.PlidSv
		return None if __r is None else PlidSvVariableType(__r)

	@property
	def plst_grp1(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP1'''
		__r = self._instance.PlstGrp1
		return None if __r is None else [None if x is None else PlstGrpVariableType(x) for x in __r]

	@property
	def plst_grp2(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP2'''
		__r = self._instance.PlstGrp2
		return None if __r is None else [None if x is None else PlstGrpVariableType(x) for x in __r]

	@property
	def plst_grp3(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP3'''
		__r = self._instance.PlstGrp3
		return None if __r is None else [None if x is None else PlstGrpVariableType(x) for x in __r]

	@property
	def plst_grp4(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP4'''
		__r = self._instance.PlstGrp4
		return None if __r is None else [None if x is None else PlstGrpVariableType(x) for x in __r]

	@property
	def plst_grp5(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP5'''
		__r = self._instance.PlstGrp5
		return None if __r is None else [None if x is None else PlstGrpVariableType(x) for x in __r]

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
		__r = self._instance.PodataGrp
		return None if __r is None else [None if x is None else PodataVariableType(x) for x in __r]

	@property
	def poinfo_grp(self) -> typing.List[PoinfoVariableType]:
		'''Value of variable $POINFO_GRP'''
		__r = self._instance.PoinfoGrp
		return None if __r is None else [None if x is None else PoinfoVariableType(x) for x in __r]

	@property
	def poio_grp(self) -> typing.List[PoioVariableType]:
		'''Value of variable $POIO_GRP'''
		__r = self._instance.PoioGrp
		return None if __r is None else [None if x is None else PoioVariableType(x) for x in __r]

	@property
	def pssave_grp(self) -> typing.List[PssaveGrpVariableType]:
		'''Value of variable $PSSAVE_GRP'''
		__r = self._instance.PssaveGrp
		return None if __r is None else [None if x is None else PssaveGrpVariableType(x) for x in __r]

	@property
	def scr(self) -> ScrVariableType:
		'''Value of variable $SCR'''
		__r = self._instance.Scr
		return None if __r is None else ScrVariableType(__r)

	@property
	def scr_grp(self) -> typing.List[ScrGrpVariableType]:
		'''Value of variable $SCR_GRP'''
		__r = self._instance.ScrGrp
		return None if __r is None else [None if x is None else ScrGrpVariableType(x) for x in __r]

	@property
	def tbccfg(self) -> TbccfgVariableType:
		'''Value of variable $TBCCFG'''
		__r = self._instance.Tbccfg
		return None if __r is None else TbccfgVariableType(__r)

	@property
	def tbc_grp(self) -> typing.List[TbcGrpVariableType]:
		'''Value of variable $TBC_GRP'''
		__r = self._instance.TbcGrp
		return None if __r is None else [None if x is None else TbcGrpVariableType(x) for x in __r]

	@property
	def tbjcfg(self) -> TbjcfgVariableType:
		'''Value of variable $TBJCFG'''
		__r = self._instance.Tbjcfg
		return None if __r is None else TbjcfgVariableType(__r)

	@property
	def tbj_grp(self) -> typing.List[TbjGrpVariableType]:
		'''Value of variable $TBJ_GRP'''
		__r = self._instance.TbjGrp
		return None if __r is None else [None if x is None else TbjGrpVariableType(x) for x in __r]

	@property
	def torqctrl(self) -> TorqctrlVariableType:
		'''Value of variable $TORQCTRL'''
		__r = self._instance.Torqctrl
		return None if __r is None else TorqctrlVariableType(__r)

	@property
	def tsr_grp(self) -> typing.List[TsrGrpVariableType]:
		'''Value of variable $TSR_GRP'''
		__r = self._instance.TsrGrp
		return None if __r is None else [None if x is None else TsrGrpVariableType(x) for x in __r]

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
