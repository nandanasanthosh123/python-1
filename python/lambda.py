# f=lambda a: a*a
# a=lambda x,y:x*y
# print(a(4,5))


# filter operation

# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(lambda x: x%2==0,a)              #to find out even numbers
# print(list(b))


# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(lambda x: x%2==1,a)              #to find  out odd numbers
# print(list(b))


# for i in range(1,31):
#     if i%2==1:                           #for odd
#         print(i)


# for i in range(1,31):
#     if i%2==0:                           #for even
#         print(i)



# a=[1,2,3,4,5]
# b=map(lambda x:x**2,a)                  #to find out square
# print(list(b))


# a=[1,2,3,4,5]
# b=map(lambda x:x**3,a)                  #to find out cube
# print(list(b))



# from functools import reduce
# numbers=[1,2,3,4,5]
# product=reduce(lambda x,y:x*y,numbers)
# print(product)