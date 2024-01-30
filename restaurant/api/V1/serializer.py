from rest_framework import serializers
from ...models import *
from accounts.models import CustomeUser, Profile





class FoodSerializer(serializers.ModelSerializer):
    content = serializers.ReadOnlyField()


    class Meta:
        model = Food
        fields = '__all__'

    
    # def detail(self,obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.id)
    

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['teacher'] = TrainerSerializer(instance.teacher).data
    #     rep['category'] = CategorySerializer(instance.category, many=True).data
    #     request = self.context.get('request')
    #     kwargs = request.parser_context.get('kwargs')
    #     if kwargs.get('pk') is not None:
    #         rep.pop('content')
    #     return rep
    
    # def create(self, validated_data):
    #     #validated_data['teacher'] = self.context.get('request').user
    #     validated_data['content'] = 'for this course'
    #     return super().create(validated_data)

    

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


        

class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = '__all__'



class ChiefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chief
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'

