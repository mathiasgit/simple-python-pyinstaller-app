Feature: Component - Flexible Adder
  Scenario Outline: Add two inputs of the same type
    Given a component that processes inputs
    When I add "<input_a>" and "<input_b>"
    Then the result should be "<expected_result>"