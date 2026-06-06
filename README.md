# Chore App - Gamified Chore Tracker for Families

A mobile-friendly web application that helps parents manage household chores for their children with gamification, real money allowances, and AI-powered features.

## Features

🎮 **Gamification System**
- XP-based level progression
- Unlockable badges and achievements
- Streak tracking with multipliers
- Avatar customization with cosmetic items

💰 **Three-Currency Economy**
- **XP**: Level up and unlock items (permanent progression)
- **Points**: Spend on rewards from catalog
- **Money**: Real allowance payments via Stripe

📋 **Chore Management**
- Create and assign chores to kids
- Recurring chores (daily/weekly)
- Photo verification of completed work
- Parent approval system

📅 **Calendar & Scheduling**
- View upcoming chores
- Track completion history
- Recurring task automation

🤖 **AI Integration** (Gemini)
- Age-appropriate chore suggestions
- Smart reward recommendations
- Personalized scheduling advice

📱 **Mobile App (Android/TWA)**
- Built with Google Bubblewrap
- Home screen installation (PWA)
- Full-screen Trusted Web Activity (TWA) support

## Quick Start

### 1. Install Python and pip (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Run Setup Script

```bash
cd coffeeproject
chmod +x setup.sh
./setup.sh
```

### 3. Configure API Keys

Edit `.env` file with your API keys:

```bash
# Required for AI features
GEMINI_API_KEY=your_gemini_api_key_here

# Required for payments
STRIPE_SECRET_KEY=your_stripe_secret_key_here
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key_here

# Generate a random secret key
SECRET_KEY=your_random_secret_key_here
```

**Get API Keys:**
- Gemini: https://makersuite.google.com/app/apikey
- Stripe: https://dashboard.stripe.com/test/apikeys

### 4. Run the App

```bash
python3 run.py
```

### 5. Access the App

Open http://localhost:5000 in your browser.

## Android App (Bubblewrap)

To build the Android `.apk` or `.aab`:

1. **Install Bubblewrap CLI**:
   ```bash
   npm install -g @bubblewrap/cli
   ```

2. **Build for Production**:
   Ensure your site is live at `www.choremenow.com`, then:
   ```bash
   bubblewrap build
   ```

3. **Build for Local Testing** (if site is not live):
   ```bash
   # Using ngrok
   ngrok http 5000
   # Update twa-manifest.json with the ngrok URL, then:
   bubblewrap build
   ```

4. **Remove URL Bar**:
   After the build, copy the SHA-256 fingerprint into `app/static/.well-known/assetlinks.json`.

## Manual Setup (Alternative)

If the setup script doesn't work:

```bash
# Install dependencies
pip3 install --user -r requirements.txt

# Create directories
mkdir -p app/static/images app/static/uploads instance

# Copy environment file
cp .env.example .env
# Then edit .env with your API keys

# Run the app
python3 run.py
```

## Usage

1. **Register** a parent account at `/auth/register`
2. **Add kids** to your family
3. **Create chores** with points, money, and XP rewards
4. **Assign chores** to your kids with due dates
5. **Approve completions** to award rewards
6. **Track progress** with the gamification system!

## Database

SQLite database will be created automatically on first run at `instance/choreapp.db`.

## Project Structure

```
coffeeproject/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── routes/              # Route blueprints
│   ├── templates/           # HTML templates
│   ├── static/              # CSS, JS, images, manifest.json, sw.js
│   └── utils/               # Helper functions
├── run.py                   # Application entry point
├── twa-manifest.json        # Android TWA configuration
├── requirements.txt         # Python dependencies
└── setup.sh                 # Setup script
```

## Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Database**: SQLite
- **Payments**: Stripe API
- **AI**: Google Gemini API
- **PWA**: Service Workers, Web Manifest
- **TWA**: Google Bubblewrap

## License

MIT
