#!/bin/bash
# =============================================
# Chore Me - SiteGround Setup Script
# Run this in the SiteGround terminal after
# uploading files and activating your venv
# =============================================

echo "🚀 Chore Me - SiteGround Setup"
echo "================================"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Dependency install failed. Check errors above."
    exit 1
fi
echo "✅ Dependencies installed"

# Check .env exists
echo ""
if [ ! -f .env ]; then
    echo "⚠️  No .env file found. Creating from example..."
    cp .env.example .env
    echo "❌ STOP: Edit .env with your real values before continuing!"
    echo "   nano .env"
    exit 1
else
    echo "✅ .env file found"
fi

# Create required directories
echo ""
echo "📁 Creating directories..."
mkdir -p app/static/uploads instance
echo "✅ Directories ready"

# Initialize database
echo ""
echo "🗄️  Setting up database..."
python create_db.py
if [ $? -ne 0 ]; then
    echo "❌ Database setup failed. Check your DATABASE_URL in .env"
    exit 1
fi
echo "✅ Database ready"

echo ""
echo "================================"
echo "✅ Setup complete!"
echo ""
echo "Next: Restart your Python app in cPanel → Setup Python App"
echo "Then visit: https://choremenow.com"
echo "================================"
