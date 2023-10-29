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
    
    try:
        if int(from_Y) <= int(untill_Y):

            for d in data:
                if d['Year'] >= from_Y and d['Year'] <= untill_Y:
                    if d['Year'] in selected_data:
                        selected_data[d['Year']] +=1
                    else:
                        selected_data[d['Year']] = 1

            if len(selected_data) == 0:
                raise Exception ("No data found")
            
            data_sorted = dict(sorted(selected_data.items(), key=lambda items: items[0]))

            return data_sorted
                    
        else:
            raise Exception ("Incorrect date range")
        
    except Exception as error:
        return f"ERROR: {error}"
    

def countBySex(data):
    """This function receives a list of data and
    counts how many men and women were attacked by sharks since 1791 to 2022.
    :param data: The data to analyze.
    :type data: list[dict]
    :return: A dictionary with the counts for 'Male' and 'Female' attacks.
    :rtype: dict
    """
    by_sex = {'Male': 0, 'Female': 0}
    for d in (data):
        if d['Sex'] in by_sex:
            by_sex[d['Sex']] += 1
    
    return by_sex
    

