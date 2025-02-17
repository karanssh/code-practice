from typing import List 

class UniqueEmails:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        
        for email in emails:
            #  step 1, split based on local and domain name
            splitEmail = email.split("@")
            #  step 2, filter the local email
            #  step 2.1, ignore everything after +
            splitEmail[0] = splitEmail[0].split("+")[0]
            #  step 2.2, remove . from the string
            splitEmail[0] = splitEmail[0].replace(".","", -1)
            res.add("@".join(splitEmail)) 

        return len(res)


if __name__ == "__main__":
    
    obj = UniqueEmails()
    print(obj.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
    print(obj.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))


    
