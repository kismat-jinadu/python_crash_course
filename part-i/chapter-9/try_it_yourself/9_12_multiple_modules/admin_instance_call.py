##to import from user, privilege and admin classes

from user_class import User
from privilege_admin_class import Privileges, Admin

admin= Admin('tola','jimoh')
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()