class College:

    def __init__(self,dept,building,no_of_faculties,no_of_students):
        self.dept = dept
        self.building = building
        self.no_of_faculties = no_of_faculties
        self.no_of_students = no_of_students


    def ratio(self):
        return print("In {} deptartment the teacher student ratio is {}:{} ".format(self.dept,self.no_of_faculties,self.no_of_students))


comp_dept = College("Computer","A","30","500",)
mech_dept = College("Mechanical","B","35","600")
civil_dept = College("Civil","C","20","300") 


comp_dept.ratio()
mech_dept.ratio()
civil_dept.ratio()