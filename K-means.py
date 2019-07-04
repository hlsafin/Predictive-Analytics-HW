import pandas as pd
import numpy as np
import random



"""import data breast_truth and breast_data"""
breast_tru= pd.read_csv('breast_truth.csv')
breast_data = pd.read_csv('breast_data.csv')

""" creating C= zeros(1,569) """

C=np.transpose(np.zeros((1,569)))






""" switching from DataFrame to Matrix data type, so i can use the function random.choice, to make mu1 and mu2 as random rows of the matrix"""
asmatrix=pd.DataFrame.as_matrix(breast_data)
asmatrix2=pd.DataFrame.as_matrix(breast_tru)
"""" here i am making mu1 and mu2 random initial point of our 2 centroid"""
mu1=random.choice(asmatrix)
mu2=random.choice(asmatrix)


''' maxitter, is the max nubmer of iteration before termiate, '''
'''  mu1 and mu2 are my initial centers, however i seperated them as each vectors, instead of (D X K)'''
''' tol = .5 '''

''' so basically with the algorithm here, I do a for-loop till the end of the sample, then at each i : i compare the euclidan distance from that point to my randomly picked center mu1,mu2.'''
''' which ever point is closer , distance wise, to the center, i classify that point as either 0 or 1 '''
''' then i take the add each point of each cluster seperating, then divide by houw many vector exist in that cluster'''
'''  once i have my average for each cluster, i re-assign my clusters to those points, thus repeat again, the distance of last iteration to the current iteration is minimal , then break'''
maxitter=0
magnow=0
magnow2=0
tot1=0
tot2=0
counter=0
counter2=0
tol=0.5

""" euclidan(a,b), takes in vector a, and b, and returns the norm of a-b"""
def euclidan(a,b):
    return np.linalg.norm(a-b)


while True:
    
    for i in range(len(C)):
        
    
        if euclidan(asmatrix[i,:],mu1) > euclidan(asmatrix[i,:],mu2):
            C[i]=1

            counter=counter+1
            tot1=tot1+asmatrix[i,:]
        
        else:
            C[i]=0

            counter2=counter2+1
            tot2=tot2+asmatrix[i,:]
            
    ''' here i reassign ceneter magnow is temp value for mu2, then counter counts how many points exists in that cluster'''
    magnow2=mu2
    magnow=mu1    
    mu1=tot1/counter
    mu2=tot2/counter2
    
    
    maxitter=maxitter+1
    
    if tol > np.linalg.norm(mu1-magnow) or maxitter >1000 :
        print(maxitter) 
        break
            
      
''' lets compare what we gather on C to breast_truth '''
print(np.absolute(sum(C)-sum(asmatrix2)))

''' this prints out 29 or 174, depending where the random intial points start, which means we misrepresent 29 or 174 samples as the wrong classifiction, in a vector of size 569,  hence %94 accurcay or %69'''

''' question D, running the algorithm several times, gave me 2 different results, one with an accuracy of %94 and other with %69'''

''' Question E i wasn't able to get mu_init to run because D X K was  20 X 2, but it should have been 30 X 2, because each initial center has to be 30 X 1 '''

''' question F, If i were to intialize the true centers, then the program should terminate in one iteration '''
   

