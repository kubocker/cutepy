import fire


class Command(object):

    def hello(self, username):
        return "Hello, " + username + " !!"

if __name__ == '__main__':
    fire.Fire(Command)
