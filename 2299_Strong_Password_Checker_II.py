# 2299. Strong Password Checker II
# A password is said to be strong if it satisfies all the following criteria:

#     It has at least 8 characters.
#     It contains at least one lowercase letter.
#     It contains at least one uppercase letter.
#     It contains at least one digit.
#     It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
#     It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).

# Given a string password, return true if it is a strong password. Otherwise, return false.


class Solution(object):
    def strongPasswordCheckerII(self, password):
        reqs = []
        lenght = len(password)
        prev = ''
        if len(password) > 7: 
            for i in password:
                check = ord(i)
                if  i != prev:                
                    if check > 96 and check < 123:
                        prev = i
                        reqs.append('lowercaseletter')
                        continue
                    elif check >= 48 and check <= 57:
                        prev = i
                        reqs.append('digit')
                        continue
                    elif check > 64 and check < 91:
                        reqs.append('uppercaseletter')
                        prev = i
                        continue
                    elif i in '!@#$%^&*()-+':
                        reqs.append('special character')
                        prev = i
                        continue
                else:
                    return False
                prev = i
                    
        if 'lowercaseletter' in reqs and 'digit' in reqs and 'uppercaseletter' in reqs and 'special character' in reqs:
            return True
        
        return False
        






