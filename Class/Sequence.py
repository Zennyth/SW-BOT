from Class.Exception import Exception

class Sequence():
	def __init__(self, templates = [], mainIndex = 0, starter = False):
		self._templates = templates
		self._mainIndex = mainIndex
		self._starter = starter
		if self._starter: self._hasStarted = False

	def mainTemplate(self):
		if len(self._templates) <= 0:
			return Exception(0, "no sequence found on : get_main_template")
		elif not(self._templates[self._mainIndex]):
			return Exception(0, "no main sequence found on : get_main_template")
		elif self._starter and self._hasStarted:
			return Exception(3, "sequence has already started")
		else:
			if self._starter: self._hasStarted = True
			return self._templates[self._mainIndex]

	def execute(self):
		for i in range(len(self._templates)):
			count = 0
			if i < len(self._templates) - 1:
				# print(self._templates[i + 1])
				next_template = self._templates[i + 1].execute()
				while(isinstance(next_template, Exception)):
					if self._templates[i]._activeRate < count: 
						self._templates[i].execute()
						count = 0
					
					count += 1
					next_template = self._templates[i + 1].execute()
			else:
				res = self._templates[i].execute()
				while(isinstance(res, Exception)):
					res = self._templates[i].execute()
		print("execute !")