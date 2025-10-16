from classes.song import Song

class Block:
    def __init__(self, tracks=None, desc=""):
        self._parentBlock = None
        self._childBlocks = []
        self._songs = []
        self._categories = [] 
        if tracks and desc:
            for i, item in enumerate(tracks['items']):
                track = item['track'] 
                self._songs.append(Song(track['name'], track['external_urls']['spotify']))
            self._categories = desc.split(',')
 
    def add_song(self, song):
        self._songs.append(song)

    def set_extend(self, parentBlock):
        self._parentBlock = parentBlock
        parentBlock.addChild(self)
    
    def show_songs(self):
        for song in self._songs:
            print(song.getName())
    
    def get_songs(self):
        return self._songs
    
    def add_child(self, childBlock):
        self._childBlocks.append(childBlock)
        for song in childBlock.getSongs():
            if song.getName() not in self._songs:
                self._songs.append(song)
    
    def get_categories(self):
        return self._categories   

    def __repr__(self):
        return f"Songs: {self._songs}"
