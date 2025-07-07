import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GenericVariableTypeHelpers as generic_variable_type_helpers

class GenericVariableTypeHelpers:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_variable_type_helpers()
		else:
			self._instance = _internal
