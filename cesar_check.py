filename = "sentence.txt"
with open(filename) as f:
        
    temp = f.readline()
    temp = temp.replace('.',"")
    print(temp)
sentence_words = temp.split(" ")

print(sentence_words)

letter_dict = {"A":0, "B":0, "C":0, "D":0
               , "E":0, "F":0, "G":0, "H":0
               , "I":0, "J":0, "K":0, "L":0
               , "M":0, "N":0, "O":0, "P":0
               , "Q":0, "R":0, "S":0, "T":0
               , "U":0, "V":0, "W":0, "X":0
               , "Y":0, "Z":0}
# print(type(letter_dict["A"]))
for each_word in sentence_words:
    for each_letter in each_word:
        # print(letter_dict[each_letter])
        letter_dict[each_letter] = letter_dict[each_letter] +1

print(letter_dict)



# word_list =set()
# filename = "words.txt"
# with open(filename) as f:
#         while True:
#             temp = f.readline()
#             if not temp:
#                 break
#             word_list.add(temp[0:-1])



# x =0 
# for each in word_list:
#      print(each)
#      x =x+1
#      if x > 10 :break

# print("hand".upper())
# if "hand".upper() in word_list:
#      print("Yes hand is in wordlist.")
# else:
#     print("hand not in wordlist")
