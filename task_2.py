# Задание 2
class Tester:

    def __init__(self, name):
        self.name = name
        self.deadline = True

    def work_hard(self, deadline):
        if deadline == True:
            print(self.name + " Что ж, ещё часок поработаю!")
        else:
            print(self.name + " Можно отдыхать")


tester_1 = Tester("tester_1")
tester_2 = Tester("tester_2")
tester_1.work_hard(False)
tester_2.work_hard(True)
