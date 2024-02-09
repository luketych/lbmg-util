import datetime


''' Takes as input a list of strings, and attempts to convert each element into its appropriate type.
    ie Numeric, String, Timestamp, Date, Float, etc
'''
def determine_data_type(element):
    try:
        datetime.datetime.strptime(element, "%Y-%m-%d")
        return 'DATE'
    except ValueError:
        try:
            datetime.datetime.strptime(element, "%Y-%m-%d %H:%M:%S.%f")
            return 'TIMESTAMP'
        except ValueError:
            try:
                int(element)
                return 'NUMERIC'
            except ValueError:
                try:
                    float(element)
                    return 'FLOAT'  # Check for floating-point numbers
                except ValueError:
                    return 'STRING'