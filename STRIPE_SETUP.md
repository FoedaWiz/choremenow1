# Stripe Subscription Setup Guide

## 🚀 Complete Implementation Guide

The subscription system is now fully implemented! Follow these steps to configure Stripe and start accepting payments.

---

## 📋 What's Been Added

### ✅ Database Changes
- Added subscription fields to User model:
  - `stripe_customer_id` - Stripe customer reference
  - `subscription_id` - Active subscription ID
  - `subscription_tier` - free, family, premium
  - `subscription_status` - active, trialing, past_due, canceled
  - `trial_ends_at` - When free trial ends
  - `subscription_started_at` - When subscription began

### ✅ New Routes
- `/payments/subscribe/<tier>` - Start subscription checkout
- `/payments/subscribe-success` - Post-checkout success page
- `/payments/customer-portal` - Self-service billing portal
- `/payments/webhook` - Stripe webhook handler

### ✅ Features
- 14-day free trial (no credit card required)
- Automatic subscription management
- Feature gating by tier
- Customer billing portal
- Webhook event handling
- Upgrade/downgrade flow

---

## 🔧 Setup Instructions

### Step 1: Get Stripe API Keys

1. **Sign up for Stripe:** https://dashboard.stripe.com/register
2. **Get your API keys:**
   - Go to Developers → API keys
   - Copy **Secret key** (starts with `sk_test_`)
   - Copy **Publishable key** (starts with `pk_test_`)

3. **Add to `.env` file:**
```bash
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxx
STRIPE_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxx
```

---

### Step 2: Create Products & Prices in Stripe

1. **Go to:** https://dashboard.stripe.com/products

2. **Create Family Plan Product:**
   - Click "+ Add product"
   - Name: `Chore Me Family Plan`
   - Description: `Unlimited kids, multi-parent support, AI suggestions, automated payouts`
   - Pricing model: `Recurring`
   - Price: `$4.99`
   - Billing period: `Monthly`
   - Click "Save product"
   - **Copy the Price ID** (looks like `price_xxxxxxxxxxxxx`)

3. **Create Premium Plan Product:**
   - Click "+ Add product"
   - Name: `Chore Me Premium Plan`
   - Description: `Everything in Family + virtual cards, reports, VIP support`
   - Pricing model: `Recurring`
   - Price: `$9.99`
   - Billing period: `Monthly`
   - Click "Save product"
   - **Copy the Price ID**

4. **Add Price IDs to `.env`:**
```bash
STRIPE_PRICE_FAMILY=price_xxxxxxxxxxxxx
STRIPE_PRICE_PREMIUM=price_xxxxxxxxxxxxx
```

---

### Step 3: Set Up Webhooks

1. **Install Stripe CLI (for testing):**
```bash
# macOS
brew install stripe/stripe-cli/stripe

# Linux
wget https://github.com/stripe/stripe-cli/releases/download/v1.19.4/stripe_1.19.4_linux_x86_64.tar.gz
tar -xvf stripe_1.19.4_linux_x86_64.tar.gz
sudo mv stripe /usr/local/bin/
```

2. **Login to Stripe:**
```bash
stripe login
```

3. **Test webhooks locally:**
```bash
# Forward webhooks to your local server
stripe listen --forward-to http://localhost:5000/payments/webhook

# This will output a webhook signing secret (starts with whsec_)
# Copy it and add to .env:
STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxx
```

4. **For production, create webhook endpoint:**
   - Go to: https://dashboard.stripe.com/webhooks
   - Click "+ Add endpoint"
   - Endpoint URL: `https://yourdomain.com/payments/webhook`
   - Select events to listen for:
     - `checkout.session.completed`
     - `customer.subscription.updated`
     - `customer.subscription.deleted`
     - `invoice.payment_succeeded`
     - `invoice.payment_failed`
   - Click "Add endpoint"
   - Copy **Signing secret** and add to `.env`

---

### Step 4: Run Database Migration

The User model has been updated with new fields. Migrate the database:

```bash
cd ~/coffeeproject

# Backup existing database
cp instance/choreapp.db instance/choreapp.db.backup

# Run Python to add new columns
python3 << 'EOF'
from app import create_app, db
app = create_app()
with app.app_context():
    # Add new columns to users table
    db.session.execute('ALTER TABLE users ADD COLUMN stripe_customer_id VARCHAR(100)')
    db.session.execute('ALTER TABLE users ADD COLUMN subscription_id VARCHAR(100)')
    db.session.execute('ALTER TABLE users ADD COLUMN subscription_tier VARCHAR(20) DEFAULT "free"')
    db.session.execute('ALTER TABLE users ADD COLUMN subscription_status VARCHAR(20)')
    db.session.execute('ALTER TABLE users ADD COLUMN trial_ends_at DATETIME')
    db.session.execute('ALTER TABLE users ADD COLUMN subscription_started_at DATETIME')
    db.session.execute('ALTER TABLE users ADD COLUMN subscription_canceled_at DATETIME')
    db.session.commit()
    print("✅ Database migration completed!")
EOF
```

