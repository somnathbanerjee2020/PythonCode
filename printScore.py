# Purpose: This program automates assessing security scores from 0 - 100 
#          and prints each result to the screen
# Author: Ankita Banerjee 03/04/2019

def assessScores(scoreList):
    for i in range(0, len(scoreList)):
        if(scoreList[i] >= 100):
            print('Computer', i+1, "has no known security issues.")
        elif(scoreList[i] >= 80):
            print('Computer', i+1, "has minor security issues.")
        #elif(scoreList[i] >= 60):
          #  print('Computer', i+1, "has *moderate* security issues.")
        else:
            print('Computer', i+1, "has ***severe*** security issues.")
        
    print("Proces complete:", len(scoreList), "computers scanned.")
    return

scores = [1,50,60,70,80,90]
assessScores(scores)

