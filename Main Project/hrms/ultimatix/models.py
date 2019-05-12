from django.db import models

# Create your models here.

class Designation(models.Model):
    d_id=models.AutoField(primary_key=True)
    d_cd=models.CharField(max_length=30)
    d_desc=models.CharField(max_length=50)
    d_min=models.CharField(max_length=10)
    d_max=models.CharField(blank=True,null=True,max_length=10)
    d_role=models.IntegerField()

    def __str__(self):
        return str(self.d_id)

class Project_roles(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_cd=models.CharField(max_length=30)
    r_desc=models.CharField(max_length=50)
    r_active=models.CharField(max_length=1)
    r_updt=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return str(self.r_id)

class Employee(models.Model):
    e_id=models.AutoField(primary_key=True)
    e_fname=models.CharField(max_length=50)
    e_lname=models.CharField(max_length=50,null=True,blank=True)
    e_sname=models.CharField(max_length=50,null=True,blank=True)
    e_dob=models.DateField(null=True,blank=True)
    e_bgroup=models.CharField(max_length=3,null=True,blank=True)
    e_mstatus=models.CharField(max_length=1,null=True,blank=True)
    e_nationality=models.CharField(max_length=50,null=True,blank=True)
    e_disb=models.CharField(max_length=1,null=True,blank=True)
    e_gender=models.CharField(max_length=1,null=True,blank=True)

    e_paddr1=models.CharField(max_length=50,null=True,blank=True)
    e_paddr2=models.CharField(max_length=50,null=True,blank=True)
    e_paddr3=models.CharField(max_length=50,null=True,blank=True)
    e_caddr1=models.CharField(max_length=50,null=True,blank=True)
    e_caddr2=models.CharField(max_length=50,null=True,blank=True)
    e_caddr3=models.CharField(max_length=50,null=True,blank=True)
    e_email=models.CharField(max_length=100,null=True,blank=True)
    e_mnumber=models.IntegerField(null=True,blank=True)

    e_doj=models.DateField(null=True,blank=True)
    e_qfn=models.CharField(max_length=50,null=True,blank=True)
    e_prev_exp=models.FloatField(null=True,blank=True)
    e_prev_cmp=models.CharField(max_length=50,null=True,blank=True)

    e_cl=models.FloatField(null=True,blank=True)
    e_sl=models.FloatField(null=True,blank=True)
    e_el=models.FloatField(null=True,blank=True)
    e_fl=models.FloatField(null=True,blank=True)
    e_status=models.CharField(max_length=1)
    e_pwd=models.CharField(max_length=100)

    def __str__(self):
        return str(self.e_id)

class id_select(models.Model):
    id_desc=models.CharField(primary_key=True,max_length=50)
    id_val=models.IntegerField()

    def __str__(self):
        return self.id_desc


class Employee_desig(models.Model):
    ed_id=models.AutoField(primary_key=True)
    ed_eid=models.ForeignKey(Employee,on_delete=models.CASCADE)
    ed_did=models.ForeignKey(Designation,on_delete=models.CASCADE)
    ed_sdate=models.DateField()
    ed_edate=models.DateField(null=True,blank=True)
    ed_status=models.CharField(max_length=1)

    def __str__(self):
        return str(self.ed_id)


class Employee_sal(models.Model):
    es_id=models.AutoField(primary_key=True)
    es_eid=models.ForeignKey(Employee, on_delete=models.CASCADE)
    es_ctc=models.FloatField()
    es_sdate=models.DateField()
    es_edate=models.DateField(null=True,blank=True)
    es_status=models.CharField(max_length=1)

    def __str__(self):
        return str(self.es_id)

class Project(models.Model):
    pid=models.AutoField(primary_key=True)
    ptitle=models.CharField(max_length=50)
    pdesc=models.CharField(max_length=100,null=True,blank=True)
    psdate=models.DateField(null=True,blank=True)
    pexpedate=models.DateField(null=True,blank=True)
    pedate=models.DateField(null=True,blank=True)
    pcrtd=models.CharField(max_length=50,null=True,blank=True)
    pclient=models.CharField(max_length=100,null=True,blank=True)
    powner=models.ForeignKey(Employee,on_delete=models.CASCADE)
    pstatus=models.CharField(max_length=1)

    pcloc=models.CharField(max_length=150,null=True,blank=True)
    pcomplexity=models.CharField(max_length=150,null=True,blank=True)
    ptype=models.CharField(max_length=150,null=True,blank=True)
    pbudget=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.pid)

class Project_members(models.Model):
    pmid=models.AutoField(primary_key=True)
    pid=models.ForeignKey(Project,on_delete=models.CASCADE)
    eid=models.ForeignKey(Employee,on_delete=models.CASCADE)
    rid=models.ForeignKey(Project_roles,on_delete=models.CASCADE)
    pmsdate=models.DateTimeField(null=True,blank=True)
    pmedate=models.DateTimeField(null=True,blank=True)
    pmstatus=models.CharField(max_length=1)

    def __str__(self):
        return str(self.pmid)


class Timesheet(models.Model):
    tid=models.AutoField(primary_key=True)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tdate = models.DateField(null=True, blank=True)
    thours=models.CharField(null=True, blank=True,max_length=10)
    tstate=models.CharField(max_length=1)

    def __str__(self):
        return str(self.tid)

class Leave(models.Model):
    lid=models.AutoField(primary_key=True)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sdate=models.DateField(null=True,blank=True)
    edate=models.DateField(null=True,blank=True)
    nof=models.FloatField(null=True,blank=True)
    ltype=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=1,null=True,blank=True)
    desc=models.CharField(max_length=150,null=True,blank=True)
    reqdate=models.DateField(null=True,blank=True)
    remarks=models.CharField(max_length=150,null=True,blank=True)
    queueid=models.CharField(max_length=150,null=True,blank=True)
    updtby=models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return str(self.lid)

class Salarymaster(models.Model):
    sid=models.AutoField(primary_key=True)
    bs=models.FloatField(null=True,blank=True)
    con=models.FloatField(null=True,blank=True)
    hra=models.FloatField(null=True,blank=True)
    city=models.FloatField(null=True,blank=True)
    sundry=models.FloatField(null=True,blank=True)
    ptax=models.FloatField(null=True,blank=True)
    pf=models.FloatField(null=True,blank=True)
    esis=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.sid)


class Wage(models.Model):
    wid=models.AutoField(primary_key=True)
    eid=models.ForeignKey(Employee, on_delete=models.CASCADE)
    sdate=models.DateField(null=True,blank=True)
    edate=models.DateField(null=True,blank=True)
    ctc=models.FloatField(null=True,blank=True)
    ctc_pm=models.FloatField(null=True,blank=True)
    bs=models.FloatField(null=True,blank=True)
    conv=models.FloatField(null=True,blank=True)
    hra=models.FloatField(null=True,blank=True)
    city=models.FloatField(null=True,blank=True)
    sundry=models.FloatField(null=True,blank=True)
    ptax=models.FloatField(null=True,blank=True)
    pf=models.FloatField(null=True,blank=True)
    esis=models.FloatField(null=True,blank=True)
    lop=models.FloatField(null=True,blank=True)
    status=models.CharField(max_length=1,null=True,blank=True)

    def __str__(self):
        return str(self.wid)

class News(models.Model):
    nid=models.AutoField(primary_key=True)
    head=models.CharField(max_length=150,null=True,blank=True)
    desc=models.TextField()
    img=models.ImageField(upload_to='img/news/',default='img/news/abc.png')

    def __str__(self):
        return str(self.nid)
