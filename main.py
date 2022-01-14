# to use this file in ANY of your projects, public or private, you MUST credit me (github.com/smatman OR woaitsbren) in your README or description. Thank you!

import win32com.client # pip install pywin32
import api.Playlists
import api.Player

itunes = win32com.client.Dispatch("iTunes.Application")

#print(dir(itunes))

print("Now Playing:")
print(itunes.CurrentTrack.Name)
print(itunes.CurrentTrack.Artist)
print(itunes.CurrentTrack.Album)

print("\nPlaylists:")
for playlist in api.Playlists.list(itunes):
    print(playlist)

term = input("\n\nEnter playlist name: ")

search = api.Playlists.searchAndGet(itunes, term)

if search != False:
    api.Player.shufflePlay(itunes, search)
    print(f"Playing {term}.")
else:
    print(f"Could not find {term}.")