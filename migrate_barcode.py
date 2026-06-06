"""
Migration script to add barcode login fields to KidAccount model
Run this with: python migrate_barcode.py
"""

from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    print("Adding barcode login fields to kid_accounts table...")
    
    try:
        # Add new columns to kid_accounts table (without UNIQUE constraint initially)
        with db.engine.connect() as conn:
            # Check if columns exist before adding
            result = conn.execute(text("PRAGMA table_info(kid_accounts)"))
            columns = [row[1] for row in result]
            
            if 'email' not in columns:
                conn.execute(text("ALTER TABLE kid_accounts ADD COLUMN email VARCHAR(120)"))
                print("✓ Added email column")
            
            if 'password_hash' not in columns:
                conn.execute(text("ALTER TABLE kid_accounts ADD COLUMN password_hash VARCHAR(200)"))
                print("✓ Added password_hash column")
            
            if 'barcode_id' not in columns:
                conn.execute(text("ALTER TABLE kid_accounts ADD COLUMN barcode_id VARCHAR(100)"))
                print("✓ Added barcode_id column")
            
            if 'registration_complete' not in columns:
                conn.execute(text("ALTER TABLE kid_accounts ADD COLUMN registration_complete BOOLEAN DEFAULT 0"))
                print("✓ Added registration_complete column")
            
            conn.commit()
        
        print("\n✅ Migration completed successfully!")
        print("\nNote: UNIQUE constraints will be enforced at the application level.")
        print("Kids can now use barcode login!")
        
    except Exception as e:
        print(f"\n❌ Migration failed: {e}")
        print("If columns already exist, this is normal.")

print("\nDone!")
