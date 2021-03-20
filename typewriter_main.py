from selenium import webdriver
from BitBotClass import BitBot

login = ""
password = ""


if __name__ == "__main__":

    # Создаем экземпляр бота
    exBot = BitBot(webdriver.Firefox(), login, password)

    try:
        # Авторизация
        exBot.authorization()
        print('Авторизация...')

        # Переход на сам тест
        exBot.driver.get('https://www.ratatype.ru/typing-test/test/')
        print('Переход на тест...')

        # Начать тест
        exBot.start_test()

    except Exception as Error:
        print(Error)
        exBot.start_eval_mode()