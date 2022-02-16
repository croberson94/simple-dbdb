# Filename: tool.py
# Description: defines a command-line tool for exploring a database
#              from the terminal window
#

########
# MAIN #
########
def main(argv):
	if not (4 <= len(argv) <= 5):
		usage()
		return BAD_ARGS
	dbname, verb, key, value = (argv[1:] + [None])[:4]
	if verb not in {'get', 'set', 'delete'}:
		usage()
		return BAD_VERB
	db = dbdb.connect(dbname) # CONNECT
	try:
		if verb == 'get':
			sys.stdout.write(db[key]) # GET VALUE
		elif verb == 'set':
			db[key] = value # SET VALUE
			db.commit() # COMMIT
		else:
			db[key] = value
			db.commit()
		else:
			del db[key]
			db.commit()
	except KeyError:
		print("Key not found", file=sys.stderr)
		return BAD_KEY
	return OK