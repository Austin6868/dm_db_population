from faker import Faker
import random
from datetime import timedelta
from decimal import Decimal
import pyperclip

fake = Faker()
unique_combs = set()

def generate_random_decimal(min_value=0, max_value=100, decimal_places=2):
    factor = 10 ** decimal_places
    return Decimal(random.randint(min_value * factor, max_value * factor)) / factor

def find_combos(ranges):
    comb = generate_unique_integers(ranges)
    print(comb)
    
    while comb in unique_combs:
        comb = generate_unique_integers(ranges)
    
    unique_combs.add(comb)
    return comb

def generate_unique_integers(ranges):
    unique_integers = []

    for min_value, max_value in ranges:
        while True:
            new_integer = random.randint(min_value, max_value)
            if new_integer not in unique_integers:
                unique_integers.append(new_integer)
                break

    return tuple(unique_integers)

def generate_random_start_end_times(min_hours=1, max_hours=12):
    start_time = fake.date_time()
    duration = timedelta(hours=random.randint(min_hours, max_hours))
    end_time = start_time + duration
    start_time_sql = start_time.strftime('%Y-%m-%d %H:%M:%S')
    end_time_sql = end_time.strftime('%Y-%m-%d %H:%M:%S')
    return start_time_sql, end_time_sql

def generate_data(num_entries):
    
    data = []

    unique_combs = set()

    for i in range(1, num_entries + 1):
        
        """
        When choosing the table structure, I recommend you take the methods 
        I've already used down there and come up with a combination of them
        to suite your own needs.
        """
        
        ################################################## change this to fit your own table's needs ##################################################
        # for adversiser table
        
        record = {
            'id': i,
            'name': "'" + fake.name() + "'",
            'email': "'" + fake.email() + "'",
        }
        
        # for ad table
        """
        record = {
            'id': i,
            'advertizerid': fake.random_int(min = 1, max = 500),
            'content': "'" + fake.paragraph(nb_sentences=3) + "'",
            'email': "'" + fake.email() + "'",
        }
        """
        # for hotel table #
        """
        record = {
            'id': i,
            'name': "'" + fake.name() + "'",
            'address': "'" + fake.paragraph(nb_sentences=3) + "'",
        }
        """
        # for room table # 
        """
        record = {
            'roomnumber': fake.random_int(min = 1, max = 50),
            'hotelid': fake.unique.random_int(min = 1, max = 500),
            'size': fake.random_int(min = 500, max = 1000),
            'description': "'" + fake.paragraph(nb_sentences=3) + "'",
            'pricenight': generate_random_decimal(min_value=100, max_value=1000, decimal_places=2),
        }
        """
        # for userinfo table # 
        """
        record = {
            'id': i,
            'firstname': "'" + fake.first_name() + "'",
            'lastname': "'" + fake.last_name() + "'",
            'email': "'" + fake.email() + "'",
        }
        """
        # for booking table # 
        """
        start_time, end_time = generate_random_start_end_times()
        record = {
            'id': i,
            'userid': fake.unique.random_int(min = 1, max = 500),
            'roomnumber': fake.random_int(min = 1, max = 50),
            'hotelid': fake.random_int(min = 1, max = 500),
            "starttime": "'" + start_time + "'",
            "endtime": "'" + end_time + "'",
        }
        """
        # for invioce table # 
        """
        record = {
            'id': i,
            'userid': fake.random_int(min = 1, max = 500),
        }
        """
        
        # for invioce line table # 
        """
        combos = find_combos(ranges=[(1, 500), (1, 50)]) # add the ranges based on number of unique foreign keys you want, only applies if you id is int:)

        record = {
            'invoiceid': combos[0],
            'linenumber': combos[1],
            'bookingid': fake.random_int(min = 1, max = 500),
        }
        """

        # for review table # 
        """
        combos = find_combos(ranges=[(1, 500), (1, 500)])
        record = {
            'userid': combos[0],
            'bookingid': combos[1],
            'stars': fake.random_int(min = 1, max = 5),
            'content': "'" + fake.paragraph(nb_sentences=3) + "'",
        }
        """

        # for recommendation table # 
        """
        record = {
            'userid': fake.random_int(min = 1, max = 500),
            'id': i,
        }
        """

        # for adrec table # 
        """
        combos = find_combos(ranges=[(1, 500), (1, 500)])
        record = {
            'recid': combos[0],
            'adid': combos[1],
            'content': "'" + fake.paragraph(nb_sentences=3) + "'",
        }
        """

        # for hotelrec table # 
        """
        combos = find_combos(ranges=[(1, 500), (1, 50), (1, 500)])
        record = {
            'recid': combos[0],
            'roomnumber': combos[1],
            'hotelid': combos[2],
            'content': "'" + fake.paragraph(nb_sentences=3) + "'",
            }
        """
        ###############################################################################################################################################
        
        data.append(record)
    return data

def generate_insert_statements(data_dict):
    insert_statements = []
    for table, records in data_dict.items():
        for record in records:
            columns = ', '.join(record.keys())
            placeholders = ', '.join(['%s'] * len(record))
            values = tuple(record.values())
            statement = f"INSERT INTO {table} ({columns}) VALUES ({placeholders});"
            formatted_statement = statement % values
            insert_statements.append(formatted_statement)
    return insert_statements

def generate_all_data(table, num_entries):
    data_to_insert = {
    table: generate_data(num_entries),
}
    
    return generate_insert_statements(data_to_insert)

def main():
    
    ################################################## change this to say how many entries you want and the table you'd like to populate ##################################################
    number_of_entries = 500
    table = "Advertiser"
    #######################################################################################################################################################################################

    insert_statements = generate_all_data(table, number_of_entries)
    text_to_paste = ""
    for statement in insert_statements:
        text_to_paste += statement + "\n"
        print(statement)
    
    pyperclip.copy(text_to_paste)
    
if __name__ == "__main__":
    main()