import streamlit as st
import pandas as pd

def main ():
    df=pd.read_csv('data/iris.csv')
    # if st.button('데이터 보기') :
    #   st.dataframe(df)
    
    # name = Mike
    
    # if st.button('대문자 로'):
    #   st.write(name.upper())
    # if st.button('소문자로'):
    #   st.write(name.lower())
    st.dataframe(df)
    # 내가 누른 것에 대한 정보는 변수로 받아 주어야 한다.
    # 화면은 무조건 st가 담당
    status = st.radio('정렬을 선택하세요',['오름차순정렬','내림차순정렬'])
    
    if status == '오름차순정렬':
        st.dataframe(df.sort_values('petal_length'))
    if status == '내림차순정렬':
        st.dataframe(df.sort_values('petal_length',ascending=False))
    
if __name__ == '__main__':
    main()