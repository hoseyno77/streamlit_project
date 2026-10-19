import streamlit as st
import app_db1
st.title('STREAMLIT DATABASE UI')
option = st.sidebar.selectbox('Select Your Option:',(
'SELECT ALL RECORDS','SELECT RECORD BY ID','INSERT RECORD',
'DELETE RECORD BY ID','UPDATE RECORD BY ID'))

if option == 'SELECT ALL RECORDS':
    if st.button('SHOW DATA'):
        result = app_db1.select_all_records()
        st.write(result)
elif option == 'SELECT RECORD BY ID':
    movie_id = st.number_input('Enter movie id:',min_value=1)
    if st.button('SHOW DATA'):
        result = app_db1.select_record_by_id(movie_id)
        st.write(result)
elif option == 'INSERT RECORD':
    title = st.text_input('Enter title:')
    country = st.text_input('Enter country:')
    year = st.text_input('Enter year:')
    imdb_rate = st.number_input('Enter imdb_rate:')
    if st.button('INSERT'):
        result = app_db1.insert_record(title,country,year,imdb_rate)
        st.write(result)
elif option == 'DELETE RECORD BY ID':
    movie_id = st.number_input('Enter movie id:',min_value=1)
    if st.button('DELETE'):
        result = app_db1.delete_record_by_id(movie_id)
        st.write(result)
    
elif option == 'UPDATE RECORD BY ID':
    movie_id = st.number_input('Enter movie id:',min_value=1)
    year = st.text_input('Enter year:')
    imdb_rate = st.number_input('Enter imdb_rate:')

    if st.button('SHOW UPDATE'):
        result = app_db1.update_record_by_id(movie_id,year,imdb_rate)
        st.write(result)