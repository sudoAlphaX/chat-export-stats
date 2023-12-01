import json
import string


def read_chat_export(filename="message_1.json"):
    data = {"messages": [], "participants": {}}

    with open(f"export/instagram/{filename}", "r") as f:
        raw_data = json.load(f)

    data["participants"] = raw_data.get("participants", {})

    for msg in raw_data["messages"]:
        if msg.get("photos", False):
            msg_type = "photo"
            msg_content = msg["photos"]
        elif msg.get("videos", False):
            msg_type = "video"
            msg_content = msg["videos"]
        elif msg.get("call_duration", False):
            msg_type = "call"
            msg_content = msg["call_duration"]
        elif msg.get("content", False):
            msg_type = "text"
            msg_content = msg["content"]
        else:
            msg_type = "unknown"
            msg_content = msg

        data["messages"].append(
            {
                "sender_name": msg["sender_name"],
                "timestamp": msg["timestamp_ms"],
                "type": msg_type,
                "content": msg_content,
            }
        )

    data["messages"].reverse()

    return data


def get_words_count(rawdata):
    wordlist = {}
    translator = str.maketrans("", "", string.punctuation)

    pdict = {p["name"]: 0 for p in rawdata["participants"]}

    for msg in rawdata["messages"]:
        if msg.get("type") == "text":
            words = msg["content"].translate(translator).lower().split()
            for word in words:
                if word not in wordlist:
                    wordlist[word] = {"total": 0, **pdict}
                wordlist[word]["total"] += 1
                wordlist[word][msg["sender_name"]] += 1

    sorted_wordlist = dict(
        sorted(wordlist.items(), key=lambda x: x[1]["total"], reverse=True)
    )

    return sorted_wordlist


if __name__ == "__main__":
    data = read_chat_export()
    wordcount = get_words_count(data)
    print(wordcount)
