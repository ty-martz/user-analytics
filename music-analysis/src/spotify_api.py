import requests
import base64

def get_spotify_token(client_id, client_secret):
    """Get authorization token for Spotify API"""
    url = "https://accounts.spotify.com/api/token"
    payload = {'grant_type': 'client_credentials'}
    response = requests.post(url, auth=(client_id, client_secret), data=payload)
    token = response.json()['access_token']
    return token


def get_top_artists(spotify_token, num_artists):
    """Get a list of the top artists on Spotify"""
    url = f"https://api.spotify.com/v1/artists?limit={num_artists}"
    headers = {'Authorization': f'Bearer {spotify_token}'}
    response = requests.get(url, headers=headers)
    top_artists = response.json()['artists']
    return top_artists
  

def get_artist_top_tracks(artist_id, n, access_token):
    # set up authentication
    client_id = '<your_client_id>'
    client_secret = '<your_client_secret>'
    auth_header = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')
    
    headers = {'Authorization': 'Bearer ' + access_token}
    
    # get artist's top tracks
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
    params = {'market': 'US'}
    response = requests.get(url, headers=headers, params=params)
    response_json = response.json()
    
    # extract top tracks
    top_tracks = []
    for track in response_json['tracks'][:n]:
        track_name = track['name']
        track_id = track['id']
        top_tracks.append((track_name, track_id))
        
    return top_tracks

  

 if __name__ == '__main__':
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    num_artists = 10000
    n_songs = 10

    spotify_token = get_spotify_token(client_id, client_secret)
    top_artists = get_top_artists(spotify_token, num_artists)

    print(top_artists)
    
    artist_id = top_artists[0]
    top_tracks = get_artist_top_tracks(artist_id, n_songs, spotify_token)
    print(top_tracks)
