class Student:
    courseMarks={}
    average=0
    #name= ""
    
    def __init__(self,name,family):
        self.name=name
        self.family=family

    def addCourseMark(self,course,mark):
        Student.courseMarks[course] = mark
        
    def average(self):
        Student.average=0
        count=len(Student.courseMarks)
        total=0
        if (count>0):
            for course in Student.courseMarks.keys():
                mark=Student.courseMarks[course]
                total+=mark
            Student.average=total/count
        return Student.average
    
student= Student("Paul","xkd")
student.addCourseMark("301",4)

student.addCourseMark("333",3)

#test=student.average()
print(student.average())