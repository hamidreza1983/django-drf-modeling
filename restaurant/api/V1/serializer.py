from rest_framework import serializers
from ...models import Service ,Menu,Events,Skills,Chefs,Category






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
            "title" , "status", "content", "price", 
        ]

   
class EventSerializer(serializers.ModelSerializer):
      

    class Meta:
        model = Events
        fields =[
            "title" , "status", "content", "price", 
        ]





class SkillSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Skills
        fields =[
            "id","name"  
        ]      

 
   
       
class ChefSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Chefs
        fields = '__all__' 

        
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]