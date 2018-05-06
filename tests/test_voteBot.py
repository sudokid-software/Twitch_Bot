from unittest import TestCase

from bot import VoteBot


class TestVoteBot(TestCase):
    def setUp(self):
        self.vote_bot = VoteBot()

    def test_create_poll(self):
        self.assertEqual(
            self.vote_bot.polls,
            {}
        )

        self.vote_bot.create_poll('', 'add test')

        self.assertEqual(
            self.vote_bot.polls,
            {}
        )

        self.vote_bot.create_poll('sudokid', 'add test')

        self.assertEqual(
            self.vote_bot.polls,
            {'test': {'users': set(), 'choices': {}}}
        )

    def test_list_polls(self):
        self.assertEqual(
            'There are no current polls',
            self.vote_bot.list_polls()
        )

        self.vote_bot.create_poll('sudokid', 'add test')

        self.assertEqual(
            'test',
            self.vote_bot.list_polls()
        )

    def test_add_choice(self):
        self.assertEqual(
            self.vote_bot.polls,
            {}
        )

        self.vote_bot.add_choice('test', 'choice test test2')
        self.assertEqual(
            self.vote_bot.polls,
            {}
        )

        self.vote_bot.create_poll('sudokid', 'add test')
        self.vote_bot.add_choice('sudokid', 'choice test test')

        self.assertEqual(
            self.vote_bot.polls,
            {'test': {'users': set(), 'choices': {'test': 0}}}
        )

        self.vote_bot.add_choice('sudokid', 'choice test test2')
        self.assertEqual(
            self.vote_bot.polls,
            {'test': {'users': set(), 'choices': {'test': 0, 'test2': 0}}}
        )

    def test_vote(self):
        self.vote_bot.create_poll('sudokid', 'add test')
        self.vote_bot.add_choice('sudokid', 'choice test test')
        self.vote_bot.add_choice('sudokid', 'choice test test2')

        self.assertEqual(
            self.vote_bot.polls['test'],
            {'users': set(), 'choices': {'test': 0, 'test2': 0}}
        )

        self.vote_bot.vote('sudokid', 'test test2')

        self.assertEqual(
            self.vote_bot.polls['test'],
            {'users': {'sudokid'}, 'choices': {'test': 0, 'test2': 1}}
        )

        self.vote_bot.vote('sudokid', 'test test2')

        self.assertEqual(
            self.vote_bot.polls['test'],
            {'users': {'sudokid'}, 'choices': {'test': 0, 'test2': 1}}
        )

        self.vote_bot.vote('userman2', 'test test')

        self.assertEqual(
            self.vote_bot.polls['test'],
            {
                'users': {'sudokid', 'userman2'},
                'choices': {'test': 1, 'test2': 1}
            }
        )

    def test_reducer(self):
        response = self.vote_bot.reducer('sudokid', 'add test')
        self.assertEqual(
            'Poll test added!',
            response
        )

        response = self.vote_bot.reducer('sudokid', 'list')
        self.assertEqual(
            'test',
            response
        )
