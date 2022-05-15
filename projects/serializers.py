from rest_framework import serializers
from .models import Project, Projectlink


class ProjectlinkSerializer(serializers.ModelSerializer):
    class Meta:
      model = Projectlink
      fields = ('linkname', 'link','category','categoryid')

class ProjectSerializer(serializers.ModelSerializer):
    projectlinks = ProjectlinkSerializer(many=True)
    #serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('id','projectnumber', 'title', 'description','startdate','enddate','confidential','status','projectlinks')