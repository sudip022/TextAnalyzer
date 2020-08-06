# self created python file for views
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def analyze(request):
    # getting the text from where we submit in the textarea
    djtext = request.POST.get('text', 'default')

    # checking the checkbox value wheather it is on or off
    removepunc = request.POST.get('removepunc', 'off')
    capatilized = request.POST.get('capatilized', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    extraspacerem = request.POST.get('extraspacerem', 'off')
    charcount = request.POST.get('charcount', 'off')

    # print(removepunc)
    # analyze = djtext

    # checking the condition if checkbox is on
    if removepunc == "on":

        analyze = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        # this for loop is for removing the punctuations
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        params = {
            'purpose': 'Removing the punctuations !',
            'analyze_text': analyze
        }
        djtext = analyze

    if(capatilized == "on"):
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()

        params = {
            'purpose': 'Capitalize the text !',
            'analyze_text': analyze
        }
        djtext = analyze

    if(newlinerem == "on"):
        analyze = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyze = analyze + char

        params = {
            'purpose': 'Removing new line !',
            'analyze_text': analyze
        }
        djtext = analyze

    if(extraspacerem == "on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyze = analyze + char

        params = {
            'purpose': 'Removing extra space !',
            'analyze_text': analyze
        }
        djtext = analyze

    if(charcount == "on"):
        analyze = ""
        count = 0
        for char in djtext:
            analyze = analyze + char
            count = count+1

        params = {
            'purpose': 'Character COunt !',
            'analyze_text': "Total no. of character are " + str(count)
        }
        djtext = analyze

    if (removepunc != "on" and capatilized != "on" and newlinerem != "on" and extraspacerem != "on"):
        return HttpResponse("Please select the switches... ")

    # analyzing the text form the djtext where we get the text !
    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'about.html')

# def spaceremove(request):
#     return HttpResponse("This is space remover")


# def charcount(request):
#     return HttpResponse("This is charcount end point! ")
