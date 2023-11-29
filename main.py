def find_cargo(first_loc, second_loc, third_loc, first_weight, second_weight, third_weight):
    cargo_locations = [first_loc, second_loc, third_loc]
    total_weight = 0
    total_ws = [first_weight, second_weight, third_weight]
    
    for i in range(3):
        kilometer_mark = int(input(f"Enter the kilometer mark for box {i+1}: "))
        if cargo_locations[i] == kilometer_mark:
            print("Cargo is already found at this location!")
            total_weight += total_ws[i]
            print (total_weight)
        
        else:
            cargo_locations[i] += 2
            print(f"Box {i+1} is not at kilometer {kilometer_mark}")
            print(cargo_locations[i])
            print(cargo_locations)
            