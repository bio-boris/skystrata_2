from rest_framework import serializers

from .models import Image, CloudProvider, ProviderOption, Template, Bill, Instance
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

# class SerializerWithUri():
#     def get_uri(self,obj):
#         request = self.context.get('request')
#         return obj.get_api_uri(request=request)



class ImageSerializer(serializers.ModelSerializer):
    # action = serializers.SerializerMethodField(method_name="get_data_for_action")
    #
    # def get_data_for_action(self, obj):
    #     return "createproject"  # always add this value in the 'action' key of serialized object representation

    class Meta:
        model = Image
        fields = ['pk', 'label', 'repository_url', 'provider', 'modified_date', 'created_date']


class ProviderOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderOption
        fields = ['pk', 'label', 'provider', 'cost', 'cpu_score', 'network_score',
                  'throughput_score', 'memory_score']


class CloudProviderSerializer(serializers.ModelSerializer):
    # provider_option = ProviderOptionSerializer(many=True, read_only=True, queryset=ProviderOption.objects.all())
    # image = ImageSerializer(many=True, read_only=True,queryset=Image.objects.all())

    class Meta:
        model = CloudProvider
        fields = ['pk', 'label', 'api', ]
        # fields = ['pk', 'label', 'api', 'provider_option', 'image']
        # ProviderOption and Image is a reverse field

    # Converst to json
    # validations for data passed


class CustomerSerializer(serializers.ModelSerializer):
#    pk = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['pk']


class InstanceSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    state = serializers.SerializerMethodField()

    #customer = CustomerSerializer(read_only=True, default=serializers.CurrentUserDefault())

    def get_uri(self,obj):
        request = self.context.get('request')
        return obj.get_api_uri(request=request)

    def get_state(self,obj):
        request = self.context.get('request')
        return obj.get_state(request=request)

    class Meta:
        model = Instance
        fields = ['pk','label','customer','template','image','start_time','end_time','uri','state',]
        read_only_fields = ['pk', 'uri', 'customer','state']

class InstanceSerializerStaff(InstanceSerializer,serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = ['pk','label','customer','template','image','start_time','end_time','uri','state']
        read_only_fields = ['pk', 'uri', 'customer',]





class TemplateSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    # customer = CustomerSerializer(read_only=True, default=serializers.CurrentUserDefault())

    def get_uri(self,obj):
        request = self.context.get('request')
        return obj.get_api_uri(request=request)

    class Meta:
        model = Template
        fields = ['pk', 'label', 'cpu', 'memory', 'io', 'disk', 'cost', 'uri','customer']
        read_only_fields = ['pk', 'uri','customer', 'cost']

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     print(request)
    #     user = request.user
    #     return Template.objects.create(
    #         customer=user,
    #         **validated_data
    #     )


        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Template.objects.all(),
        #         fields=('customer', 'label')
        #     )
        # ]



class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['pk', 'customer', 'instance', 'cost']



