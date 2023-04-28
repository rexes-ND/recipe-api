"""
Test custom Django management commands.
"""
# In order to mock the behaviour of DB (simulate DB)
from unittest.mock import patch
# One of the error we might get when connecting to DB
from psycopg2 import OperationalError as Psycopg2Error
# Used to actually call the command
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


# check is provided by BaseCommand
@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')  # Pass through without really sleeping
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]
        """
        Raise Psycopg2Error 2 times,
              OperationalError 3 times,
              and finally, return true.
        Psycopg2Error -
            happens when postgres haven't even started yet
        OperationalError -
            happens when postgres started
            but haven't setup the testing/dev DB yet
        """

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
