from Cpu import Cpu
from Process import Process
from Scheduler import Scheduler
import random
import time
from colorama import Fore, Style, init

tick = 0
sch = Scheduler(3)
cpu = Cpu()

pid_counter = 0


print(f"Timeslice = {sch.timeSlice}")
while True:
    print(f"Fila de processos em Ready: {sch.readyProcesses}\n")
    if random.random() < 0.6:
        burstTime = random.randint(1, 10)
        p = Process(pid_counter, tick, burstTime)
        pid_counter+=1
        sch.addProcess(p)
        print(f"Tick: {tick} - Processo PID: {Fore.BLUE}{p.pid} CRIADO{Fore.RESET} com sucesso com {burstTime} ticks de carga de processamento.")
        
        time.sleep(5)
    
    if cpu.isFree() and sch.hasProcess():
        cpu.addProcess(sch.moveProcessToCpu())

    if not cpu.isFree():
        cpu.runTick(tick)
        print(f"Current process {cpu.currentProcess}\n")

        p = cpu.currentProcess

        if p is not None and p.isFinished():
            print(f"Tick {tick} - Processo {Fore.GREEN}{p.pid}{Fore.RESET} finalizado com sucesso!\n")
            p.finishTime = tick + 1
            cpu.removeProcess()
        
        elif p is not None and p.burstExecuted == sch.timeSlice:
            print(f"Tick {tick} - Processo {Fore.RED}{p.pid}{Fore.RESET} enviado para o fim da fila.\n")
            time.sleep(5)
            p.burstExecuted = 0
            removed = cpu.removeProcess()
            sch.addProcess(removed)
            p.setReady()
    tick +=1

#Se surgir um novo processo, adicione a lista de scheduler


#Se ha processos em ready e a CPU esta livre, passe-o para a CPU

#A cada tick 
    #Diminuir o tempo de remaining time
    # if check se o processo finalizou
        #se sim, 
            # set totalTime = endTime-arrivalTime
            # remova-o de readyProcesses
        #se nao
            # mova-o para o fim da fila, incremente numRounds      
    # else tick eh multiplo do time slice = mova o processo para o fim da fila, incremente numRounds
    