import threading


class BankAccount:
    def __init__(self, name, balance, lock, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.name = name
        self.balance = balance
        self.lock = lock

    def withdraw(self, amount1):
        with self.lock:
            self.amount1 = amount1
            self.balance -= self.amount1
            print(f'Withdrew {self.amount1}, new balance is {self.balance}')

    def deposit(self, amount2):
        with self.lock:
            self.amount2 = amount2
            self.balance += self.amount2
            print(f'Deposited {self.amount2}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


lock = threading.Lock()
account = BankAccount('101102', 1000, lock=lock)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
