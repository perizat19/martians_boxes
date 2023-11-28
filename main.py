def find_cargo(first_loc, second_loc, third_loc, first_weight, second_weight, third_weight):
    cargo_locations = [first_loc, second_loc, third_loc]
    total_weight = 0
    total_ws = [first_weight, second_weight, third_weight]
    
kilometer_mark = int(input(f"Enter the kilometer mark for box {i+1}: "))
if cargo_locations[i] == kilometer_mark:
                print("Cargo already found at this location!")