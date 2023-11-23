def function():
    main_var = "I am a variable in __main__ block" + "s"
    print(main_var)  # 本地变量只在函数内可见


if __name__ == "__main__":
    main_var = "I am a variable in __main__ block"
    function()  # 调用函数，函数内可以访问全局变量
