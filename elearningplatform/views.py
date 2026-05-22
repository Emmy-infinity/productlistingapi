
from django.shortcuts import redirect,render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import login, logout,authenticate
from .forms import *

from .models import *
from django.contrib.auth.decorators import login_required
def home(request):
     videoobj=Videotutorial.objects.all()
     context={'videoobj':videoobj}
     return render(request,'caninstitutehome.html',context)
#def coursemenu(request):
 #   return render(request, 'coursemenu.html')
@login_required(login_url='elearningplatform:login')
def quizz(request):
    question=Add_Questions.objects.all()
           
    paginator=Paginator(question,50)
    page = request.GET.get('page', 1)
    try:
          users = paginator.page(page)
    except PageNotAnInteger:
          users = paginator.page(1)
    except EmptyPage:
           users = paginator.page(paginator.num_page)
    if request.method == 'POST':
        
        score=0
        wrong=0
        correct=0
        total=0
        question_number=1
        for q in users:
            total+=1
            question_number+=1
            
            
            if q.Answer ==  request.POST.get(q.Question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        time=request.POST.get('timer')
        context = {
            'users':users,
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        
        
        return render(request,'results.html',context)
    else:
        
        return render(request,'multichoice.html',{'users': users})
def certificatecourses(request):
   
    return render(request,'certificatecourses.html')
def helpcipse(request):
    return render(request,'helpcipse.html')

def diplomacourses(request):
    return render(request,'diplomacourses.html')
def undergraduatecourses(request):
    return render(request,'undergraduatecourses.html')
def postgraduatecourses(request):
    return render(request,'postgraduatecourse.html')
def professionalcourses(request):
    return render(request,'professionalcourses.html')
def Notes(request):
    return(request,'cansinstitute.html')
def Videos(request):
    videoobj=Videotutorial.objects.all()
    context={'videoobj':videoobj}
    return(request,'caninstitutevideo.html',context)
def Register(request):
    return(request,'caninstitute.html')
def About(request):
    pass
def Article(request):
    
    articles=Articles2.objects.all()
    context={'articles':articles}
    return render(request,'caninstitutearticle.html',context)

def Learning_materials(request):
    return render(request,'multichoice.html')
def PrivacyPolicy(request):
    pass
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form=createuserform()
        if request.method =='POST':
            form=createuserform(request.POST)
            if form.is_valid():
             user= form.save()
            return redirect('elearningplatform:login')
        context={'form':form}
        return render(request,'register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('elearningplatform:home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')    


    
