# Source File Name: textrpg.py
# Author's Name: Trevor Kamerman
# Last Modified By: Trevor Kamerman
# Date Last Modified: Thursday May 23, 2013
""" 
  Program Description:  This program is a roleplaying game conveyd through 
                        text and played by imputting commands into the comsole
  
  Version: 0.1 - * created node class to hold the properties of each location within the game universe
                   (the current values are placeholders) 
                 * completed game logic, the game functions as expected to meet the basic requirements
           0.2 - * finilized game strings
"""

import time

class node:
    pass
    
def chooseCave(prompt):
    cave = ''
    while cave != '1' and cave != '2':
        print(prompt)
        cave = raw_input()
    return cave

def printWithDelay(text):
    for s in text.split('\n'):
        print(s)
        time.sleep(1)
                
def initLocations():
    node1 = node()
    node1.description = 'You are on a planet full of dragons. In front of you,\n'
                        'you see two caves. In one cave, the dragon is friendly\n'
                        'and will share his treasure with you. The other dragon\n'
                        'is greedy and hungry, and will eat you on sight.\n'
    node1.prompt = "Which cave will you go into? (1 or 2)"
    node1.outcomes = ["you went to node 2", "you went to node 3"]
    node2 = node()
    node2.description = "The starting location's left (node 2)"
    node2.prompt = "Which cave will you go into? (1 or 2)"
    node2.outcomes = ["you went to node 4", "you went to node 5"]
    node3 = node()
    node3.description = "The starting location's right (node 3)"
    node3.prompt = "Which cave will you go into? (1 or 2)"
    node3.outcomes = ["you went to node 6", "you went to node 7"]
    node4 = node()
    node4.description = "The starting location's left left (node 4)"
    node4.prompt = "Which cave will you go into? (1 or 2)"
    node4.outcomes = ["you picked outcome 1 and died lol", "you picked outcome 2 and died lol"]
    node5 = node()
    node5.description = "The starting location's left right (node 5)"
    node5.prompt = "Which cave will you go into? (1 or 2)"
    node5.outcomes = ["you picked outcome 3 and died lol", "you picked outcome 4 and died lol"]
    node6 = node()
    node6.description = "The starting location's right left (node 6)"
    node6.prompt = "Which cave will you go into? (1 or 2)"
    node6.outcomes = ["you picked outcome 5 and died lol", "you picked outcome 6 and died lol"]
    node7 = node()
    node7.description = "The starting location's right right (node 7)"
    node7.prompt = "Which cave will you go into? (1 or 2)"
    node7.outcomes = ["you picked outcome 7 and died lol", "you picked outcome 8 and win ... gratz"]
    
    node1.children = [node2, node3]
    node2.children = [node4, node5]
    node3.children = [node6, node7]
    
    return node1
    
def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        currentNode = initLocations()
        while True:
            print(currentNode.description)
            choice = int(chooseCave(currentNode.prompt)) - 1
            print(currentNode.outcomes[choice])
            if not hasattr(currentNode, 'children'):
                break
            currentNode = currentNode.children[choice]
        print ('\nDo you want to play again? (yes or no)')
        playAgain = raw_input()

if __name__ == "__main__": main()
