import spotipy
import yt_dlp
from spotipy.oauth2 import SpotifyClientCredentials

def main():
    print("""Welcome to spotify-ytdlp, a command line script for converting a spotify playlist to individual .mp3 files
This script is mainly for things like burning your spotify playlists to cds for use in systems without bluetooth or spotify
a quick note before the script runs:
          
          1. Please ensure your spotify playlist is public so the script can see it and fetch the tracklist
          2. these playlists are usually very compressed by spotify so may seem smaller when downloaded via them, ensure you have plenty
          of space free on your drive and multiple cds if you plan on burning it
          3. This script requires you to create your own developer app on spotify for developers, can be found at https://developer.spotify.com/dashboard
          """)
    consent = input("Would you like to continue with the script Y/n:")
    while True:
        if consent == "y" or consent == "Y" or consent == "":
            break
        elif consent == "n" or consent == "N":
            exit()
        else:
            consent = input("Would you like to continue with the script Y/n:")
        
    clientId = input("please input your client id found at https://developer.spotify.com/dashboard in the settings page for your specific app: ")
    clientSecret = input("please input your client secret found at https://developer.spotify.com/dashboard in the settings page for your specific app: ")

    auth_manager = SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    link = input("input the link to your spotify playlist: ")
    playlist = sp.playlist_tracks(link)
    tracks = playlist['items']
    while playlist['next']:
        playlist = sp.next(playlist)
        tracks.extend(playlist['items'])
    for i in tracks:
        p = i["track"]
        a = p["artists"]
        a = a[0]
        print(f"{a["name"]} - {p["name"]}")
    
    consent = input("Does this look correct? Y/n:")
    while True:
        if consent == "y" or consent == "Y" or consent == "":
            break
        elif consent == "n" or consent == "N":
            exit()
        else:
            consent = input("Does this look correct? Y/n:")
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': 'output/%(title)s.%(ext)s',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for i in tracks:
            p = i["track"]
            a = p["artists"]
            a = a[0]
            error_code = ydl.download(f"ytsearch:{a["name"]} - {p["name"]}")

    


    






if __name__ == "__main__":
    main()