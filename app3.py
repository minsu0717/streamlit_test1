import streamlit as st
import pandas as pd

def main() :
    #  데이터프레임 읽기만 하면 출력을 안한다.
    df=pd.read_csv('data/iris.csv')
    st.dataframe(df)
    
    species=df['species'].unique()
    st.text('아이리스 꽃은' + species + '으로 되어있다.')
    
    st.write(df.head())
    
if __name__ == '__main__':
    main()