"""
Migration script to add kid user support
Run this with: python migrate_kid_users.py
"""

from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    print("Adding kid user fields to users table...")
    
    try:
        with db.engine.connect() as conn:
            # Check if columns exist before adding
            result = conn.execute(text("PRAGMA table_info(users)"))
            columns = [row[1] for row in result]
            
            if 'user_type' not in columns:
                conn.execute(text("ALTER TABLE users ADD COLUMN user_type VARCHAR(20) DEFAULT 'parent'"))
                print("✓ Added user_type column")
            
            if 'kid_id' not in columns:
                conn.execute(text("ALTER TABLE users ADD COLUMN kid_id INTEGER REFERENCES kids(id)"))
                print("✓ Added kid_id column")
            
            conn.commit()
        
        print("\n✅ Migration completed successfully!")
        print("\nKids can now create User accounts!")
        
    except Exception as e:
        print(f"\n❌ Migration failed: {e}")
        print("If columns already exist, this is normal.")

print("\nDone!")
