# coding: utf-8
from PIL import Image
import math

class Neuron(object):
    """docstring for Neuron"""
    def __init__(self, value=0, weights=[], bias=0):
        self.value = value
        self.weights = weights
        self.bias = bias

    def loadWeights(self, filename, source=False):
        img = Image.open('imgs/' + filename)
        pixels = []
        for i in list(img.getdata()):
            # values range 0.0 -> 1.0
            if source: pixels.append(float( i[0] ) / 255)
            # values range -1.0 -> 1.0
            if not source: pixels.append((float( i[0] ) - 127.5) / 127.5) 
        self.weights = pixels
        img.close()

    def sig(self, vector):
        vectorProduct = []
        for i in range(0, len(vector)):
            vectorProduct.append(vector[i]*self.weights[i])
        vectorSum = sum(vectorProduct)+self.bias
        self.value = (1/(1+math.e**(-vectorSum)))

def main():

    inputData = Neuron()
    inputData.loadWeights('5.png', source=True)
    inputNodes = inputData.weights

    symbols = ["/_", "_\\", "¯/", "\\¯", "|/", "|\\", "//|", "\\|", "O", "•"]
    parts = ["¯", "_", "| ", " |", "\\", "/", "•"]

    hiddenNeurons = []
    for i in range(0,len(parts)):
        hiddenNeurons.append(Neuron())
        hiddenNeurons[i].loadWeights(str(i+1)+'n.png')
        hiddenNeurons[i].sig(inputNodes)

    hiddenNodes = []
    for i in hiddenNeurons:
        hiddenNodes.append(i.value)

    outputNeurons = []
    for i in range(0,len(symbols)):
        outputNeurons.append(Neuron())
        outputNeurons[i].loadWeights(str(i+1)+'o.png')
        outputNeurons[i].sig(hiddenNodes)

    ouputNodes = []
    for i in outputNeurons:
        ouputNodes.append(i.value)

    print("Guess is: " + str( symbols[ouputNodes.index(max(ouputNodes))] ) )

    outputTotal = sum(ouputNodes)
    print("Breakdown:")
    for i in range(0,len(ouputNodes)):
        print(symbols[i] + ": {0:.1f}%".format( (ouputNodes[i]/outputTotal)*100 ) )



if __name__ == '__main__':
    main()
        
