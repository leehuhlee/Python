import sys

python_is_glorious = True
failure_is_option = False
proper_greeting = False

if len(sys.argv) == 2 and sys.argv[1] == "For the glory of Python!":
    proper_greeting = True

print(python_is_glorious)
print(failure_is_option)
print(proper_greeting)