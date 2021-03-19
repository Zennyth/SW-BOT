import json
import datetime

class Status():
    def __init__(self, tasks):
        self._state = "on"
        self._history = []
        self._errors = []
        self._stats = [
            { "type": "gb12", "time":0, "runs":0, "total_time":0 },
            { "type": "db12", "time":0, "runs":0, "total_time":0 },
            { "type": "nb12", "time":0, "runs":0, "total_time":0 },
            { "type": "r5", "time":0, "runs":0, "total_time":0 },
        ]
        self._tasks = tasks
        self._actual = "Start"

        self.add_error('Manual intervention is required due to quizz template found')

    def send(self):
        return {
            "state": self._state,
            "history": self._history[:9],
            "stats": self._stats,
            "tasks": self._tasks,
            "errors": self._errors,
            "actual": self._actual
        }

    def switch_state(self, boolean):
        if boolean: 
            self._state = "on" 
        else: 
            self._state = "off"

    def add_error(self, error):
        self._errors.append({
            "type": error,
            "date": str(datetime.datetime.now())
        })

    def add_history(self, run, multiplier = 10):
        self._history.insert(0, run)
        self.update_stats(run, multiplier)
        self.update_tasks(run)

    def update_stats(self, run, multiplier):
        is_exist = False
        for stat in self._stats:
            if run["type"] == stat["type"]:
                stat["runs"] += 1*multiplier
                stat["total_time"] += run["time"]
                stat["time"] = stat["total_time"]/stat["runs"]
                is_exist = True
        if not(is_exist):
            self._stats.append({"type": run["type"], "time": run["time"], "runs": 1, "total_time": run["time"]})

    def update_tasks(self, run):
        for task in self._tasks:
            if task["type"] == run["type"]:
                if task["times"] < task["progress"]:
                    task["times"] += 1
                
                if task["times"] >= task["progress"]:
                    task["completed"] = True
                    task["times"] = task["progress"]

    def get_task(self):
        for task in self._tasks:
            if not(task["completed"]):
                return task
