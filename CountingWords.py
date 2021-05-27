Intro = input("Enter your Introduction : ")

WordCount = 1
CharacterCount = 0

for Character in Intro:
    CharacterCount = CharacterCount + 1
    if(Character ==' '):
        wordCount = WordCount + 1
        
print("Number of words in the string : ")
print(wordCount)

print("Number of Characters in the String : ")
print(CharacterCount)