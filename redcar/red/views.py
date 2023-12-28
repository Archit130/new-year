from django.shortcuts import render, redirect
from red.models import FormModel, SaveImage
from red.forms import FormForm, SaveImageForm
from red import views
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import base64
from io import BytesIO
# Create your views here.


@csrf_exempt
def Index(request):
    form = FormForm()

    if request.method == 'POST':
        form = FormForm(request.POST, request.FILES)
        img = request.POST.get('img')
        print("Img: ", img)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        adult = request.POST.get('adult')
        child = request.POST.get('child')
        data_url = request.POST.get('img')

        print("Name: ", name, phone, adult, child)

        img_data = data_url.split(',')[1]

        # Decode the base64 image data
        img_bytes = base64.b64decode(img_data)

        # Create a BytesIO object to work with PIL
        img_buffer = BytesIO(img_bytes)

        # Open the image using PIL
        img = Image.open(img_buffer)

        # Save the PIL image as a JPEG file
        img.save('converted_image.jpg', 'JPEG')
        print(img)

        s = FormModel(name=name, phone=phone,
                      adult=adult, child=child, img=img_buffer)
        s.save()
        print("Form Saved")
    context = {'form': form}
    return render(request, 'redcar/index.html', context)


@csrf_exempt
def SaveImageview(request):
    form = SaveImageForm()

    if request.method == 'POST':
        form = SaveImageForm(request.POST, request.FILES)
        img = request.POST.get('img')
        print("Img: ", img)

        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect('/')
        else:
            print("Error.....", form.errors)

    context = {'form': form}
    return render(request, 'redcar/index.html', context)
