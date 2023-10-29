def countAttacksByYearRange(from_Y, untill_Y,data):
    """
    This function receives the start year and end year to search for data and a list of data.

    It returns a dictionary with the years and the count of occurrences for each year.

    :param from_Y: The start year for data search.
    :type from_Y: str
    :param untill_Y: The end year for data search.
    :type untill_Y: str
    :param data: The data to analyze.
    :type data: list[dict]
    :return: A dictionary with years and the count of occurrences.
    :rtype: dict
    """
    
    selected_data = {}
    attacks_in_year= 0
    
    try:
        if int(from_Y) <= int(untill_Y):

            for d in data:
                if d['Year'] >= from_Y and d['Year'] <= untill_Y:
                    attacks_in_year +=1
                    if d['Year'] in selected_data:
                        selected_data[d['Year']] +=1
                    else:
                        selected_data[d['Year']] = 1
 
            

            if len(selected_data) == 0:
                raise Exception ("No data found")
            
            return selected_data
                    
        else:
            raise Exception ("Incorrect date range")
        
    except Exception as error:
        return f"ERROR: {error}"
    


