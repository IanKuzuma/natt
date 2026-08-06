# Portfolio, Streamlit version

This folder is a Streamlit app that shows the portfolio website. All of the
design, animations and page snapping live in `index.html`. The Streamlit app
displays that file full width, and folds in any photos from the images folder.

The site adjusts to the screen. On a laptop it snaps firmly from one full page
to the next. On a phone the pages flow and scroll so nothing is cut off in the
narrow vertical space, with a gentler snap.

## Files

- `streamlit_app.py`, the app that renders the website
- `index.html`, the actual website, edit this to change any wording
- `requirements.txt`, the one dependency, Streamlit
- `images/`, drop photos here, see the guide inside that folder

## Run it on your own computer

1. Open a terminal in this folder.
2. Install the dependency:
   ```
   pip install -r requirements.txt
   ```
3. Start the app:
   ```
   streamlit run streamlit_app.py
   ```
4. Your browser opens the site automatically. If not, open the local URL that
   the terminal prints, usually http://localhost:8501
