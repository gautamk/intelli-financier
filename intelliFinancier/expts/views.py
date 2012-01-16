# Create your views here.
from django.shortcuts import render,render_to_response
from django.template import Context, loader
from nltk import word_tokenize , pos_tag
    
def defaultView(request):
    sentence = request.GET.get('Sentence','')
    tok = word_tokenize(sentence)

    c = Context({
        'tagged_sentence':pos_tag(tok)
    })
    return render(request,'index.html',c)
