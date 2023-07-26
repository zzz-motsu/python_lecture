# import myfirstpackage.module1
# import myfirstpackage.module2
# from myfirstpackage import module1
# from myfirstpackage.subdir import module2

# myfirstpackage.module1.myfunc()
# module1.myfunc()
# myfirstpackage.module2.myfunc()
# module2.myfunc()

from myfirstpackage.subdir import *
myfunc()
myfunc2()