import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MtparamFile as mtparam_file

class MtparamFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mtparam_file()
		else:
			self._instance = _internal
	@property
	def def_itm(self) -> typing.List[int]:
		return self._instance.DefItm
	@property
	def intl_act(self) -> typing.List[int]:
		return self._instance.IntlAct
	@property
	def intl_run(self) -> typing.List[int]:
		return self._instance.IntlRun
	@property
	def due_once(self) -> typing.List[int]:
		return self._instance.DueOnce
	@property
	def def_itm2(self) -> typing.List[int]:
		return self._instance.DefItm2
	@property
	def intl_act2(self) -> typing.List[int]:
		return self._instance.IntlAct2
	@property
	def intl_run2(self) -> typing.List[int]:
		return self._instance.IntlRun2
	@property
	def due_once2(self) -> typing.List[int]:
		return self._instance.DueOnce2
	@property
	def def_itm_i(self) -> typing.List[int]:
		return self._instance.DefItmI
	@property
	def intl_act_i(self) -> typing.List[int]:
		return self._instance.IntlActI
	@property
	def intl_run_i(self) -> typing.List[int]:
		return self._instance.IntlRunI
	@property
	def due_once_i(self) -> typing.List[int]:
		return self._instance.DueOnceI
	@property
	def intell_grs(self) -> int:
		return self._instance.IntellGrs
	@property
	def coulomb_n(self) -> typing.List[float]:
		return self._instance.CoulombN
	@property
	def coulomb_n0(self) -> typing.List[float]:
		return self._instance.CoulombN0
	@property
	def viscosity(self) -> typing.List[float]:
		return self._instance.Viscosity
	@property
	def a_motor(self) -> typing.List[float]:
		return self._instance.AMotor
	@property
	def a_friction(self) -> typing.List[float]:
		return self._instance.AFriction
	@property
	def a_dissip(self) -> typing.List[float]:
		return self._instance.ADissip
	@property
	def a_other1(self) -> typing.List[float]:
		return self._instance.AOther1
	@property
	def a_other2(self) -> typing.List[float]:
		return self._instance.AOther2
	@property
	def a_other3(self) -> typing.List[float]:
		return self._instance.AOther3
	@property
	def a_other4(self) -> typing.List[float]:
		return self._instance.AOther4
	@property
	def a_other5(self) -> typing.List[float]:
		return self._instance.AOther5
	@property
	def a_other6(self) -> typing.List[float]:
		return self._instance.AOther6
	@property
	def a_exponent(self) -> typing.List[float]:
		return self._instance.AExponent
	@property
	def distance(self) -> typing.List[float]:
		return self._instance.Distance
	@property
	def max_v_motor(self) -> typing.List[float]:
		return self._instance.MaxVMotor
	@property
	def coeff_off(self) -> typing.List[float]:
		return self._instance.CoeffOff
	@property
	def sg_rate(self) -> typing.List[float]:
		return self._instance.SgRate
	@property
	def t_grs_lim(self) -> typing.List[float]:
		return self._instance.TGrsLim
	@property
	def formula_id(self) -> typing.List[int]:
		return self._instance.FormulaId
	@property
	def t_grs_thre(self) -> typing.List[float]:
		return self._instance.TGrsThre
	@property
	def grs_life(self) -> typing.List[float]:
		return self._instance.GrsLife
	@property
	def weight1(self) -> typing.List[float]:
		return self._instance.Weight1
	@property
	def weight2(self) -> typing.List[float]:
		return self._instance.Weight2
	@property
	def weight3(self) -> typing.List[float]:
		return self._instance.Weight3
	@property
	def weight4(self) -> typing.List[float]:
		return self._instance.Weight4
	@property
	def weight5(self) -> typing.List[float]:
		return self._instance.Weight5
	@property
	def theta1(self) -> typing.List[float]:
		return self._instance.Theta1
	@property
	def theta2(self) -> typing.List[float]:
		return self._instance.Theta2
	@property
	def theta3(self) -> typing.List[float]:
		return self._instance.Theta3
	@property
	def theta4(self) -> typing.List[float]:
		return self._instance.Theta4
	@property
	def theta5(self) -> typing.List[float]:
		return self._instance.Theta5
	@property
	def limit(self) -> typing.List[float]:
		return self._instance.Limit
