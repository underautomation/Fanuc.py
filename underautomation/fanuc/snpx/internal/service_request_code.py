import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import ServiceRequestCode as service_request_code

class ServiceRequestCode(int):
	PLC_SHORT_STATUS = service_request_code.PLC_SHORT_STATUS
	GET_PROGNAME = service_request_code.GET_PROGNAME
	READ_SYS_MEM = service_request_code.READ_SYS_MEM
	READ_TASK_MEM = service_request_code.READ_TASK_MEM
	READ_PROG_MEM = service_request_code.READ_PROG_MEM
	WRITE_SYS_MEM = service_request_code.WRITE_SYS_MEM
	WRITE_TASK_MEM = service_request_code.WRITE_TASK_MEM
	WRITE_PROG_MEM = service_request_code.WRITE_PROG_MEM
	PROG_LOGON = service_request_code.PROG_LOGON
	CHANGE_PRIV = service_request_code.CHANGE_PRIV
	SET_CPU_ID = service_request_code.SET_CPU_ID
	SET_PLC_RUN = service_request_code.SET_PLC_RUN
	SET_PLC_TIME = service_request_code.SET_PLC_TIME
	GET_PKC_TIME = service_request_code.GET_PKC_TIME
	GET_FAULT = service_request_code.GET_FAULT
	CLR_FAULT = service_request_code.CLR_FAULT
	PROG_STORE = service_request_code.PROG_STORE
	PROG_LOAD = service_request_code.PROG_LOAD
	GET_INFO = service_request_code.GET_INFO
	TOGGLE_FORCE_SYS_MEM = service_request_code.TOGGLE_FORCE_SYS_MEM
	INIT = service_request_code.INIT
