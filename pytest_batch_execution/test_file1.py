def test_login():
    raise Exception



def test_logout():
    print("logout executing")



def test_signup():
    pt("signup exceuting")




#
#
# collected 8 items
#
# test_file1.py::test_login FAILED
# test_file1.py::test_logout logout executing
# PASSED
# test_file1.py::test_signup FAILED
# test_file2.py::test_login FAILED
# test_file2.py::test_logout logout executing
# PASSED
# test_file2.py::test_signup FAILED
# test_file3.py::test_login login executing
# PASSED
# test_file3.py::test_signup FAILED
#
# =============================================== FAILURES ================================================
# ______________________________________________ test_login _______________________________________________
#
#     def test_login():
# >       raise Exception
# E       Exception
#
# test_file1.py:2: Exception
# ______________________________________________ test_signup ______________________________________________
#
#     def test_signup():
# >       pt("signup exceuting")
#         ^^
# E       NameError: name 'pt' is not defined
#
# test_file1.py:12: NameError
# ______________________________________________ test_login _______________________________________________
#
#     def test_login():
# >       raise Exception
# E       Exception
#
# test_file2.py:2: Exception
# ______________________________________________ test_signup ______________________________________________
#
#     def test_signup():
# >       pt("signup exceuting")
#         ^^
# E       NameError: name 'pt' is not defined
#
# test_file2.py:10: NameError
# ______________________________________________ test_signup ______________________________________________
#
#     def test_signup():
# >       pt("signup exceuting")
#         ^^
# E       NameError: name 'pt' is not defined
#
# test_file3.py:10: NameError
# ======================================== short test summary info ========================================
# FAILED test_file1.py::test_login - Exception
# FAILED test_file1.py::test_signup - NameError: name 'pt' is not defined
# FAILED test_file2.py::test_login - Exception
# FAILED test_file2.py::test_signup - NameError: name 'pt' is not defined
# FAILED test_file3.py::test_signup - NameError: name 'pt' is not defined
# ====================================== 5 failed, 3 passed in 0.39s =======