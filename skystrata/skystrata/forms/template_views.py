from .views import *


class AddTemplate(Add):
    template_name = 'pages/template/add.html'

    def __init__(self):
        super().__init__(Template, TemplateSerializer, 'template')

    def post(self, request):
        new_record = self.serializer(data=request.data)
        if not new_record.is_valid():
            return Response({'serializer': self.serializer, 'error': 'Serializer not valid',
                             'instance_name': self.instance_name})
        new_record.save(customer=self.request.user,)
        pk = str(new_record.instance.pk)
        label = new_record.instance.label
        self.template_name = 'pages/template/edit.html'
        msg = "Successfully created new {} '{}' (id:{})".format(self.instance_name, label, pk)
        return Response({'serializer': new_record, 'instance': new_record.instance, 'msg': msg,
                         'instance_name': self.instance_name})


class EditTemplate(Edit):
    template_name = 'pages/template/edit.html'

    def __init__(self):
        super().__init__(Template, TemplateSerializer, 'template')

    def post(self, request, pk):
        instance = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer(instance, data=request.data)
        if not serializer.is_valid():
            return Response(
                {'serializer': serializer, 'instance': instance, 'error': 'Serializer not valid',
                 'instance_name': self.instance_name})
        serializer.save()
        msg = "Successfully modified {} {} (id:{})".format(self.instance_name, instance.label, pk)
        return Response({'serializer': serializer, 'instance': instance, 'msg': msg,
                         'instance_name': self.instance_name})



