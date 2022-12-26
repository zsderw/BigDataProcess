import os
import sys
import numpy as np
import operator

def matrix(file): 
    matrix = np.zeros((1, 1024))
    with open(file) as fp:
        for i in range(32):
            s = fp.readline()
            for j in range(32):
                matrix[0, i * 32 + j] = int(s[j])
        return matrix        

def createDataSet(dir):
    labels = []
    data = os.listdir(dir)
    n = len(data)
    group = np.zeros((n, 1024))
    for i in range(n):
        result = data[i]
        answer = int(result.split('_')[0])
        labels.append(answer)
        group[i, :] = matrix(dir + '/' + result)
    return group, labels 

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

dataFile = sys.argv[1]
testFile = sys.argv[2]

testFileList = os.listdir(testFile)
length = len(testFileList)

group, labels = createDataSet(dataFile)

for k in range(1, 21):
    cnt = 0
    errorCnt = 0
    for i in range(length):
        answer = int(testFileList[i].split('_')[0])
        list = matrix(testFile + '/' + testFileList[i])
        knn_result = classify0(list, group, labels, k)
        cnt += 1
        if answer != knn_result :
            errorCnt += 1
    
    print(int(errorCnt / cnt * 100))