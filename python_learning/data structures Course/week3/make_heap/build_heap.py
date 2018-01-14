# python3
import random
class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    n=len(self._data)
    for i in range(int(n/2)-1,-1,-1):
      j=i
      while j<int(n/2):
        if 2*j+2>=n:
          swap_index=2*j+1
        elif self._data[2*j+1]<self._data[2*j+2]:
          swap_index=2*j+1
        else:
          swap_index=2*j+2
        if self._data[j]>self._data[swap_index]:
          self._data[j],self._data[swap_index]=self._data[swap_index],self._data[j]
          self._swaps.append((j,swap_index))
          j=swap_index
        else:
          break





  def GenerateSwapsSlow(self):
      # The following naive implementation just sorts
      # the given sequence using selection sort algorithm
      # and saves the resulting sequence of swaps.
      # This turns the given array into a heap,
      # but in the worst case gives a quadratic number of swaps.
      #
      # TODO: replace by a more efficient implementation
      for i in range(len(self._data)):
        for j in range(i + 1, len(self._data)):
          if self._data[i] > self._data[j]:
            self._swaps.append((i, j))
            self._data[i], self._data[j] = self._data[j], self._data[i]




  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

# def test(n):
#     data=[]
#     l=len(data)
#     while len(data)<n:
#         t=random.randint(0,25)
#         if t not in data:
#             data.append(t)
#     print(data)
#     heap=HeapBuilder()
#     heap._data=data
#     heap.GenerateSwaps()
#     heap.WriteResponse()
#
# test(10)


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

