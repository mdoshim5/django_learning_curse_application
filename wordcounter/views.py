from django.shortcuts import render

def home(request):
    if request.method == "POST":
        inputdata = request.POST['inputdata']
        wordlist = inputdata.split()
        totalwords = len(wordlist)
        frequency = {}
        for word in wordlist:
            if word in frequency:
                frequency[word] = frequency[word] + 1
            else:
                frequency[word] = 1
        frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        return render(request, 'wordcounter/reply.html', {'inputdata' : inputdata, 'totalwords' : totalwords, 'frequency': frequency})
    else:
        return render(request, 'wordcounter/home.html')