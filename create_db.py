from app import create_app, db
import os

# Ensure the instance folder exists
instance_path = os.path.join(os.getcwd(), 'instance')
os.makedirs(instance_path, exist_ok=True)

app = create_app()
app.app_context().push()

db.create_all()
print("Database recreated successfully!")

# Seed initial data (optional, but good for development)
from app.utils.seed_data import seed_badges_and_items
seed_badges_and_items()
print("Database seeded with initial data!")
