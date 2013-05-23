import time

class location:
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

def checkCave(chosenCave, outcomes):
    printWithDelay('You approach the dark and spooky cave,\nA large dragon jumps out in front of you!\nHe opens his jaws and...\n')
        
    if chosenCave == '1':
                print (outcomes[0])
    elif chosenCave == '2':
                print (outcomes[1])
    
def initLocations():
    node1 = location()
    node1.description = '''
You are on a planet full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.
'''
    node1.prompt = "Which cave will you go into? (1 or 2)"
    node1.outcomes = ["outcome1", "outcome2"]
    node2 = location()
    node2.description = "The starting location's left"
    node3 = location()
    node3.description = "The starting location's right"
    node4 = location()
    node4.description = "The starting location's left left"
    node5 = location()
    node5.description = "The starting location's left right"
    node6 = location()
    node6.description = "The starting location's right left"
    node7 = location()
    node7.description = "The starting location's right right"
    
    node1.children = [node2, node3]
    node2.children = [node4, node5]
    node3.children = [node6, node7]
    
    return node1
    
def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        currentNode = initLocations()
        print(currentNode.description)
        checkCave(chooseCave(currentNode.prompt), currentNode.outcomes)
        print ('\nDo you want to play again? (yes or no)')
        playAgain = raw_input()

if __name__ == "__main__": main()
