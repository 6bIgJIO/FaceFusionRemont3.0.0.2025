import importlib

print("TEST 1: trying to import layout module...")
try:
    m = importlib.import_module("facefusion.uis.layouts.default")
    print("SUCCESS: Imported:", m)
except Exception as e:
    print("FAILED:", e)

print("\nTEST 2: listing directory...")
import os
print(os.listdir("facefusion/uis/layouts"))