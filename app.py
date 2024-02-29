#backend
import project
# Streamlit
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import project

# Funcion de animación

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# llamar a los elementos de media

lottie_coding = load_lottieurl("https://lottie.host/4bb416f5-a45a-4804-83e8-408744a8e9c2/ymOTQZ7ZT7.json")
image = Image.open("E:/Proyectos/Python/Ejercicios/Capstone Project/prueba.jpg")

# Listas de preguntas y de respuestas

#if 'preguntas' not in st.session_state:
#    st.session_state.preguntas = []
#if 'respuestas' not in st.session_states:
#    st.session_states.respuestas = []

# Estructura de la pagina

#def click():
#    if st.session_state.user != "":
#        pregunta = st.session_state.user
#        respuesta = project.pedir_dieta(pregunta)

#        st.session_state.pregunta.append(pregunta)
#        st.session_state.respuesta.append(respuesta)


with st.container():
    st.subheader("Hola!, yo sere tu entrenador personal :wave: ")
    st.title("Proyecto base de ChatGPT Open IA")
    st.write(" Una breve descripcion de nuestro trabajo")


with st.container():
    st.title("Informacion del cliente:")
    
    with st.form("user_input"):
        firstname = st.text_input("Nombre") 
        genero = st.multiselect(("Genero"), ["Masculino","Femenino"], max_selections= 1)
        edad = st.number_input("edad", min_value=0)
        peso = st.number_input("Peso en gr", min_value=0)
        a_fisica = st.multiselect(("Actividad Fisica"), ["Si","No"], max_selections = 1) 
        a_tipo = st.text_input("Tipo de Actividad")
        objetivo = st.text_input("Objetivo")

        # Boton de mandar informacion

        submit_button = st.form_submit_button(label='Hacer Dieta')

    
       
    if submit_button:
        st.info("Esta es tu dieta")
        result_formato = project.consulta(firstname, edad, genero, peso, a_fisica, a_tipo, objetivo)
        result_dieta = project.pedir_dieta(result_formato)
        st.write(result_dieta)
        
        
#with right_column:
#    st_lottie(lottie_coding, height=300, key="coding")
            

"""
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Mi objetivo")
        st.write(
            "dieta"
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
"""
    

    
