#Write a program to ask a student for their percentage mark and convert this to a grade.
#The conversion will be done in a function called mark_grade


#Ask the user for their target grade and print this with their mark
# If their target grade > exam grade display a suitable message
# If their target grade = exam grade display a suitable message
# If their target grade < exam grade display a suitable message

def mark_grade (permark):
    if permark >=90:
        return "A"

    elif permark <90 and permark >=80 :
        return "B"

    elif permark <80 and permark >=70 :
        return "C"

    elif permark <70 and permark >=60 :
        return "D"

    elif permark <60 and permark >=50 :
        return "E"

    elif permark <50 :
        return "FAIL"

def grade_mark (want,permark):
    if (want == "A" or want =="a") and permark >= 90:
        return "achieved"
    elif (want == "A" or want == "a") and permark <90:
        return "did not achieve"

    elif (want == "B" or want =="b") and permark >=80 and permark <90:
        return "achieved"
    elif (want == "B" or want =="b") and permark >=90:
        return "exceeded"
    elif (want == "B" or want == "b") and permark >80:
        return "did not achieve"

    elif (want == "C" or want =="c") and permark >=70 and permark <80:
        return "achieved"
    elif (want == "C" or want =="c") and permark >=80:
        return "exceeded"
    elif (want == "C" or want == "c") and permark >70:
        return "did not achieve"

    elif (want == "D" or want == "d") and permark >= 60 and permark < 70:
        return "achieved"
    elif (want == "D" or want == "d") and permark >= 70:
        return "exceeded"
    elif (want == "D" or want == "d") and permark > 60:
        return "did not achieve"

    elif (want == "E" or want == "e") and permark >= 50 and permark < 60:
        return "achieved"
    elif (want == "E" or want == "e") and permark >= 60:
        return "exceeded"
    elif (want == "E" or want == "e") and permark > 50:
        return "did not achieve"

print("Hi, I'm here to calculate your grade!")
want = str(input("First though, what grade are you hoping for?"))
permark = int(input("What % mark did you get?"))

grade = mark_grade(int(permark))
wanted = grade_mark(want,permark)
if wanted == "achieved":
    endit = "Congratulations!"

elif wanted == "exceeded":
    endit = "OMG! CONGRATULATIONS! THAT IS EPIC!!!"

elif wanted == "did not achieve":
    endit = "Better luck next time!"

print("Your grade is", grade, "you", wanted,"the", want, "you wanted.", endit)




