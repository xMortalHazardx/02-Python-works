import streamlit as st
import pandas
#from streamlit_carousel import carousel


st.set_page_config(layout="wide")


col1,empty_b, col2 = st.columns([1.5,0.5,1.5])

information = """Below you can find some of the apps I have built in Python. Feel free to contact me!
    """

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Alguem Sulce")
    content = """ What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap into
 electronic typesetting, remaining essentially unchanged. It was popularised in 
 the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
 and more recently with desktop publishing software like Aldus PageMaker including 
 versions of Lorem Ipsum
    """
    st.info(content)

st.text(information)

st.write(information)

#"""test_items = [
#    dict(
 #       title="Slide 1",
  #      text="A tree in the savannah",
   #     img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
    #    link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819"
#    ),
#    dict(
#        title="Slide 2",
#        text="A wooden bridge in a forest in Autumn",
#        img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
#        link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel"
#    ),
#    dict(
#        title="Slide 3",
#        text="A distant mountain chain preceded by a sea",
#        img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
#        link="https://github.com/thomasbs17/streamlit-contributions/tree/master"
#    ),
#    dict(
#        title="Slide 4",
#        text="A distant mountain chain preceded by a sea",
#        img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
#        link="https://github.com/thomasbs17/streamlit-contributions/tree/master"
#    ),
#    dict(
#        title="Slide 5",
#        text="A distant mountain chain preceded by a sea",
#        img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
#        link="https://github.com/thomasbs17/streamlit-contributions/tree/master"
#    ),
#]

#carousel(items=test_items, width=0.5)"""

col3, sidebarra, col4 = st.columns(3)



df = pandas.read_csv("data.csv", sep=";")

with st.sidebar:
    st.button("Home","images/1.png")
    st.link_button("Home","http://localhost:8501")
    

with col3:
    for i, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=800)
        st.write("[Source Code](https://google.com)")
        

with col4:
    for i, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=800)
        st.write(f"[Link]({row["url"]})")
        




