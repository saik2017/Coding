# Uses python3
import sys
import random
import time
import bisect



def fast_count_segments(starts, ends, points):
    cnt=[]
    starts.sort()
    ends.sort()
    for i in range(len(points)):
        temp=bisect.bisect_right(starts,points[i])-bisect.bisect_left(ends,points[i])
        cnt.append(temp)

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

# def test(s,p):
#     starts,ends=[],[]
#     points=[]
#     for i in range(p):
#         points.append(random.randint(-10**8,10**8))
#     for i in range(s):
#         starts.append(random.randint(-10**8,10**8))
#         ends.append(random.randint(starts[i],10**8))
#     #t1=time.time()
#     cnt2=naive_count_segments(starts,ends,points)
#     cnt1=fast_count_segments(starts,ends,points)
#     #t2=time.time()
#     for i in range(len(cnt1)):
#         if cnt1[i]!=cnt2[i]:
#             print("Test Failed")
#             return
#     print("Test Passed")
#
#     #print(t2-t1)
# test(1000,1000)
"""
Failure of edge cases also leads to exceeded time limits and better to use inbuilt binary seach functions 
"""