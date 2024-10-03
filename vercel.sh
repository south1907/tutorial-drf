#!/bin/bash

# Output the current Vercel environment
echo "Vercel Environment: $VERCEL_ENV"
echo "Git Commit Ref: $VERCEL_GIT_COMMIT_REF"

echo "Running production build..."
npm python manage.py runserver