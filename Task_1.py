def total_salary(path):
    from pathlib import Path

    # Check if file exists. 
    if Path(path).exists() == False:
        print(f'Файл {Path(path)} не існує')
        return
    else:
        # Reading file and removing \n from the end of each line
        with open(path, 'r', encoding='utf-8') as file:
            content = [el.strip() for el in file.readlines()]
            file.close()

        # Initiating counters for the loop  
        sum = 0
        count = 0
        
        # Catching errors, such as empty file, wrong values, etc.
        try: 
            # Iteration of each raw and working only with salary
            for i in content:
                line = i.split(',')
                sum = sum + int(line[1])
                count = count +1
            return [sum, int(sum/count)]
        except (ValueError, IndexError, ZeroDivisionError):
            print(f"Please provide list in a correct format \"Name,Salary\"")