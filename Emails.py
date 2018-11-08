#https://leetcode.com/problems/unique-email-addresses/description/

def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    newEmails = []
    for email in emails:
        name = email.split("+")[0]
        nameSplit = name.split(".")
        nameJoin = "".join(nameSplit)
        domain = email.split("@")[1]
        NewEmail = nameJoin + "@" + domain
        newEmails.append(NewEmail)
    return len(set(newEmails))


