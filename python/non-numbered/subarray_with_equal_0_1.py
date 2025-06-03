def largest_subarray(arr):
    # Initialize hash map to store cumulative sum and its index
    sum_index = {0: -1}  # Base case: sum is 0 at index -1
    cumulative_sum = 0
    max_length = 0
    
    for i, num in enumerate(arr):
        # Update cumulative sum (treat 0 as -1, 1 as 1)
        cumulative_sum += 1 if num == 1 else -1
        
        # If we've seen this cumulative sum before, update max_length
        if cumulative_sum in sum_index:
            max_length = max(max_length, i - sum_index[cumulative_sum])
        else:
            # Store the cumulative sum and its index
            sum_index[cumulative_sum] = i
    
    return max_length

# Example usage:
arr = [0, 1, 0, 1, 0, 0, 1, 1]
print(largest_subarray(arr))  # Output: 8