import streamlit as st

tab1,tab2,tab3 = st.tabs(["About","Hobbies","Contact"])

with tab1:
    
    col1,col2 = st.columns([0.3,0.7])
    
    with col1:
        st.image("my_picture/my_pic_kool.jpg",width=200)
        st.subheader("DTM :sunglasses:")
    
    with col2:
        st.write("Hi, I am DTM, a Junior Developer :computer: . I made this website because I often overspend and I need to track my expenses. You can use this website to manage and track your expenses as well. I hope you all 💛 it.")

with tab2:
     st.write("I love math and coding:abacus: problems and playing video games 	:video_game:. Also, I'm into taekwondo and I have a gold belt.")

with tab3:
    st.write("Email : deetyamsoni@gmail.com")
    st.write("Phone(totally) : 1234567890")

