from openai import OpenAI
import io

client = OpenAI()

def process_audio(audio_data) -> str:
    """
    Transcribes speech from an audio file (bytes or file-like object) using OpenAI's API.
    audio_data: bytes or file-like object (e.g., io.BytesIO)
    """
    try:
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_data,
            response_format="text"
        )
        return transcription.strip()
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return ""
