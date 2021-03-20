from selenium import webdriver
from ratatype_bot_typewriter.ratatype_bot import RatatypeBot

login = ""
password = ""


if __name__ == "__main__":

    # Создаем экземпляр бота
    exBot = RatatypeBot(webdriver.Firefox(executable_path='ratatype_bot_typewriter/driver/geckodriver'), login, password)

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
