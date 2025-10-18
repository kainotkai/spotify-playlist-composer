from flask import Flask, jsonify, request
from flask_cors import CORS
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os

from classes import Block, BlockPlaylist, Song
from utils import getAllBlocks

app = Flask(__name__)
# origins is * - fix later 
CORS(app, resources={r"/api/*": {"origins": "*"}})

block_storage = {}

load_dotenv()
scope = "user-library-modify playlist-read-private playlist-modify-private playlist-modify-public"
client_id = os.getenv("SPOTIPY_CLIENT_ID").strip()
 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id[0:len(client_id) - 1],
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope=scope
))
 

def get_spotify_client():
    scope = "user-library-modify playlist-read-private playlist-modify-private playlist-modify-public"
    client_id = os.getenv("SPOTIPY_CLIENT_ID").strip()
    print(client_id)
    print(os.getenv("SPOTIPY_CLIENT_SECRET"))

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id[0:len(client_id) - 1],
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope
    ))
    return sp

@app.route('/')
def home():
    return jsonify({"message": "SpotifyComposer is Running!"})

@app.route("/api/blocks", methods=["GET"])
def get_blocks():
    global block_storage
    sp = get_spotify_client()
    results = sp.current_user_playlists()
    all_blocks = getAllBlocks(sp, results)

    blocks_data = []
    block_storage = {}
    for block in all_blocks:
        blocks_data.append(block.process_to_json())
        block_storage[block.get_name()] = block
    
    return jsonify(blocks_data)
    

@app.route("/api/create-playlist", methods=["POST"])
def create_playlist():
    try:
        data = request.json
        components = data.get("components", [])

        for component_data in components:
            block_names = component_data['blockNames']
            playlist_name = component_data['playlistName']

            block_playlist = BlockPlaylist()
            for block_name in block_names:
                if block_name in block_storage:
                    block = block_storage[block_name]
                    block_playlist.add_block(block)
            block_playlist.create_spotify_playlist(sp, playlist_name)

    except:
        print("failed :(")
        return jsonify({":(" : ":("})

    return jsonify({":)": ":)"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)

