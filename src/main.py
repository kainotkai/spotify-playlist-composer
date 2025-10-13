from classes.blockPlaylist import BlockPlaylist 
from classes.block import Block
from classes.song import Song 
from utils import addBlocksToPlaylist
from getAllBlocks import getAllBlocks

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

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
        newPlaylist.addBlock(block)
    newPlaylist.createSpotifyPlaylist(sp, "New Playlist From Blocks")

if __name__ == "__main__":
    main()