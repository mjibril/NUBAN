public class NUBAN {
  public static boolean isValidNUBAN(String bankCode, String accountNumber) {
      return isValidNUBAN(padBankCode(bankCode.trim()) + accountNumber.trim());
  }
  static String padBankCode(String bankCode)
  {
    String pad="";
    if(bankCode.length() < 6)
    {
	for(int i=0;i<6-bankCode.length();i++)
	{
	    pad=pad+'0';
	}
	return pad+bankCode;
    }
    return bankCode;

	
  }
  public static boolean isValidNUBAN(String accountNumber) {
    accountNumber = accountNumber.trim();

    if (accountNumber.length() > 16) return false; // 3-digit bank code + 10-digit NUBAN

    int[] accountNumberDigits = accountNumber.chars().map(x -> x - '0').toArray();

    int sum =
        (accountNumberDigits[0] * 3) + (accountNumberDigits[1] * 7) + (accountNumberDigits[2] * 3) +
        (accountNumberDigits[3] * 3) + (accountNumberDigits[4] * 7) + (accountNumberDigits[5] * 3) +
        (accountNumberDigits[6] * 3) + (accountNumberDigits[7] * 7) + (accountNumberDigits[8] * 3) +
        (accountNumberDigits[9] * 3) + (accountNumberDigits[10] * 7) + (accountNumberDigits[11] * 3)+
	(accountNumberDigits[12] * 3) + (accountNumberDigits[13] * 7) + (accountNumberDigits[14] * 3);
	;

    int mod = sum % 10;
    int checkDigit = (mod == 0) ? mod : 10 - mod;

    return checkDigit == accountNumberDigits[15];
  }

}
