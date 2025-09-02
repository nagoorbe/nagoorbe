#reverse  a string using while loop
word="computer"
rev=""
i=len(word)-1

while i>=0:
    rev =rev+word[i]
    i=i-1
print(rev)


#reverse a string using for loop
word="cat"
rev=""
for ch in word:
    rev=ch+rev
print(rev)    
