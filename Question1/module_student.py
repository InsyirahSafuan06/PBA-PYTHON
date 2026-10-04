class student:
    def __init__(self,name,student_id,age,course):
        #private attributes
        self._namest = name
        self._student_idst = student_id
        self._agest = age
        self._coursest = course

    #mutator methods
    def set_name(self,namestudent):
        self._namest = namestudent

    def set_id(self,idstudent):
        self._student_idst = idstudent

    def set_age(self,agestudent):
        self._agest = agestudent

    def set_course(self,coursestudent):
        self._coursest = coursestudent

    #accessor methods
    def get_name(self):
        return self._namest

    def get_id(self):
        return self._student_idst

    def get_age(self):
        return self._agest

    def get_course(self):
        return self._coursest

#subclass for undergraduate student
class Undergraduate(student):
    def __init__(self, name, student_id, age, course,year_level):
        student.__init__(self, name, student_id, age, course)
        self._yearst = year_level

    def set_year (self, yearstudent):
            self._yearst = yearstudent

    def get_year(self):
            return self._yearst

#subcalss for postgraduate student
class Postgraduate(student):
    def __init__(self, name, student_id, age, course,year_level, Research_topic):
        student.__init__(self, name, student_id, age, course)
        self._yearst = year_level
        self._topicst = Research_topic

    def set_year (self, yearstudent):
        self._yearst = yearstudent

    def set_topic (self, topicstudent):
        self._topicst= topicstudent
    
    def get_year(self):
        return self._yearst

    def get_topic(self):
        return self._topicst

#subclass for part-time student
class PartTime_Student(student):
    def __init__(self, name, student_id, age, course,year_level, Research_topic,Work_hour):
        student.__init__(self, name, student_id, age, course)
        self._yearst = year_level
        self._topicst = Research_topic
        self._workhourst = Work_hour

    def set_year (self, yearstudent):
        self._yearst = yearstudent

    def set_topic (self, topicstudent):
        self._topicst= topicstudent

    def set_workhour (self, workhourstudent):
        self._workhourst= workhourstudent
    
    def get_year(self):
        return self._yearst

    def get_topic(self):
        return self._topicst

    def get_workhour(self):
        return self._workhourst