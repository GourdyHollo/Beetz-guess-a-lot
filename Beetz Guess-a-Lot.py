# This is The programming assignment, Beetz Guess-a-Lot

# important musica initiation stuffie :3
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame, os

pygame.mixer.init()

musicFilePath = os.path.dirname(os.path.abspath(__file__))


# The class each song is a type of
class Song:
    def __init__(self, file, guessingType, correctAnswer, falseAnswers, hasBeeten):
        self.file = file
        self.guessingType = guessingType
        self.correctAnswer = correctAnswer
        self.falseAnswers = falseAnswers
        self.hasBeeten = hasBeeten

# A class for gamestate variables
class gameState:
    def __init__(self, isChoosingType, isGuessing, isPlaying, guessingType, allTimeSigs, allScales, guessChoices):

        # Is choosing time sigs or scales
        self.isChoosingType = isChoosingType

        # In the act of listening to a song?
        self.isGuessing = isGuessing

        # Has the player quit or not
        self.isPlaying = isPlaying

        # Time sigs or scales
        self.guessingType = guessingType

        # List of songs the player hasn't guessed succesfully yet
        self.allTimeSigs = allTimeSigs
        self.allScales = allScales

        # The choices the player has to guess on during a song
        self.guessChoices = guessChoices

        # EXTRA unguessed songs
        self.unguessedTimeSigs = allTimeSigs
        self.unguessedScales = allScales



# Time signature songs
fourFour = Song("4-4 time sig.wav", "TimeSig", "4/4", ["12/8", "6/8", "47/32"], False)
fiveFour = Song("5-4 time sig.wav", "TimeSig", "5/4", ["4/4", "3/4", "13/8"], False)
threeFour = Song("3-4 time sig.wav", "TimeSig", "3/4", ["4/4", "5/4", "12/8"], False)

# Scale songs
MajorScale = Song("Ionian scale.wav", "Scale", "Major/Ionian", 
                  ["Dorian", "Natrual minor/Aeolian", "Mixolydian"], False)
HarmMinorScale = Song("Harmonic Minor scale.wav", "Scale", "Harmonic Minor", 
                      ["Natrual minor/Aeolian", "Phrygian dominant", "Half-Whole Diminished"], False)
Mixolydianb6Scale = Song("Mixolydian b6 scale.wav", "Scale", "Mixolydian b6",
                         ["Major/Ionian", "Natrual minor/Aeolian", "Harmonic Minor"], False)


# The gameState master variable-thingie
theGameState = gameState(True, False, True, "",
                          [fourFour, fiveFour, threeFour], [MajorScale, HarmMinorScale, Mixolydianb6Scale],
                          [])


print("\n\nWelcome to BEETZ GUESS-A-LOT!\n")

import random


IndexToLetterDict = {0:"a", 1:"b", 2:"c", 3:"d"}

