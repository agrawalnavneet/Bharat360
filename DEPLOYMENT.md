# Deployment Guide for Render.com

## Quick Fix for Current Error

The error `ModuleNotFoundError: No module named 'Bharat360'` occurs because Render.com is looking for the wrong module name.

## Steps to Deploy:

### Option 1: Using Render Dashboard (Recommended)

1. **Go to Render Dashboard**: https://dashboard.render.com
2. **Select your service** "Bharat360"
3. **Go to Settings** (left sidebar)
4. **Update Start Command**:
   ```
   gunicorn newsfeedback.wsgi:application --bind 0.0.0.0:$PORT
   ```
5. **Update Build Command**:
   ```
   pip install -r requirements.txt && python manage.py migrate
   ```
6. **Save Changes** - Render will automatically redeploy

### Option 2: Using render.yaml (If using Blueprint)

If you're using Render Blueprint, the `render.yaml` file is already configured correctly.

## Environment Variables (Optional but Recommended)

In Render Dashboard → Settings → Environment Variables, add:

- `SECRET_KEY`: Generate a secure key (use Django's `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Your Render domain (e.g., `your-app.onrender.com`)

## Important Notes:

1. **Database**: Currently using SQLite. For production, consider PostgreSQL:
   - Add PostgreSQL database in Render
   - Update DATABASES in settings.py to use PostgreSQL

2. **Static Files**: Static files will be collected automatically during build

3. **Migrations**: Run automatically during build via build command

## After Deployment:

1. Create superuser: Use Render Shell or add a management command
2. Access admin: https://your-app.onrender.com/admin/
3. Add news sources and articles through admin panel

