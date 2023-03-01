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
        i = 0                     
        while gotSwap:            #will get it sorted if n-1 items are sorted
            gotSwap = False                    
            maxIndex = len(data)-i-1
            # print(data)
            for j in range(i, len(data)-i-1):   #start from i and check j with j+1
                # print("outer loop:", i, "compare between", data[j], data[j+1],", and data[max] now is", data[maxIndex])
                if data[j] < data[j+1]: 
                    gotSwap = True
                    data[j], data[j+1] = data[j+1], data[j]
                if data[j] > data[maxIndex]:
                    maxIndex = j 
            data[i], data[maxIndex] = data[maxIndex], data[i]   # selection sort
            i += 1
        print("End of outer loop: ", self.numbers)

def main():
    print("Original array")
    A=sortArray(1)
    print(A)
    A.descHybridSort()
    print("Sorted array")
    print(A)

if __name__ == "__main__":
    main() 
