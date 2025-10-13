from utils import getTracksByLink

class BlockPlaylist:
    def __init__(self):
        self._composedBlocks = []
        self._allBlockCategories = []
        self._allSongsList = [] 
        self._allSongsCount = {}
    
    def getBlock(self):
        return self._composedBlocks
    
    def addBlock(self, block):
        self._composedBlocks.append(block)
        for song in block.getSongs():
            self._allSongsCount[song.getName()] = self._allSongsCount.get(song.getName(), 0) + 1
            if self._allSongsCount[song.getName()] == 1:
                self._allSongsList.append(song)
    
    def createSpotifyPlaylist(self, sp, name):
        user_id = sp.current_user()['id']
        newPlaylist = sp.user_playlist_create(
            user = user_id,
            name=name,
            public=True,
            description="Pass"
        )
        trackLinks = getTracksByLink(self._allSongsList)
        
        sp.playlist_add_items(newPlaylist['id'], trackLinks)        

        print(f"Created new playlist: {name}")

        
