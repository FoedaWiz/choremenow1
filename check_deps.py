#!/usr/bin/env python3
"""
Chore Me - Dependency Checker
Checks if all required packages are installed and provides installation instructions.
"""

import sys
import subprocess

REQUIRED_PACKAGES = [
    ('flask', 'Flask'),
    ('flask_sqlalchemy', 'Flask-SQLAlchemy'),
    ('flask_login', 'Flask-Login'),
    ('werkzeug', 'Werkzeug'),
    ('dotenv', 'python-dotenv'),
]

OPTIONAL_PACKAGES = [
    ('google.generativeai', 'google-generativeai'),
    ('stripe', 'stripe'),
    ('PIL', 'Pillow'),
]

def check_package(module_name, package_name):
    """Check if a package is installed"""
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

def main():
    print("=" * 50)
    print("🎮 Chore Me - Dependency Checker")
    print("=" * 50)
    print()
    
    missing_required = []
    missing_optional = []
    
    print("Checking required packages...")
    for module, package in REQUIRED_PACKAGES:
        if check_package(module, package):
            print(f"  ✅ {package}")
        else:
            print(f"  ❌ {package} - MISSING")
            missing_required.append(package)
    
    print()
    print("Checking optional packages...")
    for module, package in OPTIONAL_PACKAGES:
        if check_package(module, package):
            print(f"  ✅ {package}")
        else:
            print(f"  ⚠️  {package} - Optional (for AI & payments)")
            missing_optional.append(package)
    
    print()
    print("=" * 50)
    
    if missing_required:
        print("❌ MISSING REQUIRED PACKAGES")
        print("=" * 50)
        print()
        print("Install with:")
        print(f"  pip3 install --user {' '.join(missing_required)}")
        print()
        print("Or install all dependencies:")
        print("  pip3 install --user -r requirements.txt")
        print()
        return 1
    else:
        print("✅ ALL REQUIRED PACKAGES INSTALLED!")
        print("=" * 50)
        print()
        
        if missing_optional:
            print("Note: Optional packages missing (AI & payment features):")
            for pkg in missing_optional:
                print(f"  - {pkg}")
            print()
        
        print("🚀 Ready to run Chore Me!")
        print()
        print("Start the app:")
        print("  python3 run.py")
        print()
        print("Then open: http://localhost:5000")
        print()
        return 0

if __name__ == '__main__':
    sys.exit(main())
