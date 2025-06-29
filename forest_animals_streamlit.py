import streamlit as st

# File name where animals will be saved
FILE = "forest_animals.txt"

# Load animals from the file
def load_animals():
    try:
        with open(FILE, "r") as f:
            animals = f.read().splitlines()
    except FileNotFoundError:
        animals = []
    return animals

# Save new animal to the file
def save_animal(animal):
    with open(FILE, "a") as f:
        f.write(animal + "\n")

# Streamlit App
st.title("🌳 Forest Animals Tracker 🐾")

# User input box
animal = st.text_input("Enter an animal name:")

if animal:
    animal = animal.strip().lower()
    animals = load_animals()
    
    if animal in animals:
        st.warning(f"✅ The animal '{animal}' is already in the forest!")
    else:
        save_animal(animal)
        st.success(f"🌟 The animal '{animal}' has been added to the forest!")

    st.subheader("🌿 Animals currently in the forest:")
    st.write(animals)
    
    st.session_state["animal_input"] = ""
    
# Author LinkedIn link
author_name = '[Usama Israr Khan](https://www.linkedin.com/in/usama-israr-khan-3b68312ab/)'

# Display author credit with LinkedIn link
st.markdown(f"**Made by {author_name}**")
