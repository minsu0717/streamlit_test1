## 여러 파일을 업로드 하는 앱

import streamlit as st
from PIL import Image
import pandas as pd
import os
# 현재시간 가져오기 위한 라이브 러리
from datetime import datetime


# 파일 업로드 하는 함수!
def save_uploaded_file(directory,file) :
    # 1. 디렉토리가 있는지 확인하여, 없으면 디렉토리부터 만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory,file.name),'wb') as f :
        f.write(file.getbuffer())
    return st.success('Saved file : {} in {}'.format(file.name,directory))


def main():
    st.title('여러 파일들을 업로드 하는 앱')
    
    # 사이드바용 메뉴
    menu = ['Image','CSV','About']
    choice = st.sidebar.selectbox('메뉴',menu)
    
    if choice == 'Image' :
        uploaded_files=st.file_uploader('이미지파일 업로드',
                                        type=['jpg','png','jpeg'],
                                        accept_multiple_files=True)
        print(uploaded_files)
        
        if uploaded_files is not None :
            for file in uploaded_files :
                save_uploaded_file('temp_files',file)
                
                img = Image.open(file)
                st.image(img)

    ## CSV 파일 여러개 올리는 코드를 아래 작성하세요
    ## CSV 파일명은 시간.csv 의 조합된 파일명으로 저장하세요
    
    elif choice == 'CSV' :
        up_files=st.file_uploader('CSV파일 업로드',
                         type=['csv'],
                         accept_multiple_files=True)
        if up_files is not None :
            for file in up_files :
                file.name=datetime.now().isoformat().replace(':','_')+'.csv'
                save_uploaded_file('new_csv_file',file)
                
                st.dataframe(file)
    




if __name__ == '__main__':
    main()