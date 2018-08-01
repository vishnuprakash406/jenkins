import sqlite3
conn=sqlite3.connect('im.db')
cur=conn.cursor()
s=input('1:remove item  2: price 3:tax 4:quantity')
print(' ')
print('------------------------------------------------------------')
i=raw_input('enter the id for delete')
sql="DELETE FROM stock WHERE item_id = %s" %(i)
try:
	cur.execute(sql)
	conn.commit()
except:
	conn.rollback()
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
print('=======================================================================')
conn.close()
