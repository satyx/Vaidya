from tkinter import *
import numpy as np

User_Array = [0, 0, 0, 0, 0, 0]

# Common diseases ...
# 1 fever
# 2 cough
# 3 headache
# 4 skin_rashes
# 5 sore_throat

# d1 viral_fever
# d2 sinusitis
# d3 allergic rhinitis
# d4 asthma
# d5 RTI
# d6 measles
# d7 mumps
# d8 gerd
# d9 tuberculosis
# d10 pharyngitis
# d11 laryngitis


def myCommand1():
    if CheckVar1.get() == 1:
        User_Array[0] = var1.get()
    if CheckVar2.get() == 1:
        User_Array[1] = var2.get()
    if CheckVar3.get() == 1:
        User_Array[2] = var3.get()
    if CheckVar4.get() == 1:
        User_Array[3] = var4.get()
    if CheckVar5.get() == 1:
        User_Array[4] = var5.get()
    if CheckVar6.get() == 1:
        User_Array[5] = var6.get()
    print(User_Array)

    # User_Array is an array which consists of intensities of all common symptoms given by the user

    user_input = User_Array
    user_output_array = ["very_low", "very_low",
                         "very_low", "very_low", "very_low", "very_low"]
    for i in range(0, 6):
        if user_input[i] in range(1, 4):
            user_output_array[i] = "low"
        elif user_input[i] in range(4, 7):
            user_output_array[i] = "medium"
        elif user_input[i] in range(7, 11):
            user_output_array[i] = "high"
    print(user_output_array)
    # User_Output_Array is a changed form of user array (changing crisp intensities to fuzzy(low,medium,high) for each common symptom)

    # Rule Base
    d1 = {1: "high", 2: "low", 3: "medium", 4: "low", 6: "medium"}
    d2 = {1: "low", 2: "low", 3: "medium"}
    d3 = {1: "very_low", 2: "medium", 4: "medium", 6: "medium"}
    d4 = {1: "very_low", 2: "high"}
    d5 = {1: "medium", 5: "medium"}
    d6 = {1: "high", 2: "low", 4: "high"}
    d7 = {1: "medium", 3: "low"}
    d8 = {1: "very_low", 2: "low"}
    d9 = {1: "low", 2: "high"}
    d10 = {1: "medium", 2: "low", 3: "low", 5: "high", 6: "medium"}
    d11 = {1: "low", 5: "medium"}

    # Making all rule base templates
    # will help in passing them all inside a loop ...
    diseases = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11]

    print("The disease rule base is:")
    print(diseases)

    fever = {'very_low': np.array([0, 0, 0.5]), 'low': np.array(
        [0, 0.5, 5]), 'medium': np.array([0, 5, 10]), 'high': np.array([5, 10, 10])}
    cough = {'very_low': np.array([0, 0, 0.5]), 'low': np.array(
        [0, 0.5, 5]), 'medium': np.array([0, 5, 10]), 'high': np.array([5, 10, 10])}
    headache = {'very_low': np.array([0, 0, 0.5]), 'low': np.array(
        [0, 0.5, 5]), 'medium': np.array([0, 5, 10]), 'high': np.array([5, 10, 10])}
    skin_rashes = {'very_low': np.array([0, 0, 0.5]), 'low': np.array(
        [0, 0.5, 5]), 'medium': np.array([0, 5, 10]), 'high': np.array([5, 10, 10])}
    sore_throat = {'very_low': np.array([0, 0, 0.5]), 'low': np.array(
        [0, 0.5, 5]), 'medium': np.array([0, 5, 10]), 'high': np.array([5, 10, 10])}
    sneezing = {'very_low': np.array([0, 0, 0.5]), 'low': np.array(
        [0, 0.5, 5]), 'medium': np.array([0, 5, 10]), 'high': np.array([5, 10, 10])}

    symptoms = {1: fever, 2: cough, 3: headache,
                4: skin_rashes, 5: sore_throat, 6: sneezing}

    list_of_templates = []

    # Loop for Template Making corresponding to each disease
    for d in diseases:
        tmp = np.array([0, 0, 0])
        for i in d:
            tmp = tmp + symptoms[i][d[i]]
        tmp = [x/len(d) for x in tmp]
        list_of_templates.append(tmp)

    print(list_of_templates)

    # Making 11 dictionaries for data given by the user

    U1 = {1: "very_low", 2: "very_low",
          3: "very_low", 4: "very_low", 6: "very_low"}
    U2 = {1: "very_low", 2: "very_low", 3: "very_low"}
    U3 = {1: "very_low", 2: "very_low", 4: "very_low", 6: "very_low"}
    U4 = {1: "very_low", 2: "very_low"}
    U5 = {1: "very_low", 5: "very_low"}
    U6 = {1: "very_low", 2: "very_low", 4: "very_low"}
    U7 = {1: "very_low", 3: "very_low"}
    U8 = {1: "very_low", 2: "very_low"}
    U9 = {1: "very_low", 2: "very_low"}
    U10 = {1: "very_low", 2: "very_low",
           3: "very_low", 5: "very_low", 6: "very_low"}
    U11 = {1: "very_low", 5: "very_low"}

    user = [U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11]

    for U in user:
        for i in U.keys():
            U[i] = user_output_array[i-1]

    print("The dictionaries made from the user data is")
    print(user)

    # Making user templates
    user_template = []

    for U in user:
        tmp = np.array([0, 0, 0])
        for i in U:
            tmp = tmp + symptoms[i][U[i]]
        tmp = [x/len(U) for x in tmp]
        user_template.append(tmp)

    print(user_template)


top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
C1 = Checkbutton(top, text="Fever", variable=CheckVar1, height=5, width=20)
C2 = Checkbutton(top, text="Cough", variable=CheckVar2, height=5, width=20)
C3 = Checkbutton(top, text="Headache", variable=CheckVar3, height=5, width=20)
C4 = Checkbutton(top, text="Skin Rashes",
                 variable=CheckVar4, height=5, width=20)
C5 = Checkbutton(top, text="Sore Throat",
                 variable=CheckVar5, height=5, width=20)
C6 = Checkbutton(top, text="Sneezing",
                 variable=CheckVar6, height=5, width=20)
C1.grid(row=0, column=0)
C2.grid(row=1, column=0)
C3.grid(row=2, column=0)
C4.grid(row=3, column=0)
C5.grid(row=4, column=0)
C6.grid(row=5, column=0)

var1 = IntVar()
scale1 = Scale(top, variable=var1, orient=HORIZONTAL, from_=0, to=10)
scale1.grid(row=0, column=1)
var2 = IntVar()
scale2 = Scale(top, variable=var2, orient=HORIZONTAL, from_=0, to=10)
scale2.grid(row=1, column=1)
var3 = IntVar()
scale3 = Scale(top, variable=var3, orient=HORIZONTAL, from_=0, to=10)
scale3.grid(row=2, column=1)
var4 = IntVar()
scale4 = Scale(top, variable=var4, orient=HORIZONTAL, from_=0, to=10)
scale4.grid(row=3, column=1)
var5 = IntVar()
scale5 = Scale(top, variable=var5, orient=HORIZONTAL, from_=0, to=10)
scale5.grid(row=4, column=1)
var6 = IntVar()
scale6 = Scale(top, variable=var6, orient=HORIZONTAL, from_=0, to=10)
scale6.grid(row=5, column=1)

button1 = Button(top, text='Submit', command=myCommand1)
button1.grid(row=6, column=0)

top.mainloop()
