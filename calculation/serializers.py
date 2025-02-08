from rest_framework import serializers

class DrillRequestSerializer(serializers.Serializer):
    use_fraction = serializers.BooleanField()
    digit_type = serializers.IntegerField()
    allow_negative = serializers.BooleanField()
    operator = serializers.CharField(max_length=1)
    num_questions = serializers.IntegerField()


class AnswerCheckSerializer(serializers.Serializer):
    operator = serializers.CharField(max_length=1)
    user_answer = serializers.IntegerField(required=False)  # 整数の場合

    # 分数の場合
    numerator1 = serializers.IntegerField(required=False)
    denominator1 = serializers.IntegerField(required=False)
    numerator2 = serializers.IntegerField(required=False)
    denominator2 = serializers.IntegerField(required=False)
    user_numerator = serializers.IntegerField(required=False)
    user_denominator = serializers.IntegerField(required=False)

    # 整数の場合
    number1 = serializers.IntegerField(required=False)
    number2 = serializers.IntegerField(required=False)
