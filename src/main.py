import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from random import randint
from datetime import datetime

from classes import Block, BlockPlaylist, Song
from utils import getAllBlocks

load_dotenv()
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

scope = "user-library-modify playlist-read-private playlist-modify-private playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id[0:len(client_id) - 1],
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope=scope
))

def main():
    # Example usage:

    newPlaylist = BlockPlaylist() 
    results = sp.current_user_playlists()
    allBlocks = getAllBlocks(sp, results)

    for block in allBlocks:
        if "chill" in block.getCategories() and randint(1, 10) <= 5:
            newPlaylist.addBlock(block)
    
    newPlaylist.createSpotifyPlaylist(sp, f"Random Chill Playlist - {datetime.now()}")


if __name__ == "__main__":
    main()