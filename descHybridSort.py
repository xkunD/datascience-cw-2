import numpy as np
class sortArray:

    def __init__(self,size):
        self.size=2
        self.setSize(size) 
        self.numbers=np.random.random([self.size])*100 
        self.numbers=self.numbers.round(0)

    def __str__(self):
        return "Array of "+str(self.size)+" numbers"+"\n"+str(self.numbers)

    def setSize(self,size): 
        if(size>=2):
            self.size=size

    def descHybridSort(self):
        data = self.numbers
        for i in range(len(data)-1):            #will get it sorted if n-1 items are sorted
            swapped = False                    # will stop when no swap can be found by bubble
            maxIndex = i
            for j in range(i, len(data)-i-1):   #start from i and check j with j+1
                if data[j+1] > data[maxIndex]: 
                    maxIndex = j                #keep tracking max index
                if data[j] < data[j+1]: 
                    swapped = True
                    data[j], data[j+1] = data[j+1], data[j]
            if not swapped:                 # if need to change to above?
                break
            if maxIndex != i:
                data[i], data[maxIndex] = data[maxIndex], data[i]   # selection sort

def main():
    arraysort = sortArray(10)
    print(arraysort)
    arraysort.descHybridSort()
    print(arraysort)


if __name__ == "__main__":
    main() 
