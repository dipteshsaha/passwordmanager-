# Zara is developing a new version of password manager. Earlier, she was using some third-party password manager but she figured out that it can't keep track of all the passwords which has been set for the respective account. As she is very concerned about the security, she decided to develop her own version of the password manager

# Objective: To develop a custom password manager using Python
# Domain:  Security
#Name Diptesh Saha
""""code starts from here """""
class BasePasswordManager:
  def __init__(self,old_passwords):
      self.old_passwords = old_passwords
  def get_password(self):
    print(self.old_passwords[-1])
  def is_correct(self, password):
              if password == self.old_passwords[-1] :
                  print(True)
              else:
                  print(False)
class PasswordManager(BasePasswordManager):
    def __init__(self,old_passwords):
        BasePasswordManager.__init__(self,old_passwords)
    def get_level(self):
            if self.old_passwords[-1].isalpha() or self.old_passwords[-1].isdigit():
                print('Before level 0')
                print('level 0')
            elif self.old_passwords[-1].isalnum():
                print('level 1')
            else:
                print('level 2')
    def set_password(self):
        if self.old_passwords[-1].isalpha() or self.old_passwords[-1].isdigit():
            y=1 
        elif self.old_passwords[-1].isalnum():
            y=2
        else:
            y=3
        while(True):
            k=input('\nPlease input a Strong Password:')
            if k.isalpha() or k.isdigit():
                z=1
            elif k.isalnum():
                 z=2
            else:
                z=3
            if len(k)>=6 and z==3:
                break
            elif len(k)>=6 and z>y:
                break
            else:
                print('\nPassword Not Set!Required a password of higher level than you previous password.')
        print('\nNew Password Set!')
        self.old_passwords.append(k)
x = ['1365357', "diptesh12345", 'Diptesh']
current = PasswordManager(x)
a=input('Type your password:')
current.is_correct(a)
current.get_level()
current.set_password()
current.get_password()