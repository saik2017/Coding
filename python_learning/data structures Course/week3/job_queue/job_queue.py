# python3
import heapq

class Worker(object):
    def __init__(self,index):
        self.index=index
        self.value=0
    def getIndex(self):
        return self.index
    def getValue(self):
        return self.value
    def __lt__(self, other):
        if self.getValue()==other.getValue():
            return self.getIndex()<other.getIndex()
        else:
            return self.getValue()<other.getValue()

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 



    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_times=[]
        for i in range(self.num_workers):
            next_free_times.append(Worker(i))
        heapq.heapify(next_free_times)
        for i in range(len(self.jobs)):
            next_worker=heapq.heappop(next_free_times)
            self.assigned_workers[i]=next_worker.getIndex()
            self.start_times[i]=next_worker.getValue()
            next_worker.value+=self.jobs[i]
            heapq.heappush(next_free_times,next_worker)



    def assign_jobsSlow(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

