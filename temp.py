import sys

# Check if user provided an argument
if len(sys.argv) > 1:
    temperature = float(sys.argv[1])
else:
    # Default value when user doesn't give input
    temperature = 25.0  # default temperature

# Check temperature condition
if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 30:
    print("Normal")
else:
    print("Hot")
