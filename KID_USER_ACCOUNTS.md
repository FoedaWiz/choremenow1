# Kid User Accounts & Parent Access Control Implementation

## Overview
Successfully implemented full User account creation for kids with email/password authentication and comprehensive parent route protection.

## Major Changes

### 1. User Model Updates (`app/models.py`)
Added fields to User model:
- `user_type` - Distinguishes between 'parent' and 'kid' users
- `kid_id` - Foreign key linking kid users to Kid profiles
- `kid_profile` relationship - Access Kid data from User account

New User methods:
- `is_parent()` - Check if user is a parent
- `is_kid()` - Check if user is a kid
- `get_kid()` - Get associated Kid profile for kid users

Updated relationships:
- `kids` relationship now uses `foreign_keys='Kid.parent_id'` to avoid conflicts
- Added `kid_profile` relationship for kid users

### 2. Kid Registration Flow (`app/routes/kid_portal.py`)
**Complete rewrite of authentication:**

**Old System:**
- Session-based auth using `session['kid_id']`
- KidAccount model only
- No Flask-Login integration

**New System:**
- Flask-Login for all users (parents AND kids)
- Creates User account with `user_type='kid'`
- Links User to Kid via `kid_id` field
- Also updates KidAccount for backward compatibility

**Registration Process:**
1. Scan barcode → Choose name → Enter email & password
2. Creates `User` with user_type='kid', linked to Kid
3. Updates `KidAccount` with same credentials
4. Auto-login using `login_user()`
5. Redirects to kid dashboard

**Login Process:**
1. Scan barcode → System finds KidAccount
2. Looks up associated User account
3. Validates password against User model
4. Uses `login_user()` for authentication
5. Kid can now use `current_user` throughout the app

### 3. Access Control System

#### New Decorators (`app/utils/decorators.py`)
Created role-based access control decorators:

- `@parent_required` - Ensures only parents can access
  - Checks `current_user.is_parent()`
  - Redirects kids to kid dashboard
  - Redirects unauthenticated to login

- `@kid_required` - Ensures only kids can access
  - Checks `current_user.is_kid()`
  - Redirects parents to parent dashboard
  - Redirects unauthenticated to barcode scan

#### Updated Household Context (`app/utils/household_context.py`)
- `require_household_access` now blocks kids completely
- Added kid user type check
- Kids redirected to kid portal if they try to access

#### Updated Kid Portal Functions
- `get_current_kid()` now uses `current_user.get_kid()` instead of session
- `require_kid_login` checks Flask-Login + user_type
- Removed all session-based auth code

### 4. Parent Route Protection (`app/routes/main.py`)
Updated main dashboard:
- Added `@parent_required` decorator
- Index route redirects based on user_type:
  - Parents → parent dashboard
  - Kids → kid dashboard
  - Unauthenticated → landing page

### 5. Routes Kids CANNOT Access
With the new system, kids are blocked from:

**Household Management:**
- `/household/*` - All household routes
- `/dashboard` - Parent dashboard

**Financial:**
- `/payments/*` - Payment and wallet management
- Stripe integration routes

**Administrative:**
- `/chores/create` - Creating chores
- `/chores/assign` - Assigning chores
- `/kids/*` - Managing kid profiles (except their own)
- `/household/invite` - Inviting co-parents

**Content Control:**
- `/newsfeed/manage` - Parent newsfeed controls
- `/education/manage` - Education content settings

All these routes now use `@login_required` + `@parent_required` or `@require_household_access`

### 6. Routes Kids CAN Access
Kids have access to:

**Authentication:**
- `/kid/scan` - Barcode scanning
- `/kid/register` - Registration
- `/kid/barcode-login` - Login
- `/kid/logout` - Logout

**Dashboard:**
- `/kid/dashboard` - Kid dashboard
- `/kid/profile` - Their profile
- `/kid/chore/<id>/complete` - Complete chores

**Fun Features:**
- `/education/` - Educational videos (kid-safe)
- `/barcode/my-code` - Their QR code
- `/barcode/trade` - Chore trading
- `/kid_dashboard/<id>` - Cyber dashboard

### 7. Migration Scripts
Created `migrate_kid_users.py`:
- Adds `user_type` column to users table
- Adds `kid_id` column to users table
- Sets defaults for existing users
- Successfully executed

## Security Improvements

1. **Dual Authentication:**
   - Both User and KidAccount store credentials
   - User model is primary auth source
   - KidAccount maintained for compatibility

2. **Role-Based Access Control:**
   - Every parent route protected with decorators
   - Automatic redirection based on user type
   - Clear separation of kid vs parent interfaces

3. **Flask-Login Integration:**
   - Kids use proper authentication framework
   - Session management handled by Flask-Login
   - Logout properly clears authentication

4. **Account Lockout:**
   - Failed login attempts tracked in KidAccount
   - 5 failed attempts = 15 minute lockout
   - Prevents brute force attacks

## Testing Checklist

- [ ] Kid registration: barcode → name → email/password → dashboard
- [ ] Kid login: barcode → password → dashboard
- [ ] Kid logout redirects to barcode scan
- [ ] Kids blocked from `/dashboard`
- [ ] Kids blocked from `/household/manage`
- [ ] Kids blocked from `/chores/create`
- [ ] Kids blocked from `/payments/*`
- [ ] Kids blocked from `/newsfeed/manage`
- [ ] Kids CAN access `/education/`
- [ ] Kids CAN access `/kid/dashboard`
- [ ] Kids CAN access `/barcode/trade`
- [ ] Parents can still access all parent routes
- [ ] Parent login still works normally
- [ ] current_user.is_parent() works correctly
- [ ] current_user.is_kid() works correctly
- [ ] current_user.get_kid() returns Kid profile

## Files Modified

1. `app/models.py` - Added user_type and kid_id to User
2. `app/routes/kid_portal.py` - Complete auth rewrite
3. `app/routes/main.py` - Added parent_required
4. `app/utils/household_context.py` - Added kid blocking
5. `app/utils/decorators.py` - NEW FILE with role decorators
6. `migrate_kid_users.py` - NEW FILE for database migration

## Architecture Diagram

```
User (Flask-Login)
├── user_type = 'parent'
│   ├── Has household access
│   ├── Can manage kids
│   └── Can access all parent routes
│
└── user_type = 'kid'
    ├── Linked to Kid via kid_id
    ├── No household access
    ├── Limited to kid routes only
    └── Blocked from parent controls
```

## Backward Compatibility

- KidAccount still exists and is updated during registration
- PIN login system preserved (though barcode/password is primary)
- Existing parent accounts unaffected
- All existing relationships maintained

## Next Steps

1. Test complete registration flow
2. Test parent route blocking
3. Update navigation to hide parent links for kids
4. Add "Switch Account" feature for parents
5. Consider removing old session-based code
6. Add user type indicator in UI
7. Update documentation for users
