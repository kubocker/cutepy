import subprocess
import fire

files = ['__init__.py', 'forms.py', 'views.py', 'models.py']


class Command(object):

    def hello(self, username):
        return "Hello, " + username + " !!"

    def startproject(self, name):
        pass

    def startapp(self, name):
        cmd = "cd ../ && mkdir {0}".format(name)
        subprocess.call(cmd, shell=True)

        print("creating...")
        for k in range(len(files)):
            cmd = "cd ../{0} && touch {1}".format(name, files[k])
            print(name + "/" + files[k])
            subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    fire.Fire(Command)
