# Write a python program to read a string and find the number of vowels and consonants in the string
str=input()
l=len(str)
vov=0
cons=0
for wo in str:
  if( wo =="a"or wo =="A" or wo =="e" or wo =="E" or wo =="i"or wo =="I"or wo =="o"or wo =="O"or wo =="u"or wo =="U"):
    vov=vov+1
  else:
    cons=cons+1
print("vovels:",vov)
print("consonents:",cons)