from collections import Counter

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def _order_by_repetition(array):
    counter = Counter(array)
    response = []

    for elem, rep in counter.most_common():
         for _ in range(rep):
             response.append(elem)

    return response


@api_view(['POST'])
def lambda_function(request):
    question = request.data.get('question')

    if question is None:
        return Response({'message': 'question not found'},
                        status.HTTP_400_BAD_REQUEST)

    if not isinstance(question, list):
        return Response({'message': 'only a list can be sorted'},
                        status.HTTP_400_BAD_REQUEST)

    return Response({'solution': _order_by_repetition(question)})



