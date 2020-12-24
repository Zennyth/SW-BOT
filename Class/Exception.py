EXCEPTIONS_TYPE = [
	"Error : NOF",
	"Error : Wrong ID",
	"Error : Manual Intervention",
	"Warning : AS"
]

class Exception():
	def __init__(self, _id, description = None):
		self._id = _id
		self._description = description
		self._type = EXCEPTIONS_TYPE[self._id]
		# print(str(self))


	def __str__(self):
		return "Exception [" + self._type + "] / " + self._description if self._description != None else self._type