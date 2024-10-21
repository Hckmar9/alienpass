import streamlit as st
import secrets, string, random

# I still need to check if this list is working as expected.
alien_names = [
    "Zorg", "Klaatu", "Xenon", "Quark", "Nebula", "Orion", "Nova", "Vortex",
    "Cosmo", "Zeta", "Andromeda", "Altair", "Rigel", "Sirius", "Cygnus",
    "Draco", "Lyra", "Vega", "Antares", "Arcturus"
]

def generate_alien_password(length=20, use_symbols=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?" if use_symbols else ""


    all_characters = lowercase + uppercase + digits + symbols
    alien_name = secrets.choice(alien_names)
    password = list(alien_name)
    password.append(secrets.choice(lowercase))
    password.append(secrets.choice(uppercase))
    password.append(secrets.choice(digits))
    if use_symbols:
        password.append(secrets.choice(symbols))


    while len(password) < length:
        if random.random() < 0.3 and len(password) + len(alien_name) <= length:
            password.extend(list(secrets.choice(alien_names)))
        else:
            password.append(secrets.choice(all_characters))

    password = password[:length]
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

st.title("Alien Password Generator 👽🔐")

st.write("""
Generate passwords with a touch of extraterrestrial flair. This app creates strong passwords that include alien names along with a mix of characters.
""")

length = st.slider("Password Length", min_value=10, max_value=33, value=20, step=1)
use_symbols = st.checkbox("Include Symbols", value=True)

if st.button("Generate Password"):
    password = generate_alien_password(length, use_symbols)
    st.success("Your alien-themed password is:")
    st.code(password)