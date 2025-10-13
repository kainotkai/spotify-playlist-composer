class Song:
    def __init__(this, name, link):
        this._name = name
        this._link = link
        print(this._link)

    def getName(this):
        return this._name
    
    def getLink(this):
        return this._link
    
    def __repr__(self):
        return str(self._name)


