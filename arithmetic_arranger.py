def arithmetic_arranger(problems, show_result=False):

  lines = {
    "top": "",
    "bottom": "",
    "dashes": ""
  }

  if show_result : lines["result"] = ""

  # fail condition: more than five problems
  if len(problems) > 5:
    return "Error: Too many problems."

  count = 0
  for problem in problems:

    # parse each argument
    operand_one, operator, operand_two = problem.split(' ')

    # fail condition: operator other than '+' or '-'
    if operator not in '+-':
      return "Error: Operator must be '+' or '-'."

    # fail condition: operands contain something other than digits
    if not operand_one.isdigit() or not operand_two.isdigit():
      return "Error: Numbers must only contain digits."

    # fail condition: operands have length greater than 4 digits
    if len(operand_one) > 4 or len(operand_two) > 4:
      return "Error: Numbers cannot be more than four digits."

    # set up variables
    count += 1
    offset = abs(len(operand_one) - len(operand_two))

    # build lines
    lines["top"] += ' ' * 2
    lines["bottom"] += operator + ' '
    lines["dashes"] += '-' * 2

    if len(operand_one) > len(operand_two):
      lines["top"] += operand_one
      lines["bottom"] += ' ' * offset + operand_two
      lines["dashes"] += '-' * len(operand_one)
    else:
      lines["top"] += ' ' * offset + operand_one
      lines["bottom"] += operand_two
      lines["dashes"] += '-' * len(operand_two)

    # conditional: results line
    if show_result:
      if operator == '+':
        result = str(int(operand_one) + int(operand_two))
      else:
        result = str(int(operand_one) - int(operand_two))

      lines["result"] += ' ' * (2 + max(len(operand_one), len(operand_two)) - len(result)) + result

    for line in lines:
      lines[line] += ' ' * 4 if count < len(problems) else '\n'

  # concatenate lines
  arranged_problems = lines["top"] + lines["bottom"] + lines["dashes"]

  # return arranged_problems
  return (arranged_problems + lines["result"].rstrip() if show_result
         else arranged_problems.rstrip())
