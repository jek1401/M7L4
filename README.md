# User Management System

Простая система управления пользователями, реализованная на Python и использующая SQLite для хранения данных пользователей. Программа позволяет добавлять новых пользователей, аутентифицировать существующих пользователей и отображать список всех пользователей.

## Особенности

- **Добавление новых пользователей**: Сохраните данные новых пользователей в базе данных.
- **Аутентификация пользователей**: Проверьте учетные данные пользователя для аутентификации.
- **Отображение списка пользователей**: Выведите список всех пользователей с их данными, за исключением паролей.

## Начало работы

Для работы с программой убедитесь, что у вас установлен Python версии 3.6 или выше и SQLite.

### Установка

1. Клонируйте репозиторий на свой локальный компьютер:
    ```bash
    git clone путь_к_репозиторию
    ```
2. Перейдите в каталог проекта:
    ```bash
    cd User_Management_System_DB
    ```

### Использование

Для запуска программы выполните следующую команду в терминале:
```bash
python registration.py
```
После запуска следуйте инструкциям в консоли для управления пользователями.

### Тестирование
![image](https://github.com/user-attachments/assets/f7cbc475-b061-4a65-b841-19ba9a106398)
![image](https://github.com/user-attachments/assets/e1d226b7-9de0-48c6-aa9e-1e00aaec9fc0)

Программа включает unit тесты, написанные с использованием библиотеки pytest. Для запуска тестов убедитесь, что у вас установлен pytest, если нет, установите его с помощью pip:
```bash
pip install pytest
```

Запустите тесты из корневой директории проекта следующей командой:
```bash
pytest
```
## Автор
Давид
