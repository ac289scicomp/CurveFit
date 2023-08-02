import numpy as np
import numpy.linalg as lng
from matplotlib import pyplot as plt
def fitCurveQuad(points):
    arr =np.array([[points[0][0]**2, points[0][0], 1], 
                      [points[1][0]**2, points[1][0], 1],
                      [points[2][0]**2, points[2][0], 1]])
    ans = np.array([points[0][1], points[1][1], points[2][1]])
    a, b, c = lng.solve(arr, ans)
    print(lng.solve(arr, ans))
    x = np.linspace(-8, 8, 100)
    y = a*x**2 + b*x + c
    plt.plot(x, y)
    plt.scatter(points[0][0], points[0][1])
    plt.scatter(points[1][0], points[1][1])
    plt.scatter(points[2][0], points[2][1])
    plt.show()
    return lng.solve(arr, ans)

arr = np.array([[1, 4], [4, 6], [5, 2]])
#print(fitCurveQuad(arr))


def fitCurve(points, minX, maxX):
    dim = len(points)
    arr = [(points[i][0])**j for i in range(dim) for j in range(dim-1, -1, -1)]
    #arr2 = [[arr[dim * (i):dim * (i + 1)] for i in range(0:len(dim))]]
    arr2 = [arr[dim * i:dim * (i+1)] for i in range(dim)]
    ans = [points[i][1] for i in range(len(points))]
    arry= np.array(arr2)
    ansr = np.array(ans)
    l = lng.solve(arry, ansr)
    x = np.linspace(minX, maxX, 100)
    y = np.zeros(100)
    counter = 0
    for i in range(dim):
        base = l[i]
        power = dim - 1 - counter
        expo = np.power(x, power)
        y += base * expo
        counter += 1
        
        
    plt.plot(x, y)
    
    for i in range(len(points)):
        plt.scatter(points[i][0], points[i][1])
    
    plt.show()
        
    
                                                
    return l

import random as rd

#numPoints = 4
#maxi = 20
#mini = -20
#points3 = []


def pickPoints(numPoints, mini, maxi):
    pointsArray = []
    for i in range(numPoints):
        x = rd.randint(mini, maxi)
        y = rd.randint(mini, maxi)
        
        point = [x, y]
        
        pointsArray.append(point)
    pointsArray = np.array(pointsArray)
    return pointsArray
