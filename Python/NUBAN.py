
def __main__():
    '''Program to validate NUBAN account'''
    print("Hello!")
    code = input("Enter the bank code:_")
    account_number = input("Enter the account number:_")

    if validate_nuban_account(code, account_number):
        response = "Valid"
    else:
        response = "Invalid"

    print("The account number is {}.".format(response))

def pad_bank_code(bank_code,total_length=6):
    return "0"*(total_length-len(bank_code))+bank_code

def validate_nuban_account(bank_code, account_number):
    '''Validate Account Function'''
    result = False
    
    if  len(bank_code.strip()) <= 6 and len(account_number.strip()) == 10:
        bank_code=pad_bank_code(bank_code.strip())
        nuban = bank_code + account_number[:-1]

        check_digit = int(account_number[-1])
        nuban_array = [int(str(num)) for num in nuban ]
        nuban_sum = (nuban_array[0]*3 + nuban_array[1]*7 + nuban_array[2]*3
                     + nuban_array[3]*3 + nuban_array[4]*7 + nuban_array[5]*3
                     + nuban_array[6]*3 + nuban_array[7]*7 + nuban_array[8]*3
                     + nuban_array[9]*3 + nuban_array[10]*7 + nuban_array[11]*3
                     + nuban_array[12]*3 + nuban_array[13]*7 + nuban_array[14]*3)

        cal_check_digit = 10 - (nuban_sum%10)
        if cal_check_digit == 10:
            cal_check_digit = 0

        if check_digit == cal_check_digit:
            result = True
    return result

class NUBAN(object):
  """Utility for verifying NUBAN"""
  
  def is_valid_NUBAN(self, bank_code, account_number):
    return validate_nuban_account(bank_code.strip(), account_number.strip())

  def is_valid_NUBAN(self, nuban_number):
    """
    @param account_number A X-digit bank_code+NUBAN string 
    """
    nuban_number = nuban_number.strip()

    if len(nuban_number) > 16 or len(nuban_number)  <= 10: 
        return False
    account_number = nuban_number[-10:]
    bank_code = nuban_number[:len(nuban_number)-10]
    
if __name__ == '__main__':
    __main__()
