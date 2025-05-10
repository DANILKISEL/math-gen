from random import randint
import uuid
def looptru(listtoloop):
    questions  = ""
    for item in enumerate(listtoloop):
        questions = questions + "\n" + str(item)
    return questions

def generateMathQuestions():
    awns = []
    variant = "Variant:" + str(randint(100000, 999999))
    qus = [variant]

    for index in range(1, 21):
        q1 = str(randint(1,10))
        q2 = str(randint(1, int(q1)))
        q = q1 + "=" + q2 + "+"
        evalstr = q1 + "-" + q2
        awns.append(eval(evalstr))
        qus.append(q)
    for index in range(1, 11):
        q = str(randint(1,10)) + "+" + str(randint(1,10))
        awns.append(eval(q))
        qus.append(q + "=")
    for index in range(1, 6):
        q = str(randint(10,20)) + "-" + str(randint(1,10))
        awns.append(eval(q))
        qus.append(q + "=")

    variantUuid =  str(uuid.uuid4())
    idAwns = variantUuid + "awns.txt"
    awnserkey = open(idAwns, "w")
    awnserkey.write(str(looptru(awns)))
    idQus = variantUuid + "qus.txt"
    Queskey = open(idQus, "w")
    Queskey.write(str(looptru(qus)))
    return
