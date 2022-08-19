# question_list=["How many continents are there?", "What is capital of India?", "Which course is taught in navgurukul?"]
# option_list=[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
# answer_list=[3,4,1]
def option(index):
    j=0
    while j<len(option_list[index]):
        print(j+1,option_list[index][j])
        j=j+1
    user_ans = int(input('enter your answer:'))
    if user_ans==answer_list[index]:
        return True
    else:
        return False
def que():
    index=0
    while index<len(question_list):
        print("Q.",index+1,question_list[index],"?")
        result=option(index)
        if result=="no":
            index+=1
        elif result==True:
            print("Congratulations!")
        else:
            print("you lose")
            break   
        index+=1
question_list=["How many continents are there?", "What is capital of India?", "Which course is taught in navgurukul?"]
option_list=[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
answer_list=[3,4,1]
def main():
    que()
main()