def grade(x):
    if(x>=90):
        return 10
    elif(89<=x>=80):
        return 9
    elif(79<=x>=70):
        return 8
    elif(69<=x>=60):
        return 7
    elif(59<=x>=50):
        return 6
    elif(49<=x>=40):
        return 5
    else:
        return 2
    
def First_Semester():
    print("\n\t   Semester selected: 1st\n\n\tEnter marks of each subject (out of 100)")
    Mathematics=int(input("\nMathematics - I\t\t\t: "))
    a=grade(Mathematics)
    a*=4
    Chemistry=int(input("\nChemistry\t\t\t: "))
    b=grade(Chemistry)
    b*=3
    Chemistry_Lab=int(input("\nChemistry Lab\t\t\t: "))
    c=grade(Chemistry_Lab)
    c*=1.5
    Biology=int(input("\nBiology\t\t\t\t: "))
    d=grade(Biology)
    d*=1
    language=int(input("\nlanguage\t\t\t: "))
    e=grade(language)
    e*=2
    Professional_Communication=int(input("\nProfessional Communication\t: "))
    f=grade(Professional_Communication)
    f*=2
    Computer_Programming=int(input("\nComputer_Programming\t\t: "))
    g=grade(Computer_Programming)
    g*=4
    Engineering_Graphics=int(input("\nEngineering_Graphics\t\t: "))
    h=grade(Engineering_Graphics)
    h*=2
    credit_total=a+b+c+d+e+f+g+h
    credit_total/=19.5
    print("\n\n\tYour SGPA Calculated {:.1f}".format(credit_total))  
    
    
def Second_Semester():
    print("\n\t   Semester selected: 2nd\n\n\tEnter marks of each subject (out of 100)")
    Mathematics=int(input("\nMathematics - II\t\t\t: "))
    a=grade(Mathematics)
    a*=4
    Physics=int(input("\nPhysics\t\t\t\t\t: "))
    b=grade(Physics)
    b*=4
    Physics_Lab=int(input("\nPhysics Lab\t\t\t\t: "))
    c=grade(Physics_Lab)
    c*=1.5
    Basic_Electrical_Engineering=int(input("\nBasic Electrical Engineering\t\t: "))
    d=grade(Basic_Electrical_Engineering)
    d*=3
    Analog_Electronic_Circuits=int(input("\nAnalog Electronic Circuits\t\t: "))
    e=grade(Analog_Electronic_Circuits)
    e*=3
    Physics_Lab=int(input("\nPhysics Lab\t\t\t\t: "))
    f=grade(Physics_Lab)
    f*=1.5
    Basic_Electrical_Engineering_lab=int(input("\nBasic_Electrical_Engineering_lab\t: "))
    g=grade(Basic_Electrical_Engineering_lab)
    g*=1
    Analog_Electronic_Circuits_lab=int(input("\nAnalog_Electronic_Circuits_lab\t\t: "))
    h=grade(Analog_Electronic_Circuits_lab)
    h*=2
    Basic_Manufacturing_Systems=int(input("\nBasic Manufacturing Systems\t\t: "))
    i=grade(Basic_Manufacturing_Systems)
    i*=2
    Environmental_Science=int(input("\nEnvironmental Science\t\t\t: "))
    j=grade(Environmental_Science)
    j*=1
    Yoga=int(input("\nYoga and Human Consciousness\t\t: "))
    k=grade(Yoga)
    k*=1
    credit_total=a+b+c+d+e+f+g+h+i+j+k
    credit_total/=21.5
    print("\n")
    print("\n\tYour SGPA Calculated {:.1f}".format(credit_total)) 
    
