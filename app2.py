# 스트림릿 라이브러리를 사용하기 위한 임포트문 작성

import streamlit as st

# 웹 대시보드 개발 라이브러리인 스트림릿은 main 함수가 잇어야한다.

def main() :
    st.title('Hello Streamlit. 웹 대시보드')
    st.title('헬로우')

if __name__ =='main' :
    main()

# 터미널에서 ctrl+c 를 하면 streamlit이 꺼진다

if __name__ == '__main__' :
    print(__name__)
    main()