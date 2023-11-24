import json
import string

with open("test/message_1.json", "r") as f:
    data = json.load(f)

# print(data.keys())

wordlist = {}
translator = str.maketrans("", "", string.punctuation)

# msg = (data["messages"][3]["content"]).translate(translator).split()


for i in data["messages"]:
    if i.get("content", False):
        words = (i["content"]).translate(translator).lower().split()

        for j in words:
            if j in wordlist:
                wordlist[j] += 1
            else:
                wordlist[j] = 1

sorted_dict = dict(sorted(wordlist.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)

