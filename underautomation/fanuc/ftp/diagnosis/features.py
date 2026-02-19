import typing
from underautomation.fanuc.ftp.diagnosis.feature import Feature
from UnderAutomation.Fanuc.Ftp.Diagnosis import Features as features

class Features:
	'''Represents the collection of features available on the controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = features()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def features_list(self) -> typing.List[Feature]:
		'''List of features'''
		return [Feature(x) for x in self._instance.FeaturesList]

	@property
	def has_telnet(self) -> bool:
		'''Indicates if the robot has the TELNET feature enabled (TELN).'''
		return self._instance.HasTelnet

	@property
	def has_snpx(self) -> bool:
		'''Indicates if the robot has the SNPX feature enabled (R553 or R651).'''
		return self._instance.HasSnpx

	@property
	def has_ascii_upload(self) -> bool:
		'''Indicates if the robot has the ASCII upload feature enabled : R507 ("ASCII Upload" on older controllers) or R796 ("ASCII Program Loader" on most recent controllers).'''
		return self._instance.HasAsciiUpload

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Features):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
