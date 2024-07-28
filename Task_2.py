def get_cats_info(path):
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

        # Initiating result list 
        result = []
        
        # Catching errors, such as empty file, wrong values, etc.
        try: 
            # Iteration of each raw and parsing values
            for i in content:
                line = i.split(',')
                
                #Catching value errors
                if len(line[0]) != 24: 
                    print(f"Wrong format of ID, correct {line[0]}")
                    return
                
                try:
                    int(line[2])
                except:
                    print(f"Wrong format of {line[1]}'s age, please provide a number")
                    return

                result.append({"id":line[0], "name":line[1], "age":line[2]})
                
            return result
        except (ValueError, IndexError, ZeroDivisionError):
            print(f"Please provide list in a correct format \"ID,cat's name,cat's age\"")