import MySQLdb
import json
import datetime

sqlserver = "127.0.0.1"
sqluser = "root"
sqlpass = "test4321"
sqldata = "dev_directory"

sqllists_json = []

def connect(self):
	global sqlserver
	global sqluser
	global sqlpass
	# Open database connection
#	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
	db = MySQLdb.connect(sqlserver,sqluser,sqlpass)

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	# execute SQL query using execute() method.
	cursor.execute("SELECT VERSION()")

	# Fetch a single row using fetchone() method.
	data = cursor.fetchone()

	print("Database version : %s " % data)

	# disconnect from server
	db.close()


 
def call_mlists_get():
	global sqllists_json
	sqllists_json = []
	sqllist_str = []
	try:
		conn = MySQLdb.connect(sqlserver,sqluser,sqlpass,sqldata)
		c = conn.cursor()
		c.callproc('mlists_get')

        # print out the result
		for result in c.fetchall():
#			sqllists_json.append(result)
			build = {}
			build['list_id'] = result[0]
			build['list_created'] = result[1].strftime('%m/%d/%Y')
			build['list_moddified'] = result[2].strftime('%m/%d/%Y')
			build['list_name'] = result[3]
			build['list_chimp_id'] = result[4]
			build['list_status'] = result[5]
#			print(build)
			sqllists_json.append(build)
#		print("sqllist - " + json.dumps(sqllists_json))

	except MySQLdb.Error as e:
		print(e)

	finally:
		c.close()
		conn.close()


def call_mlist_add(mname, mcid = None):
	try:
		conn = MySQLdb.connect(sqlserver,sqluser,sqlpass,sqldata)
		c = conn.cursor()
		c.callproc("mlists_add", (mname, mcid))
		conn.commit()
		print(c.fetchone())

	except MySQLdb.Error as e:
		print(e)

	finally:
		c.close()
		conn.close()