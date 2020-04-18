# Caleb Neale, can4ku

import urllib.request
import re

stream = urllib.request.urlopen("http://cs1110.cs.virginia.edu/emails.php")
decodedlist = []

for line in stream:
    decoded = line.decode("UTF-8").strip()
    decodedlist.append(decoded)

newlist = []
for item in decodedlist:
    if "at" in item or '@' in item:
        newlist.append(item)

newlist2 = []
for item in newlist:
    item = item.replace(" ", "")
    newlist2.append(item)

regex = re.compile(r"(.*?)[@](.*?)")

stream = urllib.request.urlopen("http://cs1110.cs.virginia.edu/emails.php")
answer = []
for line in stream:
    decoded = line.decode("UTF-8").strip()

    temp_result = regex.findall(decoded)

    for i in temp_result:
        answer.append(i)


print(answer)
