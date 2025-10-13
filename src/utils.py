def addBlocksToPlaylist(block , playlist):
    playlist.addBlock(block)

def getTracksByLink(songLinkList):
    trackLinks = []
    for song in songLinkList:
        trackId = song.getLink().split("https://open.spotify.com/track/")[-1].split('?')[0]
        trackLinks.append(f"spotify:track:{trackId}")
    
    return trackLinks


