def studentInfo(firstName, lastName, age, **kwargs):

    student = {"first_name": firstName, "last_name": lastName, "age": age}

    for key, value in kwargs.items():

        student[key] = value

    return student


result = studentInfo("Neco", "Gedikli", 23, school = "lanet olsun ki halic", department = "Computer Engineering",
                     Gpa = 3.21, City = "Istanbul")

print(result)