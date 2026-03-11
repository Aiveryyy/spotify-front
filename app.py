from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

sidebar_links = [
    {"label": "Home", "icon": "home", "active": True},
    {"label": "Search", "icon": "search"},
    {"label": "Your Library", "icon": "library"},
]

hero_cards = [
    {
        "title": "Daily Focus",
        "subtitle": "Soft electronic beats",
        "desc": "Perfect for deep work sessions",
        "cover": "linear-gradient(135deg, #1db954, #1db954 60%, #121212)",
    },
    {
        "title": "Upbeat Evenings",
        "subtitle": "Feel-good pop",
        "desc": "Revive your post-work mood",
        "cover": "linear-gradient(135deg, #ff5f6d, #ffc371)",
    },
]

playlists = [
    {
        "title": "Neon Nights",
        "description": "Retro-inspired synthwave",
        "tracks": 42,
        "cover": "linear-gradient(135deg, #8321fd, #ff6eb4)",
    },
    {
        "title": "City Coffee",
        "description": "Acoustic warmth for mornings",
        "tracks": 37,
        "cover": "linear-gradient(135deg, #f2994a, #f2c94c)",
    },
    {
        "title": "Pulse Pop",
        "description": "High-energy hits",
        "tracks": 58,
        "cover": "linear-gradient(135deg, #2b6cb0, #9f7aea)",
    },
    {
        "title": "Underwater",
        "description": "Ambient textures",
        "tracks": 23,
        "cover": "linear-gradient(135deg, #0f2027, #203a43, #2c5364)",
    },
]

top_tracks = [
    {"title": "Midnight Bloom", "artist": "Aural Tide", "duration": "3:47"},
    {"title": "Paper Planes", "artist": "Lumen Arc", "duration": "4:02"},
    {"title": "Slow Drift", "artist": "Nebula Branch", "duration": "3:33"},
    {"title": "Tidal Glow", "artist": "Kara Waves", "duration": "2:58"},
    {"title": "Orbitals", "artist": "Venus Exit", "duration": "4:10"},
]

now_playing = {
    "title": "Neon Bloom",
    "artist": "Pulse Theory",
    "album": "City Afterglow",
    "cover": "linear-gradient(135deg, #009ffd, #ec2f4b)",
    "progress": 62,
}

@app.route("/")
def index():
    return render_template(
        "index.html",
        sidebar_links=sidebar_links,
        hero_cards=hero_cards,
        playlists=playlists,
        top_tracks=top_tracks,
        now_playing=now_playing,
    )

if __name__ == "__main__":
    app.run(debug=True, port=8500)
