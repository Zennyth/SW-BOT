class Type():
	def __init__(self, stage, description = "", sequenceName = "autofarm"):
		self._stage = stage
		self._description = description
		self._sequenceName = sequenceName

	def export(self, time):
		return {
			"type": self._stage, 
			"description": self._description,
			"time": time,
			"progress": "completed"
		}
