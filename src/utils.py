from classes.block import Block 

def addBlocksToPlaylist(block , playlist):
    playlist.addBlock(block)

def getTracksByLink(songLinkList):
    trackLinks = []
    for song in songLinkList:
        trackId = song.get_link().split("https://open.spotify.com/track/")[-1].split('?')[0]
        trackLinks.append(f"spotify:track:{trackId}")
    
    return trackLinks

def getAllBlocks(sp, results):
    blockList = []
    for playlist in results['items']:
        if "BLOCK" in playlist["name"]:
            playlistInfo= sp.playlist(playlist['id'], fields='tracks,nest')
            tracks = playlistInfo['tracks']
            blockList.append(Block(tracks, playlist['description']))
    
    return blockList




