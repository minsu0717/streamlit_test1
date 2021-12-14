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
    elif status == '내림차순정렬':
        st.dataframe(df.sort_values('petal_length',ascending=False))
        
    if st.checkbox('show/hide') :
        st.dataframe(df.head())
    else :
        st.write('데이터가 없습니다')
        
    language = ['Python','C','Java','Go']
    my_choice = st.selectbox('좋아하는 언어를 선택하세요',language)
    if my_choice == 'C':
        st.write('저는 C가 좋아요')
    elif my_choice == 'Python':
        st.write('파이썬 최고')
        
    
    choice_list=st.multiselect('여러개를 선택할수 있습니다',language)
    
    # 여러분들이 디버깅을 하고 싶으면,
    # 파이썬의 print 함수를 이용하면, 아래의 터미널에
    # 출력이 된다.
    print(choice_list)
    
    choice_list=st.multiselect('컬럼을 선택하세요',df.columns)
    print(choice_list)
    print(df[choice_list])
    st.write(df[choice_list])


    age = st.slider('나이',1,100,value=20)
    
    st.text('선택한 나이는 {}입니다'.format(age))
    
    with st.expander('Hello') :
        st.text('안녕하세요')



if __name__ == '__main__':
    main()