#!/bin/bash

echo "🎮 Chore Me Setup Script"
echo "=========================="

# Check Python version
echo "Checking Python version..."
python3 --version

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created. Please edit it with your API keys."
else
    echo "✅ .env file already exists."
fi

# Create necessary directories
echo "Creating directories..."
mkdir -p app/static/images app/static/uploads instance

# Install dependencies
echo ""
echo "Installing dependencies..."
echo "Note: You may need to install pip first with:"
echo "  sudo apt install python3-pip python3-venv"
echo ""

# Try to install with user flag if pip is available
if command -v pip3 &> /dev/null; then
    pip3 install --user -r requirements.txt
    echo "✅ Dependencies installed!"
else
    echo "❌ pip3 not found. Please install it first:"
    echo "   sudo apt install python3-pip"
    exit 1
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your API keys:"
echo "   - GEMINI_API_KEY: Get from https://makersuite.google.com/app/apikey"
echo "   - STRIPE_SECRET_KEY: Get from https://dashboard.stripe.com/test/apikeys"
echo "   - SECRET_KEY: Generate a random string"
echo ""
echo "2. Run the app:"
echo "   python3 run.py"
echo ""
echo "3. Open http://localhost:5000 in your browser"
