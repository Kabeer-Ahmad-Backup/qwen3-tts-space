# Qwen3 TTS Space

Hugging Face Space for [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS). It launches the official Gradio demo for **Qwen/Qwen3-TTS-12Hz-1.7B-Base**, including zero-shot voice cloning, and listens on port **7860**.

The Space picks CUDA and `float16` when a GPU is available, and falls back to CPU and `float32` otherwise.

## Layout

Everything Hugging Face needs lives in [`hf_space/`](hf_space/):

| File | Role |
| --- | --- |
| `app.py` | Starts `qwen-tts-demo` with the Base model |
| `Dockerfile` | CUDA 12.1 image, PyTorch, flash-attn, and app dependencies |
| `requirements.txt` | Python packages, including `qwen-tts` |

## Models

`app.py` is set to the Base model. Swap `model_id` if you want a different variant:

| Model | What it does |
| --- | --- |
| `Qwen/Qwen3-TTS-12Hz-1.7B-Base` | Preset voices plus zero-shot voice cloning (current default) |
| `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` | Preset voices only |
| `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` | Design a voice from a text description |

## Run with Docker

A GPU is recommended. The 1.7B model is slow on CPU, and the image compiles `flash-attn`, which can take 10–20 minutes.

```bash
cd hf_space
docker build -t qwen3-tts .
docker run --gpus all -p 7860:7860 qwen3-tts
```

Open [http://localhost:7860](http://localhost:7860).

## Deploy on Hugging Face Spaces

1. Create a **Docker** Space.
2. Use the files in `hf_space/` as the Space root (`app.py`, `Dockerfile`, `requirements.txt`).
3. Pick a GPU hardware tier. Free CPU hardware will start, but generation will be slow.

The container already runs as the non-root `user` account Spaces expects and exposes port `7860`.

## Run locally

```bash
cd hf_space
python3 -m venv .venv
source .venv/bin/activate
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
python app.py
```

On a machine without CUDA, install the default CPU builds of `torch` and `torchaudio` instead of the `cu121` index. The app detects that and uses CPU automatically.
