class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amt = f"{entry['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    # 1. Get withdrawal totals
    withdrawals = [sum(-item['amount'] for item in cat.ledger if item['amount'] < 0) for cat in categories]
    total_spent = sum(withdrawals)
    percentages = [int((w / total_spent) * 10) * 10 for w in withdrawals]
    
    # 2. Build bars
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for p in percentages:
            chart += " o " if p >= i else "   "
        chart += " \n" # Important: Space here before newline
    
    # 3. Add horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    
    # 4. Build vertical names
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "    "
        for name in [cat.name for cat in categories]:
            chart += f" {name[i] if i < len(name) else ' '} "
        chart += " \n" # Important: Space here before newline
        
    return chart.rstrip('\n')
