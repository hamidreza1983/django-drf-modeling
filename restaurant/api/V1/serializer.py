from rest_framework import serializers
from ...models import *







class ServiceSerializer(serializers.ModelSerializer):
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.context.get('request').user
    #     return super().create(validated_data)    

    class Meta:
        model = Service
        fields =[
            "title" , "status", "content",
        ]
    
class MenuSerializer(serializers.ModelSerializer):
      

    class Meta:
        model = Menu
        fields =[
            "title" , "status", "content", "price", "category"
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep

   
class EventSerializer(serializers.ModelSerializer):
      

    class Meta:
        model = Events
        fields =[
            "title" , "status", "content", "price", 
        ]




  

 
   
       
class ChefSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Chefs
        fields = [
            'name','skills','status'
        ]
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['skills'] = ServiceSerializer(instance.skills).data
        return rep


class SkillSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Skills
        fields =[
            "id","name"  
        ]    




        
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]