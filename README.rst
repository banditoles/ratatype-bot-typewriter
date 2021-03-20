=================================
ratatype-bot-typewriter
=================================
Bot that automatically passes the typing speed test on the website `ratatype.ru <https://ratatype.ru>`_

======================
Как использовать?
======================

В **typewriter_main.py** указать логин и пароль. (`Регистрация <https://www.ratatype.ru/signup/>`_)


Скачать `geckodriver <https://github.com/mozilla/geckodriver/releases/>`_ и поместить в **ratatype_bot_typewriter/driver/**, в итоге в **typewriter_main.py** должно быть:

.. code-block:: python

  BitBot(webdriver.Firefox(executable_path="ratatype_bot_typewriter/driver/geckodriver"), login, password)
 
Либо, если у вас Linux и уставновлен Firefox, то можно просто:

.. code-block:: python
  BitBot(webdriver.Firefox(), login, password)
