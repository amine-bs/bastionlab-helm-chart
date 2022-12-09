from keys import SigningKey

data_owner_key = SigningKey.generate()
data_owner_key.save_pem("/home/privkeys/data_owner.key.pem")
data_owner_pub_key = data_owner_key.pubkey.save_pem("/home/owners/data_owner.pem")

data_scientist_key = SigningKey.generate()
data_scientist_key.save_pem("home/privkeys/data_scientist.key.pem")
data_scientist_pub_key = data_scientist_key.pubkey.save_pem("home/users/data_scientist.pem")