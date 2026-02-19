from enum import IntEnum

class CommunicationVerb(IntEnum):
	'''RMI communication verbs.'''
	FRC_Connect = 0 # Request permission and the working data port from the controller.
	FRC_Disconnect = 1 # Gracefully end an RMI session on the working data port.
	FRC_Terminate = 2 # Sent by controller on idle timeout to close the session.
	FRC_SystemFault = 3 # Sent by controller when a system fault pauses TP program.
