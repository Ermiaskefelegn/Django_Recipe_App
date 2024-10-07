"""
Django Command to wait for the database to be available
"""
from django.core.management.base import BaseCommand
import time

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError  # Use Django's OperationalError

class Command(BaseCommand):
    """Django command to wait for the database to be available"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])  # Check if database is ready
                db_up = True
            except (Psycopg2OpError, OperationalError):  # Catch both psycopg2 and Django errors
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)  # Wait for a second before retrying

        self.stdout.write(self.style.SUCCESS('Database Available!'))  # Success message