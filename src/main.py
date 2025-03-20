def main():
    print("""Welcome to spotify-ytdlp, a command line script for converting a spotify playlist to individual .mp3 files
This script is mainly for things like burning your spotify playlists to cds for use in systems without bluetooth or spotify
a quick note before the script runs:
          
          1. Please ensure your spotify playlist is public so the script can see it and fetch the tracklist
          2. these playlists are usually very compressed by spotify so may seem smaller when downloaded via them, ensure you have plenty
          of space free on your drive and multiple cds if you plan on burning it
          3. This script may take a long time to run, please ensure a stable internet connection and and your device is plugged in if its a laptop
          """)
    consent = input("Would you like to continue with the script Y/n:")
    while True:
        if consent == "y" or consent == "Y" or consent == "":
            break
        elif consent == "n" or consent == "N":
            exit()
        else:
            consent = input("Would you like to continue with the script Y/n:")
    print("BEGIN!!!")






if __name__ == "__main__":
    main()