# I have created this file-Vicky
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')
def analyze(request):
    # get the text from textarea
    djtext=request.POST.get("text","default")
    #checks checkbox values
    removepunc=request.POST.get('removepunc',"off")
    fullcaps=request.POST.get("fullcaps","off")
    newlineremover=request.POST.get("newlineremover","off")
    extraspaceremover=request.POST.get("extraspaceremover","off")
    charcounter=request.POST.get("charcounter","off")
    #check which check is on

    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
            djtext=analyzed
        params = {"purpose": "Remove Punctuations", "analyze_text": analyzed}
        #return render(request, "analyze.html", params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        djtext=analyzed
        params = {"purpose": "Capitalized all", "analyze_text": analyzed}
        #return render(request, "analyze.html", params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
            djtext=analyzed
        params = {"purpose": "New lines removed", "analyze_text": analyzed}
        #return render(request, "analyze.html", params)
    if(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" "and djtext[index+1]==" "):
               analyzed = analyzed + char
        djtext=analyzed
        params = {"purpose": "EXTRaSpaces  removed", "analyze_text": analyzed}
        #return render(request, "analyze.html", params)
    if (charcounter == "on"):
        analyzed = ""
        count=0
        for char in djtext:
            count+=1
        analyzed=count

        params = {"purpose": "Char counter", "analyze_text": analyzed}
        #return render(request, "analyze.html", params)

    return render(request, "analyze.html", params)




