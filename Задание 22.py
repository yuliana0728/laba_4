class Validator:
    def __init__(self, validator):
     print(isinstance(validator,Validator))
    email=input()
    def isEmail(self):
     if '@' and '.' in email: 
      print('Correct') 
     else: 
      print('Incorrect') 
    def isDomain(self, domain):
        domain=(int(input()).split('.'))
        if min(domain) >= 0 and max(domain) <= 255:
          print('Correct')
        else:
          print('Incorrect')
    def isNumber(self, lst):
        return any(isinstance(item, (int, float)) for item in lst)
