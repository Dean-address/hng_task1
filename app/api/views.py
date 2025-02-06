# from .serializers import NumberSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


def is_prime(num):
    if num < 0:
        return False
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True


def is_perfect(num):
    if num < 2:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num


def get_properties(num):
    # Check if Armstrong number
    num_str = str(abs(num))
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    is_armstrong = armstrong_sum == abs(num)

    # Check if Odd or Even
    if num % 2 == 0:
        is_even = True
        is_odd = False
    else:
        is_even = False
        is_odd = True

    # Return in the requested format
    if is_armstrong:
        if is_odd:
            return ["armstrong", "odd"]
        else:
            return ["armstrong", "even"]
    else:
        if is_even:
            return ["even"]
        else:
            return []


def digit_sum(num):
    n = abs(num)
    total = 0

    while n > 0:
        total += n % 10
        n //= 10
    return total


def fun_fact(num):
    url = f"http://numbersapi.com/{num}/math"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text  # Return the value from the response
    else:
        return "Error: Unable to fetch data."


class NumberView(APIView):
    def get(self, request):
        number_param = request.query_params["number"]

        if not number_param.isdigit():
            return Response(
                {
                    "number": "alphabet",
                    "error": True,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "number": int(number_param),
                "is_prime": is_prime(int(number_param)),
                "is_perfect": is_perfect(int(number_param)),
                "properties": get_properties(int(number_param)),
                "digit_sum": digit_sum(int(number_param)),
                "fun_fact": fun_fact(int(number_param)),
            },
            status=status.HTTP_200_OK,
        )
