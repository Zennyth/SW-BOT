import Class.Mail

EXCEPTIONS_TYPE = [
	"Error : NOF",
	"Error : Wrong ID",
	"Error : Manual Intervention",
	"Warning : AS"
]

class Exception():
	def __init__(self, _id, description = None, status = None):
		self._id = _id
		self._description = description
		self._type = EXCEPTIONS_TYPE[self._id]

		if self._id == 2:
			Mail.send_mail('Manual intervention is required due to quizz template found')
			if status: status.add_error('Manual intervention is required due to quizz template found')
		# print(str(self))


	def __str__(self):
		return "Exception [" + self._type + "] / " + self._description if self._description != None else self._type