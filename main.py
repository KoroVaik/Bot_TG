import os
import time

def main():
    token = os.getenv("BOT_TOKEN", "no_token_found")
    print(f"Бот запущено. Токен: {token}")
    
    # Нескінченний цикл для дебагу (щоб контейнер не падав)
    while True:
        print("Дебаг: бот працює...")
        time.sleep(5)

if __name__ == "__main__":
    main()
