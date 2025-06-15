import cv2
import numpy as np
from deepface import DeepFace
import time
from music_player import MusicPlayer
import pygame

def detect_mood():
    print("Starting automatic emotion detection...")
    
    # Start webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Cannot access webcam.")
        return "neutral"

    print("Camera opened successfully!")
    print("Detecting emotion automatically...")

    # Font settings for displaying text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (0, 255, 0)
    thickness = 2

    # Create music player object
    player = MusicPlayer()

    # Initialize pygame mixer (for sound)
    pygame.mixer.init()

    # Counters and time tracking
    emotion_count = 0
    required_detections = 3  # how many times same emotion should appear to confirm
    last_valid_emotion = None
    detection_start_time = time.time()
    max_detection_time = 15  # maximum 15 seconds for detection

    while True:
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        # Check if time exceeded
        time_elapsed = time.time() - detection_start_time
        if time_elapsed > max_detection_time:
            print("No stable emotion detected within time limit.")
            break

        try:
            # Detect emotion from frame
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

            # Extract emotion and face region
            emotion = result[0]['dominant_emotion'] if isinstance(result, list) else result['dominant_emotion']
            region = result[0].get('region', None) if isinstance(result, list) else result.get('region', None)
            current_emotion = emotion.lower()

            # Confirm valid emotion (not neutral/unknown)
            if current_emotion not in ["neutral", "unknown", "none"]:
                if current_emotion == last_valid_emotion:
                    emotion_count += 1
                else:
                    emotion_count = 1
                    last_valid_emotion = current_emotion
            else:
                emotion_count = 0
                last_valid_emotion = None

        except Exception as e:
            print(f"Emotion detection error: {e}")
            emotion_count = 0
            last_valid_emotion = None
            current_emotion = "neutral"
            region = None

        # Draw face rectangle and emotion label
        if region and all(k in region for k in ('x', 'y', 'w', 'h')):
            x, y, w, h = region['x'], region['y'], region['w'], region['h']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, current_emotion, (x, y - 10), font, font_scale, color, thickness)
        else:
            cv2.putText(frame, "No face detected", (30, 50), font, font_scale, (0, 0, 255), thickness)

        # Display detection status and timer
        status_text = f"Detecting emotion... ({emotion_count}/{required_detections})"
        cv2.putText(frame, status_text, (30, 80), font, font_scale, (255, 255, 255), thickness)

        time_remaining = max(0, max_detection_time - time_elapsed)
        cv2.putText(frame, f"Time: {time_remaining:.1f}s", (30, 110), font, font_scale, (255, 255, 255), thickness)

        # Show video feed
        cv2.imshow('Real-Time Mood Detection', frame)

        # If enough detections of the same emotion, break the loop
        if emotion_count >= required_detections:
            print(f"Detected emotion: {last_valid_emotion}")
            time.sleep(1)
            break

        # Press 'q' to quit manually
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting detection early.")
            break

    # Release webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

    # Map detected emotion to your music folder names
    emotion_map = {
        "happy": "happy",
        "sad": "sad",
        "angry": "angry",
        "fear": "Afraid",
        "disgust": "neutral",
        "surprise": "neutral",
        "neutral": "neutral"
    }

    mapped_emotion = emotion_map.get(last_valid_emotion, "neutral")
    print(f"Raw detected emotion: {last_valid_emotion}")
    print(f"Mapped to folder: {mapped_emotion}")
    return mapped_emotion
