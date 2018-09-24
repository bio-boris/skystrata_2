
from django.shortcuts import get_object_or_404, render


def main(request):
        return render(request, 'templates/base.html')