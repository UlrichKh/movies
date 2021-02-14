from random import choice
from django.shortcuts import render

# Create your views here.


def ind(request):
    return render(request, 'love/index.html')


def valnt(request):
    var_text = [
        'Пафдравляю тебя, ф днем свитова валимпина! Ула! Очень люблю тебя!',
        "Поздравляю тебя, Зайка моя, с празником! Ты самая хорошая и самая лучшая! Всегда будь такой милашкой!",
        "Поздравляю, Поздравляю, Поздравляю! Ура Ура Ура!",
        "С празником! Таичка-Заичка"
    ]
    pic_urls = [
        "http://www.mcgilltribune.com/wp-content/uploads/2019/02/Untitled-drawing-1-700x500.png",
        "https://catholic-sf.org/pictures/2020/2/Valentines_Day_Credit_MarjanCermelj__Shutterstock-1.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ05IY57AtM07F-lYuGtdQd4ihrnMcKpaIDHA&usqp=CAU",
        "https://c.files.bbci.co.uk/E10C/production/_105621675_gettyimages-1125351857.jpg",

    ]
    text = choice(var_text)
    img = choice(pic_urls)
    return render(request, 'love/val.html', {
        'text': text,
        'img': img,
    })