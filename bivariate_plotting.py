import numpy as np

"""
Function that assigns a value (x) to one of three bins (0, 1, 2).
The break points for the bins can be defined by break_a and break_b.
"""

def set_interval_value(x, break_1, break_2):
    if x <= break_1: 
        return 0
    elif break_1 < x <= break_2: 
        return 1
    else: 
        return 2

"""
Function that adds a column 'biv_bins' to the dataframe containing the 
position in the 9-color matrix for the bivariate colors
    
Arguments:
    df: Dataframe
    x: Name of the column containing values of the first variable
    y: Name of the column containing values of the second variable

"""

def prepare_df(df, x='x', y='y'):
    
    # Check if arguments match all requirements
    if df[x].shape[0] != df[y].shape[0]:
        raise ValueError('ERROR: The list of x and y coordinates must have the same length.')
    
    # Calculate break points at percentiles 33 and 66
    x_breaks = np.percentile(df[x], [33, 66])
    y_breaks = np.percentile(df[y], [33, 66])
    
    # Assign values of both variables to one of three bins (0, 1, 2)
    x_bins = [set_interval_value(value_x, x_breaks[0], x_breaks[1]) for value_x in df[x]]
    y_bins = [set_interval_value(value_y, y_breaks[0], y_breaks[1]) for value_y in df[y]]
    
    # Calculate the position of each x/y value pair in the 9-color matrix of bivariate colors
    df['biv_bins'] = [int(value_x + 3 * value_y) for value_x, value_y in zip(x_bins, y_bins)]
    
    return df

color_sets = {
    'pink-blue':   ['#e8e8e8', '#ace4e4', '#5ac8c8', '#dfb0d6', '#a5add3', '#5698b9', '#be64ac', '#8c62aa', '#3b4994'],
    'teal-red':    ['#e8e8e8', '#e4acac', '#c85a5a', '#b0d5df', '#ad9ea5', '#985356', '#64acbe', '#627f8c', '#574249'],
    'blue-organe': ['#fef1e4', '#fab186', '#f3742d',  '#97d0e7', '#b0988c', '#ab5f37', '#18aee5', '#407b8f', '#5c473d']
}

def load_geojson(geojson_url, data_dir="data", local_file=False):
    # Make sure data_dir is a string
    data_dir = str(data_dir)

    # Set name for the file to be saved
    if not local_file:
        # Use original file name if none is specified
        url_parsed = urlparse(geojson_url)
        local_file = os.path.basename(url_parsed.path)

    geojson_file = data_dir + "/" + str(local_file)

    # Create folder for data if it does not exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download GeoJSON in case it doesn't exist
    if not os.path.exists(geojson_file):
        # Make http request for remote file data
        geojson_request = requests.get(geojson_url)

        # Save file to local copy
        with open(geojson_file, "wb") as file:
            file.write(geojson_request.content)

    # Load GeoJSON file
    geojson = json.load(open(geojson_file, "r"))

    # Return GeoJSON object
    return geojson