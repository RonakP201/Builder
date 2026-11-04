from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Outfit Builder", page_icon="👕", layout="centered")

# Hide Streamlit chrome so the builder fills the screen
st.markdown(
    """<style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0.5rem 0.25rem 0 0.25rem; max-width: 820px;}
    </style>""",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "outfit_builder.html").read_text(encoding="utf-8")
components.html(html, height=1950, scrolling=False)
