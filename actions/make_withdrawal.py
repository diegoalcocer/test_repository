"""Withdrawal Dialog."""

import sys
import questionary


def make_withdrawal(account):
    """Adjusts account balance for withdrawal.

        Script that verifies withdrawal amount is valid and adjusts account balance.

        Arg:
            account(dict): contains pin and balance for account

        Return:
            account(dict): returns account with balance adjusted for withdrawal

    """

    # @TODO:  Use questionary to capture the withdrawal and set it equal to amount variable. Be sure that amount is a floating point number.
    amount = questionary.text("How much would you like to withdrawal?").ask()
    amount = float(amount)
    # @TODO:  Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if amount <= 0.0:
        sys.exit(f"Your current account balance is {account['balance']: .2f}")
   
        # sys.exit(f"Your current account balance is {account['balance']: .2f}")
    # @TODO: Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    if account['balance'] >= amount:
        account['balance']-=amount
        print("Withdrawal successful")
        return account
    else:
        sys.exit("Not enough funds")