from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def count(request):
    count = len(request.GET['text'])
    user_text = request.GET['text']
    word_dict = {}
    for i in user_text:
        if i not in word_dict:
            word_dict[i] = 1;
        else:
            word_dict[i] += 1;
    sorted_dict = sorted(word_dict.items(),key=lambda w:w[1],reverse=True)
    return render(request, "count.html",
                  {"count":count,
                   'text':user_text,
                   'dict':sorted_dict
                   })

def about(request):
    return render(request,"about.html")

