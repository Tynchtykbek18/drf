from rest_framework import serializers
from .models import Women

class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = '__all__'




# def encode():
#     model = WomenModel('Angeline Jolie', 'Content: Angeline Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angeline Jolie","content":"Content: Angeliine Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')