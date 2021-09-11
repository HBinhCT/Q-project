#!/bin/python3


def main(person_list):
    users = []
    for name, email in person_list:
        if email.endswith('@gmail.com'):
            users.append(name)
    print(*sorted(users), sep='\n')


if __name__ == '__main__':
    N = int(input())
    persons = []
    for N_itr in range(N):
        firstName, emailID = input().split()
        persons.append((firstName, emailID))
    main(persons)
