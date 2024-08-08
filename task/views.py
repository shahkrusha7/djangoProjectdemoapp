from django.shortcuts import render,redirect

# Create your views here.

tasklist=['mobile recharge','gas bill','grocery','laundry']

def home(request):
    return render(request,'task/home.html',{'tasklist':tasklist})

def addtask(request):
    if request.method=='POST':
        task=request.POST['task']
        tasklist.append(task)
        return redirect('task_home')
    else:
        return render(request,'task/addtask.html')