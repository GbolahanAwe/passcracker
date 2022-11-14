#!/bin/python3

import hashlib

type_of_hash = str(input('Which type of hash do you want to bruteforce ? '))
file_path = str(input('Enter path to the file to Bruteforce with: '))
hash_to_decrypt = str(input('Enter Hash Value to Brute force: '))

with open(file_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('\n')
                print('Found MD5 password: ' + line.strip())
                exit(0)
                
                
        if type_of_hash == 'sha1':
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('\n')
                print('Found SHA1 password: ' + line.strip())
                exit(0)      
                

    print('Password not in file.')                
