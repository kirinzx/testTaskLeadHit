**Инструкция по запуску(она предполагает, что у вас установлен docker)**:

1) Клонируем репозиторий используя команду: git clone https://github.com/kirinzx/testTaskLeadHit.git

2) Переходим в директорию проекта. Запускаем docker-compose командой: docker-compose up -d

3) Заполним нашу базу данных формами. В терминале напишите команду: docker exec -it backend-django-container /bin/bash
    После этого вы должны увидеть в терминале следующее: root@2db2c85bfab2:/app#
    Далее запустите скрипт для заполнения: python fillDb.py


**Совершение тестовых запросов (Предполагается, что докер контейнер запущен)**:

Напишите команду docker exec -it backend-django-container /bin/bash
Напишите команду: python testRequests.py

Далее в терминале вы увидите ответы сервера

При желании, вы можете изменить отправляемые данные. Для этого измените словарь testForms в файле backend/testRequests.py