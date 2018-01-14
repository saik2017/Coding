# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    if segments==[]:
        return []
    points=[]
    rem_segments=[]
    #we find the left most  lying or least among the end points of each segment
    left_most=min(s.end  for s in segments)
    # all segments which have their starting point greater than left_most will not be covered
    for s in segments:
        if s.start>left_most:
            # rem_segmens is the remaining segments not covered
            rem_segments.append(s)
    return [left_most]+optimal_points(rem_segments)



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    #print(n)
    #print(data)
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #print(segments)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
