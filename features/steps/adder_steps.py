from behave import given, when, then
from sources import add2vals as adder


@given('a component that processes inputs')
def step_given_two_numbers(context, num1, num2):
    context.num1 = num1
    context.num2 = num2
@when('I add "{a}" and "{b}"')
def step_when_i_add(context, a, b):
    context.result = adder.add2(a, b)
@then('the result should be "{expected_result}"')
def step_then_result_should_be(context, expected_result):
    assert str(context.result) == expected_result