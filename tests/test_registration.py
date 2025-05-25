import pytest
import sqlite3
import os
from registration.registration import create_db, add_user, authenticate_user, display_users

@pytest.fixture(scope="module")
def setup_database():
    """Фикстура для настройки базы данных перед тестами и её очистки после."""
    create_db()
    yield
    try:
        os.remove('users.db')
    except PermissionError:
        pass

@pytest.fixture
def connection():
    """Фикстура для получения соединения с базой данных и его закрытия после теста."""
    conn = sqlite3.connect('users.db')
    yield conn
    conn.close()

@pytest.fixture
def sample_users(setup_database, connection):
    """Фикстура для добавления тестовых пользователей в базу данных."""
    add_user('user1', 'user1@example.com', 'pass1')
    add_user('user2', 'user2@example.com', 'pass2')
    yield
    # Очистка тестовых пользователей
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE username IN ('user1', 'user2')")
    connection.commit()

def test_create_db(setup_database, connection):
    """Тест создания базы данных и таблицы пользователей."""
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    table_exists = cursor.fetchone()
    assert table_exists, "Таблица 'users' должна существовать в базе данных."

def test_add_new_user(setup_database, connection):
    """Тест добавления нового пользователя."""
    # Удаляем пользователя, если он уже существует
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE username='testuser'")
    connection.commit()
    
    # Пытаемся добавить нового пользователя
    result = add_user('testuser', 'testuser@example.com', 'password123')
    assert result is True, f"Ожидалось True, получено {result}. Пользователь не был добавлен."
    
    # Проверяем, что пользователь действительно добавлен
    cursor.execute("SELECT * FROM users WHERE username='testuser'")
    user = cursor.fetchone()
    assert user is not None, "Пользователь не найден в базе данных"
    assert user[0] == 'testuser', "Неверное имя пользователя"
    assert user[1] == 'testuser@example.com', "Неверный email"
    assert user[2] == 'password123', "Неверный пароль"

def test_add_duplicate_user(setup_database):
    """Тест добавления пользователя с существующим логином."""
    add_user('duplicate', 'duplicate@example.com', 'password')
    assert not add_user('duplicate', 'newemail@example.com', 'newpass'), "Не должно быть возможности добавить пользователя с существующим логином."

def test_authenticate_user_success(sample_users):
    """Тест успешной аутентификации пользователя."""
    assert authenticate_user('user1', 'pass1'), "Аутентификация должна пройти успешно для правильных учетных данных."

def test_authenticate_user_wrong_password(sample_users):
    """Тест аутентификации пользователя с неправильным паролем."""
    assert not authenticate_user('user1', 'wrongpass'), "Аутентификация не должна проходить с неправильным паролем."

def test_authenticate_user_nonexistent(sample_users):
    """Тест аутентификации несуществующего пользователя."""
    assert not authenticate_user('nonexistent', 'pass1'), "Аутентификация не должна проходить для несуществующего пользователя."

def test_display_users(sample_users, capsys):
    """Тест отображения списка пользователей."""
    display_users()
    captured = capsys.readouterr()
    assert "Логин: user1, Электронная почта: user1@example.com" in captured.out
    assert "Логин: user2, Электронная почта: user2@example.com" in captured.out
