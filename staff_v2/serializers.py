from rest_framework import serializers

from staff.models import Doctor

class DoctorSerializers(serializers.Serializer):

    id=serializers.CharField(read_only=True)

    name=serializers.CharField()

    specialization = serializers.ChoiceField(choices=Doctor.SPECIALIZATION_OPTIONS)

    fee=serializers.IntegerField()

    qualification = serializers.CharField()

    email = serializers.EmailField()

    def validate(self,validated_data):

        fee = validated_data.get("fee")

        if fee<250:

            raise serializers.ValidationError("invalid fee,fee should be greater than 250")

        return validated_data



class UserSerializers(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()