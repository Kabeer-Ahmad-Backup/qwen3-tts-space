FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

# Setup basic environment and Python 3.10
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=UTC

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    ffmpeg \
    sox \
    libsox-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --no-cache-dir --upgrade pip

# Create a non-root user that HuggingFace Spaces expects
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR /home/user/app

# Option 1: Install PyTorch FIRST, explicitly.
RUN pip install --no-cache-dir torch torchaudio --index-url https://download.pytorch.org/whl/cu121

# Option 2: Build flash-attn now that torch is installed
# Note: This compilation step may take 10-20 minutes on Hugging Face builder machines.
RUN pip install --no-cache-dir packaging ninja psutil
RUN pip install --no-cache-dir flash-attn --no-build-isolation

# Option 3: Install the rest of our requirements
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our app files
COPY --chown=user . .

# Expose the Gradio port
EXPOSE 7860

# Run the app
CMD ["python3", "app.py"]
