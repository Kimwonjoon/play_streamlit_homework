import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html

def main():
    st.set_page_config(layout="wide")
    #logo_url = 'title.jpg'
    #st.sidebar.image(logo_url)
    with st.sidebar:
        choice = option_menu("Menu", ["위치","커리큘럼","정리노트"],
                            icons=['bi bi-people', 'bi bi-map', 'bi bi-backpack3', 'bi bi-graph-up-arrow', 'bi bi-globe-americas'],
                            menu_icon="bi bi-app-indicator", default_index=0,
                            styles={
            "container": {"padding": "4!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
            "nav-link-selected": {"background-color": "#08c7b4"},
        })
    st.sidebar.markdown("※정리 노트 업뎃중※")
    if choice == "위치":
       st.header("플레이데이터 서초")
       st.divider()
       path_to_html = "위치대충.html" 
       with open(path_to_html,'r',encoding='UTF-8') as f:
           html_data = f.read()
       html(html_data, width=1400, height=800)
    elif choice == "커리큘럼":
        st.header("PlayData 커리큘럼")
        st.divider()
        st.image('커리큘럼.png')
    else:
        st.header("정리 모음")
        st.divider()
        st.link_button("1주차 회고","https://velog.io/@kimpass189/PlayData-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-1%EC%A3%BC%EC%B0%A8-%ED%9A%8C%EA%B3%A0")

if __name__ == '__main__':
    main()

#st.header("PlayData 정보 모음")
#st.divider()
