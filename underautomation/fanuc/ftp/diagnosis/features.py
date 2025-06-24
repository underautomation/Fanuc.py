import typing
from underautomation.fanuc.ftp.diagnosis.feature import Feature
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import Features as features

class Features:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = features()
		else:
			self._instance = _internal
	@property
	def features_list(self) -> typing.List[Feature]:
		return [Feature(x) for x in self._instance.FeaturesList]
	@property
	def has_telnet(self) -> bool:
		return self._instance.HasTelnet
	@property
	def has_snpx(self) -> bool:
		return self._instance.HasSnpx
	@property
	def has_ascii_upload(self) -> bool:
		return self._instance.HasAsciiUpload
