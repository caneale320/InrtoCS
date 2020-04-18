# Caleb Neale, can4ku

import urllib.request

url = "http://cs1110.cs.virginia.edu/files/words.txt"

stream = urllib.request.urlopen(url)
words = []

for line in stream:
    word = line.decode("UTF-8").strip().lower()
    words.append(word)

user_response = (str(input("Type text; enter a blank line to end.")))

while user_response != "":
    user_response = user_response.strip(".?!,()\"'").lower().split()
    for i in user_response:
        i = i.strip(".?!,()\"'")
        if i not in words:
            print("  MISSPELLED:", i)
    user_response = input()




