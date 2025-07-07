# string reversing type 1
def str_rev(n):
    print(n[::-1])
str_rev("hello")
#string reversal type 2
def rev_str(n):
    a=reversed(n)
    print(''.join(a))
rev_str("hello")
def re_st(n):
    a=''
    for i in n:
        a=i+a
    print(a)
re_st("hello")