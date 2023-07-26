# インポートの優先順
# 標準ライブラリ、　サードパーティのライブラリ、　自分たちのライブラリ、　ローカルのライブラリ
# 各ジャンル毎に1行開ける

import sys
sys.path.append("/Users/twawf/PythonLecture/Function/")

import mymodule
import docstring
# from mymodule import myfunc, myvar
mymodule.myfunc()
# print(mymodule.myvar)
# myfunc()
# print(str(myvar))
# print(type(myvar)
print(mymodule.myvar)
print(sys.path)
print(docstring.multiply(1, 5))