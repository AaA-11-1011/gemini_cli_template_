import os
from google import genai

client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))
# 対話セッションを開始
chat = client.chats.create(model='models/gemini-2.5-flash')

print("Geminiと接続しました。'exit'で終了、'read [ファイル名]'でファイルを読み込みます。")

while True:
    user_input = input("あなた: ")
    if user_input.lower() == 'exit':
        break
    
    # ファイル読み込み機能（おまけ）
    if user_input.startswith('read '):
        filename = user_input.split(' ')[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                user_input = f"以下のファイル内容を解析して:\n\n{f.read()}"
        except Exception as e:
            print(f"エラー: {e}")
            continue

    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}")