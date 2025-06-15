import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from mood_detector import detect_mood  # Import the mood detection function
from music_player import MusicPlayer  # Import the music player class

# Main class for GUI application
class MoodTunesApp:
    def __init__(self):
        # Create application and main window
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("MoodTunes - AI Mood Detection Music Player")

        # Create a label and button
        self.label = QLabel("Press 'Detect Mood' to start")
        self.button = QPushButton("Detect Mood")

        # Connect button click to mood detection and music playing
        self.button.clicked.connect(self.detect_and_play)

        # Layout for window elements
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.window.setLayout(layout)

        # Create music player object
        self.player = MusicPlayer()

    def detect_and_play(self):
        # When button is clicked, detect mood using webcam
        mood = detect_mood()

        # Update the label to show the detected mood
        self.label.setText(f"Detected Mood: {mood}")

        # Play the music based on detected mood
        self.player.play_music_for_mood(mood)

    def run(self):
        # Show the application window and run the app loop
        self.window.show()
        sys.exit(self.app.exec_())
