# Barcode Login Flow - One-Time Setup

## Overview
Barcodes are used **ONLY** for first-time kid account setup. After registration, kids login with email/password.

## Flow

### 1. Parent Setup
- Parent goes to kid's profile page
- System generates unique barcode for each kid (format: `0001-3847`)
- Barcode is displayed as:
  - **iOS**: Number to type manually (with copy button)
  - **Android**: QR code to scan
- Barcode saved to `KidAccount.barcode_id`

### 2. Kid First-Time Setup

**Step 1: Enter Code**
- Kid visits `/kid/scan` (Kid Login page)
- Enters barcode manually (e.g., `0001-3847`) OR scans QR code
- Link: "Already registered? Login here" → goes to email/password login

**Step 2: Choose Name**
- System finds household from barcode
- Shows list of ALL kids in that household
- **Available kids**: Can click to register
- **Already registered**: Shown but disabled (with link to login)

**Step 3: Create Account**
- Kid clicks their name
- Fills out registration form:
  - Email address
  - Password (min 6 characters)
  - Confirm password
- System creates:
  - `User` account (type='kid', linked to kid)
  - Updates `KidAccount` (marks registration_complete=True)
- Auto-logs them in
- Flash message: "From now on, log in with your email and password!"

### 3. Returning Users

**Regular Login**
- Kid visits `/kid/login`
- Enters email and password
- No barcode needed

**If they try barcode again**
- System detects account already registered
- Redirects to regular login page
- Message: "Barcode is only for first-time setup. Use email/password."

## Key Routes

| Route | Purpose | When Used |
|-------|---------|-----------|
| `/kid/scan` | Enter barcode code | First-time only |
| `/kid/select-name/<household_id>/<barcode>` | Choose name from list | After valid barcode |
| `/kid/register/<kid_id>/<barcode>` | Create email/password | After selecting name |
| `/kid/login` | Email/password login | All future logins |

## Benefits

1. **Simple for parents**: One code per kid
2. **Easy for kids**: No typing after first time
3. **Secure**: Email/password for ongoing access
4. **Household-aware**: Any household barcode shows all kids
5. **Clear separation**: First-time setup vs regular login

## Technical Details

- **Barcode format**: `XXXX-YYYY` (kid_id + random suffix)
- **Storage**: `KidAccount.barcode_id` (persistent)
- **Validation**: Barcode must belong to valid kid in household
- **Registration check**: `KidAccount.registration_complete` flag
- **Authentication**: Flask-Login with `User.user_type='kid'`

## User Experience

### First Time
```
1. Parent: "Here's your code: 0001-3847"
2. Kid: Visits kid login → enters code
3. System: Shows household kids → kid clicks their name
4. Kid: Creates email/password → account ready!
5. Next time: Login with email/password (no code needed)
```

### Already Registered
```
1. Kid tries to scan code again
2. System: "You're already registered! Use email/password"
3. Kid: Clicks login link → enters email/password
```

## Parent View
- Each kid profile shows:
  - iOS code (blue box, copyable)
  - Android QR code (green box, scannable)
  - Both use same barcode number
  - Can regenerate if kid hasn't registered yet
