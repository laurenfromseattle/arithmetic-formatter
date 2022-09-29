def arithmetic_arranger(problems, show_result=False):
  '''Takes list of strings of arithmetic problems and returns the problems
     nicely formatted, including results if the optional second parameter is
     set to True.

     :param problems: list - list of arithmetic problems as strings, max of 5,
        only + or - operations, with operands limited to 4 digits,
        formatted as so 'x + y' or 'x - y'
     :param show_result: boolean (optional) - True to include results
     :result: str - formatted string of arithmetic problems
  '''

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
    x, operator, y = problem.split(' ')

    # fail condition: operator other than '+' or '-'
    if operator not in '+-':
      return "Error: Operator must be '+' or '-'."

    # fail condition: operands contain something other than digits
    if not x.isdigit() or not y.isdigit():
      return "Error: Numbers must only contain digits."

    # fail condition: operands have length greater than 4 digits
    if len(x) > 4 or len(y) > 4:
      return "Error: Numbers cannot be more than four digits."

    # set up variables
    count += 1
    offset = abs(len(x) - len(y))

    # build lines
    lines["top"] += ' ' * 2
    lines["bottom"] += operator + ' '
    lines["dashes"] += '-' * 2

    if len(x) > len(y):
      lines["top"] += x
      lines["bottom"] += ' ' * offset + y
      lines["dashes"] += '-' * len(x)
    else:
      lines["top"] += ' ' * offset + x
      lines["bottom"] += y
      lines["dashes"] += '-' * len(y)

    # conditional: results line
    if show_result:
      if operator == '+':
        result = str(int(x) + int(y))
      else:
        result = str(int(x) - int(y))

      lines["result"] += ' ' * (2 + max(len(x), len(y)) - len(result)) + result

    for line in lines:
      lines[line] += ' ' * 4 if count < len(problems) else '\n'

  # concatenate lines
  arranged_problems = lines["top"] + lines["bottom"] + lines["dashes"]

  # return arranged_problems
  return (arranged_problems + lines["result"].rstrip() if show_result
         else arranged_problems.rstrip())
