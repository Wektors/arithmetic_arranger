import re
def arithmetic_arranger(problems_list, *bool):
  
    problems = problems_list
  
    if bool:
      result_wanted = True
    else: 
      result_wanted = False

    print(problems, "\n")
    
    error_message = ""
  
    first_line = ""

    second_line = ""

    third_line = ""

    fourth_line = ""
    
    for operation in problems:
      if re.search("[a-zA-Z]", operation) != None:
        error_message = "Error: Numbers must only contain digits."
        
      if re.search(r"[/*]", operation) != None: 
        error_message = "Error: Operator must be \'+\' or \'-\'."
        
      new_operation = re.split('\s', operation)

      if len(new_operation[0]) > 4 or len(new_operation[2]) > 4:
        error_message = "Error: Numbers cannot be more than four digits."
      
      first_line_distance = ""

      second_line_distance = ""    

      distance_between_operation = "    "

      if first_line == "":
        distance_between_operation = ""

      to_first_line = new_operation[0]
      
      to_second_line = new_operation[2]
      
      to_first_line = "  " + to_first_line
      to_second_line = " " + to_second_line
      
      while len(to_first_line) - 1 < len(to_second_line):
        to_first_line = " " + to_first_line

      while len(to_first_line) - 1 > len(to_second_line):
        to_second_line = " " + to_second_line
      
      first_line += distance_between_operation + to_first_line
      
      second_line += distance_between_operation + new_operation[1] + to_second_line
      
      hyphens = ""
      
      for each in range(len(to_first_line)):
          hyphens += "-"

      third_line += distance_between_operation + hyphens
      result = ""
      if new_operation[1] == "+" and error_message == "":
        result = int(new_operation[0]) + int(new_operation[2])
      if new_operation[1] == "-" and error_message == "":
        result = int(new_operation[0]) - int(new_operation[2])
        
      to_fourth_line = str(result)

      while len(to_fourth_line) < len(to_first_line):
        to_fourth_line = " " + to_fourth_line

      fourth_line += distance_between_operation + to_fourth_line 
      
      arranged_problems = first_line + "\n" + second_line + "\n" + third_line
      
      if result_wanted:
        arranged_problems += "\n" + fourth_line

    if len(problems) > 5:
      error_message = "Error: Too many problems."

    if error_message != "":
      arranged_problems = error_message
  
    return arranged_problems