from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import SMark


def index(request):
    plainText = request.POST.get('plainText', "")
    template = loader.get_template('watermark/index.html')
    waterText = SMark.SynonymWatermark(plainText, .5)
    watermarkText = waterText.makeCopy()

    context = {
        'plainText': plainText,
        'watermarkText': watermarkText,
    }

    return render(request, 'watermark/index.html',  context)
