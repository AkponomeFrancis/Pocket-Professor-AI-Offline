#!/usr/bin/env bash
set -e

MODEL_DIR="model"
MODEL_FILE="Llama-3.2-3B-Instruct-Q4_K_M.gguf"
MODEL_URL="https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf?download=true"
EXPECTED_SHA256="6C1A2B41161032677BE168D354123594C0E6E67D2B9227C84F296AD037C728FF"

mkdir -p "$MODEL_DIR"

MODEL_PATH="$MODEL_DIR/$MODEL_FILE"

if [ -f "$MODEL_PATH" ]; then
    echo "Model already exists."
else
    echo "Downloading Llama 3.2 3B Instruct Q4_K_M..."
    curl -L --fail --retry 3 "$MODEL_URL" -o "$MODEL_PATH"
    echo "Model downloaded successfully."
fi

echo "Verifying model checksum..."

if command -v sha256sum >/dev/null 2>&1; then
    ACTUAL_SHA256=$(sha256sum "$MODEL_PATH" | awk '{print $1}')
elif command -v shasum >/dev/null 2>&1; then
    ACTUAL_SHA256=$(shasum -a 256 "$MODEL_PATH" | awk '{print $1}')
else
    echo "ERROR: No SHA-256 utility found."
    exit 1
fi

if [ "$ACTUAL_SHA256" != "$EXPECTED_SHA256" ]; then
    echo "ERROR: Model checksum does not match."
    echo "Expected: $EXPECTED_SHA256"
    echo "Actual:   $ACTUAL_SHA256"
    exit 1
fi

echo "Model checksum verified successfully."
echo "Pocket Professor AI model is ready."