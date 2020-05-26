def fun(s):
    # return True if s is a valid email, else return False
    import re
    # Email address must have the username@websitename.extension format type.
    # The username can only contain letters, digits, dashes and underscores.
    # The website name can only have letters and digits.
    # The maximum length of the extension is 3.
    return re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)