from enum import IntEnum

class ValueKind(IntEnum):
	'''Describes the kind of a variable value'''
	Value = 0 # A single scalar value
	Array = 1 # An array of values
	Structure = 2 # A structured type with named fields
	File = 3 # A file-level container
