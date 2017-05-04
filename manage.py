import subprocess
import fire

project_files = ['__init__.py', 'settings.py', 'app.py']
app_files = ['__init__.py', 'forms.py', 'views.py', 'models.py']


class Command(object):

    def hello(self, username):
        """ テストテスト """
        return "Hello, " + username + " !!"

    def startproject(self, name):
        """ プロジェクトディレクトリを作成する
        @param name
        """
        cmd = "cd ../ && mkdir {0}".format(name)
        subprocess.call(cmd, shell=True)

        print("creating...")
        for k in range(len(project_files) - 1):
            cmd = "cd ../"
        subprocess.call(cmd, shell=True)

    def startapp(self, name):
        """ アプリディレクトリを作成する
        @param name
        """
        cmd = "cd ../ && mkdir {0}".format(name)
        subprocess.call(cmd, shell=True)

        print("creating...")
        for k in range(len(app_files)):
            cmd = "cd ../{0} && touch {1}".format(name, app_files[k])
            print(name + "/" + app_files[k])
            subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    fire.Fire(Command)
