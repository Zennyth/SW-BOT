from setup import registry
from Class.Exception import Exception

class Manager():
    def __init__(self):
        self._hasLaunched = True
        #self.launchSequence(registry['in_game']['types'][registry['setup']._data['start']['type']])
        self.launchSequence(registry['in_game']['types']['start'])
    
    def launchSequence(self, sequence):
        print(sequence._sequenceName)
        sequenceName = sequence._sequenceName

        self._times = 1
        self._maxTimes = registry['setup']._data['start']['times']

        print("Manager has started task : 'start' => '" + sequenceName + "'")

        while self._times < self._maxTimes:
            if registry['in_game']['farms'][sequenceName]:
                res = registry['in_game']['farms'][sequenceName].selectSequence(registry['status'], registry['socket'])
                if res: self._times += 1
            else:
                Exception(1, "Main sequence in farms[" + sequenceName + "] undefined")
                break

        print("Manager has finished task : 'start'")
        
