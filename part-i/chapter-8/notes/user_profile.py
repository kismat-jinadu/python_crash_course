#using arbituary keyword arguments
#to accept arbituary number of arguments, but dont know what kind of info sill be passed

def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=build_profile('albert','eisntein', 
              location='princeton',
              field='physics')
            
print(user_profile)