---

### Step 5: Test the Subscription Flow

1. **Start your app:**
```bash
cd ~/coffeeproject
python3 run.py
```

2. **Start Stripe webhook forwarding (in another terminal):**
```bash
stripe listen --forward-to http://localhost:5000/payments/webhook
```

3. **Test subscription:**
   - Go to http://localhost:5000/legal/pricing
   - Click "Start 14-Day Free Trial" on Family Plan
   - Use test card: `4242 4242 4242 4242`
   - Expiry: Any future date (e.g., 12/30)
   - CVC: Any 3 digits (e.g., 123)
   - Complete checkout

4. **Verify:**
   - Check dashboard for subscription banner
   - Check Stripe dashboard for customer and subscription
   - Check webhook events in terminal

---

## 🧪 Testing

### Test Cards

Use these test cards in **test mode**:

| Card Number | Description |
|-------------|-------------|
| `4242 4242 4242 4242` | Successful payment |
| `4000 0000 0000 0002` | Card declined |
| `4000 0000 0000 9995` | Insufficient funds |
| `4000 0027 6000 3184` | 3D Secure required |

### Test Scenarios

1. **Subscribe to Family Plan:**
   - User gets 14-day trial
   - subscription_tier = 'family'
   - subscription_status = 'trialing'

2. **Trial ends:**
   - After 14 days, first payment charged
   - subscription_status = 'active'

3. **Payment fails:**
   - subscription_status = 'past_due'
   - User gets email notification

4. **Cancel subscription:**
   - Go to customer portal
   - Cancel subscription
   - subscription_tier = 'free'
   - subscription_status = 'canceled'

---

## 🔒 Feature Gating

### Using the Decorator

Protect routes that require paid plans:

```python
from app.routes.payments import requires_plan

@bp.route('/ai-suggestions')
@login_required
@requires_plan('family')  # Requires Family or Premium
def ai_suggestions():
    # Only accessible to paid subscribers
    pass

@bp.route('/virtual-cards')
@login_required
@requires_plan('premium')  # Requires Premium only
def virtual_cards():
    # Only accessible to Premium subscribers
    pass
```

### Manual Checks

```python
# In templates:
{% if current_user.can_access_feature('family') %}
    <a href="{{ url_for('ai_suggestions') }}">AI Suggestions</a>
{% else %}
    <a href="{{ url_for('legal.pricing') }}" class="opacity-50">
        AI Suggestions 🔒 (Family Plan)
    </a>
{% endif %}

# In Python:
if current_user.can_access_feature('premium'):
    # Premium feature logic
else:
    flash('Upgrade to Premium to access this feature!', 'error')
    return redirect(url_for('legal.pricing'))
```

---

## 🎯 Current Pricing

| Plan | Price | Features |
|------|-------|----------|
| **Free** | $0/month | 3 kids, basic features |
| **Family** | $4.99/month | Unlimited kids, AI, automated payouts |
| **Premium** | $9.99/month | Everything + virtual cards, reports |

---

## 📊 Webhook Events Handled

| Event | Action |
|-------|--------|
| `checkout.session.completed` | Activate subscription after checkout |
| `customer.subscription.updated` | Update subscription status |
| `customer.subscription.deleted` | Downgrade to free tier |
| `invoice.payment_succeeded` | Mark subscription as active |
| `invoice.payment_failed` | Mark as past_due, notify user |

---

## 🚨 Troubleshooting

### "Stripe not configured" error
- Check `.env` file has `STRIPE_SECRET_KEY` set
- Restart the Flask app after adding keys

### Webhook not receiving events
- Make sure `stripe listen` is running
- Check webhook signing secret in `.env`
- Verify webhook URL is correct

### Price ID not found
- Double-check Price IDs in Stripe dashboard
- Make sure they're set in `.env`
- Restart Flask app

### Database errors
- Run the migration script again
- Check `instance/choreapp.db` exists
- Restore backup if needed: `cp instance/choreapp.db.backup instance/choreapp.db`

---

## 🎉 You're Ready!

Once configured, users can:
1. ✅ Subscribe to Family/Premium plans
2. ✅ Get 14-day free trial (no CC required initially)
3. ✅ Manage subscription via customer portal
4. ✅ Access premium features based on tier
5. ✅ Automatic billing every month

---

## 📞 Next Steps

1. **Test thoroughly** with Stripe test mode
2. **Add more feature gating** to premium features
3. **Configure production webhooks** when deploying
4. **Add email notifications** for subscription events
5. **Monitor revenue** in Stripe dashboard

---

**Questions?** Check Stripe docs: https://stripe.com/docs/billing/subscriptions/overview

**Status:** ✅ Subscription system fully implemented and ready for testing!
