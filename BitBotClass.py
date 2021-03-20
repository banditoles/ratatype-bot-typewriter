from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class BitBot():


    def __init__(self, driver, login, password, eval_mode=True):

        self.driver = driver
        self.login = login
        self.password = password
        self.letters = 0
        self.count_letters = 0
        self.eval_mode = eval_mode
        self.step = 1


    def authorization(self):

        self.driver.get("https://www.ratatype.ru/login/")
        self.driver.find_element_by_id("email").send_keys(self.login)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/div[3]/button').click()
        self.authorization = True

    def get_letters(self):

        def _get_letters(self):

            print('Получаем все букАвы...')
            raw_letters = self.driver.find_elements_by_class_name("wblack")
            letters = []

            for raw_letter in raw_letters:
                letters.append(raw_letter.text)

            return letters


        while self.count_letters == 0:

            self.letters = _get_letters(self)
            self.count_letters = len(self.letters)

        print(f"Всего букАв: {self.count_letters}")


    def check_load(self):

        if self.driver.execute_script('return document.readyState') != 'complete':
            self.check_load()

    def start_test(self):

        self.check_load()
        self.driver.find_element_by_xpath('//*[@id="startButton"]').click()
        print('Нажатие на старт...')

        self.get_letters()

        # Необходимо для ввода текста
        self.input_field = self.driver.find_element_by_tag_name("body")

        print('Прохождение теста...')
        self.bot_main()

        if self.eval_mode: self.start_eval_mode()
        else: self.quit()

    def bot_main(self):

        #Конструкция работатает до последего символа, чтобы регулировать скорость
        if self.step <= self.count_letters:

            # Получаем символ
            letter = self.driver.find_element_by_class_name("wgreen").text

            if letter == '': letter = ' '

            print(f"{letter}", end='')

            # Основая конструкция, где происходит имитация нажатия на клавишу
            self.input_field.send_keys(letter)

            # Проверяем, была ли нажата клавиша
            letter_type = self.driver.find_element_by_xpath(f'/html/body/div[2]/div/div[1]/div[2]/div/div[1]/span[{self.step}]').get_attribute('class')

            if letter_type == 'passed-text':
                self.step += 1
                self.bot_main()

            else: self.bot_main()

        else:

            # Сбрасывааем шаги, чтобы бот был готов к следующему тесту
            self.step = 1

    def start_eval_mode(self):

        work = True

        while work:

            try:
                print(eval(input('\nmode_ebal: ')))

            except Exception as Error:
                print(Error)

    def wait(self, timeout=5): WebDriverWait(self.driver, timeout=timeout)

    def quit(self): self.driver.quit()


