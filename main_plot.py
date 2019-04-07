# -*- coding: utf-8 -*-
import datetime
import numpy as np
import pdb
def debug_signal_handler(signal, frame):
    pdb.set_trace()

from pythondb import DataBase
import matplotlib.pyplot as plt
import numpy as np


def question_distribution():
    questionlinks_date = DataBase(0, '0', '0', 0, '0', '0', 0).select_questionlinks_date()
    Mar, Mar1, Mar2, Mar3, Mar4 = 0, 0, 0, 0, 0
    Feb, Feb1, Feb2, Feb3, Feb4 = 0, 0, 0, 0, 0
    Jan, Jan1, Jan2, Jan3, Jan4 = 0, 0, 0, 0, 0
    Dec, Dec0, Dec1, Dec2, Dec3, Dec4= 0, 0, 0, 0, 0, 0

    for links in questionlinks_date:
        date = str(links[2])
        # if date.find('2019/3')>=0: Mar = Mar + 1
        # if date.find('2019/2')>=0: Feb = Feb + 1
        # if date.find('2019/1')>=0: Jan = Jan + 1
        # if date.find('2018/12')>=0: Dec = Dec + 1
        datenorm = datetime.datetime.strptime(date, '%Y/%m/%d')
        datenum = int(datenorm.strftime('%Y%m%d'))
        if datenum >= 20190321: Mar4 = Mar4 + 1
        if datenum >= 20190314 and datenum < 20190321: Mar3 = Mar3 + 1
        if datenum >= 20190307 and datenum < 20190314: Mar2 = Mar2 + 1
        if datenum >= 20190301 and datenum < 20190307: Mar1 = Mar1 + 1
        if datenum >= 20190222 and datenum < 20190301: Feb4 = Feb4 + 1
        if datenum >= 20190215 and datenum < 20190222: Feb3 = Feb3 + 1
        if datenum >= 20190208 and datenum < 20190215: Feb2 = Feb2 + 1
        if datenum >= 20190201 and datenum < 20190208: Feb1 = Feb1 + 1
        if datenum >= 20190125 and datenum < 20190201: Jan4 = Jan4 + 1
        if datenum >= 20190118 and datenum < 20190125: Jan3 = Jan3 + 1
        if datenum >= 20190111 and datenum < 20190118: Jan2 = Jan2 + 1
        if datenum >= 20190104 and datenum < 20190111: Jan1 = Jan1 + 1
        if datenum >= 20181228 and datenum < 20190104: Dec4 = Dec4 + 1
        if datenum >= 20181221 and datenum < 20181228: Dec3 = Dec3 + 1
        if datenum >= 20181214 and datenum < 20181221: Dec2 = Dec2 + 1
        if datenum >= 20181206 and datenum < 20181214: Dec1 = Dec1 + 1
        
    monthlist = ['Dec1', 'Dec2', 'Dec3', 'Dec4',
                'Jan1', 'Jan2', 'Jan3', 'Jan4', 
                'Feb1', 'Feb2', 'Feb3', 'Feb4',
                'Mar1', 'Mar2', 'Mar3', 'Mar4']
    numberlist = [Dec1, Dec2, Dec3, Dec4,  
                Jan1, Jan2, Jan3, Jan4, 
                Feb1, Feb2, Feb3, Feb4, 
                Mar1, Mar2, Mar3, Mar4]
    nummean = np.mean(numberlist)
    
    return monthlist, numberlist, nummean

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
    monthlist, numberlist, nummean = question_distribution()
    namelist, countlist, sumcount = answer_distribution()
    # Questions Last Followed
    plt.subplot(211)
    plt.bar(monthlist, numberlist)
    lim=[nummean]*16
    plt.plot(lim, 'r--', label = 'mean of questions last followed in weeks')

    plt.legend()
    plt.ylim(0, 390)
    for x, y in zip(monthlist, numberlist):
        plt.text(x, y+35, '%.0f' % y, ha ='center', va='top')
    plt.xlabel('A Season Span (From Dec, 2018 to Mar, 2019)')
    plt.ylabel('Questions Last Followed Number')
    plt.title('Questions Last Followed Number Varing in Weeks')
    plt.tight_layout()
    # Answercount Distribution
    plt.subplot(212)
    plt.bar(namelist, countlist)
    plt.ylim(0, 1950)
    for x, y in zip(namelist, countlist):
        plt.text(x, y+180, '%.0f' % y, ha='center', va='top')
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