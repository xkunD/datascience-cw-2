import numpy as np
import random
import matplotlib.pyplot as plt

class noisyPattern:

    def __init__(self):
        self.image = np.full([80, 80], 255)
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

    def removeNoise(self):
        a = 0;
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


if __name__ == "__main__":
    main() 