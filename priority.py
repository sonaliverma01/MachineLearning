'''
Core Concept
In traditional systems, each vehicle is treated equally when determining 
traffic flow. However, this results in no special consideration for emergency vehicles. 
To solve this, we introduced a priority-based weighting system, where emergency vehicles 
are assigned a significantly higher weight compared to regular vehicles. 
This weight ensures that the lane with the emergency vehicle receives the highest 
priority in signal timing calculations.
'''

'''
Logic
1. Weight Assignment
Normal Vehicles: Assigned a weight of 1.
Emergency Vehicles: Assigned a weight of 100 (or a sufficiently high value).
This ensures that the emergency vehicle's presence heavily influences the c
alculation of green light durations.

2. Dynamic Signal Timing Calculation
The green light duration for each lane is calculated based on the proportion 
of its weighted vehicle count to the total weighted vehicle count across all lanes.

3. Real-Time Priority Adjustment
When an emergency vehicle is detected in a specific lane:

The vehicle count for that lane is updated by adding a weight of 100.
Signal timings are recalculated dynamically, giving the emergency vehicle's 
lane a longer green light duration.
Other lanes revert to their default or minimum timing.
'''
'''
Conclusion
By assigning higher weights to emergency vehicles in traffic calculations, 
our system ensures that critical services receive the priority they need, 
without disrupting the overall flow of traffic. This approach is efficient, 
scalable, and easily adaptable to real-world scenarios, paving the way for smarter, 
safer cities.
'''

# Dictionary to store the vehicle counts for each lane
# Normal vehicles are counted as 1, while emergency vehicles will have higher weight
vehicle_counts = {
    "North": 20,
    "South": 15,
    "East": 25,
    "West": 10
}

# Function to calculate green light durations based on weighted vehicle counts
def calculate_signal_timings(vehicle_counts):
    """
    Calculate the green light duration for each lane based on the proportion
    of vehicles in that lane to the total vehicles across all lanes.
    """
    # Calculate the total weighted vehicle count
    total_count = sum(vehicle_counts.values())
    signal_timings = {}

    # Determine green light duration for each lane
    for direction, count in vehicle_counts.items():
        # Proportional duration with a minimum of 10 seconds
        duration = max(10, int((count / total_count) * 60))
        signal_timings[direction] = duration

    return signal_timings

# Function to prioritize the lane with an emergency vehicle
def handle_emergency(vehicle_counts, emergency_direction):
    """
    Add a higher weight to the lane where the emergency vehicle is detected.
    This increases the priority for that lane during green light calculation.
    """
    # Assign a large weight to the emergency vehicle's lane
    vehicle_counts[emergency_direction] += 100
    return vehicle_counts

# Main function to simulate the priority-based traffic signal management
def main():
    """
    Main logic to handle emergency vehicle detection and recalculate
    green light durations dynamically.
    """
    # Detect an emergency vehicle in a specific lane (e.g., East lane)
    emergency_direction = "East"
    vehicle_counts_with_priority = handle_emergency(vehicle_counts, emergency_direction)

    # Recalculate the green light durations after assigning priority
    signal_timings = calculate_signal_timings(vehicle_counts_with_priority)

    # Print the final signal timings (this part can be replaced with actual signal control logic)
    return signal_timings

# Run the traffic signal logic
if __name__ == "__main__":
    main()