while theGameState.isPlaying:

    # Making sure the correct answer index position is saved outside where it's assigned
    correctAnswerIndex = 0

    # The game speaks to the player
    if theGameState.isChoosingType == True:
        print("Choose what you would like to guess in the songs:\n")
        print("A: TIME SIGNATURES!\nor\nB: SCALES!")


    elif theGameState.isGuessing == True:

        # You are now guessing either time signatures or scales
        if theGameState.guessingType == "time sig":

            if len(theGameState.unguessedTimeSigs) <= 0:
                print("\n\nCongratulations! You guessed all the time signatures!")
                if len(theGameState.unguessedScales) <= 0:
                    print("\nOh, you seemed to have completed all of the scales as well.")
                    theGameState.isPlaying = False
                    input("Welp, that is all for me. I hope you didn't just guess randomly!")
                    break
                
                else:
                    input("Now moving onto scales.\n")
                    theGameState.guessingType = "scale"
                    continue

            else:
                print ('\n\nOkay, try to guess this songs TIME SIGNATURE!\nPlay by typing for example "A" or "c"')
                print ('\nYou can quit the program at any time by typing "quit"')

        elif theGameState.guessingType == "scale":

            if len(theGameState.unguessedScales) <= 0:
                print("\n\nCongratulations! You have completed all of the scales!")
                if len(theGameState.unguessedTimeSigs) <= 0:
                    print("\nAh, Already got all the time sigs as well?")
                    theGameState.isPlaying = False
                    input("Well, that's all folks! \nI hope you enjoyed and could actually not guess randomly")
                    break

                else:
                    input("Now moving onto the time signatures.\n")
                    theGameState.guessingType = "time sig"
                    continue

            else:       
                print ('\n\nOkay, try to guess this songs SCALE! (Note: the scale may have multiple names, but only 1 of the 4 answers is correct)\nPlay by typing for example "A" or "c"')
                print ('\nYou can quit the program at any time by typing "quit"')

        # Specific song related info
        print ("Is it:\n")

        if theGameState.guessingType == "time sig":
            # Here is what position the correct answer gets assigned to.
            correctAnswerIndex = random.randrange(0, 4)
            
            currentSong = theGameState.allTimeSigs[random.randrange(0, len(theGameState.allTimeSigs))]

            # Activate the music (time sig edition)
            pygame.mixer.music.load(os.path.join(musicFilePath, currentSong.file))
            pygame.mixer.music.play(loops=-1)

            falseAnswerList = list(currentSong.falseAnswers)

            for i in range(4):
                if i == correctAnswerIndex:
                    # This is the correct one
                    print(IndexToLetterDict[i].capitalize() + ". " + currentSong.correctAnswer)
                else:
                    # A random incorrect one
                    print(IndexToLetterDict[i].capitalize() + ". " + falseAnswerList.pop(random.randrange(0, len(falseAnswerList))))


        # Same but for scales   
        elif theGameState.guessingType == "scale":
            # Here is what position the correct answer gets assigned to.
            correctAnswerIndex = random.randrange(0, 4)
            
            currentSong = theGameState.allScales[random.randrange(0, len(theGameState.allScales))]

            # Activate the music (scale edition)
            pygame.mixer.music.load(os.path.join(musicFilePath, currentSong.file))
            pygame.mixer.music.play(loops=-1)

            falseAnswerList = list(currentSong.falseAnswers)

            for i in range(4):
                if i == correctAnswerIndex:
                    # This is the correct one
                    print(IndexToLetterDict[i].capitalize() + ". " + currentSong.correctAnswer)
                else:
                    # A random incorrect one
                    print(IndexToLetterDict[i].capitalize() + ". " + falseAnswerList.pop(random.randrange(0, len(falseAnswerList))))
        

    # Command colon three
    command = input("\n")

    command = command.strip()
    command = command.lower()

    # I don't wanna play with you anymore
    if command == "quit":
        theGameState.isPlaying = False
        break
        
    # Go left! :3c (back)
    if command == "back":
        if theGameState.isGuessing == True:
            theGameState.isGuessing = False
            theGameState.isChoosingType = True
            pygame.mixer.music.unload()
            continue
        

    # if the player is choosing they wanna guess at time signatures or scales
    if theGameState.isChoosingType == True:
        if command == "a" or command == "a.":
            theGameState.isChoosingType = False
            theGameState.guessingType = "time sig"
            theGameState.isGuessing = True


        elif command == "b" or command == "b.":
            theGameState.isChoosingType = False
            theGameState.guessingType = "scale"
            theGameState.isGuessing = True

    # This... is a guess... 
    # Dear god...
    # There's more.
    # No!-...
    elif theGameState.isGuessing == True:
        LetterToIndexDict = {"a":0, "b":1, "c":2, "d":3}
        if len(command) != 0:
            if command[-1] == ".":
                command = command[:-1]
            
        # It contains a correct answer.
        if LetterToIndexDict[command] == correctAnswerIndex:
            if theGameState.guessingType == "time sig":
                theGameState.unguessedTimeSigs.pop(theGameState.unguessedTimeSigs.index(currentSong))
            else:
                theGameState.unguessedScales.pop(theGameState.unguessedScales.index(currentSong))
            print("\nYou guessed correctly yippie! :3")
            input("Press enter to continue\n")

        # It contains a WRONG answer :3
        else:
            print("Mrow")
            input("[EXTREMELY LOUD INCORRECT BUZZER]")