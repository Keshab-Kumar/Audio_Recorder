from audio_recorder_k import AudioRecorder

def test_audio_recording():
    print("Starting test: Recording audio for 3 seconds...")
    
    recorder = AudioRecorder(duration=3, output_file="output/test_recording.wav")
    recorder.record()
    
    print("Test completed: Audio saved as 'output/test_recording.wav'.")

if __name__ == "__main__":
    test_audio_recording()
