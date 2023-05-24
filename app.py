import os
import dotenv
import azure.cognitiveservices.speech as speechsdk

# Load the environment file
dotenv.load_dotenv()

# Set your Azure Cognitive Services subscription key and region
subscription_key = os.getenv('AZURE_SUBSCRIPTION_KEY')
region = os.getenv('AZURE_REGION')

# Set the path to the audio file you want to transcribe
audio_file = 'voice.wav'

# Create an audio configuration from the audio file path
audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

# Create a speech configuration with your subscription key and region
speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
speech_config.speech_recognition_language = "th-TH"

# Create a speech recognizer with the speech configuration
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Start recognition process asynchronously
result = speech_recognizer.recognize_once_async().get()

# Check if the recognition was successful
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    # Print the transcribed text
    print("Transcription: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))