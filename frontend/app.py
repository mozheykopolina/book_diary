import streamlit as st
import requests

st.set_page_config(
    page_title="Читательский дневник",
    page_icon="📚",
    layout="centered"
)

st.title("📖 Читательский дневник")

if 'page' not in st.session_state:
    st.session_state.page = 'main'

with st.sidebar:
    st.markdown("## 📚 Меню")
    st.markdown("---")
    
    if st.button("📝 Добавить книгу", use_container_width=True):
        st.session_state.page = 'add_book'
        st.rerun()
    
    if st.button("📖 Мои книги", use_container_width=True):
        st.session_state.page = 'my_books'
        st.rerun()
    
    st.markdown("---")
    st.caption("Читательский дневник")

def show_add_book():
    st.subheader("➕ Новая книга")
    
    with st.form("add_book_form", clear_on_submit=True):
        title = st.text_input("Название книги*", placeholder="Война и мир")
        author = st.text_input("Автор*", placeholder="Лев Толстой")
        rating = st.select_slider(
            "Оценка (1-5 звёзд)",
            options=[1, 2, 3, 4, 5],
            value=None
        )
        review = st.text_area(
            "Отзыв",
            placeholder="Поделитесь впечатлениями...",
            height=100
        )
        
        submitted = st.form_submit_button("💾 Сохранить книгу", type="primary")
        
        if submitted:
            if not title or not author:
                st.error("❌ Пожалуйста, заполните название и автора")
            else:
                book_data = {
                    "title": title,
                    "author": author,
                    "rating": rating,
                    "review": review if review else None
                }
                
                try:
                    response = requests.post("http://localhost:8000/books", json=book_data)
                    if response.status_code == 200:
                        st.success(f"✅ Книга «{title}» добавлена в дневник!")
                    else:
                        st.error(f"Ошибка: {response.text}")
                except requests.exceptions.ConnectionError:
                    st.error("❌ Не удалось подключиться к серверу. Запустите бэкенд!")
    
    st.markdown("---")
    if st.button("🏠 На главную"):
        st.session_state.page = 'main'
        st.rerun()

def show_my_books():
    st.subheader("📚 Мои книги")
    
    try:
        response = requests.get("http://localhost:8000/books")
        if response.status_code == 200:
            books = response.json()
            
            if not books:
                st.info("📖 В дневнике пока нет книг. Добавьте первую книгу через меню!")
            else:
                for book in books:
                    with st.container():
                        st.markdown(f"### {book['title']}")
                        st.markdown(f"*Автор: {book['author']}*")
                        
                        if book['rating']:
                            stars = "⭐" * int(book['rating'])
                            st.markdown(f"**Оценка:** {stars} ({book['rating']}/5)")
                        else:
                            st.markdown("**Оценка:** не указана")
                        
                        if book['review']:
                            with st.expander("📝 Отзыв"):
                                st.write(book['review'])
                        else:
                            st.caption("Отзыв не оставлен")
                        
                        if st.button("🗑️ Удалить", key=f"delete_{book['id']}"):
                            delete_response = requests.delete(f"http://localhost:8000/books/{book['id']}")
                            if delete_response.status_code == 200:
                                st.success(f"Книга «{book['title']}» удалена!")
                                st.rerun()
                            else:
                                st.error("Ошибка при удалении")
                        
                        st.divider()
        else:
            st.error("Ошибка загрузки книг")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Не удалось подключиться к серверу")

def show_main():
    st.markdown("## Добро пожаловать!")
    st.markdown("Здесь вы можете вести список прочитанных книг.")
    st.markdown("---")
    st.markdown("### Как пользоваться:")
    st.markdown("""
    1. Нажмите **📝 Добавить книгу** в меню слева
    2. Заполните название, автора, оценку и отзыв
    3. Нажмите **💾 Сохранить книгу**
    4. Все ваши книги появятся в разделе **📖 Мои книги**
    """)
    
    try:
        response = requests.get("http://localhost:8000/books")
        if response.status_code == 200:
            books = response.json()
            total = len(books)
            if total > 0:
                st.info(f"📊 В вашем дневнике уже **{total}** книг!")
    except:
        pass

if st.session_state.page == 'main':
    show_main()
elif st.session_state.page == 'add_book':
    show_add_book()
elif st.session_state.page == 'my_books':
    show_my_books()