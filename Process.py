class Process:
    def __init__(self, pid, arrivalTime, burstTime ):
        self.pid = pid
        self.state = "Ready"
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime

        self.remainingTime = burstTime
        self.burstExecuted = 0
        self.totalTime = 0
        self.startTime = None
        self.finishTime = None

    def setRunning(self):
        self.state = "Running"
    
    def setReady(self):
        self.state = "Ready"

    def setBlocked(self):
        self.state = "Blocked"

    def run_one_tick(self, tick):
        if self.startTime is None:
            self.startTime = tick

        self.remainingTime -=1
        self.totalTime+=1
        self.burstExecuted +=1
        print(f"Ticks executed for process PID {self.pid}: {self.burstExecuted} ticks")

        
    def isFinished(self):
        return self.remainingTime == 0

    def __repr__(self) -> str:
        return f"(PID: {self.pid} | BurstTime: {self.burstTime} | RemainingTime: {self.remainingTime})"
