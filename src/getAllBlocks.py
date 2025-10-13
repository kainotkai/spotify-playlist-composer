from classes.block import Block

def getAllBlocks(sp, results):
    blockList = []
    for playlist in results['items']:
        if "BLOCK" in playlist["name"]:
            idk = sp.playlist(playlist['id'], fields='tracks,nest')
            tracks = idk['tracks']
            blockList.append(Block(tracks))
    
    return blockList

