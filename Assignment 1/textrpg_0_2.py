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
           0.2 - * finalized game strings
"""

class node:
    pass
    
def initNodes():
    node1 = node()
    node1.description = ('You approach a castle using two half-coconuts percussively to\n'
                         'perfectly mimic the sound of a galloping horse coming to a\n'
                         'stop. Two guards become barely visible atop the castle wall.\n')
    node1.prompt =       '(1) I seek the holy grail | (2) I seek the meaining of life\n'
    node1.outcomes =   [('The guards are too distracted by the half-coconuts,\n'
                         'you grow frustrated and emulate riding off to the east.\n'),
                        ('The guards are too distracted by the half-coconuts,\n'
                         'you grow frustrated and emulate riding off to the west.\n')]
    node2 = node()
    node2.description = ('While travelling through a forest, you encounter an epic\n' 
                         'battle between two armoured, faceless men. After the battle\n'
                         'concludes the victorious knight forbids you from crossing the\n'
                         'nearby bridge thus barring your travels.\n')
    node2.prompt =       '(1) Challenge the knight | (2) Find a different route\n'
    node2.outcomes =   [('You make quick work of the knight, leaving him dismembered\n'
                         'while you continue on your journey.\n'),
                         'You travel upstream looking for an alternative path.\n']
    node3 = node()
    node3.description = ('You discover a dungeon-themed Hawaiian restaurant at a\n'
                         'holiday resort. Inside you are presented with a menu of\n'
                         'conversation topics by the waiter.\n')
    node3.prompt =       '(1) Minorities | (2) Philosiphy and The Meaning of Life\n'
    node3.outcomes =    ['You have a pleasant conversation.\n',
                        ('The waiter starts your conversation by asking,\n'
                         '''"Have you ever wondered just why you're here?"\n''')]
    node4 = node()
    node4.description = ('While progressing through a foggy forest you find yourself\n'
                         'before a group of knights whose leader stands twice your size.\n'
                         'They are the Knights who say "Ni!"\n'
                         'They demand a shrubbery in exchange for your life.\n')
    node4.prompt =       '(1) Give them a shrubbery | (2) Refuse\n'
    node4.outcomes =   [('Intimidated by the chanting of "Ni!, Ni!, Ni!", you agree to\n'
                         'bring the knights a shrubbery. The knights then require you\n'
                         'to cut down the largest tree in the forest with a herring.\n'
                         'Unable to complete this task you can no longer continue on\n'
                         'your quest.\n'),
                        ('Unintimidated by the chanting of "Ni!, Ni!, Ni!", you refuse\n'
                         'to give the Knights a shrubbery. They kill you.\n')]
    node5 = node()
    node5.description = ('After having traveled far up the river and not found another\n'
                         'way across you decide to try something else.\n')
    node5.prompt =       '(1) Attempt to cross the river | (2) Abandon quest.\n'
    node5.outcomes =   [('Being that the gully is only 10 feet wide you attempt to\n'
                         'cross it without the aid of a bridge. You lose your footing\n'
                         'fall to your death.\n'),
                         'You abandoned the quest.\n']
    node6 = node()
    node6.description = ('Shortly after leaving the restaurant you encounter the grim\n'
                         'reaper.\n')
    node6.prompt =       '(1) Invite him in for dinner | (2) Continue on your travels.\n'
    node6.outcomes =    ['During dinner you die from eating contaminated salmon mousse.\n',
                         'Angered by not being invited over for dinner death kills you.\n']
    node7 = node()
    node7.description = ('You leave the restaurant on your way to a meeting at the Very\n'
                         'Big Corporation Of America. On your way you are handed an\n' 
                         'envelope said to contain the meaning of life.\n')
    node7.prompt =       '(1) Discard the envelope | (2) Open the envelope\n'
    node7.outcomes =   [('You discard the envelope and continue on to the meeting only\n'
                         "to learn that people aren't wearing enough hats. You realize\n"
                         'that having discarded the envelope you are no longer able to\n'
                         'learn the meaning of life\n'),
                        ('The envelope reads: "Try and be nice to people, avoid eating\n'
                         'fat, read a good book every now and then, get some walking\n'
                         'in, and try and live together in peace and harmony with\n'
                         'people of all creeds and nations". Congratulations, you\n'
                         'have learned the meaning of life.\n')]
    
    #create a tree of nodes that will be traversed by selecting one of the options given by the prompt
    node1.children = [node2, node3]
    node2.children = [node4, node5]
    node3.children = [node6, node7]
    return node1

def makeChoice(prompt, options):
    choice = None
    while choice not in options:
        choice = raw_input(prompt).lower()
    return choice

def visitNode(node):
    print node.description
    choice = int(makeChoice(node.prompt, {'1','2'})) - 1
    print node.outcomes[choice]
    if hasattr(node, 'children'):
        visitNode(node.children[choice])

def main():
    visitNode(initNodes())
    while makeChoice('Do you want to play again? [Yes/No]\n', {'yes', 'y', 'no','n'}) in {'yes', 'y'}:
        visitNode(initNodes())
    
if __name__ == "__main__": main()