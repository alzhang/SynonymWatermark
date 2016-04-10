from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import SMark


def index(request):
    plainText = request.POST.get('plainText', "")
    complexity = 0
    try :
        complexity = float(request.POST.get('complexityFactor', ".5"))
    except ValueError:
        complexity = .5
    template = loader.get_template('watermark/index.html')
    waterText = SMark.SynonymWatermark(plainText, complexity)
    watermarkText = waterText.makeCopy()

    context = {
        'plainText': plainText,
        'watermarkText': watermarkText,
        'complexityFactor': complexity,
    }

    return render(request, 'watermark/index.html',  context)
