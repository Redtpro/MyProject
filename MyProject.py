#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def run_code():
    username = input("Please enter your username to get started!")

    try:
        age = int(input(f"Thanks, {username}! Now, could you please tell us your age?"))
    except ValueError:
        print("Invalid input! Please enter a valid number for your age.")
        return

    if age > 12:
        correct_answer_1 = 16
        correct_answer_2 = 30
        success = False

        for attempt in range(2):
            if attempt == 0:
                answer = input("What is 6×2+4? ")
                try:
                    if int(answer) == correct_answer_1:
                        print("Correct! You can continue.")
                        success = True
                        break
                    else:
                        print("Oops! That’s not quite right.")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            else:
                answer = input("What is 5×6? ")
                try:
                    if int(answer) == correct_answer_2:
                        print("Correct! You can continue.")
                        success = True
                        break
                    else:
                        print("Oops! That’s not quite right.")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

        if not success:
            print("You failed both attempts. You are now considered a kid!")
    else:
        print(f"You're {age} years old, so no need for a math question. You can continue.")

if __name__ == "__main__":
    run_code()


# In[ ]:




