# Program that prints out Old Macdonald lyrics for five animals

def old():
    return "Old MacDonald had a farm, "

def call():
    return "Ee-igh, Ee-igh, Oh!\n"

def verseFor(animal, sound):
    verse1 = old() + call() 
    verse2 = "And on that farm he had a " + animal + ", " + call()
    verse3 = "With a " + sound + ", " + sound + " here and a " + sound + ", " + sound + " there.\n"
    verse4 = "Here a " + sound + ", there a " + sound + ", everywhere a " + sound + ", " + sound + ".\n"
    lyrics = verse1 + verse2 + verse3 + verse4 + verse1
    return lyrics

def main():
    print(verseFor("cow", "moo"))
    print(verseFor("cat", "meow"))
    print(verseFor("dog", "woof"))    
    print(verseFor("horse", "neigh"))


main()