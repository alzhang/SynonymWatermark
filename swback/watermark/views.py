from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from sparkpost import SparkPost
import SMark


def index(request):
    sp = SparkPost('85e32a6a831df8e5161c327f895e6efee0d40831')

    plainText = request.POST.get('plainText', "")
    email = request.POST.get('email',"")
    complexity = 0
    try :
        complexity = float(request.POST.get('complexityFactor', ".5"))
    except ValueError:
        complexity = .5
    template = loader.get_template('watermark/index.html')
    waterText = SMark.SynonymWatermark(plainText, complexity)
    watermarkText = waterText.makeCopy()
    if email != "":
        response = sp.transmissions.send(
            recipients=[email],
            html=watermarkText,
            from_email='test@sparkpostbox.com',
            subject='Your Watermarked Document',
        )

    context = {
        'plainText': plainText,
        'watermarkText': watermarkText,
        'complexityFactor': complexity,
    }

    return render(request, 'watermark/index.html',  context)
