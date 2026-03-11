# Spotify-style Python Frontend

This lightweight Flask app recreates a Spotify-inspired layout entirely in Python with plain CSS and JavaScript for interactions.

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run

```bash
python app.py
```

Then open http://127.0.0.1:8500 in a browser. The UI shows playlists, top tracks, and a mock now-playing footer with basic interactions powered by `static/app.js`.
