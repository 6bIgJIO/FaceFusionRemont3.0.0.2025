from facefusion import runtime, temp_helper

print("CALLING runtime.init() ...")
runtime.init()

print("TEMP DIR:", temp_helper.get_temp_directory())

import os
print("EXISTS:", os.path.isdir(temp_helper.get_temp_directory()))