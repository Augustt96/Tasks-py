from cs50 import get_string

text = get_string("Text: ")

# counting letters, words and sentences

let = 0
word = 1
sent = 0

for i in text:
    if i.isalpha() == True:
        let += 1
        
    if i == " ":
        word += 1
        
    if i == "." or i == "?" or i == "!":
        sent += 1

# counting L and S for formula

L = let / word * 100
S = sent / word * 100

# counting index and round to the nearest integer

index = round(0.0588 * L - 0.296 * S - 15.8)

# indicating the grade

if index >= 16:
    print("Grade 16+")
    
elif index < 1:
    print("Before Grade 1")

else:
    print("Grade", index)