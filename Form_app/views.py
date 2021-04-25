from django.shortcuts import render, redirect
GENDER = (
    'Male',
    'Female',
    'Other'
)

LOCATIONS = (
    'San Marcos',
    'Schertz',
    'Chicago',
    'Seattle'
)

LANGS = (
    'Python',
    'Java',
    'Sql',
    'CSS'
)


# Create your views here.
def index(request):
    context = {
        'gender': GENDER,
        'locations': LOCATIONS,
        'languages': LANGS
    }
    return render(request, 'index.html', context)


def process(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['results'] = {
        'name': request.POST['name'],
        'gender': request.POST['gender'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    return redirect('/results')


def results(request):
    context = {
        'results': request.session['results']
    }
    return render(request, 'results.html', context)
