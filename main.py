#the imports
#
# enterprise part

import enterprise_part.BackEnd.decrypt_local
import enterprise_part.BackEnd.encrypt_local
import enterprise_part.BackEnd.encrypt_wide
import enterprise_part.BackEnd.fragmenting
import enterprise_part.BackEnd.sending_to_intermediate


# intermediate part
 import intermediate_part.BackEnd.compute_data
  import intermediate_part.BackEnd.decrypt_wide
   import intermediate_part.BackEnd.encrypt_wide
    import intermediate_part.BackEnd.receive
     import intermediate_part.Backend.sending_to_main

# main server part
import server_part.BackEnd.compute
import server_part.BackEnd.decrypt_wide
import server_part.BackEnd.encrypt_wide
import server_part.BackEnd.receive



# init phase

# first, we fragment
# *
# then, we encrypt localy
#
# then, we encrypt wodely
#
# then, we send data
#
#



#intermediate phase
#
# first, we receive
#
# then, we decrypt
#
#
# then, we compute
#
# then, we encrypt
#
# then we send
#
#
#
#



#final part
#
#
# first, we decrypt
#
# then, we compute,
#
#
#
# last, we decrypt

