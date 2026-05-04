current_users = ['emily','jackson','david','leo','mark']
new_users = ['melona','Erick','david','leo']
for new_user in new_users:
    if new_user in current_users:
        print('Enter new username')
    else:
        print('is available')
    