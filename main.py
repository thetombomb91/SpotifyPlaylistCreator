import spotipy
import spotipy.util as util
import keyring


def get_spotify_token():
    global token
    scope = 'user-library-read playlist-modify-public'
    username = keyring.get_password("system", "SpotifyUsername")
    clientId = keyring.get_password("system", "SpotifyClientId")
    clientSecret = keyring.get_password("system", "SpotifyClientSecret")
    token = util.prompt_for_user_token(username, scope, client_id=clientId, client_secret=clientSecret,
                                       redirect_uri='http://localhost/')
    return token





def request_list_of_artists():
    artists_separated_by_commas = input("Enter comma separated list of artists: ")
    formatted_list_of_artists = artists_separated_by_commas.split(',')
    return formatted_list_of_artists


def get_list_of_top_tracks(artist_id, number_of_tracks_to_request=5):
    all_top_tracks = sp.artist_top_tracks(artist_id)
    top_track_list = []
    count = 0
    for track in all_top_tracks['tracks']:
        if count >= number_of_tracks_to_request:
            break
        top_track_list.append(track['uri'])
        count += 1

    return top_track_list


def get_artist_id(artist):
    artistJson = sp.search(artist, 1, 0, type='artist')
    artist_id = artistJson['artists']['items'][0]['id']
    return artist_id




spotify_token = get_spotify_token()

if spotify_token:
    sp = spotipy.Spotify(auth=spotify_token)

    list_of_artists = request_list_of_artists()

    for artist in list_of_artists:
        artist_id = get_artist_id()
        track_list = get_list_of_top_tracks(artist_id)
        print("Tracks to be added " + track_list + " from artist " + artist)


    createdPlaylist = sp.search("TestPlaylist", 1, 0, type='playlist')
    print(createdPlaylist)
    # sp.user_playlist_add_tracks(username, '33pktSGVpcIPisikK8oc1K', topTrackList)


