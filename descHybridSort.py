import numpy as np

class sortArray:

    def __init__(self,size):
        self.size = 2
        self.setSize(size) 
        self.numbers = np.random.random([self.size])*100 
        self.numbers = self.numbers.round(0)

    def __str__(self):
        return "Array of " + str(self.size) + " numbers" + "\n" + str(self.numbers)

    def setSize(self, size): 
        if(size >= 2):
            self.size = size

    def descHybridSort(self):
        swapped = True   
        i = 0

        while swapped and i < int(len(self.numbers)/2):         # outer loop only need n/2(ground) times
            swapped = False                    
            maxIndex = len(self.numbers) - i - 1

            for j in range(i, len(self.numbers) - i - 1):       # inner loop start from i and stop -i
                
                if self.numbers[j] < self.numbers[j+1]:         # bubble sort check j with j+1
                    swapped = True
                    self.numbers[j], self.numbers[j+1] = self.numbers[j+1], self.numbers[j]
                                    
                if self.numbers[j] > self.numbers[maxIndex]:    # keep maxIndex
                    maxIndex = j 
            
            self.numbers[i], self.numbers[maxIndex] = self.numbers[maxIndex], self.numbers[i]   # selection sort
            i += 1
        
        print("End of outer loop:", self.numbers)


def main():
    print("Original array:")
    A = sortArray(1)
    print(A, "\n")
    
    A.descHybridSort()
    
    print("\nSorted array:")
    print(A)


if __name__ == "__main__":
    main() 
