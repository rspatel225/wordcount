from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    book = {}

    for word in word_list:
        if word in book:
            book[word] += 1
        else:
            book[word] = 1

    sorted_words = sorted(book.items(), key=operator.itemgetter(1), reverse=True)        
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(word_list), 'book': sorted_words})

def about(request):
    return render(request, 'about.html')