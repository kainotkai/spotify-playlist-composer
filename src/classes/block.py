class Block:
    def __init__(this):
        this._parentBlock = None
        this._childBlocks = []
        this._songs = []
        this._categories = [] 
    
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