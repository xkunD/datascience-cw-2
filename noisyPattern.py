import numpy as np
import random
import matplotlib.pyplot as plt

class noisyPattern:

    def __init__(self):
        self.image = np.full([80, 80], 255)   # size, fillvalue
        self.setLines()

    def setLines(self):
        self.image[:, 0:16] = 0
        self.image[:, 32:48] = 0
        self.image[:, 64:80] = 0
        plt.imsave('lines.png', self.image, cmap=plt.cm.gray)
    
    def addNoise(self):
        noise = 0.05
        for i in range (0, self.image.shape[0]):
            for j in range(0, self.image.shape[1]):
                if(noise > random.random()):
                    self.image[i,j] = 255
        plt.imsave('noisy_pattern.png', self.image, cmap=plt.cm.gray)

    # working on following

    def test(self):
        print(self.image.shape)

    def __getMajority(self, i, j):
        pixels = self.image[max(i-1, 0):min(i+2,self.image.shape[0]), max(j-1, 0):min(j+2,self.image.shape[1])]
        # Flatten the pixels to simplify the counting
        pixels_flat = pixels.reshape(-1)
        # Count the number of black and white pixels
        black_count = white_count = 0
        black_count = np.count_nonzero(pixels_flat == 0)
        white_count = np.count_nonzero(pixels_flat == 255)
        # Return the majority color, or None if there is a tie
        if black_count > white_count:
            return 0
        elif black_count < white_count:
            return 255
        else:
            print("this is equal:", i, j)
            return self.image[i,j]
            
        

    def removeNoise(self):
        for i in range(self.image.shape[0]):
            for j in range (self.image.shape[1]):
                if self.image[i, j] == 255:
                    self.image[i, j] = self.__getMajority(i, j)
        plt.imsave('noise_removed.png', self.image, cmap=plt.cm.gray)
        #your code here
        #if there is a white dot, replace its value by the value # of the majority of neighbouring pixels
        #save the resulting image in file noise_removed.png
        
    def filter1(self):
        print("good")
        #your code here
        #replace the value of every pixel by the average of the values #of its neighbouring pixels
        #save the resulting image in file pattern_filter1.png      

def main():
    noisyp = noisyPattern()
    noisyp.setLines()
    noisyp.addNoise()
    noisyp.removeNoise()
    
if __name__ == "__main__":
    main() 