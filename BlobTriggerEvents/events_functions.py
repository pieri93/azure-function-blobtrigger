from bs4 import BeautifulSoup 
import bs4
import pandas as pd

def read_events_xml(xml_file):
    """Obtains xml and transforms to a tidy pd DF 
    Parameters
    ----------
    xml_file : str
        xml file 
    Returns
    -------
    pd.DataFrame
        A tidy pd DataFrame 
    """

    soup = BeautifulSoup(xml_file, "xml")

    # According to xml structure, starts parsing by tag    
    child = soup.find("input")

    all_rows = []

    while True:
        try:
            row = {}

            serial_number = child.find("ElectronicSerialNumber").text
            row["SerialNumber"] = serial_number 

            timestamp = child.find("Timestamp")
            row[timestamp.name] = timestamp.text

            actual = timestamp.next_sibling

            # Creates a list data in row to group values under Arguments tag  
            row['data'] = [] 

            while actual is not None:
                if actual.name == 'Arguments': 
                    arg_list = reads_arguments(actual)
                    row['data'].append({"Arguments" : arg_list})   
                else:
                    row['data'].append({actual.name : actual.text})
                actual = actual.next_sibling
                    
            all_rows.append(row.copy())
            child = child.find_next_sibling("input")
        except:
            break

        # Generates DataFrame
        df = pd.DataFrame(all_rows)

        # Transforms Timestamp column to datetime 
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%dT%H:%M:%S.%f')
        df.set_index(['SerialNumber', 'Timestamp'])

        return(df)
    
def reads_arguments(tag: bs4.PageElement) -> list:
    """Reads name and value inside the tag Argument and returns a list

    Parameters
    ----------
    tag : bs4.PageElement
        xml element that contains the structure of Arguments. 

    Returns
    -------
    list
        List of arguments 
    """
    arg_list = []
    for argument in tag.children:
        name = argument.find("Name")
        value = argument.find("Value")
        arg_list.append({name.text : value.text})
    return arg_list
                        
def events_to_json(tidy_df: pd.DataFrame) -> str:
    """Transforms pandas DF into json 
    Parameters
    ----------
    tidy_df : pd.DataFrame
        DataFrame with the corresponding timestamp 
    Returns
    -------
    str
        Data in json format 
    """
    tidy_df.reset_index(drop=True)
    tidy_df.Timestamp = tidy_df.Timestamp.dt.tz_convert(tz="America/Costa_Rica").dt.strftime("%Y-%m-%d %H:%M:%S")

    # transformo a json por fila el pandas DF
    json_event = tidy_df.to_json(orient="records")
    return json_event