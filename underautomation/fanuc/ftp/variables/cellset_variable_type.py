import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CellsetVariableType as cellset_variable_type

class CellsetVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cellset_variable_type()
		else:
			self._instance = _internal
	@property
	def gi_stysel_p(self) -> str:
		return self._instance.GiStyselP
	@property
	def gi_stysel_t(self) -> int:
		return self._instance.GiStyselT
	@property
	def gi_stysel_i(self) -> int:
		return self._instance.GiStyselI
	@property
	def go_stysel_p(self) -> str:
		return self._instance.GoStyselP
	@property
	def go_stysel_t(self) -> int:
		return self._instance.GoStyselT
	@property
	def go_stysel_i(self) -> int:
		return self._instance.GoStyselI
	@property
	def do_stystr_p(self) -> str:
		return self._instance.DoStystrP
	@property
	def do_stystr_t(self) -> int:
		return self._instance.DoStystrT
	@property
	def do_stystr_i(self) -> int:
		return self._instance.DoStystrI
	@property
	def di_inisty_p(self) -> str:
		return self._instance.DiInistyP
	@property
	def di_inisty_t(self) -> int:
		return self._instance.DiInistyT
	@property
	def di_inisty_i(self) -> int:
		return self._instance.DiInistyI
	@property
	def ui_start_i(self) -> int:
		return self._instance.UiStartI
	@property
	def rsrpns1_t(self) -> int:
		return self._instance.Rsrpns1T
	@property
	def rsrpns2_t(self) -> int:
		return self._instance.Rsrpns2T
	@property
	def rsrpns3_t(self) -> int:
		return self._instance.Rsrpns3T
	@property
	def rsrpns4_t(self) -> int:
		return self._instance.Rsrpns4T
	@property
	def rsrpns5_t(self) -> int:
		return self._instance.Rsrpns5T
	@property
	def rsrpns6_t(self) -> int:
		return self._instance.Rsrpns6T
	@property
	def rsrpns7_t(self) -> int:
		return self._instance.Rsrpns7T
	@property
	def rsrpns8_t(self) -> int:
		return self._instance.Rsrpns8T
	@property
	def pnstrob_t(self) -> int:
		return self._instance.PnstrobT
	@property
	def acksno1_t(self) -> int:
		return self._instance.Acksno1T
	@property
	def acksno2_t(self) -> int:
		return self._instance.Acksno2T
	@property
	def acksno3_t(self) -> int:
		return self._instance.Acksno3T
	@property
	def acksno4_t(self) -> int:
		return self._instance.Acksno4T
	@property
	def acksno5_t(self) -> int:
		return self._instance.Acksno5T
	@property
	def acksno6_t(self) -> int:
		return self._instance.Acksno6T
	@property
	def acksno7_t(self) -> int:
		return self._instance.Acksno7T
	@property
	def acksno8_t(self) -> int:
		return self._instance.Acksno8T
	@property
	def ackstrob_t(self) -> int:
		return self._instance.AckstrobT
	@property
	def rsrpns1_i(self) -> int:
		return self._instance.Rsrpns1I
	@property
	def rsrpns2_i(self) -> int:
		return self._instance.Rsrpns2I
	@property
	def rsrpns3_i(self) -> int:
		return self._instance.Rsrpns3I
	@property
	def rsrpns4_i(self) -> int:
		return self._instance.Rsrpns4I
	@property
	def rsrpns5_i(self) -> int:
		return self._instance.Rsrpns5I
	@property
	def rsrpns6_i(self) -> int:
		return self._instance.Rsrpns6I
	@property
	def rsrpns7_i(self) -> int:
		return self._instance.Rsrpns7I
	@property
	def rsrpns8_i(self) -> int:
		return self._instance.Rsrpns8I
	@property
	def pnstrob_i(self) -> int:
		return self._instance.PnstrobI
	@property
	def pnsgin_i(self) -> int:
		return self._instance.PnsginI
	@property
	def pnsdin_i(self) -> int:
		return self._instance.PnsdinI
	@property
	def acksno1_i(self) -> int:
		return self._instance.Acksno1I
	@property
	def acksno2_i(self) -> int:
		return self._instance.Acksno2I
	@property
	def acksno3_i(self) -> int:
		return self._instance.Acksno3I
	@property
	def acksno4_i(self) -> int:
		return self._instance.Acksno4I
	@property
	def acksno5_i(self) -> int:
		return self._instance.Acksno5I
	@property
	def acksno6_i(self) -> int:
		return self._instance.Acksno6I
	@property
	def acksno7_i(self) -> int:
		return self._instance.Acksno7I
	@property
	def acksno8_i(self) -> int:
		return self._instance.Acksno8I
	@property
	def snack_i(self) -> int:
		return self._instance.SnackI
	@property
	def pnsgout_i(self) -> int:
		return self._instance.PnsgoutI
	@property
	def pnsdout_i(self) -> int:
		return self._instance.PnsdoutI
	@property
	def di_optna_p(self) -> str:
		return self._instance.DiOptnaP
	@property
	def di_optna_t(self) -> int:
		return self._instance.DiOptnaT
	@property
	def di_optna_i(self) -> int:
		return self._instance.DiOptnaI
	@property
	def di_optnb_p(self) -> str:
		return self._instance.DiOptnbP
	@property
	def di_optnb_t(self) -> int:
		return self._instance.DiOptnbT
	@property
	def di_optnb_i(self) -> int:
		return self._instance.DiOptnbI
	@property
	def di_optnc_p(self) -> str:
		return self._instance.DiOptncP
	@property
	def di_optnc_t(self) -> int:
		return self._instance.DiOptncT
	@property
	def di_optnc_i(self) -> int:
		return self._instance.DiOptncI
	@property
	def gi_decsn_p(self) -> str:
		return self._instance.GiDecsnP
	@property
	def gi_decsn_t(self) -> int:
		return self._instance.GiDecsnT
	@property
	def gi_decsn_i(self) -> int:
		return self._instance.GiDecsnI
	@property
	def di_tryout_p(self) -> str:
		return self._instance.DiTryoutP
	@property
	def di_tryout_t(self) -> int:
		return self._instance.DiTryoutT
	@property
	def di_tryout_i(self) -> int:
		return self._instance.DiTryoutI
	@property
	def di_pthcnt_p(self) -> str:
		return self._instance.DiPthcntP
	@property
	def di_pthcnt_t(self) -> int:
		return self._instance.DiPthcntT
	@property
	def di_pthcnt_i(self) -> int:
		return self._instance.DiPthcntI
	@property
	def do_incycl_p(self) -> str:
		return self._instance.DoIncyclP
	@property
	def do_incycl_t(self) -> int:
		return self._instance.DoIncyclT
	@property
	def do_incycl_i(self) -> int:
		return self._instance.DoIncyclI
	@property
	def do_taskok_p(self) -> str:
		return self._instance.DoTaskokP
	@property
	def do_taskok_t(self) -> int:
		return self._instance.DoTaskokT
	@property
	def do_taskok_i(self) -> int:
		return self._instance.DoTaskokI
	@property
	def do_optna_p(self) -> str:
		return self._instance.DoOptnaP
	@property
	def do_optna_t(self) -> int:
		return self._instance.DoOptnaT
	@property
	def do_optna_i(self) -> int:
		return self._instance.DoOptnaI
	@property
	def do_optnb_p(self) -> str:
		return self._instance.DoOptnbP
	@property
	def do_optnb_t(self) -> int:
		return self._instance.DoOptnbT
	@property
	def do_optnb_i(self) -> int:
		return self._instance.DoOptnbI
	@property
	def do_optnc_p(self) -> str:
		return self._instance.DoOptncP
	@property
	def do_optnc_t(self) -> int:
		return self._instance.DoOptncT
	@property
	def do_optnc_i(self) -> int:
		return self._instance.DoOptncI
	@property
	def go_decsn_p(self) -> str:
		return self._instance.GoDecsnP
	@property
	def go_decsn_t(self) -> int:
		return self._instance.GoDecsnT
	@property
	def go_decsn_i(self) -> int:
		return self._instance.GoDecsnI
	@property
	def do_intlck_p(self) -> str:
		return self._instance.DoIntlckP
	@property
	def do_intlck_t(self) -> int:
		return self._instance.DoIntlckT
	@property
	def do_intlck_i(self) -> int:
		return self._instance.DoIntlckI
	@property
	def do_isolat_p(self) -> str:
		return self._instance.DoIsolatP
	@property
	def do_isolat_t(self) -> int:
		return self._instance.DoIsolatT
	@property
	def do_isolat_i(self) -> int:
		return self._instance.DoIsolatI
	@property
	def do_mansty_p(self) -> str:
		return self._instance.DoManstyP
	@property
	def do_mansty_t(self) -> int:
		return self._instance.DoManstyT
	@property
	def do_mansty_i(self) -> int:
		return self._instance.DoManstyI
	@property
	def go_pthseg_p(self) -> str:
		return self._instance.GoPthsegP
	@property
	def go_pthseg_t(self) -> int:
		return self._instance.GoPthsegT
	@property
	def go_pthseg_i(self) -> int:
		return self._instance.GoPthsegI
	@property
	def do_pthreq_p(self) -> str:
		return self._instance.DoPthreqP
	@property
	def do_pthreq_t(self) -> int:
		return self._instance.DoPthreqT
	@property
	def do_pthreq_i(self) -> int:
		return self._instance.DoPthreqI
	@property
	def do_tryout_p(self) -> str:
		return self._instance.DoTryoutP
	@property
	def do_tryout_t(self) -> int:
		return self._instance.DoTryoutT
	@property
	def do_tryout_i(self) -> int:
		return self._instance.DoTryoutI
	@property
	def do_hfault_p(self) -> str:
		return self._instance.DoHfaultP
	@property
	def do_hfault_t(self) -> int:
		return self._instance.DoHfaultT
	@property
	def do_hfault_i(self) -> int:
		return self._instance.DoHfaultI
	@property
	def do_halert_p(self) -> str:
		return self._instance.DoHalertP
	@property
	def do_halert_t(self) -> int:
		return self._instance.DoHalertT
	@property
	def do_halert_i(self) -> int:
		return self._instance.DoHalertI
	@property
	def do_heartb_t(self) -> int:
		return self._instance.DoHeartbT
	@property
	def do_heartb_i(self) -> int:
		return self._instance.DoHeartbI
	@property
	def do_hndbrk_t(self) -> int:
		return self._instance.DoHndbrkT
	@property
	def do_hndbrk_i(self) -> int:
		return self._instance.DoHndbrkI
	@property
	def do_prgabt_t(self) -> int:
		return self._instance.DoPrgabtT
	@property
	def do_prgabt_i(self) -> int:
		return self._instance.DoPrgabtI
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
