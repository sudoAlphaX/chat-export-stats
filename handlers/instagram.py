import json


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
