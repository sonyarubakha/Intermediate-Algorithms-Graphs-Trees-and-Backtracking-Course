'''Module to find median from a dynamically growing list input.'''
import heapq
class MedianFinder:
    '''
    class to find median from a data stream
    '''
    def __init__(self):
        self.leftHalf = []
        self.rightHalf = []


    def addNum(self, num: int) -> None:
        '''
        adds num to heapq from max or min heap
        '''
        if not self.leftHalf or num <= -self.leftHalf[0]:
            heapq.heappush(self.leftHalf, -num)
        else:
            heapq.heappush(self.rightHalf, num)
        if len(self.leftHalf) > len(self.rightHalf) + 1:
            heapq.heappush(self.rightHalf, -heapq.heappop(self.leftHalf))
        elif len(self.rightHalf) > len(self.leftHalf):
            heapq.heappush(self.leftHalf, -heapq.heappop(self.rightHalf))


    def findMedian(self) -> float:
        '''
        Finds median from a data stream.
        '''
        if len(self.leftHalf) > len(self.rightHalf):
            return -self.leftHalf[0]
        elif len(self.rightHalf) > len(self.leftHalf):
            return self.rightHalf[0]
        else:
            return (-self.leftHalf[0] + self.rightHalf[0])/2.0
