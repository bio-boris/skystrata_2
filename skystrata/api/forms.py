from django.shortcuts import get_object_or_404,HttpResponse,redirect
from .models import Template
from .serializers import TemplateSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        template = get_object_or_404(Template, pk=pk)
        serializer = TemplateSerializer(template)
        return HttpResponse({'serializer': serializer, 'template': template})

    def post(self, request, pk):
        template = get_object_or_404(Template, pk=pk)
        serializer = TemplateSerializer(template, data=request.data)
        if not serializer.is_valid():
            return HttpResponse({'serializer': serializer, 'template': template})
        serializer.save()
        return redirect('profile-list')
