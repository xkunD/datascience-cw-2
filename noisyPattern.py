import numpy as np
import random
import matplotlib.pyplot as plt

class noisyPattern:
    def __init__(self): 
        self.image=np.full([80,80],255) 
        self.setFigure()
    
    def setFigure(self):
        for i in range(20,30):
            self.image[i,20:30]=0
            self.image[i, 49:59]=0 
        for i in range(40,60):
            self.image[i,i:i+10]=0
            self.image[i,79-i-10:79-i]=0 
        plt.imsave('figure.png', self.image, cmap=plt.cm.gray)

    def addNoise(self):
        noise=0.05
        for i in range (0,self.image.shape[0]):
            for j in range(0,self.image.shape[1]): 
                if(noise > random.random()):
                    self.image[i,j]=255
        plt.imsave('noisy_pattern.png', self.image, cmap=plt.cm.gray)

    def __getMajority(self, i, j):
        neighbours = self.image[max(i-1, 0) : min(i+2, self.image.shape[0]), \
                                max(j-1, 0) : min(j+2, self.image.shape[1])].reshape(-1)

        blackNum = np.count_nonzero(neighbours == 0)
        whiteNum = np.count_nonzero(neighbours == 255) - 1

        if blackNum > whiteNum:         # if black more than white
            return 0
        else:                           # if black less or equal to white
            return 255


    def removeNoise(self):
        changed = True
        while changed:
            changed = False
            for i in range(self.image.shape[0]):
                for j in range (self.image.shape[1]):
                    if self.image[i, j] == 255:     
                        if self.image[i, j] != self.__getMajority(i, j):
                            self.image[i, j] = 255 - self.image[i, j]
                            changed = True
        plt.imsave('noise_removed.png', self.image, cmap=plt.cm.gray)

    def invert(self):
        self.image = self.image[::-1]
        plt.imsave('inverted.png', self.image, cmap=plt.cm.gray)

    # def invert(self):
    #     for i in range(int(self.image.shape[0]/2)):
    #         for j in range (self.image.shape[1]):
    #             self.image[i, j], self.image[self.image.shape[0] - i - 1, j] = self.image[self.image.shape[0] - i - 1, j], self.image[i, j]
    #     plt.imsave('noise_inverted.png', self.image, cmap=plt.cm.gray)

def main():
    noisyp = noisyPattern()
    noisyp.setFigure()
    noisyp.addNoise()
    noisyp.removeNoise()
    noisyp.invert()
    
if __name__ == "__main__":
    main() 