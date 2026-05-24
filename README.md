# Читательский дневник:

Веб-приложение для ведения списка прочитанных книг с возможностью добавления книги и её оценки, а также для написания отзыва и удаления записей.

## Основные возможности:
- ➕ **Добавить книгу** - указать название, автора, оценку (1-5 звёзд) и отзыв
- 📖 **Мои книги** - просмотр всех добавленных книг
- 🗑️ **Удалить** - возможность удалить книгу из дневника


## Технологический стек:
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Database:** SQLite + SQLAlchemy
- **Language:** Python


## Быстрый старт

### 1. Создание и активация виртуального окружения
bash
python -m venv myvenv

*Для Windows:*
myvenv\Scripts\activate

*Для Linux / macOS:*
source myvenv/bin/activate

### 2. Установка зависимостей
bash
pip install -r requirements.txt

### 3. Запуск
*Запустить бэкенд:* bash
uvicorn backend.main:app --reload

*Запустить фронтенд (в другом терминале):* bash
streamlit run frontend/app.py

### Веб-риложение откроется по адресу: http://localhost:8501
