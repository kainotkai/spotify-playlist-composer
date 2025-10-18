class Song:
    def __init__(self, name, link):
        self._name = name
        self._link = link
        print(f"Reading: {name}")

    def get_name(self):
        """
            Returns the name of this Song object 
        """
        return self._name
    
    def get_link(self):
        """
            Returns the spotify - clickable link of a spotify song 
        """
        return self._link.strip()
    
    def __repr__(self):
        return str(self._name)
    
    def __hash__(self):
        return hash(self._name + self._link)
    
    def __eq__(self, other):
        if isinstance(other, Song):
            return self._name == other._name and self._link == other._link


