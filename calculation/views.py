from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DrillRequestSerializer, AnswerCheckSerializer
from .drill_generator import DrillGenerator, Calculator

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})


class HelloUserView(APIView):
    def get(self, request):
        return Response({"message": f"Hello, User!"})


class GenerateDrillView(APIView):
    def post(self, request):
        print(request.data)
        serializer = DrillRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            print(data)
            generator = DrillGenerator(
                use_fraction=data['use_fraction'],
                digit_type=data['digit_type'],
                allow_negative=data['allow_negative'],
                operator=data['operator'],
                num_questions=data['num_questions']
            )
            questions = generator.generate_quiz()
            return Response({"questions": questions}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckAnswerView(APIView):
    """ユーザーの解答をチェックする API"""
    def post(self, request):
        serializer = AnswerCheckSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            operator = data['operator']
            is_fraction = "numerator1" in data  # 分数かどうか判定
            
            if is_fraction:
                # 分数の正解を計算
                correct_answer = Calculator.calculate_fraction(
                    data['numerator1'], data['numerator2'], data['denominator1'], data['denominator2'], operator
                )
                user_answer = (data['user_numerator'], data['user_denominator'])
            else:
                # 整数の正解を計算
                correct_answer = Calculator.calculate_integer(data['number1'], data['number2'], operator)
                user_answer = data['user_answer']

            is_correct = user_answer == correct_answer

            return Response({
                "correct_answer": correct_answer,
                "is_correct": is_correct
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)