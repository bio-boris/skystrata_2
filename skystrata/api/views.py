from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .permissions import *
from .serializers import *
from rest_framework.exceptions import PermissionDenied


class ImageRudView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a specific image

    put:
    Update a specific image.

    """
    lookup_field = "pk"  # // = url()
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)


class ImageLCView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing images.

    post:
    Create a new image instance.
    """
    lookup_field = "pk"  # // = url()
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)


class CloudProviderRudView(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    lookup_field = "pk"  # // = url()
    serializer_class = CloudProviderSerializer

    def get_queryset(self):
        return CloudProvider.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser)


class CloudProviderLCView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing cloud providers.

    post:
    Create a new cloud provider instance.
    """
    lookup_field = "pk"  # // = url()
    serializer_class = CloudProviderSerializer

    def get_queryset(self):
        return CloudProvider.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser)


class ProviderOptionRudView(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    lookup_field = "pk"  # // = url()
    serializer_class = ProviderOptionSerializer

    def get_queryset(self):
        return ProviderOption.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProviderOptionLCView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing provider options.

    post:
    Create a new cloud provider option .
    """
    lookup_field = "pk"  # // = url()
    serializer_class = ProviderOptionSerializer

    def get_queryset(self):
        return ProviderOption.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)


class TemplateView:
    lookup_field = "pk"  # // = url()
    serializer_class = TemplateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    model = Template

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        elif self.request.user.is_anonymous:
            raise PermissionDenied('User is not Authenticated')
        else:
            return self.model.objects.filter(customer=self.request.user)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class TemplateLCView(TemplateView, generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing templates .

    post:
    Create a new templates option .
    """


class TemplateRUDView(TemplateView, generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    View specific template

    post:
    Update a specific template
    """


class InstanceView:
    lookup_field = "pk"  # // = url()
    serializer_class = InstanceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    model = Instance

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return InstanceSerializerStaff
        return InstanceSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        elif self.request.user.is_anonymous:
            raise PermissionDenied('User is not Authenticated')
        else:
            return self.model.objects.filter(customer=self.request.user)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class InstanceLCView(InstanceView, generics.ListCreateAPIView):
    """

    """
    # lookup_field = "pk"  # // = url()
    # serializer_class = InstanceSerializer
    #
    # permission_classes = [IsOwner]
    #
    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return Instance.objects.all()
    #     elif self.request.user.is_anonymous:
    #         raise PermissionDenied('User is not Authenticated')
    #     else:
    #         return Instance.objects.filter(customer=self.request.user)
    #
    # def get_serializer_context(self, *args, **kwargs):
    #     return {"request": self.request}
    pass


class InstanceRUDView(InstanceView, generics.RetrieveUpdateDestroyAPIView):
    # """
    #
    # """
    # lookup_field = "pk"  # // = url()
    # serializer_class = InstanceSerializer
    #
    # permission_classes = [IsOwner]
    pass

# from django.shortcuts import redirect
# from .models import Template
# from .serializers import TemplateSerializer
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
#
#
# from rest_framework.response import Response
#
#
# class TemplateList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'pages/forms.html'
#
#     def get(self, request, pk):
#         template = get_object_or_404(Template, pk=pk)
#         serializer = TemplateSerializer(template)
#         return Response({'serializer': serializer, 'template': template})
#
#     def post(self, request, pk):
#         template = get_object_or_404(Template, pk=pk)
#         serializer = TemplateSerializer(template, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'template': template})
#         serializer.save()
#         # return redirect(reversed('skystrata.api:templates-rud-detail')
#         return redirect(request.get_full_path())
#

# class TemplateView2(APIView):
#     lookup_field = "pk"  # // = url()
#     serializer_class = TemplateSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'pages/forms.html'
#
#     def get_queryset(self):
#         return Template.objects.all()
#
#     def get_serializer_context(self, *args, **kwargs):
#         return {"request": self.request}
#
#     def get(self, request):
#         template = get_object_or_404(Template)
#         serializer = TemplateSerializer(template)
#         return Response({'serializer': serializer, 'template': template})
#
#
# class TemplateCreate(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'pages/forms.html'
#
#     def get(self, request):
#         template = get_object_or_404(Template)
#         serializer = TemplateSerializer(template)
#         return Response({'serializer': serializer, 'template': template})
#
#     ##KEEP THIS MIGHT BE WORKAROUND FOR UNIQUE_CONSTRAINT
#     # def post(self, request, pk):
#     #     template = get_object_or_404(Template, pk=pk)
#     #     serializer = TemplateSerializer(template, data=request.data)
#     #     if not serializer.is_valid():
#     #         return Response({'serializer': serializer, 'template': template})
#     #     serializer.save()
#     #     #return redirect(reversed('skystrata.api:templates-rud-detail')
#     #     return redirect(request.get_full_path())


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

from django.shortcuts import render
from api.celery_home.tasks import *

"""
DELETE THIS SOON
"""
def viewCelery(request):
    res = add.delay(1,2)
    return render(request, 'pages/template/view.html', {'message' : res})

