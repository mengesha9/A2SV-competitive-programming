def gradingStudents(grades):
    arr=[]
    for grade in grades:
        if grade>=38:
            mod5=grade%5
            if mod5>=3:
                grade+=(5-mod5)
        arr.append(grade)
        grade=grade +1
    return arr 
