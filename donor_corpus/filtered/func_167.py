def run():
    """The main function for running the script."""
    bank_data = load_bank_data()
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()
    qualifying_loans = find_qualifying_loans(bank_data, credit_score, debt, income, loan_amount, home_value)
    save_qualifying_loans(qualifying_loans)