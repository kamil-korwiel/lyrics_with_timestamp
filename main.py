import torch
from pathlib import Path



def main():
    if torch.cuda.is_available():
        print(f"CUDA is available! Device: {torch.cuda.get_device_name(0)}")

    else:
        print("CUDA is not available on this platform.")

if __name__ == "__main__":
    main()