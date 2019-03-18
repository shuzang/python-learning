"""
@title:商人过河问题
@author:shuzang
@date:2018-9-14 17:03
@brief: 三名商人各带一个随从过河，一只小船只能容纳两个人，随从们约定，只要在河的任何一岸，
一旦随从人数多于商人人数就杀人越货，但是商人们知道了他们的约定，并且如何过河的大权掌握在
商人们手中，商人们该采取怎样的策略才能安全过河呢？。
"""
# -*- coding: utf-8 -*-
# https://blog.csdn.net/luoyhang003/article/details/50468316
import random


class Boat(object):
    def __init__(self, merchants, servants, capacity):
        self.merchants = merchants
        self.servants = servants
        self.capacity = capacity

        print("初始状态: {:d}个商人, {:d}个随从".format(merchants, servants))

    '''创建允许状态集合'''

    def allowset(self):
        allowset = []
        for i in range(self.merchants + 1):
            for j in range(self.servants + 1):
                if i == 0:
                    allowset.append([i, j])
                elif i == self.merchants:
                    allowset.append([i, j])
                elif (i >= j
                      and ((self.merchants - i) >= (self.servants - j))):
                    allowset.append([i, j])
        return allowset

    '''创建允许决策集合'''

    def allowaction(self):
        allowactionset = []
        for i in range(self.capacity + 1):
            for j in range(self.capacity + 1):
                if (i + j) <= self.capacity and (i + j) != 0:
                    allowactionset.append([i, j])
        return allowactionset

    '''渡河'''

    def solve(self, allowactionset, allowstate):
        count = 1
        current = (self.merchants, self.servants)
        while current != [0, 0]:
            move = allowactionset[random.randint(0, len(allowactionset) - 1)]
            temp = [
                current[0] + ((-1)**count) * move[0],
                current[1] + ((-1)**count) * move[1]
            ]
            if (temp in allowstate):
                current = [
                    current[0] + ((-1)**count) * move[0],
                    current[1] + ((-1)**count) * move[1]
                ]
                if (count % 2 == 1):
                    print("此岸——>彼岸：{:d}个商人,{:d}个随从".format(move[0], move[1]))
                elif (count % 2 == 0):
                    print("此岸<——彼岸：{:d}个商人,{:d}个随从".format(move[0], move[1]))

            count = count + 1


def main():
    boat = Boat(3, 3, 2)
    allowstate = boat.allowset()
    print("允许状态集合为：")
    print(allowstate)

    actionset = boat.allowaction()
    print("允许决策集合为：")
    print(actionset)

    boat.solve(actionset, allowstate)


if __name__ == '__main__':
    main()
