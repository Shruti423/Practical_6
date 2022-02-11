# STUDENT NAME: SHRUTI PAGHADAL
# STUDENT ID: 20CE065
# AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 
#Github link: 
print ("\n------------------------------------PRACTICAL 6-----------------------------------\n")
n= int(input())
count= {}
list = []

for i in range(n):
  word = input()
  list.append(word)
  if word in count:
    count[word] += 1
  else:
    count[word] = 1

print("\nThe output is:\n")    
print(len(count))
print(' '.join([str(count[word]) for word in count]))
print("\n------------------------------------------END OF PRACTICAL 6-------------------\n")