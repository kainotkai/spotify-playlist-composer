class Song:
    def __init__(self, name, link):
        self._name = name
        self._link = link
        print(self._link)

    def getName(self):
        """
            Returns the name of this Song object 
        """
        return self._name
    
    def getLink(self):
        """
            Returns the spotify - clickable link of a spotify song 
        """
        return self._link
    
    def __repr__(self):
        return str(self._name)


