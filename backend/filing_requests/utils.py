def validate_range(data, errors, min_field, max_field, label):
    min_value = data.get(min_field)
    max_value = data.get(max_field) 

    if min_value is not None and max_value is not None and min_value > max_value:
        errors[max_field] = f"{label}: مقدار حداکثر باید بزرگ‌تر یا مساوی حداقل باشد."
