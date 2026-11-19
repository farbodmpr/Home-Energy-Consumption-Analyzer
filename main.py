# HOME ENERGY CONSUMPTION ANALYZER

# Store all electrical devices
devices = []

# Store device names
device_names = []

# Store daily energy consumption
daily_consumption = []

# Get electricity price
electricity_price = input("Enter electricity price per kWh: ").strip()

if electricity_price.isdigit() is False:
    print("Invalid electricity price.")

else:

    electricity_price = float(electricity_price)

    # Register 5 electrical devices
    for i in range(5):

        print("\nDevice Number:", i + 1)

        name = input("Enter device name: ").strip().capitalize()

        if name == "":
            print("Device name cannot be empty.")
            continue

        power = input("Enter device power in watts: ").strip()

        if power.isdigit() is False:
            print("Invalid power value.")
            continue

        power = float(power)

        if power <= 0:
            print("Power must be greater than zero.")
            continue

        hours = input("Enter daily usage hours: ").strip()

        if hours.isdigit() is False:
            print("Invalid usage hours.")
            continue

        hours = float(hours)

        if hours <= 0 or hours > 24:
            print("Usage hours must be between 0 and 24.")
            continue

        # Calculate daily energy consumption in kWh
        daily_kwh = (power * hours) / 1000

        # Store device information
        devices.append([name, power, hours, daily_kwh])

        device_names.append(name)

        daily_consumption.append(daily_kwh)

    # Analyze registered devices
    print("\n========== ENERGY REPORT ==========")

    total_daily = 0
    total_monthly = 0

    if len(devices) > 0:

        for device in devices:

            name = device[0]
            power = device[1]
            hours = device[2]
            daily_kwh = device[3]

            monthly_kwh = daily_kwh * 30
            monthly_cost = monthly_kwh * electricity_price

            total_daily += daily_kwh
            total_monthly += monthly_kwh

            print("\nDevice:", name)
            print("Power:", power, "Watts")
            print("Daily Usage:", hours, "Hours")
            print("Daily Consumption:", daily_kwh, "kWh")
            print("Monthly Consumption:", monthly_kwh, "kWh")
            print("Monthly Cost:", monthly_cost)

            # Classify energy consumption
            if daily_kwh >= 5:
                print("Status: High Consumption")

            elif daily_kwh >= 1:
                print("Status: Medium Consumption")

            else:
                print("Status: Low Consumption")

        # Calculate total monthly electricity cost
        total_cost = total_monthly * electricity_price

        print("\n========== HOUSE SUMMARY ==========")

        print("Daily Consumption:", total_daily, "kWh")
        print("Monthly Consumption:", total_monthly, "kWh")
        print("Monthly Electricity Cost:", total_cost)

        # Find the highest and lowest consumers
        highest = devices[0]
        lowest = devices[0]

        for device in devices:

            if device[3] > highest[3]:
                highest = device

            if device[3] < lowest[3]:
                lowest = device

        print("\nHighest Consumer:", highest[0])
        print("Daily Consumption:", highest[3], "kWh")

        print("\nLowest Consumer:", lowest[0])
        print("Daily Consumption:", lowest[3], "kWh")

        # Sort device names alphabetically
        device_names.sort()

        print("\n========== DEVICE LIST ==========")

        for name in device_names:
            print(name)

        # Search for a device
        search_name = input("\nEnter a device name to search: ").strip().lower()

        found = False

        for device in devices:

            if search_name in device[0].lower():

                print("\nDevice Found:", device[0])
                print("Power:", device[1])
                print("Daily Consumption:", device[3], "kWh")

                found = True
                break

        else:
            print("Device not found.")

    else:
        print("No valid devices were registered.")

    print("\nProgram finished.")
