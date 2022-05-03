with open("Admin/RegisteredStudents.txt","r") as f:
    L=[]
    s=f.readlines()
    for i in s:
            L.append(i.split())
  




    

    FinalReport = open('FinalReport.txt', 'w')
   
    with open('Admin/AnswerKey.txt', 'r') as f2:
        answers = []
        k=f2.readlines()
        anotherk=[i.strip() for i in k]
        for x in anotherk:
            answers.append(x[-1])
        
        for i in range(len(L)) :
            student_file = (L[i][0]) + '_' + L[i][1] + '.txt' 
            student_name = (L[i][0])
            rollno = (L[i][1]) 
            marks=0
            f3 = open('Student/{}'.format(student_file), 'r')
            ans=f3.readlines()
            anotherans=[i.strip() for i in ans]
            studentans = []
            for x in anotherans:
                studentans.append(x[-1])
            
               
            for x in range(20):
                if studentans[x]==answers[x]:
                    marks+=4
                    
                elif studentans[x]=="-":
                    pass
                   

                else:
                    marks-=1
                    

                

                    continue

            Report = student_name + ' ' + rollno + ' ' + str(marks) + '\n'
            FinalReport.write(Report)    
                   
    FinalReport.close()                        






        

            
