from classes.song import Song

class Block:
    def __init__(self):
        self._parentBlock = None
        self._childBlocks = []
        self._songs = []
        self._categories = [] 

    def __init__(self, tracks, desc):
        self._parentBlock = None
        self._childBlocks = [] 
        self._songs = []
        for i, item in enumerate(tracks['items']):
            track = item['track'] 
            self._songs.append(Song(track['name'], track['external_urls']['spotify']))
        
        self._categories = desc.split(',')

    def addSong(self, song):
        self._songs.append(song)

    def setExtend(self, parentBlock):
        self._parentBlock = parentBlock
        parentBlock.addChild(self)
    
    def showSongs(self):
        for song in self._songs:
            print(song.getName())
    
    def getSongs(self):
        return self._songs
    
    def addChild(self, childBlock):
        self._childBlocks.append(childBlock)
        for song in childBlock.getSongs():
            if song.getName() not in self._songs:
                self._songs.append(song)
    
    def getCategories(self):
        return self._categories   

    def __repr__(self):
        return f"Songs: {self._songs}"
