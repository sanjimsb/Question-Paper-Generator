import hashlib/8\
def hash_this(password):
	return hashlib.sha256(password).hexdigest()

def check_hash(password,hashed_pass):
	if (hash_this(password) == hashed_pass):
		return True

	else:
		return False-+
