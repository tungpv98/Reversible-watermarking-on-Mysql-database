import MySQLdb as mysql
def connect():
	conn=mysql.connect('localhost','root','123456','test')
	return conn


def close(conn):
	conn.close()
