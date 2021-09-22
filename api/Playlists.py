# to use this file in ANY of your projects, public or private, you MUST credit me (github.com/smatman OR woaitsbren) in your README or description. Thank you!

def list(itunes):
    data = []
    for i in range(itunes.LibrarySource.Playlists.Count):
        data.append(itunes.LibrarySource.Playlists.Item(i+1).Name)
    return data

def search(itunes, term: str):
    playlists = list(itunes)
    data = []
    for i in range(len(playlists)):
        if playlists[i] == term:
            data.append(True)
            data.append(i+1)
            return data
    if data == []:
        data.append(False)
        data.append(0)
        return data

def get(itunes, number):
    return itunes.LibrarySource.Playlists.Item(number)

def searchAndGet(itunes, term: str):
    data = search(itunes, term)
    if data[0]:
        return get(itunes, data[1])
    else:
        return False