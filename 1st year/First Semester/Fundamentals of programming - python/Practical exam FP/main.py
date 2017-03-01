from ui import MenuUI
from repo import Repository
from controller import Controller


def main():
    repo = Repository("sentences.txt")
    controller = Controller(repo)
    MenuUI(controller, repo.getFileName())



if __name__ == '__main__':
    main()