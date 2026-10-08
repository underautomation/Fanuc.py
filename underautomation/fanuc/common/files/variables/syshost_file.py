from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.bin_cfg_variable_type import BinCfgVariableType
from underautomation.fanuc.common.files.variables.dhcp_ctrl_variable_type import DhcpCtrlVariableType
from underautomation.fanuc.common.files.variables.dnss_cfg_variable_type import DnssCfgVariableType
from underautomation.fanuc.common.files.variables.dns_cfg_variable_type import DnsCfgVariableType
from underautomation.fanuc.common.files.variables.ftp_ctrl_variable_type import FtpCtrlVariableType
from underautomation.fanuc.common.files.variables.hostent_variable_type import HostentVariableType
from underautomation.fanuc.common.files.variables.pppcfg_lst_variable_type import PppcfgLstVariableType
from underautomation.fanuc.common.files.variables.rcmcfg_variable_type import RcmcfgVariableType
from underautomation.fanuc.common.files.variables.rdm_cfg_variable_type import RdmCfgVariableType
from underautomation.fanuc.common.files.variables.smb_variable_type import SmbVariableType
from underautomation.fanuc.common.files.variables.smb_clnt_variable_type import SmbClntVariableType
from underautomation.fanuc.common.files.variables.smtp_ctrl_variable_type import SmtpCtrlVariableType
from underautomation.fanuc.common.files.variables.sntp_cfg_variable_type import SntpCfgVariableType
from underautomation.fanuc.common.files.variables.sntp_custom_variable_type import SntpCustomVariableType
from underautomation.fanuc.common.files.variables.tcpipcfg_variable_type import TcpipcfgVariableType
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Common.Files.Variables import SyshostFile as syshost_file

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
		__r = self._instance.BinCfg
		return None if __r is None else BinCfgVariableType(__r)

	@property
	def dhcp_ctrl(self) -> typing.List[DhcpCtrlVariableType]:
		'''Value of variable $DHCP_CTRL'''
		__r = self._instance.DhcpCtrl
		return None if __r is None else [None if x is None else DhcpCtrlVariableType(x) for x in __r]

	@property
	def dnss_cfg(self) -> DnssCfgVariableType:
		'''Value of variable $DNSS_CFG'''
		__r = self._instance.DnssCfg
		return None if __r is None else DnssCfgVariableType(__r)

	@property
	def dns_cfg(self) -> DnsCfgVariableType:
		'''Value of variable $DNS_CFG'''
		__r = self._instance.DnsCfg
		return None if __r is None else DnsCfgVariableType(__r)

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
		__r = self._instance.FtpCtrl
		return None if __r is None else FtpCtrlVariableType(__r)

	@property
	def host_shared(self) -> typing.List[HostentVariableType]:
		'''Value of variable $HOST_SHARED'''
		__r = self._instance.HostShared
		return None if __r is None else [None if x is None else HostentVariableType(x) for x in __r]

	@property
	def ppp_list(self) -> typing.List[PppcfgLstVariableType]:
		'''Value of variable $PPP_LIST'''
		__r = self._instance.PppList
		return None if __r is None else [None if x is None else PppcfgLstVariableType(x) for x in __r]

	@property
	def rcmcfg(self) -> RcmcfgVariableType:
		'''Value of variable $RCMCFG'''
		__r = self._instance.Rcmcfg
		return None if __r is None else RcmcfgVariableType(__r)

	@property
	def rdm_cfg(self) -> RdmCfgVariableType:
		'''Value of variable $RDM_CFG'''
		__r = self._instance.RdmCfg
		return None if __r is None else RdmCfgVariableType(__r)

	@property
	def smb(self) -> SmbVariableType:
		'''Value of variable $SMB'''
		__r = self._instance.Smb
		return None if __r is None else SmbVariableType(__r)

	@property
	def smb_clnt(self) -> typing.List[SmbClntVariableType]:
		'''Value of variable $SMB_CLNT'''
		__r = self._instance.SmbClnt
		return None if __r is None else [None if x is None else SmbClntVariableType(x) for x in __r]

	@property
	def smtp_ctrl(self) -> SmtpCtrlVariableType:
		'''Value of variable $SMTP_CTRL'''
		__r = self._instance.SmtpCtrl
		return None if __r is None else SmtpCtrlVariableType(__r)

	@property
	def sntp_cfg(self) -> SntpCfgVariableType:
		'''Value of variable $SNTP_CFG'''
		__r = self._instance.SntpCfg
		return None if __r is None else SntpCfgVariableType(__r)

	@property
	def sntp_custom(self) -> SntpCustomVariableType:
		'''Value of variable $SNTP_CUSTOM'''
		__r = self._instance.SntpCustom
		return None if __r is None else SntpCustomVariableType(__r)

	@property
	def tcpipcfg(self) -> TcpipcfgVariableType:
		'''Value of variable $TCPIPCFG'''
		__r = self._instance.Tcpipcfg
		return None if __r is None else TcpipcfgVariableType(__r)

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
