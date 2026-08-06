# Portfolio website, wrapped in Streamlit.
# This script renders the same index.html file inside a full width iframe, so the
# animations and page snapping behave exactly like the standalone site.
# It also reads the images folder and builds any photos found there straight into
# the page, so dropping files into images/ is all that is needed to see them here.

from pathlib import Path
import base64
import mimetypes
import streamlit as st
import streamlit.components.v1 as components

HERE = Path(__file__).parent
IMAGES_DIR = HERE / "images"

st.set_page_config(
    page_title="Portfolio",
    page_icon="\U0001F98B",  # butterfly, change if you like
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own menu, header and footer, and remove page padding, so the
# website fills the whole window instead of sitting in a narrow column.
st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      header {visibility: hidden;}
      footer {visibility: hidden;}
      .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] {padding: 0 !important;}
      [data-testid="stHeader"] {height: 0 !important; visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)


def embed_images(html: str) -> str:
    # For every image file in the images folder, replace its src="images/NAME"
    # reference in the page with the image data itself. This makes photos show up
    # inside the Streamlit frame, which cannot otherwise reach a local folder.
    if not IMAGES_DIR.exists():
        return html
    allowed = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
    for img in sorted(IMAGES_DIR.iterdir()):
        if img.is_file() and img.suffix.lower() in allowed:
            mime = mimetypes.guess_type(img.name)[0] or "image/jpeg"
            data = base64.b64encode(img.read_bytes()).decode("ascii")
            data_uri = "data:" + mime + ";base64," + data
            html = html.replace('src="images/' + img.name + '"', 'src="' + data_uri + '"')
    return html


# Read the site file that sits next to this script, then fold in any photos.
html = (HERE / "index.html").read_text(encoding="utf-8")
html = embed_images(html)

# Render it inside an iframe.
# The height value sets how tall the iframe is. Each page measures itself as one
# screen height inside this iframe, so a taller value makes each page fill more
# of the window. 900 suits most laptops. Raise or lower it to taste.
components.html(html, height=900, scrolling=True)
