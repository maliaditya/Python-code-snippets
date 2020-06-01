class College:

    def __init__(self,cname,c_address,university,principal):
        self.cname = cname
        self.c_address = c_address
        self.university = university
        self.principal = principal

    def principalname(self):
        print("The principal of {} {} is {}".format(self.cname,self.c_address,self.principal))


class Computer(College):
    def __init__(self,cname,c_address,university,principal,hod,dept):
        super().__init__(self, cname, c_address,principal)
        self.hod = hod
        self.dept = dept

 
    def comp_hod(self):
        print("The Head of Department of {} of {} is {}".format(self.dept,self.cname,self.hod))

    
college_info = College("ZCOER","Narhe,pune","SPPU","Dr.A.M.Kate",)
comp_dept = Computer("ZCOER","Narhe,pune","SPPU","Dr.A.M.Kate","Dr.S.M.Sangve","Computer")
# mech_dept = College("Mechanical","B","35","600")
# civil_dept = College("Civil","C","20","300") 

college_info.principalname()

comp_dept.comp_hod()
# mech_dept.ratio()
# civil_dept.ratio()