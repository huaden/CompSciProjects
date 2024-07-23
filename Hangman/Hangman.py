import random

file = open("words.txt", "r")
content = file.read()
content = content.splitlines()
file.close()
playAgain = "y"


def play_game():
    global content
    word = list(content[random.randint(0, len(content)-1)])
    curWord = ""
    for i in range(len(word)):
        print("_ ", end ="")
        curWord += "_"
    userGuesses = list()
    curWord = list(curWord)
    counter = 0
    print
    while curWord != word:
        userGuesses.append(input("Please enter a letter: "))
        for i in range(len(word)):
            x = len(userGuesses)-1
            if word[i] == userGuesses[x]:
                print(str(userGuesses[x]) + " ", end="")
                curWord[i] = userGuesses[x]
                counter -= 1

            else:
                print(curWord[i], end="")
        print("    ", userGuesses)
        counter += 1
        if counter == 12:
            print("\n\n\nHe died, you took to many guesses")
            z = "".join(word)
            print("Word was \"" + z + "\"")
            break
        if(curWord == word):
            print("\n\n!!!!!!!!!!!!!!!!!!\nYay! You won")
            z = "".join(curWord)
            print("You guessed my word \"" + z + "\"")

while playAgain == "y":
    play_game()
    print("\n\n")
    playAgain = input("Play again (y or n): ")



