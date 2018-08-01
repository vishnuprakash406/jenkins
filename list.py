import sqlite3
conn=sqlite3.connect('im.db')
cur=conn.cursor()
def list() : 
	t1=[]
	condition1='y'
	print('--------------------------------------------------------------------------------')
	print ('id       ','name       ','price      ','tax      ','quantity   ','total')
	print('--------------------------------------------------------------------------------')
	while condition1=='y' or condition2=='y':
		condition1='n'
		i=raw_input('enter the item id    :')
		q=input('enter the quantity of item  :')
		sql="SELECT * FROM stock WHERE item_id = %s" %(i)
		cur.execute(sql)
		conn.commit()
		a=cur.fetchall()
		l=len(a)
		o=[]
		print(' ')
		for j in range(0,l) :
			t=(a[j][3]+a[j][4])*q
			t1.append(t)
			print(' ')
			print a[j][0],'\t\t',a[j][1],'\t\t',a[j][3],'\t\t',a[j][4],'\t\t',q,'\t\t',t
			x=a[j][2]
			o.append(x)
		i1=o[0]-q
		item_id=i
		sql="UPDATE stock SET quantity = %s WHERE item_id = %s" %(i1,item_id)
		cur.execute(sql)
		conn.commit()
		condition2=raw_input("Do you want to add more items (y/n) ? ")
	le=len(t1)
	print (' ')
	print(' ')
	print ('                                                                GRAND TOTAL='),sum(t1)
	print(' ')
list()
print('===================================================================================================')
conn.commit()
