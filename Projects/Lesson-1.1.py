import os
def LessonPy1(name, CurentFile):
    print("Hello," , name, "you are working on", CurentFile )
FileCur = __file__
Sded = os.getlogin()
LessonPy1(Sded, FileCur)
print("What's now?")
Anwser1 = input("Type your anwser: ")
print(Anwser1 +"?", "Fine.")
AnwserNumber1 = int(input("Type how much time it take: "))
AnwserNumber2 = int(input("Type how many times you want repeat it: "))
print(AnwserNumber1 + AnwserNumber2)
print(AnwserNumber1, "and repeat", AnwserNumber2,"times")