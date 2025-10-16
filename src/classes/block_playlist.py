from utils import getTracksByLink

class BlockPlaylist:
    def __init__(self):
        self._composedBlocks = []
        # TODO: Implement Block Categories
        self._allBlockCategories = []
        self._allSongsList = [] 
        self._allSongsCount = {}
    
    def get_block(self):
        return self._composedBlocks
    
    def add_block(self, block):
        self._composedBlocks.append(block)
        for song in block.get_songs():
            self._allSongsCount[song.get_name()] = self._allSongsCount.get(song.get_name(), 0) + 1
            if self._allSongsCount[song.get_name()] == 1:
                self._allSongsList.append(song)
    
    def create_spotify_playlist(self, sp, name):
        user_id = sp.current_user()['id']
        newPlaylist = sp.user_playlist_create(
            user = user_id,
            name=name,
            public=True,
            # TODO: This is hardcoded - add category list
            description="Pass"
        )
        trackLinks = getTracksByLink(self._allSongsList)
        
        sp.playlist_add_items(newPlaylist['id'], trackLinks)        

        print(f"Created new playlist: {name}")

        
