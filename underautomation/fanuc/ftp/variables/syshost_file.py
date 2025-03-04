import typing
from underautomation.fanuc.ftp.variables.bin_cfg_variable_type import BinCfgVariableType
from underautomation.fanuc.ftp.variables.dhcp_ctrl_variable_type import DhcpCtrlVariableType
from underautomation.fanuc.ftp.variables.dnss_cfg_variable_type import DnssCfgVariableType
from underautomation.fanuc.ftp.variables.dns_cfg_variable_type import DnsCfgVariableType
from underautomation.fanuc.ftp.variables.ftp_ctrl_variable_type import FtpCtrlVariableType
from underautomation.fanuc.ftp.variables.hostent_variable_type import HostentVariableType
from underautomation.fanuc.ftp.variables.pppcfg_lst_variable_type import PppcfgLstVariableType
from underautomation.fanuc.ftp.variables.rcmcfg_variable_type import RcmcfgVariableType
from underautomation.fanuc.ftp.variables.rdm_cfg_variable_type import RdmCfgVariableType
from underautomation.fanuc.ftp.variables.smb_variable_type import SmbVariableType
from underautomation.fanuc.ftp.variables.smb_clnt_variable_type import SmbClntVariableType
from underautomation.fanuc.ftp.variables.smtp_ctrl_variable_type import SmtpCtrlVariableType
from underautomation.fanuc.ftp.variables.sntp_cfg_variable_type import SntpCfgVariableType
from underautomation.fanuc.ftp.variables.sntp_custom_variable_type import SntpCustomVariableType
from underautomation.fanuc.ftp.variables.tcpipcfg_variable_type import TcpipcfgVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SyshostFile as syshost_file

class SyshostFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = syshost_file()
		else:
			self._instance = _internal
	@property
	def bin_cfg(self) -> BinCfgVariableType:
		return BinCfgVariableType(self._instance.BinCfg)
	@property
	def dhcp_ctrl(self) -> typing.List[DhcpCtrlVariableType]:
		return [DhcpCtrlVariableType(x) for x in self._instance.DhcpCtrl]
	@property
	def dnss_cfg(self) -> DnssCfgVariableType:
		return DnssCfgVariableType(self._instance.DnssCfg)
	@property
	def dns_cfg(self) -> DnsCfgVariableType:
		return DnsCfgVariableType(self._instance.DnsCfg)
	@property
	def dns_loc_dom(self) -> typing.List[int]:
		return self._instance.DnsLocDom
	@property
	def eth_fltr(self) -> typing.List[int]:
		return self._instance.EthFltr
	@property
	def ftp_ctrl(self) -> FtpCtrlVariableType:
		return FtpCtrlVariableType(self._instance.FtpCtrl)
	@property
	def host_shared(self) -> typing.List[HostentVariableType]:
		return [HostentVariableType(x) for x in self._instance.HostShared]
	@property
	def ppp_list(self) -> typing.List[PppcfgLstVariableType]:
		return [PppcfgLstVariableType(x) for x in self._instance.PppList]
	@property
	def rcmcfg(self) -> RcmcfgVariableType:
		return RcmcfgVariableType(self._instance.Rcmcfg)
	@property
	def rdm_cfg(self) -> RdmCfgVariableType:
		return RdmCfgVariableType(self._instance.RdmCfg)
	@property
	def smb(self) -> SmbVariableType:
		return SmbVariableType(self._instance.Smb)
	@property
	def smb_clnt(self) -> typing.List[SmbClntVariableType]:
		return [SmbClntVariableType(x) for x in self._instance.SmbClnt]
	@property
	def smtp_ctrl(self) -> SmtpCtrlVariableType:
		return SmtpCtrlVariableType(self._instance.SmtpCtrl)
	@property
	def sntp_cfg(self) -> SntpCfgVariableType:
		return SntpCfgVariableType(self._instance.SntpCfg)
	@property
	def sntp_custom(self) -> SntpCustomVariableType:
		return SntpCustomVariableType(self._instance.SntpCustom)
	@property
	def tcpipcfg(self) -> TcpipcfgVariableType:
		return TcpipcfgVariableType(self._instance.Tcpipcfg)
