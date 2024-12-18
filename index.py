import streamlit as st
from PIL import Image

st.title("Hello Gomycode ")
st.header("This is a header")
st.subheader("This is a subheader" )

texte = "Streamlit est une bibliothèque Python utilisée pour créer des applications web interactives pour la data science et l'apprentissage automatique. Cependant, elle nécessite un serveur local et des dépendances au niveau du système pour fonctionner, et Google Colab ne fournit pas de serveur local pouvant être utilisé pour exécuter des applications Streamlit. De plus, les applications Streamlit doivent souvent accéder à des ressources locales, qui peuvent ne pas être disponibles dans un environnement cloud comme Colab. Par conséquent, il est recommandé d'utiliser un environnement de développement local comme PyCharm pour créer et déployer des applications Streamlit afin d'obtenir les meilleurs résultats."
st.text(texte)

st.markdown("### Ceci est un markdown")

st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero" )

st.exception(exp)

img = Image.open("invoice.png")
st.image(img, width=100)

# ============================

if st.checkbox("Show/Hide"):
    # affiche le texte si la case à cocher renvoie la valeur True
    st.text("Showing the widget")

check = st.checkbox("check: Show/Hide")
st.text(check)

# le premier argument est le titre du bouton radio
# le deuxième argument est l'option du bouton radio
status = st.radio("Select Gender: ", ('Male', 'Female'), index=None, horizontal=True)


# déclaration conditionnelle à imprimer
# mâle si le mâle est sélectionné sinon imprimer female
# afficher le résultat à l'aide de la fonction de réussite
if status == 'Male':
    st.success("Male")
elif status == 'Female':
    st.success("Female")
else:
    st.text("fait un choix")

# Le premier argument est le titre de la boîte de sélection.
# le deuxième argument prend les options :
hobby = st.selectbox("Hobbies: ",['Dancing', 'Reading', 'Sports'])
# imprimer le hobby sélectionné :
st.write("Your hobby is: ", hobby)

# Le premier argument prend le titre de la boîte :
# Le deuxième argument contient les options à afficher :
hobbies = st.multiselect("Hobbies: ",['Dancing', 'Reading', 'Sports'])
st.write(hobbies)
# st.write("You selected", len(hobbies), 'hobbies')

# =========================

btn = st.button("Click me")
if btn:
    st.text("Welcome To Gomycode!!!")
    st.write("You selected", len(hobbies), 'hobbies')

# ===========================

# Le premier argument affiche le titre de la zone de saisie de texte.
# Le deuxième argument affiche un texte par défaut à l'intérieur de la zone de saisie de texte.
st.write("======== Begin Mon mini formulaire =========")

name = st.text_input("Enter Your name", placeholder="Type Here ...")
formBtn = st.button('Submit')
if formBtn:
    result = name
    st.success(result)

st.write("======== End Mon mini formulaire =========")

level = st.slider("Select the level", 0, 15)
st.text('Selected: {}'.format(level))
