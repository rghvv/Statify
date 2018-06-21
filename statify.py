import sys
import spotipy
import spotipy.util as util
import collections
import pprint

scopes = 'user-top-read playlist-modify-public'
ranges = ['short_term', 'medium_term', 'long_term']

def add_user_playlist(user, name, username, recommended_tracks, public = True):
    spotify = spotipy.Spotify(auth=token)
    created_playlist = spotify.user_playlist_create(user = spotify.me()['id'],
                                                                    name = 'Statify Recommendation Playlist',
                                                                    public = True)
    spotify.user_playlist_add_tracks(user = spotify.me()['id'],
                                                 playlist_id = created_playlist['id'],
                                                 tracks = recommended_tracks)
    print("\nPlaylist saved")

def get_top_tracks():
    for t_range in ranges:
        print("\nTOP TRACKS - " + t_range.upper() + '\n')
        top_tracks = spotify.current_user_top_tracks(limit=50, time_range=t_range)
        index = 1
        for track in top_tracks['items']:
            print(str(index) + ". " + track['artists'][0]['name'] + " - " + track['album']['name'] + " - " + track['name'])
            index += 1

def get_top_artists():
    pops = []
    for t_range in ranges:
        print("\nTOP ARTISTS - " + t_range.upper() + '\n')
        top_artists = spotify.current_user_top_artists(limit=50, time_range=t_range)
        index = 1
        for artist in top_artists['items']:
            print(str(index) + ". " + artist['name'] + ", Popularity: " + str(artist['popularity']))
            index += 1
            pops.append(artist['popularity'])
        avg_pop = 0
        for score in pops:
            avg_pop += score
        avg_pop = avg_pop / len(pops)
        print("\nAVERAGE POPULARITY - " + str(avg_pop))

def get_genres_for_recommendations():
    unordered_recs = dict()
    for t_range in ranges:
        top_artists = spotify.current_user_top_artists(limit=50, time_range = t_range)
        i = 0
        while i < len(top_artists):
            for genre in top_artists['items'][i]['genres']:
                if genre not in unordered_recs.keys():
                    unordered_recs[genre] = 1
                else:
                    unordered_recs[genre] += 1
            i += 1
    genres_from_user = [genre for genre in sorted(unordered_recs, key = unordered_recs.get, reverse=True)]
    acceptable_genres = spotify.recommendation_genre_seeds()['genres']
    for genre in genres_from_user:
        if genre not in acceptable_genres:
            genres_from_user.remove(genre)
    return genres_from_user

def get_recommendations():
    genres_from_user = get_genres_for_recommendations()
    recommended_tracks = []
    for track in spotify.recommendations(seed_genres=genres_from_user[0:5], limit=50, target_popularity = 70)['tracks']:
        recommended_tracks.append(track['id'])
    return recommended_tracks


if __name__=='__main__':
    #Get username
    username = sys.argv[1]
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Need to specify username\nUsage: python statify.py [username]")
        sys.exit()

    #Prompt for user permissions
    token = util.prompt_for_user_token(username, scopes)
    if token:
        spotify = spotipy.Spotify(auth=token)

        user = spotify.current_user()
        if user['display_name']:
            name = user['display_name']
        else:
            name = user['id']

        print("\nHello, " + name)

        get_top_tracks()

        get_top_artists()

        while True:
            add_playlist = input("\nCreate playlist of recommended tracks? (y/n)   ")
            if add_playlist.lower() in ['y', 'n']:
                break
            else:
                print("Invalid choice, try again.")

        if add_playlist == 'y':
            recommended_tracks = get_recommendations()
            add_user_playlist(user = user['id'],
                                      name = 'Statify Recommendation Playlist',
                                      public = True,
                                      username = username,
                                      recommended_tracks = recommended_tracks)

    else:
        print("Failed to fetch token for", name)
