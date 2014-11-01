__author__ = 'nouma'
#coding:utf-8
from random import randint
import operator
import time

time_allow = 10
def Input_convert( str ):
    "Covert a str to int number with except handling"
    num = 0
    try:
        num = int(str)
    except ValueError:
        print '输入错误，请输入一个输入数字!'
        num = None
    return num

def Pratice( option, num_range = 50 ):
    "Generate two nums not greater than num_ran randomly, and verify the tester to give the right answer"
    num1 = randint(0, num_range)
    num2 = randint(0, num_range)
    option_dict = { '+':operator.add, '-':operator.sub, 'X':operator.mul, '/':operator.div}
    right_count = 0
    test = None
    type = option[randint(0, len(option)-1)]
    if (type == '-' or type == '/') and ( num1 < num2 ):
        num_tmp = num1
        num1 = num2
        num2 = num_tmp

    t1 = time.time()
    while test== None:
        answer = option_dict[type](num1, num2)
        test = raw_input('%-3d %s %-3d = ' %( num1, type, num2))
        test = Input_convert(test)
    time_cost = time.time() -t1

    if answer == test:
        if time_cost < time_allow:
            print '答案正确! 用时%f秒!' % time_cost
            right_count = 1
        else:
            print '答案正确! 用时%f秒,已超时,不得分!'% time_cost
    else:
        print '答案错误!\n正确答案是: %d' % answer
    return right_count

def Letter():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cha_test = alphabet[randint(0, 24)]
    type_test = randint(0,1)
    t1 = time.time()
    if type_test == 0:
        test = raw_input( '%s的大写字母是： ' % cha_test)[0]
        answer = cha_test.upper()
    else:
        test = raw_input( '%s的小写字母是： ' % cha_test.upper())[0]
        answer = cha_test
    time_cost = time.time() -t1

    if answer == test:
        if time_cost < time_allow:
            print '答案正确! 用时%f秒!' % time_cost
            right_count = 1
        else:
            print '答案正确! 用时%f秒,已超时,不得分!'% time_cost
    else:
        print '答案错误!\n正确答案是: %d' % answer
    return right_count


def main():
    round_times = 10
    right_count = 0
    for i in range(round_times):
        print '%s第%d题%s' % ('-'*10, i+1,'-'*10)
        #right_count += Pratice('X', 9)
        right_count += Letter()
    print '测试完成，成绩是%3.1f分' % (right_count * 100.0 / round_times)


if __name__ == '__main__':
    main()