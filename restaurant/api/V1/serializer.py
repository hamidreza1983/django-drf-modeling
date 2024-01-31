from rest_framework import serializers
from ...models import *


class MenuSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset = Category.objects.all()
    )

   
    class Meta:
        model = Menu
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category, many=True).data
        return rep



class EventSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Event
        fields = "__all__"



class ChefsSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset = Skills.objects.all()
    )

    class Meta:
        model = Chefs
        fields = ['name','skills','status']



    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['skills'] = SkillsSerializer(instance.skills, many=True).data
        return rep
    
    


    def create(self, validated_data):
        
        validated_data['info'] = self.context.get('request').user
        return super().create(validated_data)    




class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


        

class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ["id","name"]


class OrderSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Order
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ContactUs
        fields = "__all__"