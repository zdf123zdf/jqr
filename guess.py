import random
import time

# 猜数字
def csz():
    guess_limit = 3  # 最多猜测次数
    scores = []  # 战绩
    cycle = 0  # 第几轮
    while True:
        cycle += 1
        answer = random.randint(1, 10)
        is_right = False  # 记录是否猜对

        begin_time = time.time()
        for i in range(3):
            guess = int(input('请输入1-10之间的数字:'))
            if guess == answer:
                is_right = True
                break
            elif guess > answer:
                print("哥，大了大了~~~", end=' ')
            else:
                print('嘿，小了，小了~~~', end=' ')
            if i < guess_limit - 1:
                print("再试一次吧!")

        # 处理结果
        if is_right:
            print('恭喜你，你猜对了！')
        else:
            print('机会用光咯T_T')
        end_time = time.time()
        use_time = end_time - begin_time  # 用了多少时间
        print(f'共用时{int(use_time)}秒')

        # 保存战绩
        scores.append((cycle, is_right, int(use_time)))
        best_sores = min(scores, key=lambda x: x[2] if x[1] else 9999)
        print('===========战绩============')
        for _cycle, _is_right, _use_time in scores:
            label = '胜利' if is_right else '失败'
            best_label = 'o(*￣︶￣*)o' if (_cycle == best_sores[0] and best_sores[1]) else ''  # 设定最好的标记
            print(f'{_cycle}轮,{label},{_use_time},{best_label}')

        print('===========================')

        con = input('是否要继续游戏？输入y继续，否则直接回车')
        if con != 'y':
            print('游戏结束，不玩啦^_^')
            break  # 退出游戏

#猜拳
def cq():
    user = int(input('请出拳 0(石头) 1(剪刀) 2(布):'))
    if user > 2:
        print('不能输入大于2的值,请重新输入')
        cq()
    else:
        data = ['石头', '剪刀', '布']
        com = random.randint(0, 2)
        print('您出的是{},咸鱼出的是{}'.format(data[user], data[com]))
        if user == com:
            print('平局')
        elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com == 0):
            print('你赢了')
        else:
            print('你输了')
        con = input('是否要继续游戏？输入y继续，否则直接回车')
        if con != 'y':
            return
        else:
            cq()

