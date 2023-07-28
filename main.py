class Worker:
    def work(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Человек работает")

    def eat(self):
        print("Человек ест")


class RobotWorker(Worker):
    def work(self):
        print("Робот работает")

    def eat(self):
        pass


def process_eating(worker):
    eat = worker.eat


# -------------------------------------
class Text:
    text = ""
    def Text(self, text):
        self.text = text

    def getText(self, text):
        return text

class Printer:
    def print(self, text):
        print(Text.getText)