def Third_Semester():
    print("\n\t   Semester selected: 3rd\n\n\tEnter marks of each subject (out of 100)")
    DSA=int(input("\nData Structures and Algorithms\t\t\t: "))
    a=grade(DSA)
    a*=4
    DE=int(input("\nDigital Electronics\t\t\t\t: "))
    b=grade(DE)
    b*=3
    Eco=int(input("\nEngineering Economics\t\t\t\t: "))
    c=grade(Eco)
    c*=3
    DMS=int(input("\nDiscrete Mathematics\t\t\t\t: "))
    d=grade(DMS)
    d*=3
    OOP=int(input("\nObject Oriented Programming\t\t\t: "))
    e=grade(OOP)
    e*=3
    PS=int(input("\nProbability & Statistics\t\t\t: "))
    f=grade(PS)
    f*=3
    DSA_lab=int(input("\nData Structures Laboratory\t\t\t: "))
    g=grade(DSA_lab)
    g*=1
    OOP_lab=int(input("\nObject Oriented Programming Laboratory\t\t: "))
    h=grade(OOP_lab)
    h*=1
    credit_total=a+b+c+d+e+f+g+h
    credit_total/=21
    print("\n")
    print("\tYour SGPA Calculated {:.1f}".format(credit_total)) 
    
def Fouth_Semester():
    print("\n\t   Semester selected: 4th\n\n\tEnter marks of each subject (out of 100)")
    OS=int(input("\nOperating Systems\t\t\t: "))
    a=grade(OS)
    a*=3
    AFL=int(input("\nAutomata and Formal Languages\t\t: "))
    b=grade(AFL)
    b*=4
    WT=int(input("\nWeb Technology\t\t\t\t: "))
    c=grade(WT)
    c*=3
    DBMS=int(input("\nDatabase Management System\t\t: "))
    d=grade(DBMS)
    d*=4
    CA=int(input("\nComputer Architecture\t\t\t: "))
    e=grade(CA)
    e*=4
    PDC=int(input("\nPrinciple of Digital Communication\t: "))
    f=grade(PDC)
    f*=4
    DBMS_lab=int(input("\nDatabase Management System Laboratory\t: "))
    g=grade(DBMS_lab)
    g*=1
    OS_lab=int(input("\nOperating Systems Laboratory\t\t: "))
    h=grade(OS_lab)
    h*=1
    WT_Lab=int(input("\nWeb Technology Laboratory\t\t: "))
    i=grade(WT_Lab)
    i*=1
    BC=int(input("\nBusiness Communication\t\t\t: "))
    j=grade(BC)
    j*=1
    credit_total=a+b+c+d+e+f+g+h+i+j
    credit_total/=26
    print("\n")
    print("\tYour SGPA Calculated {:.1f}".format(credit_total)) 
    
def Fifth_Semester():
    print("\n\t   Semester selected: 5th\n\n\tEnter marks of each subject (out of 100)")
    HPC=int(input("\nHigh Performance Computing\t\t: "))
    a=grade(HPC)
    a*=4
    CN=int(input("\nComputer Networks\t\t\t: "))
    b=grade(CN)
    b*=3
    DAA=int(input("\nDesign and Analysis of Algorithms\t: "))
    c=grade(DAA)
    c*=3
    SE=int(input("\nSoftware Engineering\t\t\t: "))
    d=grade(SE)
    d*=4
    DE1=int(input("\nDepartment Elective-I\t\t\t: "))
    e=grade(DE1)
    e*=3
    DE2=int(input("\nDepartment Elective-II\t\t\t: "))
    f=grade(DE2)
    f*=3
    NL=int(input("\nNetworks Laboratory\t\t\t: "))
    g=grade(NL)
    g*=1
    AL=int(input("\nAlgorithms Laboratory\t\t\t: "))
    h=grade(AL)
    h*=1
    
    credit_total=a+b+c+d+e+f+g+h
    credit_total/=22
    print("\n")
    print("\tYour SGPA Calculated {:.1f}".format(credit_total)) 
    
