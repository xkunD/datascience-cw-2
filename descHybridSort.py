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
        swapped = True   
        i = 0                     
        while swapped and i < int(len(self.numbers)/2):        # only need to do n/2(ground) times (example case with 3 elems)
            swapped = False                    
            maxIndex = len(self.numbers) - i - 1
            for j in range(i, len(self.numbers)-i-1):   #start from i and check j with j+1
                if self.numbers[j] < self.numbers[j+1]: 
                    swapped = True
                    self.numbers[j], self.numbers[j+1] = self.numbers[j+1], self.numbers[j]
                # check maxIndex
                if self.numbers[j] > self.numbers[maxIndex]:
                    maxIndex = j 
            # selection sort
            self.numbers[i], self.numbers[maxIndex] = self.numbers[maxIndex], self.numbers[i]
            i += 1
        print("End of outer loop: ", self.numbers)

    # debugging : issue with 2 elems fixed with limit on while loop


def main():
    print("Original array")
    A=sortArray(8)
    print(A)
    A.descHybridSort()
    print("Sorted array")
    print(A)

if __name__ == "__main__":
    main() 
