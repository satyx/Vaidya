from tkinter import *
import numpy as np

User_Array = [0, 0, 0, 0, 0, 0]
# QofD is a 2d array containing the questions to be asked. The row in the 2d array is the value (disease number -1)
QofD = [None]*12

QofD[0] = ["Are you feeling Loss of Appetite?", "Are you feeling Running Nose?",
           "Are you experiencing Puffiness in your eyes?", "Are you experiencing Fatigue?"]

QofD[1] = ["Are you feeling Nasal Blockage?",
           "Are you feeling Fatigue(TiredNess)?", "Are you experiencing Running Nose?", "Are you experiencing Bad Breath?"]

QofD[2] = ["Are you experiencing Running Nose?",
           "Are you experiencing Watery Eyes?"]

QofD[3] = ["Are you feeling Difficulty in Breathing?", "Are you experiencing Discomfort in your Chest?",
           "Is there a family history of Asthma in your family?"]

QofD[4] = ["Are you feeling Productive Cough?", "Are you feeling Dry Cough?", "Are you experiencing Yellowish Green Sputum?",
           "Are you experiencing Rhinorrhea?", "Are you having difficulty in Swallowing your Food"]

QofD[5] = ["Are you feeling Rhinitis?", "Are you feeling Conjunctivitis?",
           "Are you experiencing Dry Cough", "Are you experiencing Watery Eyes?"]

QofD[6] = ["Are you feeling Loss of Appetite?", "Are you feeling Discomfort in Salivary Glands?",
           "Are you experiencing Problem in Chewing?", "Are you experiencing Tiredness?", "Are you experiencing Muscle Ache?"]

QofD[7] = ["Are you feeling Gastritis?", "Are you feeling Stomach Burn?", "Are you experiencing Mouth Ulcer?",
           "Are you experiencing Lump Sensation in Throat?", "Are you experiencing Chest Pain?"]

QofD[8] = ["Is your Weight Reducing?", "Are you feeling Loss of Appetite?",
           "Are you experiencing Gland Swelling?", "Are you experiencing Chest Pain?", "Are you experiencing Chills?"]

QofD[9] = ["Is your Body Aching?", "Are you feeling Chills in your body?"]

QofD[10] = ["Are you having difficulty in speaking?", "Are you feeling Hoarseness?",
            "Are you experiencing Weak Voice?", "Are you experiencing Dry Cough?", "Are you experiencing Dry Throat?"]

# Common diseases ...
# 1 fever
# 2 cough
# 3 headache
# 4 skin_rashes
# 5 sore_throat
# 6 sneezing

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
dictionary_of_diseases_to_num = {1: "Viral Fever", 2: "Sinusitis", 3: "Allergic Rhinitis", 4: "Asthma", 5: "Respiratory Tract Infection",
                                 6: "Measles", 7: "Mumps", 8: "Gastro Esophageal Reflux Disease", 9: "Tuberculosis", 10: "Pharyngitis", 11: "Laryngitis"}


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

    def y_points(x_y, x):
        y_pt = np.zeros(len(x))
        for index, pt in enumerate(x):
            y = 0
            if pt > x_y[0][0] and pt < x_y[1][0]:
                y = (x_y[1][1]-x_y[0][1])*(pt-x_y[0][0])/(x_y[1][0]-x_y[0][0])
                y_pt[index] = y
            elif pt >= x_y[1][0] and pt < x_y[2][0]:
                y = (x_y[1][1]-x_y[2][1])*(pt-x_y[1][0])/(x_y[2][0]-x_y[1][0])
                y_pt[index] = y
            else:
                y_pt[index] = y
        return y_pt

    def corr(disease_templ, user_templ, step=0.1):
        x_min = min(disease_templ[0][0], user_templ[0][0])
        x_max = max(disease_templ[2][0], user_templ[2][0])
        x = np.arange(x_min, x_max, step)
        # x = np.linspace (0,10,101)                             // will give the all values of x .....
        y_disease = y_points(disease_templ, x)
        y_user = y_points(user_templ, x)
        correlation = y_disease*y_user
        return np.sum(correlation)

    # Correlation corresponding to each disease in a dictionary where the keys represents diseases...
    correlation_dict = {i+1: 0 for i in range(len(diseases))}

    # Correlation values are rounded off to nearest integer ...
    for i in range(len(diseases)):
        disease_t = [[list_of_templates[i][0], 0], [
            list_of_templates[i][1], 1], [list_of_templates[i][2], 0]]
        user_t = [[user_template[i][0], 0], [
            user_template[i][1], 1], [user_template[i][2], 0]]
        correlation_dict[i+1] = round(corr(disease_t, user_t))

    tmp = [correlation_dict[i+1] for i in range(len(correlation_dict))]
    shortlisted_diseases = []

    # As we want to shorlist atleast 3 diseases .....
    for i in range(3):
        lst = [index for (index, value)
               in correlation_dict.items() if value == max(tmp)]
        for k in lst:
            tmp[k-1] = 0
        shortlisted_diseases = shortlisted_diseases + lst

    print("The shortlisted diseases are:")
    print(shortlisted_diseases)

    for child in top.winfo_children():
        child.destroy()

    number_of_questions = 0
    for disease_number in shortlisted_diseases:
        number_of_questions = number_of_questions+len(QofD[disease_number-1])

    CheckVar = [None]*number_of_questions
    labelq = [None]*number_of_questions
    i = 0
    m = 7

    var = []
    for iterable in range(number_of_questions):
        var.append(IntVar())
    final_array = [0]*11
    finaldiseases = []

    def myCommand2():
        for iterable in range(number_of_questions):
            CheckVar[iterable] = var[iterable].get()
        print("The choices entered by the user are:")
        print(CheckVar)
        j = 0
        for iterable in shortlisted_diseases:
            for another_iterable in range(len(QofD[iterable-1])):
                final_array[iterable-1] = final_array[iterable-1]+CheckVar[j]
                j += 1
        print("The array made by summing up the questions of each disease is")
        print(final_array)
        for iterable in range(11):
            if(len(QofD[iterable]) > 3 and final_array[iterable] > len(QofD[iterable])-2):
                finaldiseases.append(iterable+1)
            if(len(QofD[iterable]) < 4 and final_array[iterable] == len(QofD[iterable])):
                finaldiseases.append(iterable+1)
        print("The list of diseases finally possible are")
        for disease_number in finaldiseases:
            print(dictionary_of_diseases_to_num[disease_number])

    for disease_number in shortlisted_diseases:
        for question_number in range(len(QofD[disease_number-1])):
            labelq[i] = Label(top)
            labelq[i].config(text=QofD[disease_number-1][question_number])
            labelq[i].grid(row=i, column=0)
            Radiobutton(top, text="Yes", variable=var[i], value=1).grid(
                row=i, column=1)
            Radiobutton(top, text="No", variable=var[i], value=0).grid(
                row=i, column=2)
            i = i+1
            m = m+1

    button2 = Button(top, text='Submit Level 2', command=myCommand2)
    button2.grid(row=i+1, column=0)


top = Tk()
top.title('Vaidya')
top.minsize(1000, 450)
top.maxsize(2000, 850)
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

button1 = Button(top, text='Submit Level 1', command=myCommand1)
button1.grid(row=6, column=0)

top.mainloop()
