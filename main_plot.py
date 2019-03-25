# -*- coding: utf-8 -*-
import pdb
def debug_signal_handler(signal, frame):
    pdb.set_trace()

from pythondb import DataBase
import matplotlib.pyplot as plt
import numpy as np

def question_distribution():
    questionlinks_date = DataBase(0, '0', '0', 0, '0', '0', 0).select_questionlinks_date()
    Feb = 0
    Jan = 0
    Dec = 0
    Nov = 0
    Oct = 0
    Sep = 0
    Aug = 0
    July = 0
    June = 0
    May = 0
    Apr = 0
    Mar = 0
    sumnumber = 0
    for links in questionlinks_date:
        date = str(links[2])
        if date.find('2019/2')>=0: Feb = Feb + 1
        if date.find('2019/1')>=0: Jan = Jan + 1
        if date.find('2018/12')>=0: Dec = Dec + 1
        if date.find('2018/11')>=0: Nov = Nov + 1
        if date.find('2018/10')>=0: Oct = Oct + 1
        if date.find('2018/9')>=0: Sep = Sep + 1
        if date.find('2018/8')>=0: Aug = Aug + 1
        if date.find('2018/7')>=0: July = July + 1
        if date.find('2018/6')>=0: June = June + 1
        if date.find('2018/5')>=0: May = May + 1
        if date.find('2018/4')>=0: Apr = Apr + 1
        if date.find('2018/3')>=0: Mar = Mar + 1
        sumnumber = sumnumber + 1

    monthlist = ['Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb']
    numberlist = [Mar, Apr, May, June, July, Aug, Sep, Oct, Nov, Dec, Jan, Feb]
    return monthlist, numberlist, sumnumber

def answer_distribution():
    tv_sitcoms_answercount = DataBase(0, '0', '0', 0, '0', '0', 0).select_answercount()
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    tenmore = 0
    twentymore = 0
    fiftymore = 0
    hundredmore = 0
    sumcount = 0
    for links in tv_sitcoms_answercount:
        answercount = int(links[1])
        if answercount == 0: zero = zero + 1
        if answercount == 1: one = one + 1
        if answercount == 2: two = two + 1
        if answercount == 3: three = three + 1
        if answercount == 4: four = four + 1
        if answercount == 5: five = five + 1
        if answercount == 6: six = six + 1
        if answercount == 7: seven = seven + 1
        if answercount == 8: eight = eight + 1
        if answercount == 9: nine = nine + 1
        if answercount == 10: ten = ten + 1
        if answercount > 10 and answercount <= 20: tenmore = tenmore + 1
        if answercount > 20 and answercount <= 50: twentymore = twentymore + 1
        if answercount > 50 and answercount <= 100: fiftymore = fiftymore + 1
        if answercount > 100: hundredmore = hundredmore + 1
        sumcount = sumcount + 0
    namelist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10+', '20+', '50+', '100+']
    countlist = [zero, one, two, three, four, five, six, seven, eight, nine, ten, tenmore, twentymore, fiftymore, hundredmore]
    return namelist, countlist, sumcount

def plot():
    monthlist, numberlist, sumnumber = question_distribution()
    namelist, countlist, sumcount = answer_distribution()
    # Questions Last Followed
    plt.subplot(211)
    plt.bar(monthlist, numberlist)
    plt.ylim(0, 350)
    for x, y in zip(monthlist, numberlist):
        plt.text(x, y+30, '%.0f' % y, ha ='center', va='top')
    plt.xlabel('A Year Span (From Mar, 2018 to Feb, 2019)')
    plt.ylabel('Questions Last Followed Number')
    plt.title('Questions Last Followed Number Varing with Time')
    plt.tight_layout()
    # Answercount Distribution
    plt.subplot(212)
    plt.bar(namelist, countlist)
    plt.ylim(0, 1000)
    for x, y in zip(namelist, countlist):
        plt.text(x, y+85, '%.0f' % y, ha='center', va='top')
    plt.xlabel('Answercount')
    plt.ylabel('Answercount Number')
    plt.title('Answercount Distribution')
    plt.tight_layout()
    plt.savefig(".\pictures\plot1.png")
    plt.show()

if __name__ == "__main__":
    question_distribution()
    answer_distribution()
    plot()