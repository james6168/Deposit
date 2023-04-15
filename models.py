class User:

    deposit_account = 0

    def __init__(self, user_id,
                 user_deposit,
                 user_last_percentage,
                 ):
        self.user_id = user_id
        self.deposit = user_deposit
        self.last_percentage = user_last_percentage

    def __str__(self):
        return f"user_id: {self.user_id}, deposit: {self.deposit}, last_percentage: {self.last_percentage}"

    def get_id(self):
        return self.user_id

    def get_deposit(self):
        return self.deposit

    def get_last_percentage(self):
        return self.last_percentage

    def get_deposit_account(self):
        return self.deposit_account
