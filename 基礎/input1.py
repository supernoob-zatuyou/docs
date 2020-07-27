#inputの書き方について

def sample_function(x, y):
    z = x + y
    return z

x = int(input()) # x = input()だとstr型だと認識される？
y = int(input()) 

#例えば 
# x = input()   で1を入力
# y = input()   で2を入力にしてしまうと、
# print(z)は"12"となってしまい、単に文字としての"1"と"2"を合わせただけになる。

z = sample_function(x, y)
print(z)