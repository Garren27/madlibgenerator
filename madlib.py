import re
from os import system, name

def madlibOptions():
    infile = open("madlib choices.txt", "r")
    options = []
   
    line = infile.readline()
    options.append(line)
    while line != "":
        line = infile.readline()
        if line == "\n": #means it's the gap between stories
            line = infile.readline()
            options.append(line)

    infile.close()
    for i in range(0, len(options)):
        print(str(i + 1) + " - " + options[i].rstrip("\n"))
    
    return options

def storyOption(options):
    choice = 0
    doneChoosing = False

    while not doneChoosing:
        try:
            choice = input("Enter story number to play! ")
            choice = int(choice) - 1
        except KeyboardInterrupt:
            exit()
        except:
             print("Difficulty must be a number. Try again.")
             continue

        if (choice < 0 or choice > len(options) - 1):
            print("Invalid option. Try again.")
            continue

        print("Are you sure you want to play \"" + options[choice]
              .rstrip("\n") + "\"?")
        confirmation = input("Y / N: ").lower()
        if confirmation == "y":
            print("")
            doneChoosing = True
            return choice

def storyContent(storyTitle):
    infile = open("madlib choices.txt", "r")

    
    line = infile.readline()
    #read lines until we find the title of the player's choice
    while line != storyTitle:
        line = infile.readline()

    #add title to result string
    story = ""
    doneReading = False

    while not doneReading:
        line = infile.readline()
        
        if (line == "" or line == "\n"):
            doneReading = True

        story = story + line
        

    infile.close()
    return story
  
def extractMadLibs(story):
    required_words = re.findall("\([^\)][^\)]+\)", story)
    for index in range(0, len(required_words)):
        required_words[index] = required_words[index].rstrip(")").lstrip("(")
        

    return required_words

def getAdlibs(required_words):
    adlibs = []
    for word in required_words:
        adlibs.append(input(f"Please enter {word}: "))

    return adlibs

def insertAdlibs(adlibs, story):
    for adlib in adlibs:
        story = re.sub("_[^\)]+\)", adlib, story, 1)

    return story

def clear():
   # Clear console Windows 
   if name == 'nt':
        system('cls')

   # Clear console Linux / Mac
   else:
        system('clear')

def keepPlaying():
    doneChoosing = False

    while not doneChoosing:
        confirmation = input("Play again? (Y/N): ").lower()
        if confirmation == "n":
            return False
        if confirmation == "y":
            return True

def main():
    
    playing = True
    while playing:
        clear()
        print("Welcome to Madlib Generator!\n\nPlease choose an option:")
        options = madlibOptions()
        storyChoice = storyOption(options)
        clear()
        story = storyContent(options[storyChoice])
        required_words = extractMadLibs(story)
        adlibs = getAdlibs(required_words)
        completed_story = insertAdlibs(adlibs, story)

        #Output result
        print(options[storyChoice].rstrip("\n"))
        print(completed_story)
        print("")
        # Go again?
        playing = keepPlaying()

    print("Thanks for playing!")

main()