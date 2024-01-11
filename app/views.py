from django.shortcuts import render
from app.models import *

# Create your views here.
def dept(request):
    QLTO=Dept.objects.all()
    QLTO=Dept.objects.filter(dname__startswith='t')
    QLTO=Dept.objects.filter(dname__endswith='g')
    QLTO=Dept.objects.filter(dname__contains='a')

    d={'Dept':QLTO}
    return render(request,'dept.html',d)



def emp(request):
    QLTO=Emp.objects.all()
    QLTO=Emp.objects.filter(sal__gt=100000)
    QLTO=Emp.objects.filter(sal__gte=50000)
    QLTO=Emp.objects.filter(sal__lt=100000)
    QLTO=Emp.objects.filter(sal__lte=100000)
    QLTO=Emp.objects.filter(Hiredate__year=2024)
    QLTO=Emp.objects.filter(Hiredate__month=7)
    QLTO=Emp.objects.filter(Hiredate__day=5)
    QLTO=Emp.objects.filter(ename__in=('ANU',))
    d={'Emp':QLTO}
    return render(request,'emp.html',d)



def insert_dept(request):
    do=input('enter the deptno')
    no=input('enter the dname')
    lo=input('enter the loc')
    NDO=Dept.objects.get_or_create(deptno=do,dname=no,loc=lo)[0]
    NDO.save()

    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)



def insert_emp(request):
    do=input('enter the deptno')
    eo=input('enter the empno')
    en=input('enter the ename')
    jo=input('enter the job')
    mg=input('enter the mgr')
    hr=input('enter the hirdate')
    sa=input('enter the salary')
    com=input('enter the commission')
    DNO=Dept.objects.get(deptno=do)
    NEO=Emp.objects.get_or_create(deptno=DNO,empno=eo,ename=en,job=jo,MGR=mg,Hiredate=hr,sal=sa,comm=com)[0]
    NEO.save()

    QLTO=Emp.objects.all()
    d={'Emp':QLTO}
    return render(request,'emp.html',d)


def data_dept(request):
    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)


def data_emp(request):
    QLTO=Emp.objects.all()
    d={'Emp':QLTO}
    return render(request,'emp.html',d)



