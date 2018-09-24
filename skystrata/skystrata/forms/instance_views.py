from .views import *

class AddInstance(Add):
    template_name = 'pages/instance/add.html'

    def __init__(self):
        super().__init__(Instance, InstanceSerializer, 'instance')

    def post(self, request):
        new_record = self.serializer(data=request.data)
        if not new_record.is_valid():
            return Response({'serializer': self.serializer, 'error': 'Serializer not valid',
                             'instance_name': self.instance_name})
        new_record.save(customer=self.request.user)
        id_number = str(new_record.instance.pk)
        self.template_name = 'pages/instance/edit.html'
        msg = "Successfully created new {} (id {})".format(self.instance_name, id_number)
        return Response({'serializer': new_record, 'instance': new_record.instance, 'msg': msg,
                         'instance_name': self.instance_name})


class EditInstance(Edit):
    template_name = 'pages/instance/edit.html'

    def __init__(self):
        super().__init__(Instance, InstanceSerializer, 'instance')

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



class ListInstances(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        templates = {template.pk: template.label for template in Template.objects.all()}
        instances = {instances.pk: instances.label for instances in Instance.objects.all()}
        context = {'title': "List available Instances", 'type': 'instance', 'templates': templates,
                   'instances': instances}
        return render(request, 'pages/instance/view.html', context)
