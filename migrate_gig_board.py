from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    # Add new columns to chores table
    try:
        db.session.execute(text('ALTER TABLE chores ADD COLUMN available_in_marketplace BOOLEAN DEFAULT 0'))
        print("✓ Added available_in_marketplace column")
    except Exception as e:
        print(f"available_in_marketplace column might already exist: {e}")
    
    try:
        db.session.execute(text('ALTER TABLE chores ADD COLUMN first_come_first_serve BOOLEAN DEFAULT 1'))
        print("✓ Added first_come_first_serve column")
    except Exception as e:
        print(f"first_come_first_serve column might already exist: {e}")
    
    try:
        db.session.execute(text('ALTER TABLE chores ADD COLUMN max_claims INTEGER DEFAULT 1'))
        print("✓ Added max_claims column")
    except Exception as e:
        print(f"max_claims column might already exist: {e}")
    
    db.session.commit()
    print("\n✅ Gig Board migration completed!")
