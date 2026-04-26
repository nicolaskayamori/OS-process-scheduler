class Scheduler:
    def __init__(self, timeSlice):
        self.readyProcesses = []
        self.blockedProcesses = []
        self.timeSlice = timeSlice

    def addProcess(self, proc):
        self.readyProcesses.append(proc)

    def hasProcess(self):
        if len(self.readyProcesses)>0:
            return True
        return False
    
    def moveProcessToCpu(self):
        return self.readyProcesses.pop(0)
    
    def setRunning(self):
        self.readyProcesses[0].setRunning()

    def __repr__(self) -> str:
        return f"{self.readyProcesses}"