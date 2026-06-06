#!/bin/bash
# Run this script to commit and push all updates to GitHub
# Then pull on SiteGround to deploy

cd "$(dirname "$0")"

echo "📦 Committing all bug fixes and improvements..."

git add \
  app/__init__.py \
  app/models.py \
  app/routes/auth.py \
  app/routes/chores.py \
  app/routes/kid_dashboard.py \
  app/routes/kid_portal.py \
  app/routes/kids.py \
  app/routes/payments.py \
  app/static/manifest.json \
  app/templates/legal/pricing.html \
  passenger_wsgi.py \
  .htaccess \
  .env.example \
  siteground_setup.sh

git commit -m "Fix bugs, improve security, prep for SiteGround deploy

- Fix xp_progress_percent() wrong level XP calculation
- Fix calculate_streak() using nonexistent Assignment fields
- Fix get_household_leaderboard() using nonexistent fields
- Add @csrf.exempt to Stripe webhook endpoint
- Fix stripe.error.StripeError crash when Stripe not installed
- Add due_date validation in chores assign()
- Guard kid.account.id None checks in log_audit calls
- Make login case-insensitive (ilike)
- Gate AI suggestions behind family/premium tier
- Enforce 3-kid limit for free tier
- Fix pricing page: remove 'no credit card required' claim
- Fix Premium users seeing Family plan trial button
- Add SESSION_COOKIE_SECURE for production
- Fix manifest.json icon purpose entries for Play Store
- Update passenger_wsgi.py for SiteGround venv path
- Add HTTPS redirect and file protection to .htaccess
- Add siteground_setup.sh deployment script

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"

echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done! Now log into SiteGround and run:"
echo "   cd ~/public_html && git pull origin main"
echo "   Then restart your Python app in cPanel."
