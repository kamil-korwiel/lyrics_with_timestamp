import torch
from pathlib import Path
import whisper_timestamped
import json



def main():
    if torch.cuda.is_available():
        print(f"CUDA is available! Device: {torch.cuda.get_device_name(0)}")
        
        path_file_audio = Path("./MacDeMarco - Preoccupied (vocals).wav")
        model = whisper_timestamped.load_model("small", device="cuda")  # Choose from tiny, base, small, medium, large
        result = model.transcribe(str(path_file_audio), word_timestamps=True)

        path_file_json = Path('./gen_lyrics.json')
        with open(path_file_json,'w') as file:
            file.write(json.dumps(result, indent=4))
        
        # for segment in result['segments']:
        #     for word in segment['words']:
        #         print(f"{word['word']} [{word['start']:.2f} - {word['end']:.2f}]  conf:{word['probability']}")

    else:
        print("CUDA is not available on this platform.")

if __name__ == "__main__":
    main()