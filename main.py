from answerkey import answerkey
from tabulate import tabulate

# edit file name here
filename = "test"
filename+=".txt"

# opening user response text file
file = open(filename,'r')
# creating a custom list item for each question response
responseList = file.read().strip().replace("\n","\t").split("\t")

# converting each question response in individual list item of length 3
# Ex: [Question no, response, question type]
userResponseList = [responseList[x:x+3] for x in range(0, len(responseList),3)]

# creating length for dedicated marking scheme
questionType1MarksAptitude =[1,2,3,4,5]     # for 1mark aptitude questions
questionType2MarksAptitude =[6,7,8,9,10]    # for 2mark aptitude questions
questionType1MarkSubjective = [x for x in range(11,26)] # for 1mark subjective questions
questionType2MarkSubjective = [x for x in range(26,66)] # for 1mark subjective questions

def calculateScore(userResponseList):
    # initialising score to 0
    userScore = 0
    # an empty list for displaying summary in tabular format
    resultingList =[]
    
    # iterating over each question
    for i in range(1,66):
        # rounding score upto 2 decimal places
        userScore = round(userScore,2)
        # variables for storing current question number, user response and correct answer key
        currentQuestionNumber = answerkey[i-1][0]
        currentUserResponse = userResponseList[i-1][1]
        currentUserResponseAnswer = answerkey[i-1][1]
        # an empty list for displaying summary in tabular format for each question
        innerList =[]
        # a switch case to check type of question MCQ,MSQ,NAT
        match userResponseList[i-1][2]:
            case "MCQ":
                # adding command items such as quesiton number user resposne and correct answer for summary purpose
                innerList.append(currentQuestionNumber)
                innerList.append(currentUserResponse)
                innerList.append(currentUserResponseAnswer)
                # if the user response matches correct answer
                if currentUserResponse == currentUserResponseAnswer:
                    innerList.append("Correct")
                    # check if the question is of 1 marker
                    if(int(answerkey[i-1][0]) in questionType1MarksAptitude) or (int(answerkey[i-1][0]) in questionType1MarkSubjective):
                        innerList.append("Adding - 1")
                        userScore+=1    # adding 1 mark

                    # check if the question is of 2 marker
                    if(int(answerkey[i-1][0]) in questionType2MarksAptitude) or (int(answerkey[i-1][0]) in questionType2MarkSubjective):
                        innerList.append("Adding - 2")
                        userScore+=2    # adding 2 mark   
                    innerList.append(round(userScore,2))
                    innerList.append("MCQ")
                    
                    # if unattempted
                elif currentUserResponse == "--":
                    innerList.append("Unattempted")
                    innerList.append("------")
                    innerList.append(round(userScore,2))
                    innerList.append("MCQ")
                
                # if the user response is incorrect in case of MCQs deduct marks
                else:
                    innerList.append("Incorrect")
                    # if it's a 1 marker, deduct 1/3 or 0.33
                    if(int(answerkey[i-1][0]) in questionType1MarksAptitude) or (int(answerkey[i-1][0]) in questionType1MarkSubjective):
                        innerList.append("Deducting- 1/3")
                        userScore-=1/3
                    # if it's a 2 marker, deduct 2/3 or 0.66
                    if(int(answerkey[i-1][0]) in questionType2MarksAptitude) or (int(answerkey[i-1][0]) in questionType2MarkSubjective):
                        innerList.append("Deducting - 1/3")
                        userScore-=2/3
                    innerList.append(round(userScore,2))
                    innerList.append("MCQ")

                # checking Multiple select questions
            case "MSQ":
                innerList.append(currentQuestionNumber)
                innerList.append(currentUserResponse)
                innerList.append(currentUserResponseAnswer)
                # if the question is unattempted, print it
                if currentUserResponse == "--":
                    innerList.append("Unattempted")
                    innerList.append("------")
                    innerList.append(round(userScore,2))
                    innerList.append("MSQ")
                    # if the user respose is correct add scores
                elif currentUserResponse == currentUserResponseAnswer:
                    innerList.append("Correct")
                    if(int(answerkey[i-1][0]) in questionType1MarksAptitude) or (int(answerkey[i-1][0]) in questionType1MarkSubjective):
                        innerList.append("Adding - 1")
                        userScore+=1
                    if(int(answerkey[i-1][0]) in questionType2MarksAptitude) or (int(answerkey[i-1][0]) in questionType2MarkSubjective):
                        innerList.append("Adding - 2")
                        userScore+=2
                    innerList.append(round(userScore,2))
                    innerList.append("MSQ")

                # if the user response is in correct just print the summary for that question (no negatives)
                elif currentUserResponse != currentUserResponseAnswer:
                    innerList.append("Incorrect")
                    innerList.append("-----")
                    innerList.append(round(userScore,2))
                    innerList.append("MSQ")

            # Numerical answer type question
            case "NAT":
                innerList.append(currentQuestionNumber)
                innerList.append(currentUserResponse)
                innerList.append(currentUserResponseAnswer)
                # if not attempted just print the summary
                if currentUserResponse == "--":
                    innerList.append("Unattempted")
                    innerList.append("------")
                    innerList.append(round(userScore,2))
                    innerList.append("NAT")
                # if the reponse is correct add the scores
                elif currentUserResponse == currentUserResponseAnswer:
                    innerList.append("Correct")
                    if(int(answerkey[i-1][0]) in questionType1MarksAptitude) or (int(answerkey[i-1][0]) in questionType1MarkSubjective):
                        innerList.append("Adding - 1")
                        userScore+=1
                    if(int(answerkey[i-1][0]) in questionType2MarksAptitude) or (int(answerkey[i-1][0]) in questionType2MarkSubjective):
                        innerList.append("Adding - 2")
                        userScore+=2
                    innerList.append(round(userScore,2))
                    innerList.append("NAT")
                # if the response is incorrect just print the summary
                elif currentUserResponse != currentUserResponseAnswer:
                    innerList.append("Incorrect")
                    innerList.append("-----")
                    innerList.append(round(userScore,2))
                    innerList.append("NAT")
            case other: pass
        # append the summary of each question to the outer list
        resultingList.append(innerList)
    
    # print the entire summary in tabular format
    print(tabulate(resultingList,headers=["Question No:","Response","Correct Answer", "Correct/Incorrect","Action","Score","Type"]))
    # Print the final score
    print(f"Final Estimated Score: {userScore}")
    
scheme = """
Aptitude
--------------------
Q1 - Q5   1 Mark each
Q6 - Q10  2 Mark each

Subjective
--------------------
Q11- Q25  1 Mark each
Q26- Q65  2 Mark each

Question Types
Q1 - Q10 MCQ    Aptitude 1 & 2 Mark each

1 Mark each
------------
Q11 - Q21 MCQ   Negative Marking
Q22 - Q29 MSQ   Non Negative marking
Q30 - Q35 NAT   Non Negative marking

2 Mark each
------------
Q36 - Q48 MCQ   Negative Marking
Q49 - Q55 MSQ   Non Negative marking
Q56 - Q65 NAT   Non Negative marking
"""
print(scheme)
calculateScore(userResponseList)