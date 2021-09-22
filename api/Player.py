# to use this file in ANY of your projects, public or private, you MUST credit me (github.com/smatman OR woaitsbren) in your README or description. Thank you!

def isShuffle(itunes):
    return itunes.CurrentPlaylist.Shuffle

def toggleShuffle(itunes):
    if isShuffle(itunes):
        itunes.CurrentPlaylist.Shuffle = False
    else:
        itunes.CurrentPlaylist.Shuffle = True


def play(itunes, playlist):
    try:
        itunes.CurrentPlaylist.Shuffle = False
    except:
        itunes.Play()
        itunes.CurrentPlaylist.Shuffle = False
    playlist.PlayFirstTrack()

def shufflePlay(itunes, playlist):
    try:
        itunes.CurrentPlaylist.Shuffle = True
    except:
        itunes.Play()
        itunes.CurrentPlaylist.Shuffle = True
    playlist.PlayFirstTrack()
