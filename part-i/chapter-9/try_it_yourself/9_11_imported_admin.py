"""import admin and privileges"""

from admin_template import Privileges, Admin

admin= Admin('tola','jimoh')
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()