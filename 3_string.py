#String Manipulator
user_sentence = input("Enter a sentence: ")
#Original Sentence
print("Original:", user_sentence)
#Total characters in the sentence
print("Characters (with spaces):",len(user_sentence))
#Sentence without space
no_spaces = user_sentence.replace(" ","")
print("Characters(without spaces):",len(no_spaces))
#Total words
word = user_sentence.split()
print("Words:", len(word))
#UPPERCASE
print("UPPERCASE:",user_sentence.upper())
#lowercase
print("lowercase:",user_sentence.lower())
#Title Case
print("Title Case:",user_sentence.title())
#First word
print("First word:",word[0])
# Last word
print("Last word:",word[-1])
#Reverse sentence
print("Reversed:",user_sentence[::-1])