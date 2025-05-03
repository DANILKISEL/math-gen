from random import randint
import uuid
def looptru(listtoloop):
    questions  = ""
    for item in listtoloop:
        questions = questions + "\n" + str(item)
    return questions

def generateMathQuestionsPlusMinus():
    awns = []
    variant = "Variant:" + str(randint(100000, 999999))
    qus = [variant]

    for index in range(1, 10):
        q = str(randint(1,10)) + "+" + str(randint(1,10))
        awns.append(eval(q))
        qus.append(q + "=")

    for index in range(1, 10):
        q = str(randint(10,20)) + "-" + str(randint(1,10))
        awns.append(eval(q))
        qus.append(q + "=")

    a = input("Need awnser key?(y/n):")
    b = str(looptru(awns)) + "\n\n" + str(looptru(qus)) if a == "y" else str(looptru(qus))
    variantUuid =  str(uuid.uuid4())
    idAwns = variantUuid + "awns.txt"
    awnserkey = open(idAwns, "w")
    awnserkey.write(str(looptru(awns)))
    idQus = variantUuid + "qus.txt"
    Queskey = open(idQus, "w") 
    Queskey.write(str(looptru(qus)))
    return b