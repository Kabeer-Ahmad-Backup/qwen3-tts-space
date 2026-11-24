import sys
import torch
from qwen_tts.cli.demo import main

if __name__ == '__main__':
    # Determine the best device and dtype based on Hugging Face Spaces environment
    # By default, free HF Spaces run on CPU. GPU spaces have CUDA.
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    dtype = "float16" if torch.cuda.is_available() else "float32"
    
    # You can change the model ID here based on what you want to deploy:
    # "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice" (Standard voice only)
    # "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign" (Design your own voice)
    # "Qwen/Qwen3-TTS-12Hz-1.7B-Base" (Includes 0-shot Voice Cloning)
    model_id = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
    
    # Construct the arguments expected by the qwen-tts-demo CLI
    sys.argv = [
        "qwen-tts-demo", 
        model_id, 
        "--device", device,
        "--dtype", dtype,
        "--ip", "0.0.0.0", 
        "--port", "7860" # Standard Hugging Face Spaces Gradio port
    ]
        
    sys.exit(main())