def Sixth_Semester():
    print("\n\t   Semester selected: 6th\n\n\tEnter marks of each subject (out of 100)")
    CD=int(input("\nCompiler Design\t\t\t: "))
    a=grade(CD)
    a*=3
    CN=int(input("\nComputer Networks\t\t: "))
    b=grade(CN)
    b*=3
    CC=int(input("\nCloud Computing\t\t\t: "))
    c=grade(CC)
    c*=3
    DE3=int(input("\nDepartment Elective-III\t\t: "))
    d=grade(DE3)
    d*=3
    DE4=int(input("\nDepartment Elective-IV\t\t: "))
    e=grade(DE4)
    e*=3
    DE5=int(input("\nDepartment Elective-V\t\t: "))
    f=grade(DE5)
    f*=3
    OP=int(input("\nOpen Elective -I / (MI-1)\t: "))
    g=grade(OP)
    g*=3
    TT=int(input("\nTools and Techniques Laboratory\t: "))
    h=grade(TT)
    h*=2
    CC=int(input("\nCloud Computing Lab\t\t: "))
    i=grade(CC)
    i*=1
    
    credit_total=a+b+c+d+e+f+g+h+i
    credit_total/=23
    print("\n")
    print("\tYour SGPA Calculated {:.1f}".format(credit_total))
    
def Seventh_Semester():
    print("\n\t   Semester selected: 7th\n\n\tEnter marks of each subject (out of 100)")
    print("\t\t  MI – Minor\n\t\t  HO - Honors\n")
    HS=int(input("\nHS Elective-II\t\t\t\t\t: "))
    a=grade(HS)
    a*=3
    PP=int(input("\nProfessional Practice, Law & Ethics\t\t: "))
    b=grade(PP)
    b*=2
    OE=int(input("\nOpen Elective-II / (MI-2)\t\t\t: "))
    c=grade(OE)
    c*=3
    M1=int(input("\n(MI-3)\t\t\t\t\t\t: "))
    d=grade(M1)
    d*=3
    M2=int(input("\n(MI-4)\t\t\t\t\t\t: "))
    e=grade(M2)
    e*=3
    HO=int(input("\n(HO-1)\t\t\t\t\t\t: "))
    f=grade(HO)
    f*=3
    PI=int(input("\nProject-I/Internship\t\t\t\t: "))
    g=grade(PI)
    g*=3
    PT=int(input("\nPractical Training\t\t\t\t: "))
    h=grade(PT)
    h*=2
    PM=int(input("\n(Project – Minor / Lab)\t\t\t\t: "))
    i=grade(PM)
    i*=2
    
    credit_total=a+b+c+d+e+f+g+h+i
    credit_total/=13
    print("\n")
    print("\tYour SGPA Calculated {:.1f}".format(credit_total))
    
def Eighth_Semester():
    print("\n\t   Semester selected: 8th\n\n\tEnter marks of each subject (out of 100)")
    print("\t\t  MI – Minor\n\t\t  HO - Honors\n")
    MI5=int(input("\n(MI–5)\t\t\t: "))
    a=grade(MI5)
    a*=3
    MI6=int(input("\n(MI–6)\t\t\t: "))
    b=grade(MI6)
    b*=3
    HO2=int(input("\n(HO-2)\t\t\t: "))
    c=grade(HO2)
    c*=3
    HO3=int(input("\n(HO-3)\t\t\t: "))
    d=grade(HO3)
    d*=3
    M2=int(input("\n(MI-4)\t\t\t: "))
    e=grade(M2)
    e*=3
    HO=int(input("\n(HO-1)\t\t\t: "))
    f=grade(HO)
    f*=3
    PI=int(input("\nProject-II/Internship\t: "))
    g=grade(PI)
    g*=10
    credit_total=a+b+c+d+e+f+g
    g/=10
    print("\n")
    print("\tYour SGPA Calculated {:.1f}".format(credit_total))
    
    
print("\t\t   SGPA Calculator\n")
print("Note - SGPA/CGPA Calculator only for 'Computer Science Engineering' Branch Student \n")
n=int(input("Enter your Semester: "))
if n==1:
    First_Semester()
elif n==2:
    Second_Semester()
elif n==3:
    Third_Semester()
elif n==4:
    Fouth_Semester()
elif n==5:
    Fifth_Semester()
elif n==6:
    Sixth_Semester()
elif n==7:
    Seventh_Semester()
elif n==8:
    Eighth_Semester()
    
