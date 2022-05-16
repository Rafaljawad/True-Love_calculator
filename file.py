
print("Welcome to the True Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your partner name? \n")

combin_names=name1+name2 
name_in_lower_case=combin_names.lower()
t=name_in_lower_case.count("t")
r=name_in_lower_case.count("r")
u=name_in_lower_case.count("u")
e=name_in_lower_case.count("e")
true=t+r+u+e
# print(true)
l=name_in_lower_case.count("l")
o=name_in_lower_case.count("o")
v=name_in_lower_case.count("v")
e=name_in_lower_case.count("e")
love=l+o+v+e
# print(love)
true_love_score_string=str(true)+str(love)# here will cancatenate the true and love together and convert them to string so us not to add them as anumber
true_love_score=int(true_love_score_string)# here convert them to int them so as to use if statement on them
print(f"{true_love_score_string}%")

if true_love_score<50:
    print(f"your love score is: {true_love_score}% , your love story in danger")
elif true_love_score>50 and true_love_score<70:
    print(f"your love score is: {true_love_score}% , your love story Ok")
else:
    print(f"your love score is: {true_love_score}%, you live a real lovestory")