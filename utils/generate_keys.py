from keys import SigningKey
import sys 

def main(args):
    users_number = int(args[0])
    data_owner_key = SigningKey.generate()
    data_owner_key.save_pem("home/privkeys/data_owner.key.pem")
    data_owner_pub_key = data_owner_key.pubkey.save_pem("home/owners/data_owner.pem")
    for i in range(users_number):
        data_scientist_key = SigningKey.generate()
        data_scientist_key.save_pem("home/privkeys/data_scientist{}.key.pem".format(i+1))
        data_scientist_pub_key = data_scientist_key.pubkey.save_pem("home/users/data_scientist{}.pem".format(i+1))



if __name__=="__main__":
    main(sys.argv[1:])