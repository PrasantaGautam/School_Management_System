from django.http import HttpResponse
from django.shortcuts import render
from school_management_system.models import Sql
import random

def randtkn():
    smlLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    capLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    collection = smlLetters + capLetters + numbers
    colec = random.sample(collection,4)
    tkn = colec[0]+colec[1]+colec[2]+colec[3]
    return tkn

sq = Sql()
def dashboard(request):
    # query = "SELECT class_token,class_Name FROM classdetails"
    # result = sq.selectall(query)
    query1 = "SELECT COUNT(*) FROM teachers"
    teaCount=sq.selectone(query1)
    query2 = "SELECT std_Count FROM classdetails"
    std = sq.selectall(query2)
    stdCount=0
    for stu in std:
        stdCount += int(stu[0])

    query3 = "SELECT COUNT(*) FROM staffs"
    staff = sq.selectone(query3)

    data = {
        'teacher':teaCount[0],
        'student':stdCount,
        'staff':staff[0],
    }

    return render(request, 'dashboard.html',data)

def dataupdate(data):
    pass
name=""
address="" 
contact =""
def dataupdate(data):
    user_token = data
    # print(data,"From dataupdate function")
    queryadd = f"UPDATE teachers SET tea_Name=%s, tea_Address=%s, tea_Contact=%s WHERE user_token={user_token} "
    values = (user_token, name, address, contact)
    sq.update(queryadd, values)
    # print("Done") 

def teachers(request):
    try:
        if request.method=="POST":
            if request.POST['nameAdd']:
                name = str(request.POST['nameAdd'])
                address = str(request.POST['address'])
                contact = str(request.POST['contact'])
                user_token = randtkn()
                queryadd = "INSERT INTO teachers (user_token, tea_Name, tea_Address, tea_Contact) VALUES(%s, %s, %s, %s) "
                values = (user_token, name, address, contact)
                sq.insert(queryadd, values)
                if request.POST['nameEdit']:
                        name = str(request.POST['nameEdit'])
                        address = str(request.POST['address'])
                        contact = str(request.POST['contact'])
                      
 
    except:
        print("Something wrong on server")
        pass

    query = "SELECT user_token, tea_Name, tea_Contact, tea_Address FROM teachers"
    result = sq.selectall(query)
  
    
    return render(request, 'teachers.html', {'result':result})

def tea_id(request, id): 
    try:
        if request.method=="POST":
            
            if request.POST['nameEdit']:
                name = str(request.POST['nameEdit'])
                address = str(request.POST['address'])
                contact = str(request.POST['contact'])
                user_token = id
                queryadd = f"UPDATE teachers SET tea_Name=%s, tea_Address=%s, tea_Contact=%s WHERE user_token=%s "
                values = (name, address, contact, user_token)
                sq.update(queryadd, values)
                
                query = "SELECT user_token, tea_Name, tea_Contact, tea_Address FROM teachers"
                result = sq.selectall(query)
                return render(request, 'teachers.html', {'result':result})
    except:
        print("wrong while update")
    return render(request, 'edit.html')

def class_token(request,token):
    try:
        if request.method=="POST":
            if request.POST['nameAdd']:
                name = str(request.POST['nameAdd'])
                address = str(request.POST['address'])
                contact = str(request.POST['contact'])

                clsName = token.split("@")
                clsName=clsName[0]
                clsName=clsName[4:]
                tok1 = str(randtkn())+clsName
                tableName='class_'+str(clsName)
                query1 = f"SELECT COUNT(*) FROM {tableName}  "
                res = sq.selectone(query1)
                user_token = tok1 + '$cls' + str(int(res[0])+1)
                queryadd = f"INSERT INTO {tableName} (user_token, std_Name, std_Address, std_Contact) VALUES(%s, %s, %s, %s) "
                values = (user_token, name, address, contact)
                sq.insert(queryadd, values)
                if request.POST['nameEdit']:
                        name = str(request.POST['nameEdit'])
                        address = str(request.POST['address'])
                        contact = str(request.POST['contact'])
                      
 
    except:
        print("Something wrong on server")
        pass
    clstkn = str(token)
    query = "SELECT class_token FROM classdetails"
    result = sq.selectall(query)
    tokenExist = False
    for res in result:
        if clstkn in res:
            tokenExist = True
            break

    if tokenExist==True:
        query1 = f"SELECT class_Name FROM classdetails WHERE class_token='{clstkn}'"
        clsName = sq.selectone(query1)
       
        query = f"SELECT std_Name, std_Contact, user_token FROM {clsName[0]}"
        result = sq.selectall(query)
        data={
            'result':result,
            'clsName':clsName[0],
            'clsTkn':clstkn,

        }
        return render(request, 'class.html',data) 
        


    pass


def std_id(request,id):
    data = id
    print(data)
    try:
            if request.method=="POST":
            
                if request.POST['nameEdit']:
                    print("condition edit")
                    name = str(request.POST['nameEdit'])
                    print(name)
                    address = str(request.POST['address'])
                    print(address)
                    contact = str(request.POST['contact'])
                    user_token = data
                    print(user_token)
                    clsToken = user_token.split("$")
                    clsName = user_token.split("@")
                    clsName=clsName[0]
                    clsName=clsName[4:]
                    clsName='class_'+str(clsName)
                    queryadd = f"UPDATE {clsName} SET std_Name=%s, std_Address=%s, std_Contact=%s WHERE user_token=%s "
                    values = (name, address, contact, user_token)
                    sq.update(queryadd, values)
                    query = f"SELECT user_token, std_Name, std_Address, std_Contact FROM {clsName}"
                    result = sq.selectall(query)
                    data ={
                            'result':result,
                            'clsName':clsName,
                            'clsTkn':clsToken[0],
                        }
                    return render(request, 'class.html', data)
                    
    except:
        print("Wrong while update")
    return render(request, 'edit.html')

def refresh(request):
    for cls in range(1,8):
        query = f"SELECT COUNT(*) FROM class_{cls}"
        res = sq.selectone(query)
        class_token = f"Brss{str(cls)}@cls"
        query2 = f"UPDATE classdetails SET std_Count=%s WHERE class_token='{class_token}'"
        values = (res[0],)
        sq.update(query2, values)
    return render(request, 'server_page.html')
"""
Work for Tommorow:
    Decorate Css
    Work on class
    Work on student side
    Work on login credientials
"""