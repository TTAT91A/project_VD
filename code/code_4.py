<<<<<<< HEAD
# cf. https://github.com/PyCQA/bandit/blob/b78c938c0bd03d201932570f5e054261e10c5750/examples/crypto-md5.py

import hashlib


# ruleid:insecure-hash-algorithm-sha1
hashlib.sha1(1)

# ok:insecure-hash-algorithm-sha1
=======
# cf. https://github.com/PyCQA/bandit/blob/b78c938c0bd03d201932570f5e054261e10c5750/examples/crypto-md5.py

import hashlib


# ruleid:insecure-hash-algorithm-sha1
hashlib.sha1(1)

# ok:insecure-hash-algorithm-sha1
>>>>>>> 4568c2435b8367fca9bbe02afc2078287c266144
hashlib.sha256(1)