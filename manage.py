import fire


class Command(object):

    def hello(self, username):
        return "Hello, " + username + " !!"

    def startproject(self, name):
        pass

    def startapp(self, name):
        return "make app: " + name

if __name__ == '__main__':
    fire.Fire(Command)
