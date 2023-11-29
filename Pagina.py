import streamlit as st
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Practica Web con Streamlit",
    page_icon=":dog:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Encabezado
st.title("Encuesta: ¿Te gustan los gatos o los perros?")

# Subencabezado
st.subheader("¡Comparte tu preferencia y descubre una sorpresa!")

# Texto de Markdown
st.markdown(
    """
    Bienvenido a esta encuesta interactiva. Completa el formulario y descubre una sorpresa al final.
    """
)

# Formulario
formulario = {}

with st.form(key="formulario"):
    inputNombre = st.text_input("Tu Nombre:")
    animal = st.radio("¿Te gustan los gatos o los perros?", ["Gatos", "Perros", "Ambos"])
    submit_button = st.form_submit_button("Mostrar resultado")

# Botón
if submit_button:
    # Hola [nombre]
    st.success(f"Hola {inputNombre}!")

    # Imagen de un gato o un perro
    if animal == "Gatos":
        st.image("R.jpeg", caption="¡Aquí tienes un lindo gato!", use_column_width=True)
    elif animal == "Perros":
        st.image("perro.jpeg", caption="¡Aquí tienes un adorable perro!", use_column_width=True)
    elif animal == "Ambos":
        st.image("PerroYGato.jpeg", caption="¡Aquí tienes un perro y un gato!", use_column_width=True)

# Sidebar
st.sidebar.title("Barra lateral")

# Elementos adicionales en la barra lateral
st.sidebar.subheader("Opciones:")
if st.sidebar.checkbox("Mostrar Datos Estadísticos"):
    # Gráfico interactivo
    st.sidebar.subheader("Preferencias de Usuarios:")
    data = {"Gatos": 30, "Perros": 45, "Ambos": 25}
    fig = px.pie(values=list(data.values()), names=list(data.keys()), title="Preferencias de Usuarios")
    st.sidebar.plotly_chart(fig, use_container_width=True)

st.sidebar.subheader("Redes Sociales:")
st.sidebar.image("twitter_icon.png", width=50)
st.sidebar.image("facebook_icon.png", width=50)
st.sidebar.image("instagram_icon.png", width=50)

st.sidebar.subheader("Enlaces Útiles:")
st.sidebar.write("[Sitio Web Principal](https://github.com/LOrdi15)", unsafe_allow_html=True)
st.sidebar.write("[Contacto](https://github.com/LOrdi15)", unsafe_allow_html=True)

# Botón de reinicio
if st.sidebar.button("Reiniciar Encuesta"):
    st.experimental_rerun()

# Texto final
st.info("¡Gracias por participar en nuestra encuesta!")
st.write("Integrantes del equipo 4: Jose Andres Ordieres, Marijose Villagomez, Carlos Castañeda, Leo Marquez", align="center")
