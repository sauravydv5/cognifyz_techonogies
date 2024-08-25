def reverse_string(string):
  """Reverses a given string.

  Args:
    string: The string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

# Example usage:
input_string = "hello"
reversed_string = reverse_string(input_string)
print(reversed_string)