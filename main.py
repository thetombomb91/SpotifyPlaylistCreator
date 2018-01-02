import spotipy
import spotipy.util as util
import keyring

scope = 'user-library-read playlist-modify-public'
username = keyring.get_password("system", "SpotifyUsername")
clientId = keyring.get_password("system", "SpotifyClientId")
clientSecret = keyring.get_password("system", "SpotifyClientSecret")


token = util.prompt_for_user_token(username, scope, client_id=clientId, client_secret=clientSecret, redirect_uri='http://localhost/')

# token = token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    artistJson = sp.search('', 1,0,type='artist')
    print(artistJson)

    artistsId = artistJson['artists']['items'][0]['id']
    print(artistsId)


    topTracks = sp.artist_top_tracks(artistsId)
    print(topTracks)

    topTrackList = []
    count = 0
    for track in topTracks['tracks']:
        if count >= 5:
            break
        print(track['name'])
        print(track['uri'])
        topTrackList.append(track['uri'])
        count += 1

    createdPlaylist = sp.search("Crssd Spring 2018", 1, 0, type='playlist')
    print(createdPlaylist)
    sp.user_playlist_add_tracks(username, '33pktSGVpcIPisikK8oc1K', topTrackList)
