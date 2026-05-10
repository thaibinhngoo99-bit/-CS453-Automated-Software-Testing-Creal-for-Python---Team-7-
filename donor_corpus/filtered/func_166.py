def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    choice = questionary.confirm('Would you like to save the qualifying loans?').ask()
    if choice == T:
        filepath = questionary.text('Please enter the file path').ask()
        save_csv(qualifying_loans, filepath)