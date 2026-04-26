class Cpu:
    def __init__(self):
        self.currentProcess = None

    def isFree(self):
        return self.currentProcess is None
        
    def addProcess(self, proc):
        self.currentProcess=proc

    def runTick(self, tick):
        if self.currentProcess is None: 
            raise Exception("CPU está idle")
        
        self.currentProcess.run_one_tick(tick)

    def removeProcess(self):
        p = self.currentProcess
        self.currentProcess = None
        return p