
from django.template.loader import get_template
from django.http import HttpResponse,StreamingHttpResponse

from django.shortcuts import render
from . import models

from datetime import datetime
# Create your views here.
def test(request):
    """
    测试页
    :param request:
    :return:
    """
    template = get_template('test.html')
    html = template.render()
    return HttpResponse(html)

def homepage(request):
    """
    主页，导航页
    :param request:
    :return:
    """
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)
def brief_introduction_of_laboratory(request):
    """
    实验室简介页
    :param request:
    :return:
    """
    laboratory = models.Laboratory.objects.all()
    return render(request, "brief_introduction_of_laboratory/brief_introduction_of_laboratory.html", {'laboratory': laboratory})

def aboutUs(request):
    """
    关于我们页面
    :param request:
    :return:
    """
    return render(request, "about_us/aboutUs.html", )

# 在读研究生页面
def s_student(request):
    students=models.Student.objects.filter(graduate=False)
    return render(request, "laboratory_members/s_studentpage.html", {'students': students})

# 毕业生页面
def g_student(request):
    students=models.Student.objects.filter(graduate=True)
    return render(request, "laboratory_members/g_studentpage.html", {'students': students})

# 教师页面
def getTeacher(request):
    teacher=models.Teacher.objects.all()
    return render(request, "laboratory_members/teacher.html", {'teacher': teacher})

# 已完成项目页面
def t_project(request):
    project = models.Project.objects.filter(finish=True)

    return render(request, "undertake_projects/tpro_list.html", {'project': project})

# 已完成项目具体介绍页面
def t_project_page(request,project_id):
    project=models.Project.objects.get(pk=project_id)
    project_student=project.studentproject_set.all()
    teacher_project=project.teacherproject_set.all()
    return render(request,"undertake_projects/tpro_page.html",{'project':project,'project_student':project_student,'teacher_project':teacher_project})

# 未完成项目页面
def f_project(request):
    project = models.Project.objects.filter(finish=False)
    return render(request, "undertake_projects/fpro_list.html", {'project': project})

# 未完成项目具体介绍页面
def f_project_page(request,project_id):
    project=models.Project.objects.get(pk=project_id)
    project_student = project.studentproject_set.all()
    teacher_project = project.teacherproject_set.all()
    return render(request,"undertake_projects/fpro_page.html",{'project':project,'project_student':project_student,'teacher_project':teacher_project})

# 论文列表页面
def paperlist(request):
    paper = models.Research.objects.filter(genre='paper')
    return render(request, "achievements_in_scientific_research/paperlist.html", {'paper': paper})

#论文详情页面
def paperpage(request,paper_id):
    paper=models.Research.objects.get(pk=paper_id)
    paper_student=paper.studentresearch_set.all()
    paper_teacher=paper.teacherresearch_set.all()
    return render(request,"achievements_in_scientific_research/paperpage.html",{'paper':paper,'paper_student':paper_student,'paper_teacher':paper_teacher})

#专著列表页面
def monographlist(request):
    monograph = models.Research.objects.filter(genre='monograph')
    return render(request, "achievements_in_scientific_research/monographlist.html", {'monograph': monograph})

#专著详情页面
def monographpage(request,monograph_id):
    monograph=models.Research.objects.get(pk=monograph_id)
    monograph_student = monograph.studentresearch_set.all()
    monograph_teacher = monograph.teacherresearch_set.all()
    return render(request,"achievements_in_scientific_research/monographpage.html",{'monograph': monograph,'monograph_student':monograph_student,'monograph_teacher':monograph_teacher})

def big_file_download(request,project_id):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "word.txt"
    project = models.Research.objects.get(pk=project_id)
    thesis = project.thesis

    response = StreamingHttpResponse(file_iterator('E:\scu418web(2)\scu418web(1)\scu418web\static\%s'% thesis))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response
#获奖列表页面
def prizelist(request):
    prize1 = models.Prize.objects.all()
    prize2 = models.Research.objects.filter(prize=True)
    return render(request, "achievements_in_scientific_research/prizelist.html", {'prize1': prize1,'prize2':prize2})

#获奖详情页面
def prizepage(request,prize_id):
    prize=models.Prize.objects.get(pk=prize_id)

    return render(request,"achievements_in_scientific_research/prizepage.html",{'prize': prize})


# 校内信息通知页面
def scuInforPage(request):
    infor=models.Information.objects.filter(genre='news')
    return render(request,'information_notification/testInfor.html',{"Infor":infor})

# 实验室通知页面
def labInforPage(request):
    infor=models.Information.objects.filter(genre='conference')
    return render(request,'information_notification/labInfor.html',{"Infor":infor})

# 通知详细页面
def infor(request,infor_id):
    informa=models.Information.objects.get(pk=infor_id)
    return render(request, 'information_notification/inforOscu.html', {"Infor":informa})

# 日常活动页面
def lifeDayPage(request):
    activity=models.Activity.objects.filter(genre='entertainment')
    pictures=models.Image.objects.all()
    return render(request, 'laboratory_life/lifeOday.html', {"Activity":activity,"Picture":pictures})

# 学习活动
def lifeStudyPage(request):
    activity=models.Activity.objects.filter(genre='study')
    pictures = models.Image.objects.all()
    return render(request, 'laboratory_life/lifeOstudy.html', {"Activity":activity,"Picture":pictures})

# 活动详情页面
def lifeContentPage(request,life_id):
    activity = models.Activity.objects.get(pk=life_id)
    pictures = activity.image_set.all()
    return render(request, 'laboratory_life/lifeContent.html', {"Activity":activity,"Picture":pictures})

# 学习资源
def resourcesPage(request):
    resources=models.Resource.objects.all()
    return render(request, 'learning_resource/resource.html', {"Resources":resources})

# 学习资源下载
def fileDownload(request,re_id):
    # do something
    resource=models.Resource.objects.get(pk=re_id)
    path=str(resource.path)
    the_file_name=path[8:]             #显示在弹出对话框中的默认的下载文件名
    filename='static/'+path    #要下载的文件路径
    response=StreamingHttpResponse(readFile(filename))
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="{0}"'.format(the_file_name)
    return response

def readFile(filename,chunk_size=512):
    with open(filename,'rb') as f:
        while True:
            c=f.read(chunk_size)
            if c:
                yield c
            else:
               break

# 链接页面
def linkPage(request):
    return render(request, 'learning_resource/link.html')

