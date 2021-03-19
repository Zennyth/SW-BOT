from setup import registry
from Class.Exception import Exception
#/ Socket \#
from Class.Socket import Socket

class Manager():
    def __init__(self):
        self._socket = Socket(registry['config']._data["api"], registry['config']._data["room"], registry['status'])
        self._hasLaunched = True
        self.launchFarm()
        # self.launchFarm(registry['in_game']['types']['change'])

    def setNextFarm(self):
        if not(registry['in_game']['activeFarm']['user']):
            task = registry['status'].get_task()
            for typeFarmName, Farm in registry['in_game']['farms'].items():
                print(Farm._type._stage)
                if Farm._type._stage == task['type']:
                    registry['in_game']['activeFarm']['farm'] = typeFarmName
                    registry['in_game']['activeFarm']['times'] = task['times']
        

    def launchFarm(self, times = 1):

        self._times = 0
        self._activeFarm = registry['in_game']['activeFarm']
        self._maxTimes = registry['in_game']['activeFarm']['times']

        print("Manager has started task : '" + self._activeFarm['farm'] + "'")

        while self._times < self._maxTimes:
            print("Next Stage : ", registry['in_game']['activeFarm'])
            if registry['in_game']['farms'][self._activeFarm['farm']]:
                res = registry['in_game']['farms'][self._activeFarm['farm']].selectSequence(registry['status'], self._socket)
                if res: self._times += 1
            else:
                Exception(1, "Main sequence in farms[" + self._activeFarm['farm'] + "] undefined")
                break

        print("Manager has finished task : '" + self._activeFarm['farm'] + "'")
        self.setNextFarm()
        self.launchFarm()
        # self.launchFarm(registry['in_game']['types'][registry['setup']._data['start']['type']], times = self.launchFarm(registry['in_game']['types'][registry['setup']._data['start']['type']]))
        
