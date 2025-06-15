# 🎵 MoodTunes – AI-Based Mood Detection Music Player

MoodTunes is an intelligent music player that uses your webcam to detect your facial emotion and automatically plays a playlist that matches your mood. It combines AI-powered emotion recognition with a personalized music experience.

## 🔥 Features

- 🎥 Real-time mood detection using webcam and DeepFace
- 😄 Detects emotions like Happy, Sad, Angry, and Afraid
- 🎶 Automatically plays songs based on your mood
- 🔁 Continuously loops songs from the detected mood playlist
- 🖼 Simple UI using OpenCV to show detection status

## 🧠 How It Works

1. The app captures your face using your webcam.
2. It uses the DeepFace library to detect emotions.
3. Based on the dominant emotion (happy, sad, angry, or afraid), it loads the corresponding playlist.
4. Songs are played one by one and looped for continuous mood-based playback.

## 📁 Folder Structure

MoodTunes/
├── assets/
│ ├── happy/ # Songs for happy mood
│ ├── sad/ # Songs for sad mood
│ ├── angry/ # Songs for angry mood
│ └── afraid/ # Songs for afraid mood
├── mood_detector.py # Handles webcam and emotion detection
├── music_player.py # Manages music playback logic
├── main.py # Main script to run the app
├── config.json # Path configuration for music folder
├── README.md # Project documentation
└── .gitignore # Files/folders to ignore in Git

markdown
Copy
Edit

## ⚙️ Requirements

- Python 3.8+
- Libraries:
  - `deepface`
  - `pygame`
  - `opencv-python`
  - `numpy`

### Install dependencies:
```bash
pip install -r requirements.txt
🚀 Usage
Run the project:

bash
Copy
Edit
python main.py
Make sure your webcam is connected. The app will analyze your face, detect your mood, and start playing songs from the matching playlist.

🧾 Notes
Add .mp3 files inside assets/happy, assets/sad, etc.

You can customize or add more moods by updating the folder structure and emotion map.

❌ .gitignore Suggestions
You should ignore:

markdown
Copy
Edit
__pycache__/
*.pyc
assets/
mood_icons/
📸 Screenshot

🤖 Built With
DeepFace for emotion detection

Pygame for audio playback

OpenCV for webcam support

🧑‍💻 Author
Shivam Kaushik
🔗 GitHub

