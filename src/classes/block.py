from classes.song import Song

class Block:
    def __init__(this):
        this._parentBlock = None
        this._childBlocks = []
        this._songs = []
        this._categories = [] 

    def __init__(this, tracks):
        this._parentBlock = None
        this._childBlocks = [] 
        this._songs = []
        for i, item in enumerate(tracks['items']):
            track = item['track'] 
            this._songs.append(Song(track['name'], track['external_urls']['spotify']))

    def addSong(this, song):
        this._songs.append(song)

    def setExtend(this, parentBlock):
        this._parentBlock = parentBlock
        parentBlock.addChild(this)
    
    def showSongs(this):
        for song in this._songs:
            print(song.getName())
    
    def getSongs(this):
        return this._songs
    
    def addChild(this, childBlock):
        this._childBlocks.append(childBlock)
        for song in childBlock.getSongs():
            if song.getName() not in this._songs:
                this._songs.append(song)