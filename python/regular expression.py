# import re
# pattern='hai'
# if re.match(pattern,'hai how are you'):                              #checks for a match for only at the begining of the string
#     print('yes')
# else:
#     print('sorry')


# import re
# pattern='hai'
# if re.search(pattern,'hello hai how are you'):                                #returns a match object if there is a match anywhere in the string
#     print('yes')                                                                             
# else:
#     print('sorry')


# import re                                                                                     #returns a list containing all matches
# pattern='you'                                                                                                     
# b=re.findall(pattern,'Hi How are you,Who are you,Where are you going,Where are you') 
# c=len(b) 
# print({pattern:c})
# print(len(b))


# import re
# pattern='nandana'
# b=re.findall(pattern,'difjufidjnandanaqdiejdidjnandanawdjweidjinandanaiisjinandana')
# print(b)
# print(len(b))


# import re
# a='hai nandana who are you'
# pattern='who'
# b=re.sub(pattern,'how',a)                                                         #replace one or many matches with a string
# print(b)


# import re
# a='hai nandana who are you'
# pattern=input('enter the word to change')
# c=input('enter the new word')
# b=re.sub(pattern,c,a)
# print(b)



# a=('mango,apple,orange,grape')
# b=a.split(',')
# print(a)



# import re
# text = "apple, orange;banana grape|melon"
# pattern =r'[,\s;|]+'                                                        #split a string by the occurences of a pattern      
# split_text = re.split(pattern,text)
# print(split_text)




   