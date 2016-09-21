from rest_framework import serializers
from heatBalance.models import heatBalance

class heatBalSerializer(serializers.Serializer):
	pk=serializers.IntegerField(read_only=True)
	project=models.CharField(max_length=50)
	sensibleH=models.FloatField()
	sensibleC=models.FloatField()
	surfaceH=models.FloatField()
	surfaceC=models.FloatField()
	peopleH=models.FloatField()
	lightH=models.FloatField()
	equipH=models.FloatField()
	windowH=models.FloatField()
	transferH=models.FloatField()
	infiltrationH=models.FloatField()
	conductionH=models.FloatField()
	equipR=models.FloatField()
	windowR=models.FloatField()
	transferR=models.FloatField()
	infiltrationR=models.FloatField()
	conductionR=models.FloatField()

	def create(self,validated_data):
		return heatBalance.objects.create(**validated_data)

	
