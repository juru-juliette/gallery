from django.shortcuts import render
from django.http  import HttpResponse,Http404
# Create your views here.
def Belle(request):
    # return HttpResponse('Belles Images')
    return render(request, 'belle.html')
def Image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_images/pic.html", {"article":article})