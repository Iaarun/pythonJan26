#try except is used to handle exceptions in python. It allows you to write code that can handle errors gracefully without crashing the program.


class ArithmeticOperations:
      def divide(self, a, b):
          print("Processing division...")
          try:
            div = a/b
            print("Division:", div)
          except ZeroDivisionError:
              print("Error: Division by zero is not allowed.")
          except Exception as e:
              print("An unexpected error occurred:", str(e))
          print("Division completed.")
      def iterateOverList(self, lst):
             print("Processing list iteration...")
             try:
                for i in range(len(lst)):
                    print(lst[i], end=" ")
             except IndexError:
                 print("\nError: List index out of range.")
             except Exception as e:
                 print("\nAn unexpected error occurred:", str(e))
             finally:
                 print("\nFinished iterating over the list.")

             print("List iteration completed.")



a1 = ArithmeticOperations()
#a1.divide(10, 0) # Output: 5.0

lst= [1, 2, 3, 4, 5]
a1.iterateOverList(lst) # Output: 1 2 3 4