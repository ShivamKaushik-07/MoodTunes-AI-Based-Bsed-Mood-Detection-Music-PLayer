import os
import json
import pygame
import time
import random

# Load configuration file or set default music folder
try:
    with open("config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    print("config.json not found. Using default music folder.")
    config = {"music_folder": "assests/"}


class MusicPlayer:
    def __init__(self):
        # Initialize pygame mixer (used to play music)
        try:
            pygame.mixer.init()
            print("Pygame mixer initialized.")
        except Exception as e:
            print(f"Error initializing pygame mixer: {e}")
            return
        
        # Set up music folder and other variables
        self.music_folder = config.get("music_folder", "assests/")
        self.current_playlist = []  # List of songs in current mood
        self.current_song_index = 0
        self.is_playing = False
        self.current_song = None
        self.playlist = []  # Shuffled list of songs for the mood
        self.current_index = 0  # Index to track which song to play next

    # Load songs from the folder based on mood
    def load_playlist(self, mood):
        mood_folder = os.path.join(self.music_folder, mood)
        
        # Check if the folder exists
        if not os.path.exists(mood_folder):
            print(f"No music folder found for mood: {mood}")
            return False

        # Get all mp3 files
        self.current_playlist = [f for f in os.listdir(mood_folder) if f.endswith(".mp3")]
        if not self.current_playlist:
            print(f"No mp3 files found in {mood_folder}")
            return False

        # Sort songs and reset index
        self.current_playlist.sort()
        self.current_song_index = 0
        return True

    # Start playing music based on detected mood
    def play_music_for_mood(self, mood):
        self.current_mood = mood

        # Load songs for the mood
        if not self.load_playlist(mood):
            return

        # Get the shuffled playlist
        self.playlist = self._get_playlist(mood)
        if not self.playlist:
            print(f"No songs found for mood: {mood}")
            return

        print(f"Loaded {len(self.playlist)} songs for {mood} mood")

        # Start playing the first song
        self._play_next_song()
        self.is_playing = True

        # Set event to detect when a song ends
        pygame.mixer.music.set_endevent(pygame.USEREVENT)

    # Get and shuffle all songs for the given mood
    def _get_playlist(self, mood):
        mood_dir = os.path.join(self.music_folder, mood)

        if not os.path.exists(mood_dir):
            print(f"Warning: No music directory found for {mood}")
            return []

        songs = []
        for file in os.listdir(mood_dir):
            if file.endswith(('.mp3', '.wav')):
                songs.append(os.path.join(mood_dir, file))

        # Shuffle to play in random order
        random.shuffle(songs)
        return songs

    # Play the next song in the playlist
    def _play_next_song(self):
        if not self.playlist:
            return

        # Get the next song
        self.current_song = self.playlist[self.current_index]

        # Load and play the song
        pygame.mixer.music.load(self.current_song)
        pygame.mixer.music.play()

        print(f"Now playing: {os.path.basename(self.current_song)}")

        # Move to the next index, loop back if at end
        self.current_index = (self.current_index + 1) % len(self.playlist)

    # Check if song ended, then play the next one
    def update(self):
        if not pygame.mixer.music.get_busy() and self.playlist:
            self._play_next_song()

    # Stop the music and reset player state
    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.current_playlist = []
        self.current_song_index = 0
        self.current_song = None
        self.playlist = []
        self.current_index = 0
