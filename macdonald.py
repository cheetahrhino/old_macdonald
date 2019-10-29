# Program that prints out Old Macdonald lyrics for five animals

# def old():
#     return "Old MacDonald had a farm, "

# def call():
#     return "Ee-igh, Ee-igh, Oh!\n"

def verseFor(animal, sound):

    firstLast()

    middleThree(animal, sound)

    firstLast()

    # verse1 = old() + call() 
    # verse2 = "And on that farm he had a " + animal + ", " + call()
    # verse3 = "With a " + sound + ", " + sound + " here and a " + sound + ", " + sound + " there.\n"
    # verse4 = "Here a " + sound + ", there a " + sound + ", everywhere a " + sound + ", " + sound + ".\n"
    # lyrics = verse1 + verse2 + verse3 + verse4 + verse1
    # return lyrics

def introOutro():

    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")


def middleVerse(animal, sound):

    print("And on the farm he had a {0}, Ee-igh, Ee-igh, Oh!".format(animal))
    print("With a {0}, {0} here and a {0}, {0} there.".format(sound))
    print("Here a {0}, there a {0}, everywhere a {0}, {0}.".format(sound))

def main():
    # print(verseFor("cow", "moo"))
    # print(verseFor("cat", "meow"))
    # print(verseFor("dog", "woof"))    
    # print(verseFor("horse", "neigh"))

    animals = ["cow", "moo", "cat", "meow", "dog", "woof", "horse", "neigh"]

    for i in range(0, len(animals), 2):
        verseFor(animals[i], animals[i+1])
        print()


main()