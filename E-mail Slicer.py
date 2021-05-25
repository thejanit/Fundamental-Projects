user_email = input("Enter the E-mail: ").strip()

u_name = user_email[:user_email.index('@')]
d_name = user_email[user_email.index('@') + 1 : ]

output = print(f'Your username is: {u_name} and Your domain name is: {d_name}')
