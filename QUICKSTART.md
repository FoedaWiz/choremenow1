# 🎮 Chore Me - Quick Start Guide

## Installation (3 Steps)

### Step 1: Install Prerequisites (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Step 2: Install App Dependencies
```bash
cd coffeeproject
pip3 install --user -r requirements.txt
```

### Step 3: Configure Environment
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys (optional for basic features)
nano .env
```

## Running the App

```bash
python3 run.py
```

Then open **http://localhost:5000** in your browser.

## First-Time Setup

1. **Register** as a parent at `/auth/register`
   - Username: `parent1`
   - Email: `parent@example.com`
   - Password: `password123`

2. **Add a Kid**
   - Click "Add Kid" button
   - Name: `Alex`
   - Date of Birth: Select a date

3. **Create Your First Chore**
   - Click "Create Chore"
   - Title: `Make your bed`
   - Points: `10`
   - Money: `0.50` ($0.50)
   - XP: `20`

4. **Assign the Chore**
   - Click "Assign to Kid"
   - Select your kid
   - Choose today's date

5. **Simulate Completion & Approval**
   - In the real app, kids would mark chores complete
   - For now, manually mark as completed in the database or approve directly

## API Keys (Optional)

### For AI Features (Gemini)
Get your key at: https://makersuite.google.com/app/apikey

Add to `.env`:
```
GEMINI_API_KEY=your_key_here
```

### For Payments (Stripe)
Get test keys at: https://dashboard.stripe.com/test/apikeys

Add to `.env`:
```
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
```

### Generate Secret Key
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

Add to `.env`:
```
SECRET_KEY=your_generated_key_here
```

## Testing the Gamification

1. **Approve a chore** → Kid earns XP, points, and money
2. **Check kid's profile** → See level progress, badges, streaks
3. **Complete chores on consecutive days** → Build streaks for multipliers
4. **Reach milestones** → Unlock badges automatically
5. **Level up** → Unlock new avatar items

## Features Available

✅ **Working Now:**
- Parent authentication
- Kid management
- Chore creation and assignment
- Approval workflow
- XP/Points/Money tracking
- Level progression
- Badge system
- Streak tracking
- Avatar customization
- Wallet and transaction history

🚧 **Coming Soon:**
- Photo verification
- Kid-facing portal
- Calendar view
- AI chore suggestions
- Real Stripe payments
- Email notifications

## Troubleshooting

### Module not found error
```bash
pip3 install --user -r requirements.txt
```

### Permission denied
```bash
chmod +x setup.sh
```

### Database locked
Stop the app (Ctrl+C) and restart:
```bash
python3 run.py
```

### Reset everything
```bash
rm -rf instance/choreapp.db
python3 run.py
```

## Project Stats

- **759 lines** of Python code
- **13 database models**
- **6 route blueprints**
- **14 HTML templates**
- **11 default badges**
- **16 avatar items**

## Next Steps

1. ✅ Get the app running
2. ✅ Create your family
3. ✅ Add chores and assignments
4. 🔧 Customize the gamification settings
5. 🚀 Add AI features with Gemini
6. 💰 Connect Stripe for real payments

## Support

- Read `README.md` for detailed documentation
- Check `FEATURES.md` for complete feature list
- View `plan.md` in session folder for implementation roadmap

Happy chore questing! 🎯
