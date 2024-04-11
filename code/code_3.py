<<<<<<< HEAD
# cf. https://github.com/PyCQA/bandit/blob/b1411bfb43795d3ffd268bef17a839dee954c2b1/examples/hashlib_new_insecure_functions.py

import hashlib

# ruleid:insecure-hash-function
hashlib.new('md5')

# ruleid:insecure-hash-function
hashlib.new('md4', 'test')

# ruleid:insecure-hash-function
hashlib.new(name='md5', string='test')

# ruleid:insecure-hash-function
hashlib.new('MD4', string='test')

# ruleid:insecure-hash-function
hashlib.new(string='test', name='MD5')

# ok:insecure-hash-function
hashlib.new('sha256')

# ok:insecure-hash-function
=======
# cf. https://github.com/PyCQA/bandit/blob/b1411bfb43795d3ffd268bef17a839dee954c2b1/examples/hashlib_new_insecure_functions.py

import hashlib

# ruleid:insecure-hash-function
hashlib.new('md5')

# ruleid:insecure-hash-function
hashlib.new('md4', 'test')

# ruleid:insecure-hash-function
hashlib.new(name='md5', string='test')

# ruleid:insecure-hash-function
hashlib.new('MD4', string='test')

# ruleid:insecure-hash-function
hashlib.new(string='test', name='MD5')

# ok:insecure-hash-function
hashlib.new('sha256')

# ok:insecure-hash-function
>>>>>>> 4568c2435b8367fca9bbe02afc2078287c266144
hashlib.new('SHA512')