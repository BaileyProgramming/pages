import MySQLdb
import json
import datetime
import appconf


sqllists_json = []


def set_conn():
	conn = MySQLdb.connect(appconf.conf.get('SQL', 'sql_server'),appconf.conf.get('SQL', 'sql_user'),appconf.conf.get('SQL', 'sql_pass'),appconf.conf.get('SQL', 'sql_db'))
	return conn

def connect():
	# Open database connection
#	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
	db = set_conn()

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
		conn = set_conn()
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
		conn = set_conn()
		c = conn.cursor()
		c.callproc("mlists_add", (mname, mcid))
		conn.commit()
		print(c.fetchone())

	except MySQLdb.Error as e:
		print(e)

	finally:
		c.close()
		conn.close()


def call_mmembers_get(email):
	print(email)
	members = {}
	try:
		conn = set_conn()
		c = conn.cursor()
		c.callproc("mmembers_get", [email])

		for result in c.fetchall():
			print(result)
#			build = {}
#			build['name_id'] = result['name_id']
#			build['fname'] = result['name_first']
#			build['mname'] = result['name_middle']
#			build['lname'] = result['name_last']
#			build['maiden'] = result['name_maiden']
#			build['birthday'] = result['name_birthday']
#			build['gender'] = result['name_gender']
#			build['ms_status'] = result['ms_status']
			
#			members.append(build)

	except MySQLdb.Error as e:
		print(e)

		members.append("('error':1)")
	
	finally:
		c.close()
		conn.close()

		return members