import numpy as np

class processArray:

    def __init__(self, size):
        self.size = 2
        self.setSize(size)
        self.numbers = np.random.random([self.size])*100
        self.numbers = self.numbers.round(0).astype(int)      #added by myself

    def __str__(self):
        return "Array of "+str(self.size)+" numbers"+"\n"+str(self.numbers)
    
    def setSize(self,size):
        if(size >= 2):
            self.size=size

    def hybridSort(self):
        data = self.numbers
        for i in range(len(data)-1):            #will get it sorted if n-1 items are sorted
            swapped = False
            for j in range(len(data)-i-1):
                print("compare between", data[j], data[j+1])
                if data[j] > data[j+1]: 
                    swapped = True
                    data[j], data[j+1] = data[j+1], data[j]
            if not swapped:
                break

def main():
    arraysort = processArray(3)
    print(arraysort)
    arraysort.hybridSort()
    print(arraysort)


if __name__ == "__main__":
    main() 
