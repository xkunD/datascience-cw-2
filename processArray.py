import numpy as np
class processArray:

    def __init__(self, size):
        self.size = 2
        self.setSize(size)
        self.numbers=np.random.random([self.size])*100
        self.numbers=self.numbers.round(0).astype(int)      #added by myself

    def __str__(self):
        return "Array of "+str(self.size)+" numbers"+"\n"+str(self.numbers)
    
    def setSize(self,size):
        if(size>=2):
            self.size=size

    def hybridSort(self):
        swapped = False
        for i in range(self.size, 0, -1):
            for j in range(self.size - i):
                if(self.numbers[i] > self.numbers[i+1]):
                    self.numbers[i], self.numbers[i+1] = self.numbers[i+1], self.numbers[i]
                    swapped = True
            if(swapped == False):
                return
               
            

def main():
    arraysort = processArray(20)
    print(arraysort)


if __name__ == "__main__":
    main() 


