from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.tpgl_view_variable_type import TpglViewVariableType
from underautomation.fanuc.common.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.common.files.variables.tpglmach_variable_type import TpglmachVariableType
from underautomation.fanuc.common.files.variables.recloc_variable_type import ReclocVariableType
from underautomation.fanuc.common.files.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Common.Files.Variables import TpglOutVariableType as tpgl_out_variable_type

class TpglOutVariableType(GenericVariableType):
	'''Describes the Fanuc type TPGL_OUT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpgl_out_variable_type()
		else:
			self._instance = _internal

	@property
	def views(self) -> typing.List[TpglViewVariableType]:
		'''Value of variable $VIEWS'''
		__r = self._instance.Views
		return None if __r is None else [None if x is None else TpglViewVariableType(x) for x in __r]

	@property
	def selected(self) -> typing.List[str]:
		'''Value of variable $SELECTED'''
		return self._instance.Selected

	@property
	def selpos(self) -> typing.List[CartesianPositionVariable]:
		'''Value of variable $SELPOS'''
		__r = self._instance.Selpos
		return None if __r is None else [None if x is None else CartesianPositionVariable(None, None, x) for x in __r]

	@property
	def pip_xml(self) -> str:
		'''Value of variable $PIP_XML'''
		return self._instance.PipXml

	@property
	def nodevis(self) -> typing.List[int]:
		'''Value of variable $NODEVIS'''
		return self._instance.Nodevis

	@property
	def machines(self) -> typing.List[TpglmachVariableType]:
		'''Value of variable $MACHINES'''
		__r = self._instance.Machines
		return None if __r is None else [None if x is None else TpglmachVariableType(x) for x in __r]

	@property
	def recordedloc(self) -> typing.List[ReclocVariableType]:
		'''Value of variable $RECORDEDLOC'''
		__r = self._instance.Recordedloc
		return None if __r is None else [None if x is None else ReclocVariableType(x) for x in __r]

	@property
	def nextpipe(self) -> str:
		'''Value of variable $NEXTPIPE'''
		return self._instance.Nextpipe

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpglOutVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
