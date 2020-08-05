class Process:
    def __init__(self, number, arrival, burst, priority):
        self.number = number
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.time_remaining = burst
        self.completion = None


# define processes here #
p1 = Process(1, 1, 9, 2)
p2 = Process(2, 2, 8, 1)
p3 = Process(3, 5, 7, 4)
p4 = Process(4, 3, 4, 3)

processes = [p1, p2, p3, p4]

# algorithm = one of 
#   FCFS    - first come, first serve
#   SJF     - shortest job first
#   P       - preemptive priority
#   RR      - round-robin (q = time quantum)
# p = True/False - preemptive
def schedule(processes, alg="FCFS", p=False, q=None):
    total_time = sum([process.burst for process in processes])
    current = None
    queue = []
    gantt = ""

    print("\nScheduling processes with " + alg + (" (preemptive)" if (p and (alg == 'SJF' or alg == 'P')) else " (non-preemptive)"))
    print("t\tcurr\tqueue")

    if alg == "FCFS":
        for t in range(total_time+2):
            for process in processes:
                if process.arrival == t:
                    queue.append(process)
            if current == None or current.time_remaining == 1:
                if current != None and current.time_remaining == 1:
                    current.completion = t
                try:
                    current = queue.pop(0)
                except IndexError:
                    current = None
            else:
                current.time_remaining -= 1
            c = str(current.number) if current != None else 'x'
            print(str(t) + '\t' + c + '\t' + str([process.number for process in queue]))
            gantt += c

    elif alg == "SJF":
        for t in range(total_time+2):
            for process in processes:
                if process.arrival == t:
                    inserted = False
                    for x in queue:
                        if x.burst > process.burst:
                            queue.insert(queue.index(x), process)
                            inserted = True
                            break
                        elif x.burst == process.burst:
                            queue.insert(queue.index(x)+1, process)
                            inserted = True
                            break
                    if not inserted:
                        queue.append(process)
            if current == None or current.time_remaining == 1:
                if current != None and current.time_remaining == 1:
                    current.completion = t
                try:
                    current = queue.pop(0)
                except IndexError:
                    current = None
            else:
                current.time_remaining -= 1
            if p and current != None and len(queue) > 0 and queue[0].time_remaining < current.time_remaining:
                queue.append(current)
                current = queue.pop(0)
            c = str(current.number) if current != None else 'x'
            print(str(t) + '\t' + c + '\t' + str([process.number for process in queue]))
            gantt += c


    elif alg == "P":
        for t in range(total_time+2):
            for process in processes:
                if process.arrival == t:
                    inserted = False
                    for x in queue:
                        if x.priority > process.priority:
                            queue.insert(queue.index(x), process)
                            inserted = True
                            break
                        elif x.priority == process.priority:
                            queue.insert(queue.index(x)+1, process)
                            inserted = True
                            break
                    if not inserted:
                        queue.append(process)
            if current == None or current.time_remaining == 1:
                if current != None and current.time_remaining == 1:
                    current.completion = t
                try:
                    current = queue.pop(0)
                except IndexError:
                    current = None
            else:
                current.time_remaining -= 1
            if p and current != None and len(queue) > 0 and queue[0].priority < current.priority:
                queue.append(current)
                current = queue.pop(0)
            c = str(current.number) if current != None else 'x'
            print(str(t) + '\t' + c + '\t' + str([process.number for process in queue]))
            gantt += c

    elif alg == "RR":
        if q == None or q < 1:
            print("Round robin requires a non-negative time quantum")
            exit(1)
        for t in range(total_time+2):
            if current != None:
                current.time_remaining -= 1
            if current == None or current.time_remaining == 0 or (current.burst - current.time_remaining) % q == 0:
                if current != None and current.time_remaining == 0:
                    current.completion = t
                    current = None
                if current != None and (current.burst - current.time_remaining) % q == 0:
                    queue.append(current)
            for process in processes:
                if process.arrival == t:
                    queue.append(process)
            if current == None or current.time_remaining == 0 or (current.burst - current.time_remaining) % q == 0:
                try:
                    current = queue.pop(0)
                except IndexError:
                    current = None
            c = str(current.number) if current != None else 'x'
            print(str(t) + '\t' + c + '\t' + str([process.number for process in queue]))
            gantt += c

    else:
        print('invalid argument parameter')
        exit(1)

    print(gantt)
    print("\nProcess\tArrival\tCompltn\tTrnarnd\tBurst\tWait")
    for process in processes:
        turnaround = process.completion-process.arrival
        wait = turnaround - process.burst
        print(str(process.number) + '\t' +
        str(process.arrival) + '\t' +
        str(process.completion) + '\t' +
        str(turnaround) + '\t' +
        str(process.burst) + '\t' +
        str(wait))
    print("------------------------------------------------")
    print("avg.\t\t\t" +
        str(sum([process.completion-process.arrival for process in processes])/len(processes)) + "\t\t" +
        str(sum([(process.completion-process.arrival)-process.burst for process in processes])/len(processes)))


if __name__ == '__main__':
    schedule(processes, 'SJF', p=True)
