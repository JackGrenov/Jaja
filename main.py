import requests
import json

API_KEY = "API_KEY"  # твой ключ
MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free"
history = []

while True:
    user_input = input("Ты: ")
    if user_input.lower() in ["exit", "quit", "выход"]:
        print("Пока!")
        break

    # Добавляем сообщение пользователя в историю
    history.append({"role": "user", "content": user_input})

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": MODEL,
            "messages": history
        })
    )
    try:
        reply = response.json()["choices"][0]["message"]["content"]
    except Exception:
        print("Ошибка ответа:", response.text)
        break

    print("ИИ:", reply.strip())

    # Добавляем ответ ассистента в историю для контекста
    history.append({"role": "assistant", "content": reply})
