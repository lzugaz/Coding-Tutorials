from Beginner.Beginner_Final_Project.Solution.BankAccount import BankAccount

class TestBankAccount:
    def __init__(self):
        self.score = 0
        self.total_tests = 6
        self.points_per_test = 100 // self.total_tests

    def run_tests(self):
        try:
            self.test_create_account()
            self.test_deposit_positive()
            self.test_withdraw_positive()
            self.test_withdraw_insufficient_funds()
            self.test_deposit_negative()
            self.test_withdraw_negative()
        except AssertionError as e:
            print(e)
        finally:
            print(f"\nFinal Score: {self.score}/{100}")

    def test_create_account(self):
        account = BankAccount("Test User")
        assert account.account_holder == "Test User", "Failed to create account with correct holder"
        assert account.balance == 0.0, "Failed to initialize balance to 0.0"
        self.score += self.points_per_test + 2
        print("Test Create Account: Passed")

    def test_deposit_positive(self):
        account = BankAccount("Test User")
        account.deposit(100)
        assert account.balance == 100, "Failed to deposit positive amount correctly"
        self.score += self.points_per_test + 2
        print("Test Deposit Positive: Passed")

    def test_withdraw_positive(self):
        account = BankAccount("Test User")
        account.deposit(100)
        account.withdraw(50)
        assert account.balance == 50, "Failed to withdraw positive amount correctly"
        self.score += self.points_per_test
        print("Test Withdraw Positive: Passed")

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("Test User")
        account.deposit(50)
        try:
            account.withdraw(100)
            assert False, "Failed to handle withdrawal exceeding balance"
        except ValueError:
            self.score += self.points_per_test
            print("Test Withdraw Insufficient Funds: Passed")

    def test_deposit_negative(self):
        account = BankAccount("Test User")
        try:
            account.deposit(-100)
            assert False, "Failed to handle negative deposit"
        except ValueError:
            self.score += self.points_per_test
            print("Test Deposit Negative: Passed")

    def test_withdraw_negative(self):
        account = BankAccount("Test User")
        try:
            account.withdraw(-100)
            assert False, "Failed to handle negative withdrawal"
        except ValueError:
            self.score += self.points_per_test
            print("Test Withdraw Negative: Passed")


if __name__ == "__main__":
    tester = TestBankAccount()
    tester.run_tests()
