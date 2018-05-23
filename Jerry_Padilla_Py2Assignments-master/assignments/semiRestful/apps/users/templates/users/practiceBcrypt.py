import bcrypt
hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())

my_password = "Reh123321!1"

db_pw = bcrypt.hashpw(my_password.encode(), bcrypt.gensalt())
# print db_pw

nw_pw = 'Reh123321!1'
ms_pw = 'reh123321!1'

if bcrypt.checkpw(ms_pw.encode(),db_pw.encode()) == True:
    print 'true'
else:
    print 'false'
