import shirt_functions

shirt_functions.make_shirt('small', 'awesome')

#

from shirt_functions import make_shirt

make_shirt('large','cool')

#

from shirt_functions import make_shirt as ms

ms('xlarge','cool')

#

import shirt_functions as sf

sf.make_shirt('xsmall', 'awesome')

#

from shirt_functions import *

make_shirt('medium','so cool')

#

from shirt_functions import order_shirt

order_shirt('v neck','large','blue','cotton','40cm')