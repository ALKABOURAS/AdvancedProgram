import unittest
import coverage


# Μέθοδος που επιστρέφει το αποτέλεσμα της πράξης αφαίρεσης δύο αριθμών και το πρόσημό τους
def subtraction_and_sign(num1, num2):
    result = num1 - num2
    if result >= 0:
        return "POSITIVE"
    else:
        return "NEGATIVE"


# Κλάση που περιέχει τα unit tests
class TestSubtraction(unittest.TestCase):

    def test_positive_result(self):
        result = subtraction_and_sign(10, 5)
        self.assertEqual(result, "POSITIVE")

    def test_negative_result(self):
        result = subtraction_and_sign(5, 10)
        self.assertEqual(result, "NEGATIVE")

    def test_zero_result(self):
        result = subtraction_and_sign(5, 5)
        self.assertEqual(result, "POSITIVE")



# Κύριο πρόγραμμα
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = subtraction_and_sign(num1, num2)
    # Add breakpoint here
    breakpoint()
    print("The result is: ", result)


# Κλήση της main
if __name__ == "__main__":
    # Δημιουργία αντικειμένου coverage
    cov = coverage.Coverage()
    # Εκκίνηση του coverage
    cov.start()
    # Κλήση της main
    # main()
    # Κλήση των unit tests
    unittest.main()
    # Τερματισμός του coverage
    cov.stop()

    # Εκτύπωση του coverage report
    cov.report()

