# キーワードパラメータはポジショナルパラメータより前に定義できない
# def func(first, second="2", third):
def func(first, second, third="3"):
    print(f"first: {first}, second: {second}, third: {third}")

# argument <-> parameter
func("1", "2", "33")

# func("1", third="2", "3") → NG
func("1", third="2", second="3")
func("1", "2", third="3")