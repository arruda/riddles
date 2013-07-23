"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from riddles.test_utils.migration_testcase import MigrationTestCase


class TestMigration0003(MigrationTestCase):

    start_migration = '0001_initial'
    dest_migration = '0002_auto__add_guess'
    django_application = 'riddles'

    def test_schema_and_data_updated(self):
        # import pdb; pdb.set_trace()
        try:
            GuessStart = self.start_orm['riddles.Guess']
            self.fail("Shouln't have this model")
        except KeyError:
            pass

        self.migrate_to_dest()

        Guess = self.dest_orm['riddles.Guess']

        # Assertions
        self.assertEqual(Guess.objects.all().count(), 0)
