#!/bin/bash

echo "======================================"
echo "🎮 Chore Me Installation Guide"
echo "======================================"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! python3 -m pip --version &> /dev/null 2>&1; then
    echo "❌ pip is not installed!"
    echo ""
    echo "To install pip, run:"
    echo "  sudo apt update"
    echo "  sudo apt install python3-pip"
    echo ""
    echo "Then run this script again."
    exit 1
fi

echo "✅ pip is installed"
echo ""

# Install dependencies
echo "Installing dependencies..."
if command -v pip3 &> /dev/null; then
    pip3 install --user -r requirements.txt
else
    python3 -m pip install --user -r requirements.txt
fi

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ All dependencies installed!"
    echo ""
    echo "======================================"
    echo "🚀 Ready to run Chore Me!"
    echo "======================================"
    echo ""
    echo "Start the app with:"
    echo "  python3 run.py"
    echo ""
    echo "Then open in your browser:"
    echo "  http://localhost:5000"
    echo ""
else
    echo ""
    echo "❌ Installation failed. Please check errors above."
    exit 1
fi
