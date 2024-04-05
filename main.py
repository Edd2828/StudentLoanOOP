#if __name__ == "main":
    #pass

from datetime import datetime, UTC

today = datetime.now(UTC).strftime("%Y-%m-%d")

print(str(today))

# Extract the year
#year = date_object.year
