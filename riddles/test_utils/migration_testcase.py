# -*- coding: utf-8 -*-
"""
    test_utils.migration_testcase
    ~~~~~~~~~~~~~~

    Here will be testcases utils for Migrations

    :copyright: (c) 2013 by arruda.
"""
from django.test import TransactionTestCase
from south.migration import Migrations
from django.core.management import call_command


class MigrationTestCase(TransactionTestCase):
    """
    A Test case for testing migrations.
    Subclasse should define:
     * start_migration
     * dest_migration
     * django_application

    Use self.start_orm to get the ORM of the start_migration
    and self.dest_orm to get the ORM for the dest_migration
    Creadits to Michael:
    http://micknelson.wordpress.com/2013/03/01/testing-django-migrations/
    """

    # These must be defined by subclasses.
    start_migration = None
    dest_migration = None
    django_application = None

    def setUp(self):
        super(MigrationTestCase, self).setUp()
        migrations = Migrations(self.django_application)
        self.start_orm = migrations[self.start_migration].orm()
        self.dest_orm = migrations[self.dest_migration].orm()

        # Ensure the migration history is up-to-date with a fake migration.
        # The other option would be to use the south setting for these tests
        # so that the migrations are used to setup the test db.
        call_command('migrate', self.django_application, fake=True,
                     verbosity=0)
        # Then migrate back to the start migration.
        call_command('migrate', self.django_application, self.start_migration,
                     verbosity=0)

    def tearDown(self):
        # Leave the db in the final state so that the test runner doesn't
        # error when truncating the database.
        call_command('migrate', self.django_application, verbosity=0)

    def migrate_to_dest(self):
        call_command('migrate', self.django_application, self.dest_migration,
                     verbosity=0)
