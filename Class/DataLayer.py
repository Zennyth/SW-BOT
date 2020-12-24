import json

INDENT_LEVEL = 4

class DataLayer():
	def __init__(self, path):
		self._path = path
		self.load()

	def load(self):
		with open(self._path) as f:
			self._data = json.load(f)

	def save(self):
		with open(self._path, 'w') as f:
			json.dump(self._data, f, indent = INDENT_LEVEL)

	def __str__(self):
		return json.dumps(self._data, indent = INDENT_LEVEL, sort_keys=True)