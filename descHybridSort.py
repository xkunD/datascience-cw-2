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
        gotSwap = True
        while gotSwap:                          # will stop when no swap was found by bubble
            for i in range(len(data)-1):            #will get it sorted if n-1 items are sorted
                gotSwap = False                    
                maxIndex = i
                for j in range(i, len(data)-i-1):   #start from i and check j with j+1
                    if data[j+1] > data[maxIndex]: 
                        maxIndex = j                #keep tracking max index
                    # print("outer loop:", i, "compare between", data[j], data[j+1],", and data[max] now is", data[maxIndex])
                    if data[j] < data[j+1]: 
                        gotSwap = True
                        data[j], data[j+1] = data[j+1], data[j]
                if maxIndex != i:
                    data[i], data[maxIndex] = data[maxIndex], data[i]   # selection sort
        print("End of outer loop: ", self.numbers)

def main():
    print("Original array")
    A=sortArray(10)
    print(A)
    A.descHybridSort()
    print("Sorted array")
    print(A)

if __name__ == "__main__":
    main() 
