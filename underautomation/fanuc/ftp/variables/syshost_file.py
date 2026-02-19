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
from UnderAutomation.Fanuc.Ftp.Variables import SyshostFile as syshost_file

class SyshostFile(GenericVariableFile):
	'''Describes the Fanuc variable file syshost.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = syshost_file()
		else:
			self._instance = _internal

	@property
	def bin_cfg(self) -> BinCfgVariableType:
		'''Value of variable $BIN_CFG'''
		return BinCfgVariableType(self._instance.BinCfg)

	@property
	def dhcp_ctrl(self) -> typing.List[DhcpCtrlVariableType]:
		'''Value of variable $DHCP_CTRL'''
		return [DhcpCtrlVariableType(x) for x in self._instance.DhcpCtrl]

	@property
	def dnss_cfg(self) -> DnssCfgVariableType:
		'''Value of variable $DNSS_CFG'''
		return DnssCfgVariableType(self._instance.DnssCfg)

	@property
	def dns_cfg(self) -> DnsCfgVariableType:
		'''Value of variable $DNS_CFG'''
		return DnsCfgVariableType(self._instance.DnsCfg)

	@property
	def dns_loc_dom(self) -> typing.List[int]:
		'''Value of variable $DNS_LOC_DOM'''
		return self._instance.DnsLocDom

	@property
	def eth_fltr(self) -> typing.List[int]:
		'''Value of variable $ETH_FLTR'''
		return self._instance.EthFltr

	@property
	def ftp_ctrl(self) -> FtpCtrlVariableType:
		'''Value of variable $FTP_CTRL'''
		return FtpCtrlVariableType(self._instance.FtpCtrl)

	@property
	def host_shared(self) -> typing.List[HostentVariableType]:
		'''Value of variable $HOST_SHARED'''
		return [HostentVariableType(x) for x in self._instance.HostShared]

	@property
	def ppp_list(self) -> typing.List[PppcfgLstVariableType]:
		'''Value of variable $PPP_LIST'''
		return [PppcfgLstVariableType(x) for x in self._instance.PppList]

	@property
	def rcmcfg(self) -> RcmcfgVariableType:
		'''Value of variable $RCMCFG'''
		return RcmcfgVariableType(self._instance.Rcmcfg)

	@property
	def rdm_cfg(self) -> RdmCfgVariableType:
		'''Value of variable $RDM_CFG'''
		return RdmCfgVariableType(self._instance.RdmCfg)

	@property
	def smb(self) -> SmbVariableType:
		'''Value of variable $SMB'''
		return SmbVariableType(self._instance.Smb)

	@property
	def smb_clnt(self) -> typing.List[SmbClntVariableType]:
		'''Value of variable $SMB_CLNT'''
		return [SmbClntVariableType(x) for x in self._instance.SmbClnt]

	@property
	def smtp_ctrl(self) -> SmtpCtrlVariableType:
		'''Value of variable $SMTP_CTRL'''
		return SmtpCtrlVariableType(self._instance.SmtpCtrl)

	@property
	def sntp_cfg(self) -> SntpCfgVariableType:
		'''Value of variable $SNTP_CFG'''
		return SntpCfgVariableType(self._instance.SntpCfg)

	@property
	def sntp_custom(self) -> SntpCustomVariableType:
		'''Value of variable $SNTP_CUSTOM'''
		return SntpCustomVariableType(self._instance.SntpCustom)

	@property
	def tcpipcfg(self) -> TcpipcfgVariableType:
		'''Value of variable $TCPIPCFG'''
		return TcpipcfgVariableType(self._instance.Tcpipcfg)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SyshostFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
