class Checkbook:
    def __init__(self):
        """
        Initialise un nouveau registre de chèques avec un solde de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant dans le registre de chèques.

        Paramètre:
        amount (float) : Le montant à déposer.

        Action:
        Ajoute le montant au solde actuel et affiche le nouveau solde.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant du registre de chèques.

        Paramètre:
        amount (float) : Le montant à retirer.

        Action:
        Si le montant est supérieur au solde, affiche un message d'erreur.
        Sinon, retire le montant du solde et affiche le nouveau solde.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du registre de chèques.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Point d'entrée principal du programme.
    Permet à l'utilisateur de déposer de l'argent, de retirer de l'argent,
    de vérifier le solde ou de quitter le programme. Gère les entrées non valides.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()