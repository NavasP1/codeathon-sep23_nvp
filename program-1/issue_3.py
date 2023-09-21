def validate_ip_address(ip):
    # Step 1: Split the IP address into its components
    components = ip.split('.')

    # Step 2: Check if the IP address has 4 components
    if len(components) != 4:
        return False

    # Step 3: Check if each component is an integer between 0 and 255
    for component in components:
        if not component.isdigit() or int(component) < 0 or int(component) > 255:
            return False

    # Step 4: Check if each component has no leading zeros, except for the value 0 itself
        if component[0] == '0' and len(component) > 1:
            return False

    # Step 5: Return True if all checks pass
    return True