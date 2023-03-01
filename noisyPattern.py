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

    def removeNoise(self):
        pass

    def invert(self):
        pass

def main():
    noisyp = noisyPattern()
    noisyp.setFigure()
    noisyp.addNoise()
    # noisyp.removeNoise()
    # noisyp.filter1()
    
if __name__ == "__main__":
    main() 