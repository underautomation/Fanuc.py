import typing
from underautomation.fanuc.ftp.internal.ftp_client_base import FtpClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import FtpClientInternal as ftp_client_internal

class FtpClientInternal(FtpClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_client_internal()
		else:
			self._instance = _internal
