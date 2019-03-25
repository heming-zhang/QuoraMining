from pythondb import DataBase
import numpy as np


def classify_doc():
    questionlist_feb = []
    answerlist_feb = []
    alltextlist_feb = []
    # fw = open('./textfiles/Feb, 2019.txt', 'w')
    # fr = open('./textfiles/Feb, 2019.txt', 'r')
    tv_sitcoms_answertext = DataBase(0, '0', '0', 0, '0', '0', 0).select_answertext()
    for text in tv_sitcoms_answertext:
        date = str(text[2])
        question = str(text[4])
        # view_weight = int(text[5]) # weight to improve topic mining
        answer = str(text[6])
        # 剩下的事情就是将文本写入文件，然后把数进行清洗，然后进行主题挖掘
        if date.find('2019/2')>=0:
            questionlist_feb.append(question)
            answerlist_feb.append(answer)
            alltextlist_feb.append(question)
            alltextlist_feb.append(answer)
            # print(date, question, view_weight, answer)
    print(alltextlist_feb)
    return 0


if __name__ == "__main__":
    classify_doc()