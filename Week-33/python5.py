# # import datetime

# # x=datetime.datetime.now()
# # daily=input("Enter daily learning update")

# # with open("learning_log.txt",'a') as f:
# #     f.write(daily)
# #     f.write(str(x))


# # with open("learning_log.txt",'r') as f:
# #     x=f.read()
# # count_char=0
# # count_lines=0
# # for i in x.split():
# #  count_char+=1
# # for i in x.splitlines():
# #    count_lines+=1
# # print(count_char,count_lines)


# import csv

# # 1. Create the file and write initial student data ('w' mode)
# with open("students.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Score"])
#     writer.writerow(["Ali", "85"])
#     writer.writerow(["Sara", "92"])

# # 2. Append more data to the same file ('a' mode)
# with open("students.csv", "a", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Ahmed", "78"])
#     writer.writerow(["Fatima", "95"])

# # 3. Get/read data, calculate the average, and save the results
# scores = []

# with open("students.csv", "r") as f:
#     reader = csv.reader(f)
#     header = next(reader)  # Skip the header row
    
#     for row in reader:
#         scores.append(float(row[1]))

# # Calculate average score
# average_score = sum(scores) / len(scores)

# # Write the final average to a separate output file
# with open("student_results.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Class Average"])
#     writer.writerow([average_score])

# print(f"Processing complete! The average score is: {average_score}")

# number1=int(input("Enter first number: "))
# number2=int(input("Enter second  number: "))

# try:
#     result=number1/number2
# except ZeroDivisionError:
#     print("You cannot divide number with zero")
# else:
#     print("Sucess ", result)
# finally:
#     print("Runs in both condition")

# def robust(number):
#     if 0 <= number <= 100:
#         print(True)
#         print("success")
#     else:
#         print("Number should be between 0 and 100")


# try:
#     number1 = int(input("Enter number: "))
#     robust(number1)
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")


def calculate_file_average(filename):
    valid_numbers = []
    
    try:
        with open(filename, "r") as f:
            for line_num, line in enumerate(f, 1):
                cleaned_line = line.strip()
                
                # Skip blank lines entirely
                if not cleaned_line:
                    continue
                
                try:
                    number = float(cleaned_line)
                    valid_numbers.append(number)
                except ValueError:
                    # Handle malformed lines gracefully
                    print(f"Warning: Skipping malformed line {line_num} ('{cleaned_line}')")
                    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be found.")
        return None

    # Handle the case where no valid numbers remain
    if not valid_numbers:
        print("Notice: No valid numbers found to calculate an average.")
        return 0.0

    average = sum(valid_numbers) / len(valid_numbers)
    return average


