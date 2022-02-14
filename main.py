import random

a = 0


def clear():
    print("\n" * 10)


def wrong():
    c = ["- - -\n",
         "\t|\n"
         "\t|\n",
         "\tO\n",
         "\f\f\f\f\f\\", "|", "/\n",
         "\t|\n",
         "\f\f\f\f\f/", "\f\f\\"]
    i = 0
    temp = a
    while temp > 0:
        if i < len(c):
            print(c[i], end="")
            i += 1
            temp -= 1
        else:
            print("\n\033[1;32;31mGame Over")
            exit(0)


question = {
    "question-1": "gitar",
    "question-2": "yastık",
    "question-3": "anahtarlık",
    "question-4": "bilgisayar",
    "question-5": "portakal"
}
rand = random.randint(1, 5)
ques = str(question["question-" + str(rand)])
#print(ques)
i = 0
word = []
while i < len(ques):
    word.append("_")
    print(word[i], end="")
    i += 1
while 1:
    i = 0
    print("\n")
    wrong()
    temp = input("\nHarf Gir:")
    clear()
    if ques.find(temp) + 1:
        while i < len(ques):
            if temp == ques[i]:
                word[i] = temp
                print(word[i], end="")
                i += 1
            else:
                print(word[i], end="")
                i += 1
    else:
        error = temp
        for c in range(len(ques)):
            print(word[c], end="")
        a += 1

    if "_" not in word:
        print("\n")
        wrong()
        print("\n\033[1;32;32mGAME WİN")
        break

