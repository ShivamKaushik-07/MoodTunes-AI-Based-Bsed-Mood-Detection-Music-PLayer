from mood_detector import detect_mood  # Import function to detect mood using webcam
from music_player import MusicPlayer  # Import the MusicPlayer class
import pygame
import time

def main():
    print("Starting MoodTunes - AI Mood Detection Music Player")
    print("Camera will open automatically...")

    # Initialize pygame and its mixer for playing music
    pygame.init()
    pygame.mixer.init()

    # Detect the user's mood using the webcam
    mood = detect_mood()
    print(f"Detected mood: {mood}")

    # Create the music player object and play songs for the detected mood
    player = MusicPlayer()
    player.play_music_for_mood(mood)

    print("\nPlaylist is now playing. Press Ctrl+C to stop.")
    print("Songs will play in sequence and loop continuously.")
    
    try:
        # Keep checking if the current song finished to play the next one
        while True:
            player.update()  # This will check and play next song if needed
            time.sleep(0.1)  # Small delay to avoid using too much CPU
            
    except KeyboardInterrupt:
        # When user presses Ctrl+C, stop the music and exit the program
        print("\nStopping music and exiting...")
        player.stop()
        pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()
