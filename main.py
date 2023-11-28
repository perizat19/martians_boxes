def find_cargo():
    cargo_locations = [0, 0, 0]
    total_weight = 0

    kilometer_mark = int(input(f"Enter the kilometer mark for box: "))

    if cargo_locations == kilometer_mark:
        print("Cargo already found at this location!")
    else:
        cargo_locations = kilometer_mark
        total_weight += kilometer_mark  
        print(f"Box found at kilometer {kilometer_mark}")
        
    
find_cargo()