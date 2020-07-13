from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for CourseSerializer."""
    class Meta:
        model = Course
        fields = ('id','url','name','language','price')
