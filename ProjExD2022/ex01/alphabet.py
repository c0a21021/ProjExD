import random

tyousen_kaisu = 10
ketuson_mozi = 2
max_kaisu = 3


def shutudai(alf_lst):
    print("対象文字:")
    alf = random.sample(alf_lst, k = tyousen_kaisu)
    del_alf = random.sample(alf, k = ketuson_mozi)
    [print(i, end = " ") for i in alf]
    print("\n欠損文字")
    [print(i, end = " ") for i in del_alf]
    return del_alf
    for i in alf:
        if i in del_alf:
            #print(i)
            alf.remove(i)
        else:
            pass
    print("\n表示文字")
    [print(i, end = " ") for i in alf]



def kaitou(del_alf):
    flag = True
    ans = int(input("\n欠損文字列はいくつあるでしょうか？"))
    if ans == ketuson_mozi:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(len(del_alf)):
            alf_1 = input(str(i + 1) + "つ目の文字を入力してください:")
            if alf_1 not in del_alf:
                print("不正解です。またチャレンジしてください")
                flag = False
                break
            else:
                continue
    else:
        print("不正解です。またチャレンジしてください")
        flag = False
    return flag
    

if __name__ == "__main__":
    alf_lst = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(max_kaisu):
        ans_lst = shutudai(alf_lst)
        flag = kaitou(ans_lst)
        if flag == True:
            break