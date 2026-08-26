#!/bin/bash

set -e

MODEL_DIR="model"
MODEL_FILE="Llama-3.2-3B-Instruct-Q4_K_M.gguf"
MODEL_URL="https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf?download=true"

mkdir -p "$MODEL_DIR"

if [ -f "$MODEL_DIR/$MODEL_FILE" ]; then
    echo "Model already exists."
    exit 0
fi

echo "Downloading Llama 3.2 3B Instruct Q4_K_M..."

curl -L "$MODEL_URL" -o "$MODEL_DIR/$MODEL_FILE"

echo "Model downloaded successfully."