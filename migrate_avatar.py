#!/usr/bin/env python3
"""Migration script to add parent avatar support"""

import sqlite3
import os

# Path to database
db_path = 'instance/choreapp.db'

if not os.path.exists(db_path):
    print(f"❌ Database not found at {db_path}")
    exit(1)

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("🔄 Migrating database for parent avatar support...")

try:
    # Add avatar_url column to users table
    cursor.execute("ALTER TABLE users ADD COLUMN avatar_url VARCHAR(200) DEFAULT '👤'")
    print("✅ Added avatar_url column to users table")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("ℹ️  avatar_url column already exists in users table")
    else:
        raise

try:
    # Add rpm_avatar_url column to users table
    cursor.execute("ALTER TABLE users ADD COLUMN rpm_avatar_url VARCHAR(500)")
    print("✅ Added rpm_avatar_url column to users table")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("ℹ️  rpm_avatar_url column already exists in users table")
    else:
        raise

try:
    # Create user_avatar_items table
    cursor.execute("""
        CREATE TABLE user_avatar_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            avatar_item_id INTEGER NOT NULL,
            unlocked_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            is_equipped BOOLEAN DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (avatar_item_id) REFERENCES avatar_items(id)
        )
    """)
    print("✅ Created user_avatar_items table")
except sqlite3.OperationalError as e:
    if "already exists" in str(e):
        print("ℹ️  user_avatar_items table already exists")
    else:
        raise

# Commit changes
conn.commit()
conn.close()

print("✨ Migration complete!")
print("\nRestart the server to apply changes.")
