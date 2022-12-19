from django.shortcuts import render, redirect
from .forms import ImageForm
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Image
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

cloudinary.config(
    cloud_name=os.environ.get('cloud_name'),
    api_key=os.environ.get('api_key'),
    api_secret=os.environ.get('api_secret'),
    secure=True
)


class AdminPanel(ListView):
    model = Image
    template_name = 'admin.html'
    context_object_name = 'images'
    paginate_by = 10
    renderer_class = ['TemplateHTMLRenderer']


def upload_images(request):
    if request.method == 'POST':
        for v in request.FILES:
            image_description = 'desc_' + request.FILES[v].name
            image_description = request.POST.get(image_description)
            upload = cloudinary.uploader.upload(request.FILES[v], use_filename=True,
                                                unique_filename=True,)
            url = upload['url']
            public_id = upload['public_id']
            cloudinary.uploader.add_tag('NewsmileAliveImages', [public_id])
            Image(image_url=url, description=image_description, public_id=public_id).save()
        return redirect('../admin-panel/')
    else:
        image_form = ImageForm
        return render(request, 'image-upload.html', {'form': image_form})


def imageEdit(request, public_id):
    qs = Image.objects.get(public_id=public_id)
    if request.method == 'GET':
        image_src = qs.image_url
        image_desc = qs.description
        return render(request, 'edit-image.html', {'image_src': image_src, 'image_desc': image_desc, 'public_id': public_id})
    else:
        if request.FILES:
            for v in request.FILES:
                image_description = request.POST.get('desc')
                cloudinary.uploader.destroy(public_id)
                upload = cloudinary.uploader.upload(request.FILES[v], use_filename=True,
                                                    unique_filename=True)
                url = upload['url']
                cloudinary.uploader.add_tag('NewsmileAliveImages', [url])
                qs.image_url = url
                qs.description = image_description
            return redirect('../')
        else:
            image_description = request.POST.get('desc_1')
            qs.description = image_description

