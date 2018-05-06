import logging
import secrets

logger = logging.getLogger(__name__)


class Giveaway:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            return f'{user} you have been added to the giveaway!'
        return f'{user} you have all ready been added to the list!'

    def pick_user(self, user):
        if user != 'sudokid':
            return 'Only the channel owner can pick a winner!'

        return secrets.choice(self.users)

