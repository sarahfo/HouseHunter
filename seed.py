"""File to seed homes database from merged csv file in data/"""

from model import House, connect_to_db, db
from server import app
import datetime, csv
from collections import namedtuple



def load_homes():
    """Load homes from merged_copy.csv into database."""

    with open('data/merged_copy.csv', 'r') as f:
    # datafile = open('data/merged_copy.csv')
        reader = csv.reader(f)
        # firstline = datafile.pop(0) #let this remove first line, baby jesus!
        headers = next(reader)  # assigns the headers to the variable header    
        reader.next()       # gets rid of the headers
        for home_info in reader:
            home_info = [s.decode("utf-8", errors="ignore") for s in home_info]
            home_type = home_info[1]
            address = home_info[2]
            city = home_info[3]
            state = home_info[4]
            zip_code = home_info[5]
            list_price = home_info[6]
            beds = home_info[7]
            baths = home_info[8]
            location = home_info[9]
            sqft = home_info[10]
            lot_size = home_info[11]
            year_built = home_info[12]
            parking_spots = home_info[13]
            parking_type = home_info[14]
            status = home_info[16]
            url = home_info[24]
            source = home_info[25]
            listing_id = home_info[26]
            original_source = home_info[27]
            favorite = home_info[28]
            latitude = home_info[30]  
            longitude = home_info[31]
            city_id = home_info[33]

            
              #testing
            # latitude = home_info[31]
            # if len(home_info[31]) == 0:
            #     latitude = None
            # else:
            #     latitude = float(home_info[31])
            # if home_info[32] == None:
            #     longitude = None
            # elif len(home_info[32]) == 0:
            #     longitude = None
            # else:
            #     longitude = float(home_info[32])
            # print "HI"  #checking!


            add_home = House(home_type=home_type, address=address, city=city, state=state, zip_code=zip_code, list_price=list_price,
                beds=beds, baths=baths, location=location, sqft=sqft, lot_size=lot_size, year_built=year_built, parking_spots=parking_spots,
                parking_type=parking_type, status=status, url=url, source=source, listing_id=listing_id, original_source=original_source, favorite=favorite,
                latitude=latitude, longitude=longitude, city_id=city_id)
            # print add_home
            db.session.add(add_home)
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    #load_users()
    load_homes()