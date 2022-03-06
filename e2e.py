from TestHelper import main_function

APP_URL = "http://localhost:5000/score/ziv"

try:
    main_function(APP_URL)
except FileNotFoundError as fnf_err:
    print("File not found. More Info:\n %s" % fnf_err.with_traceback())
    exit(-1)
