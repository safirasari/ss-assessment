# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    # TODO: Write your logic here safely


    try:
        return vehicle['specs']['model_info']['year'] 
    except KeyError:
        return "Unknown"

    pass

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))