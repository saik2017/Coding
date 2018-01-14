# python3
class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time =[]

    def Process(self, request):
        finish=0
        #print(self.finish_time)
        if self.finish_time==[]:
            self.finish_time.append(request.process_time+request.arrival_time)
            return Response(False,request.arrival_time)
        j=binsearch(self.finish_time,request.arrival_time)
        #print(j)
        #print('--------')
        if j==-2 or j==len(self.finish_time)-1:
            self.finish_time=[]
            self.finish_time.append(request.process_time + request.arrival_time)
            return Response(False, request.arrival_time)
        elif j==-1 and len(self.finish_time)==self.size:
            return Response(True,-1)

        else:
            self.finish_time=self.finish_time[j+1:]
            finish=self.finish_time[-1]+request.process_time
            if len(self.finish_time)==self.size:
                return Response(True,-1)
            else:
                self.finish_time.append(finish)
                return Response(False,self.finish_time[-2])





def binsearch(List,value):
    l=len(List)
    if List[0]>value:
        return -1
    if List[-1]<value:
        return -2
    if l==1:
        return 0
    high=l-1
    low=0
    mid=int((high+low)/2)
    while True:
        if mid==l-1:
            break
        if List[mid]<=value and List[mid+1]>value:
            break
        elif List[mid]<=value:
            high=high
            low=mid
            mid=int((high+low)/2)
        elif List[mid]>value:
            high=mid
            low=low
            mid=int((high+low)/2)
    return mid



def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)
    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)
    PrintResponses(responses)
"""
l=[2,3,5,5,5,9,10,12,12,14]
s=[2,6]
print(binsearch(s,5))
"""