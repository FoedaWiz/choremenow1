"""
Migration script to add household isolation to existing database
Run this ONCE after deploying the household feature to migrate existing data
"""
from app import create_app, db
from app.models import User, Household, Kid, Chore, Reward
from datetime import datetime
from sqlalchemy import text

def migrate_to_households():
    app = create_app()
    with app.app_context():
        print("🔄 Starting household migration...")
        
        # Get all users without households
        users = User.query.all()
        migrated_count = 0
        
        for user in users:
            # Check if user already has a household
            if user.active_household_id:
                print(f"✓ User {user.username} already has household, skipping")
                continue
            
            # Create a household for this user
            household = Household(name=f"{user.username}'s Household")
            db.session.add(household)
            db.session.flush()
            
            # Add user as owner
            db.session.execute(
                text("INSERT INTO household_members (household_id, user_id, role, joined_at) VALUES (:hid, :uid, :role, :joined)"),
                {'hid': household.id, 'uid': user.id, 'role': 'owner', 'joined': datetime.utcnow()}
            )
            
            # Set as active household
            user.active_household_id = household.id
            
            # Migrate all kids to this household
            kids = Kid.query.filter_by(parent_id=user.id).all()
            for kid in kids:
                kid.household_id = household.id
            
            # Migrate all chores to this household
            chores = Chore.query.filter_by(parent_id=user.id).all()
            for chore in chores:
                chore.household_id = household.id
            
            # Migrate all rewards to this household
            rewards = Reward.query.filter_by(parent_id=user.id).all()
            for reward in rewards:
                reward.household_id = household.id
            
            migrated_count += 1
            print(f"✓ Migrated user {user.username} with {len(kids)} kids, {len(chores)} chores, {len(rewards)} rewards")
        
        # Commit all changes
        db.session.commit()
        print(f"\n✅ Migration complete! Migrated {migrated_count} users to households")

if __name__ == '__main__':
    migrate_to_households()
