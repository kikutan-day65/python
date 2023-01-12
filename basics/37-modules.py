# modules = a file containing python code. May contain functions, classes, etc.
#           used with modular programming, which is to separate a program into parts

# import module as alias
import messages as msg

msg.hello()
msg.bye()


# in this case you dont need put module name before the function
from greetings import *

japanese()
czech()
spanish()


# help("modules") = shows all modules