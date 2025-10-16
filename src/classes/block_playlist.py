from utils import getTracksByLink

class BlockPlaylist:
    def __init__(self):
        self._composed_blocksBlocks = []
        # TODO: Implement Block Categories
        self._all_block_categories = []
        self._allSongsCount = {}
    
    def get_block(self):
        return self._composed_blocksBlocks
    
    def add_block(self, block):
        self._composed_blocksBlocks.append(block)
        for song in block.get_songs():
            self._allSongsCount[song] = self._allSongsCount.get(song, 0) + 1
   
    def create_spotify_playlist(self, sp, name):
        user_id = sp.current_user()['id']
        newPlaylist = sp.user_playlist_create(
            user = user_id,
            name=name,
            public=True,
            description="Pass" # TODO: This is hardcoded - add category list
        )
        trackLinks = getTracksByLink(self.get_all_songs())
        sp.playlist_add_items(newPlaylist['id'], trackLinks)        

        print(f"Created new playlist: {name}")
    
    def get_all_songs(self):
        return list(self._allSongsCount.keys())

        
