from django.shortcuts import render
from ml.model_news import fake_news

def index(request):
    if request.method == 'POST':
        info = request.POST['news']
        predi = fake_news(info)    
        return render(request,'blog_ml/index.html',{'val':predi})
    return render(request,'blog_ml/index.html')