class ListTemplates(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        self.check_permissions(request)
        templates = {template.pk: template.label for template in
                     Template.objects.filter(customer=request.user)}
        context = {'title': "List available templates", 'type': 'template',
                   'templates': templates, }
        return render(request, 'pages/template/view.html', context)



#
#
# class AddInstance2(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'pages/add_instance.html'
#     model = Template
#     serializer = TemplateSerializer
#     # redirect_view_name = 'skystrata.forms:modify_template'
#
#
#     def get(self, request):
#         return Response({'serializer': self.serializer, 'instance_name' : 'template'})
#
#     def post(self, request):
#         new_record = self.serializer(data=request.data)
#
#         if not new_record.is_valid():
#             return Response({'serializer': self.serializer, 'error' : 'Serializer not valid', 'instance_name' : 'template'})
#         new_record.save(customer=self.request.user)
#         pk = str(new_record.instance.pk)
#         #return redirect(reverse(self.redirect_view_name,kwargs={'pk' : pk, 'error' : 'ok'}))
#         self.template_name = 'pages/edit_instance.html'
#         return Response({'serializer': new_record, 'instance': new_record.instance, 'msg' : 'Succesfully created record with PK of' + pk, 'instance_name' : 'template'})
#
#
#
#
#
#
# class EditInstance(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'pages/edit_instance.html'
#     model = Template
#     serializer = TemplateSerializer
#     name = 'template'
#     # redirect_view_name = 'skystrata.forms:modify_template'
#
#     # def __init__(self,model):
#     #     self.model = model
#     #
#
#     def get(self, request, pk):
#         instance = get_object_or_404(self.model, pk=pk)
#         serializer = self.serializer(instance)
#         return Response({'serializer': serializer, 'instance': instance})
#
#     def post(self, request, pk):
#         instance = get_object_or_404(self.model, pk=pk)
#         serializer = self.serializer(instance,   data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'instance': instance, 'error' : 'Serializer not valid', 'instance_name' : self.name})
#         serializer.save()
#         #return redirect(reverse(self.redirect_view_name,kwargs={'pk' : pk, 'error' : 'ok'}))
#         return Response({'serializer': serializer, 'instance': instance, 'msg' : 'Successfully modified record', 'instance_name' : self.name})


#
#
# def add_template(request):
#     context = {'title' : "Create a new template", 'type' : 'template', 'form': AddTemplateForm()}
#
#     response = None
#     if request.POST.get("new_template"):
#         client = simpleClient("templates")
#         response = client.create(request.POST)
#
#         context = {'title': "Create a new template", 'type': 'template', 'form': AddTemplateForm(), 'response' : response}
#
#         if(response.status_code==status.HTTP_201_CREATED):
#             context['message'] = "Great job! IT worked"
#             return render(request, 'pages/add.html', context)
#         else:
#             context['error'] = { 'error_code' : response.status_code, 'error_msg' : response }
#             print(response)
#             return render(request, 'pages/add.html', context)
#
#
#     return render(request, 'pages/add.html', context)
#
#
# def modify_template(request,pk):
#
#     #MIGHT NEED TO USE DJANGO GUARDIAN
#
#     template = Template.objects.get(pk=pk)
#     permissions = False
#
#     if template.customer.primary_key == request.user.pk:
#         permissions = True
#
#     if permissions:
#         context = {'title': "Modify template", 'type': 'template',
#                    'form': ModifyTemplateForm(instance=template), 'modify': True}
#     else:
#         context = {'title': "Modify template", 'type': 'template', 'unauthorized': True, 'msg' : template.customer.primary_key + " = " + request.user.pk }
#
#
#     return render(request, 'pages/edit.html', context)
#
#
# def modify_template_form(request, pk):
#     print("Returning modify view")
#     template_to_modify = Template.objects.get(pk=pk)
#     label = template_to_modify.label
#     return render(request, 'pages/templates.html',
#                   {'form': ModifyTemplateForm(instance=template_to_modify), 'modify': True,
#                    'label': label})
#
#
# def add_template_form(request):
#     return render(request, 'pages/templates.html',
#                   {'form': AddTemplateForm(), 'label': "Add a new template", 'new': True})


# class simpleClient(object):
#     api_url = "http://127.0.0.1:8000/api/v1"
#     client = APIClient()
#     client.login(password=secret_password, username=secret_username)
#
#     def __init__(self, endpoint):
#         """
#         Eg "http://127.0.0.1:8000/api/v1/template"
#         :param endpoint:
#         """
#         self.endpoint = '{}/{}'.format(self.api_url, endpoint)
#
#     def create(self, data):
#         endpoint = self.endpoint + "/"
#         # //response = requests.post(endpoint,data=data,json=True)
#         # location = reverse("templates-rud")
#         location = reverse("skystrata.api:templates-lc")
#         return self.client.post(location, data, format='json')
#
#     def update(self, data, pk):
#         location = reverse("skystrata.api:templates-rud") + "/" + pk + "/"
#         response = requests.put(location, data=data, json=True)
#
#     def delete(self, data, pk):
#         location = reverse("skystrata.api:templates-rud") + "/" + pk + "/"
#         response = requests.delete(location)
#


# def get_queryset(self):
#     if self.request.user.is_superuser:
#         return self.model.objects.all()
#     elif self.request.user.is_anonymous:
#         raise PermissionDenied('User is not Authenticated')
#     else:
#         return self.model.objects.filter(customer=self.request.user)
#


#
# def list_create_templates(request):
#
#     templates = {template.label: template.pk for template in Template.objects.all()}
#
#     #POST ADD ACTION
#     if (request.POST.get('submit_new_template')):
#         success = True
#         # PostHere
#         if success:
#             print("SUCCESS")
#             return render(request, 'pages/templates.html',
#                           {'success': True , 'message' : "Succesfully added item", 'list_view' : True})
#         else:
#             print("FAILURE")
#             return render(request, 'pages/templates.html',
#                           {'success': False, 'error': 'errorMessage'})
#
#
#
#     #GET DETAIL VIEW ACTION
#     if request.GET.get('selection'):
#         return modify_template_form(request, request.GET.get('selection'))
#
#     #GET NEW ITEM VIEW
#     if request.GET.get('add_new_item'):
#         return add_template_form(request)


#
# #DEFAULT VIEW ACTION
#
# return render(request, 'pages/templates.html',
#               {'list_view': True, 'available_items': templates})


# def add_template_form(request):
#     return render(request, 'pages/templates.html', {'form': AddTemplateForm()})

# elif (request.POST.get('submit')):
#     print(reverse("skystrata.api:templates-lc"))
#     print(api_reverse("skystrata.api:templates-lc"))
#     response = requests.post(api_reverse("skystrata.api:templates-lc")[1:], data={}, ) #auth=('user', 'pass')
#     pass
