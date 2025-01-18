from rest_framework import serializers

from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        fields = ['category', 'question', 'answers']

    def get_answers(self, question):
        answers = question.answers.all().order_by('?')
        return AnswerSerializer(answers, many=True).data
