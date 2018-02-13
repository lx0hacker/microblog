from werkzeug.security import generate_password_hash,check_password_hash
hash = generate_password_hash('this$is%secure&password')
print(hash)

password_list = ['qwe123','qwer1234','this$is%secure&password']
for password in password_list:
    flag = check_password_hash(hash,password)
    if flag == True:
        print(password)