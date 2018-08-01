import sqlite3
conn=sqlite3.connect('im.db')
cur=conn.cursor()
cur.execute("SELECT * FROM stock")
a=cur.fetchall()
l=len(a)
print(' ')
print('--------------------------------------------------------------------')
print ('id       ','name       ','quantity    ','price      ','tax')
print('---------------------------------------------------------------------')
for j in range(0,l) :
	print(' ')
	print a[j][0],'\t\t',a[j][1],'\t\t',a[j][2],'\t\t',a[j][3],'\t\t',a[j][4]
print('============================================================')
conn.commit()