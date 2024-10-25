#!/bin/bash
echo "Resetting the database..."

# Remove the SQLite database file (adjust path if necessary)
rm -f ./instance/app.db  # Adjust this if using another DB type

# Remove the Alembic migration history
rm -rf ./migrations/versions/*

# Reinitialize migrations and run them
flask db init  # Only if no migrations exist yet
flask db migrate  # Generate a new migration
flask db upgrade  # Apply the migration to the database

echo "Database reset complete!"