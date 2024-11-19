import speech_recognition as sr
from moviepy.editor import VideoFileClip, concatenate_videoclips
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
import IPython.display as display

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

def tokenize_text(text):
    tokens = word_tokenize(text.lower())
    print("Tokens:", tokens)
    return tokens

# Mock database with video file paths (replace these with actual paths in your project)
gesture_videos = {
    "why": "why.mp4",
    "long": "long.mp4",
    "play": "play.mp4",
    "what": "what.mp4",
    "time": "time.mp4",
    "bus": "bus.mp4",
    "food": "food.mp4",
    "give": "give.mp4",
    "goodbye": "goodbye.mp4",
    "hello": "hello.mp4",
    "me": "me.mp4",
    "please": "please.mp4",
    "water": "water.mp4",
    "where": "where.mp4",
    "which": "which.mp4",
    "your": "your.mp4"
}

def retrieve_gesture_videos(tokens):
    video_clips = []
    for token in tokens:
        if token in gesture_videos:
            clip = VideoFileClip(gesture_videos[token])
            video_clips.append(clip)
        else:
            print(f"No gesture video found for: {token}")
    return video_clips


def create_final_video(video_clips):
    if not video_clips:
        print("No video clips to concatenate.")
        return None
    final_video = concatenate_videoclips(video_clips, method="compose")
    final_video_path = "final_output.mp4"
    final_video.write_videofile(final_video_path)
    return final_video_path

def create_final_video(video_clips):
    if not video_clips:
        print("No video clips to concatenate.")
        return None
    final_video = concatenate_videoclips(video_clips, method="compose")
    final_video_path = "final_output.mp4"
    final_video.write_videofile(final_video_path)
    return final_video_path

def display_video(video_path):
    display.Video(video_path, embed=True)

# Get input from speech
input_text = speech_to_text()

# If no speech input is detected, exit the program
if not input_text:
    print("No valid speech input detected. Exiting.")
    exit()

# Tokenize text
tokens = tokenize_text(input_text)

# Retrieve gesture videos
video_clips = retrieve_gesture_videos(tokens)

# Create final video
final_video_path = create_final_video(video_clips)

# Display final video
if final_video_path:
    display_video(final_video_path)
