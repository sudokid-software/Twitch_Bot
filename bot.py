# import redis


class VoteBot:
    def __init__(self):
        # self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.polls = {}

    def create_poll(self, user, msg):  # Todo Add user support
        print('\n' * 2, user, msg, '\n' * 2)

        if user != 'sudokid':
            return 'Only the channel owner can create polls!'

        if len(msg) < 4:
            return 'You must provide a poll to create!'

        new_poll = msg[4:]

        if new_poll not in self.polls:
            self.polls[new_poll] = {
                'users': set(),
                'choices': {}
            }

        return f'Poll {new_poll} added!'

    def list_polls(self):
        polls = list(self.polls.keys())

        if len(polls) > 0:
            return ', '.join(list(self.polls.keys()))
        else:
            return 'There are no current polls'

    def add_choice(self, user, msg):
        cmd, poll, choice = msg.split(' ', 2)
        if user != 'sudokid':
            return '{user} only the channel owner can create polls!'

        if poll not in self.polls:
            return '{poll} doesn\'t exist!'

        self.polls[poll]['choices'][choice] = 0
        return f'{choice} has been added to {poll}'

    def vote(self, user, msg):
        try:
            poll, vote = msg.split(' ', 1)
        except ValueError:
            return 'To vote use `!vote [poll] [choice]`'

        if self.polls.get(poll, None) is None:
            return f'{user} the {poll} doesn\'t exist!'

        if user in self.polls[poll]['users']:
            return f'{user} you can only vote once!'

        if vote in self.polls[poll]['choices'].keys():
            self.polls[poll]['choices'][vote] += 1
            self.polls[poll]['users'].add(user)

            total_votes = self.polls[poll]['choices'][vote]
            print(f'{vote} has a total of {total_votes}')
            return f'{user} has voted {vote}!'
        return f'The choice {vote} doesn\'t exist'

    def reducer(self, user, msg):
        if msg.startswith('add'):
            return self.create_poll(user, msg)
        if msg.startswith('choice'):
            return self.add_choice(user, msg)
        if msg.startswith('list'):
            return self.list_polls()
