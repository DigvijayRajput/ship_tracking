from rest_framework import serializers
from .models import Ship, ShipPosition

class ShipSerializer(serializers.ModelSerializer):
    """
    Get ship model serializers
    """

    class Meta:
        """
        Serialising all fields
        """
        model = Ship
        fields = '__all__'


class ShipPositionSerialiser(serializers.ModelSerializer):
    """
    Get ship model serializers
    """

    class Meta:
        """Serialising all fields.
        """
        model = ShipPosition
        fields = '__all__'
