===========
ratatype-bot-typewriter
===========

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Bot that automatically passes the typing speed test on the website `ratatype.ru <https://ratatype.ru>`_

# Как использовать?
Скачать geckodriver, и в typewriter_main использовать:

.. code-block:: python

  BitBot(webdriver.Firefox(executable_path='path'), login, password)
 
Либо, если у вас Linux и уставновлен Firefox, то можно просто:

.. code-block:: python

  BitBot(webdriver.Firefox(), login, password)
