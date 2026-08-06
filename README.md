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

## Deploy it to Streamlit Community Cloud

You said you already know how to deploy to Streamlit and only need the GitHub
repo, so here is the short version.

1. Create a new GitHub repository, for example `niece-portfolio`.
2. Put these files in the root of the repo, keeping the same layout:
   `streamlit_app.py`, `index.html`, `requirements.txt`, and the `images` folder.
3. Commit and push.
4. On Streamlit Community Cloud, create a new app, pick that repo and branch,
   and set the main file to `streamlit_app.py`. Deploy.

Keep `index.html` and the `images` folder in the same place as
`streamlit_app.py`, because the app reads them from right beside itself.

## Adding photos

Open the `images` folder and read the short guide inside it. In short, drop
files in with the exact names listed, for example `profile.jpg`, `art1.jpg`,
`like1.jpg`. The app builds them into the page when it runs, so nothing in the
code needs changing. Any spot without a file keeps its tidy placeholder box.

## Filling in the words

Everything to replace is written inside square brackets like `[ Your Name ]`
in `index.html`. Open that file in any text editor, search for the bracket text,
and type the real content in its place.

## Making each page fill the window

The height of the site is set on the last line of `streamlit_app.py`:

```
components.html(html, height=900, scrolling=True)
```

Raise the number if pages feel too short, lower it if there is empty space.
