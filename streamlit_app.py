import streamlit as st
import random

if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 110)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

st.title("🎯 Number Guessing Game")

guess = st.number_input(
    "Guess a number between 1 and 110",
    min_value=1,
    max_value=110,
    step=1
)

if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("⬆️ Enter Higher Number")

    elif guess > st.session_state.secret_number:
        st.warning("⬇️ Enter Lower Number")

    else:
        st.success(
            f"🎉 Correct! You found it in {st.session_state.attempts} attempts."
        )

        st.session_state.secret_number = random.randint(1, 110)
        st.session_state.attempts = 0