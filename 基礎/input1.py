#inputの書き方について

def sample_function(x, y): #関数の定義
    z = x + y
    return z # zの計算結果を返す。

x = int(input()) # x = input()だとstr型だと認識される。
y = int(input()) 

# 例えば 
# x = input()   で1を入力
# y = input()   で2を入力にしてしまうと、
# print(z)は"12"となってしまい、単に文字としての"1"と"2"を合わせただけになる。
# int関数を使う事で文字列を整数に変換して取得する。

z = sample_function(x, y)
print(z)