from json import dumps
from classes.song import Song

class Block:
    def __init__(self, tracks=None, name=None, desc=""):
        self._parentBlock = None
        self._childBlocks = []
        self._songs = []
        self._categories = [] 
        self._name = name

        if tracks:
            for i, item in enumerate(tracks["items"]):
                track = item["track"] 
                self._songs.append(Song(track["name"], track["external_urls"]["spotify"]))
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
        for song in childBlock.get_songs():
            if song.get_name() not in self._songs:
                self._songs.append(song)
    
    def get_categories(self):
        return self._categories   

    def __repr__(self):
        return f"Songs: {self._songs}"
    
    def process_to_json(self):
        return {
            "name": f"{self._name}",
            "songs": [
                {
                    "name": song.get_name(),
                    "link": song.get_link(),
                    "id": f"song_{hash(song)}"
                } for song in self._songs
            ],
            "categories": "idk", # TODO: Implement
            "songCount": len(self._songs)
        }

    def get_name(self):
        return self._name
