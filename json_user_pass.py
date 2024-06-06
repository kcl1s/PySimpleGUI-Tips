import json

try:
    with open("json_user_pass.json", "r") as file:
        data = json.load(file)
        print(data)

except:
    data = {}
    print('No eisting file. Start from scratch')

try:
    while True:
        task = input('Enter a to add or s to search')
        if task == 'a':
            name = input('Enter username ')
            passw = input('Enter password ')
            data[name] = passw
        if task == 's':
            name = input('Enter username ')
            if name in data:
                passw = input('Enter password')
                if passw == data[name]:
                    print('Password correct')
                else:
                    print('Password not correct')
            else:
                print('Username unknown')
                
except KeyboardInterrupt:
    with open("json_user_pass.json", "w") as file:
        json.dump(data, file)
        print(data)
