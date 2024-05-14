import hashlib

var = input('Digite o que deseja calcular o hash: ')

def hashmd5(string):
	md5 = hashlib.md5()
	md5.update(var.encode('utf-8'))
	md5var = md5.hexdigest()
	return md5var

def hashsha1(string):
	sha1 = hashlib.sha1()
	sha1.update(var.encode('utf-8'))
	sha1var = sha1.hexdigest()
	return sha1var

def hashsha224(string):
	sha224 = hashlib.sha224()
	sha224.update(var.encode('utf-8'))
	sha224var = sha224.hexdigest()
	return sha224var

def hashsha256(string):
	sha256 = hashlib.sha256()
	sha256.update(var.encode('utf-8'))
	sha256var = sha256.hexdigest()
	return sha256var

def hashsha384(string):
	sha384 = hashlib.sha384()
	sha384.update(var.encode('utf-8'))
	sha384var = sha384.hexdigest()
	return sha384var

def hashsha512(string):
	sha512 = hashlib.sha512()
	sha512.update(var.encode('utf-8'))
	sha512var = sha512.hexdigest()
	return sha512var

print(f'   MD5: {hashmd5(var)}')
print(f'  SHA1: {hashsha1(var)}')
print(f'SHA224: {hashsha224(var)}')
print(f'SHA256: {hashsha256(var)}')
print(f'SHA384: {hashsha384(var)}')
print(f'SHA512: {hashsha512(var)}')

input('\nAperte ENTER para sair...')