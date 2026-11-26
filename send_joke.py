import os
import random
import json
import urllib.request

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")
JOKES_FILE = "jokes.txt"

def main():
    if not WEBHOOK_URL:
        raise ValueError("找不到 DISCORD_WEBHOOK 環境變數！請檢查 GitHub Secrets 設定。")

    with open(JOKES_FILE, "r", encoding="utf-8") as f:
        jokes = [line.strip() for line in f if line.strip()]

    if not jokes:
        print("笑話庫是空的")
        return

    # 隨機挑選一個笑話並處理換行
    chosen_joke = random.choice(jokes).replace("\\n", "\n")

    payload = {
        "content": f"🤣 **每日隨機笑話：**\n\n{chosen_joke}"
    }
    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        WEBHOOK_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )

    with urllib.request.urlopen(req) as response:
        if response.status in (200, 204):
            print("成功發送笑話到 Discord！")

if __name__ == "__main__":
    main()
