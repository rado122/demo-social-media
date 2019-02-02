from rest_framework import serializers
from .validators import email_deliverable

from .models import User, Post
 
class RegisterSerializer(serializers.ModelSerializer):
 
    date_joined = serializers.ReadOnlyField()
    email = serializers.EmailField(validators=[email_deliverable])

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {
          'password': {'write_only': True},
          'first_name': {'required': True},
          'last_name': {'required': True}
          }
    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)

class PostSerializer(serializers.ModelSerializer):
  
    creator = serializers.ReadOnlyField(source="creator.pk")
    likes = serializers.ReadOnlyField()
    liked_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta(object):
        model = Post
        fields = '__all__'
