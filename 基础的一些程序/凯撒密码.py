"""
@title:凯撒密码.py
@author:shuzang
@date:2018-8-10 9:01
@brief:
凯撒密码是古罗马凯撒大帝用来对军事情报进行加解密的算法，它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，即，字母表的对应关系如下：
原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
假设用户可能使用的输入仅包含小写字母a~z和空格，请编写一个程序，对输入字符串进行凯撒密码加密，直接输出结果，其中空格不用进行加密处理。使用input()获得输入。
"""


def change(c, i):
    c = c.lower()  # 将字符全部转换为小写
    num = ord(c)
    if num >= 97 and num <= 122:
        num = 97 + ((num-97)+i) % 26
    return chr(num)


def kaisa_jiami(string):
    string_new = ''
    for s in string:
        string_new += change(s, 3)
    print(string_new)
    return string_new


def kaisa_jiemi(string):
    string_new = ''
    for s in string:
        string_new += change(s, -3)
    print(string_new)
    return string_new


def main():
    print("请输入要进行的操作(1.凯撒加密 2.凯撒解密):")
    choice = input()
    if choice == '1':
        string = input("请输入需要加密的字符串:")
        kaisa_jiami(string)
    elif choice == '2':
        string = input('请输入需要解密的字符串:')
        kaisa_jiemi(string)
    else:
        print('输入错误,请重试!')
        main()


if __name__ == "__main__":
    main()
