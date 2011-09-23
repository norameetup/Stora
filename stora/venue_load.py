import sqlite3
import urllib2
import json


def doYourThing(url, description, price, capacity):
	try:
		result = urllib2.urlopen(url)
		json_data = json.load(result)
		locations = json_data['results']

	
		for location in locations:
			print location['geometry']['location']
			lat = location['geometry']['location']['lat']
			lon = location['geometry']['location']['lng']

			cur.execute("insert into rooms_room(name,description,icon,price,capacity,address,city,state,zip,lat,lon,ctime) values (?,?,?,?,?,?,?,?,?,?,date('now'))", 
					(location['name'], description, location['icon'], price, capacity, location['vicinity'], 'new york', 'ny', '10012', lat, lon ))

			con.commit()

	except:
		print 'error!'



con = sqlite3.connect('sqlite3.db')
cur = con.cursor()
url1 = 'https://maps.googleapis.com/maps/api/place/search/json?location=40.730869,-73.997576&radius=500&types=food&name=coffee&sensor=false&key=AIzaSyCt2nJvUU0YDNK24Bg9rNFH0HxW7C2I0bo'
url2 = 'https://maps.googleapis.com/maps/api/place/search/json?location=40.730869,-73.997576&radius=500&types=museum&name=museum&sensor=false&key=AIzaSyCt2nJvUU0YDNK24Bg9rNFH0HxW7C2I0bo'
url3 = 'https://maps.googleapis.com/maps/api/place/search/json?location=40.730869,-73.997576&radius=500&types=bar&name=beer&sensor=false&key=AIzaSyCt2nJvUU0YDNK24Bg9rNFH0HxW7C2I0bo'
url4 = 'https://maps.googleapis.com/maps/api/place/search/json?location=40.730869,-73.997576&radius=500&types=bar&name=clown&sensor=false&key=AIzaSyCt2nJvUU0YDNK24Bg9rNFH0HxW7C2I0bo'
url5 = 'https://maps.googleapis.com/maps/api/place/search/json?location=40.730869,-73.997576&radius=500&types=bowling_alley&name=bowl&sensor=false&key=AIzaSyCt2nJvUU0YDNK24Bg9rNFH0HxW7C2I0bo'

doYourThing( url1, 'lovely and quaint, great place for some old friends to get together and catch up', 0, 20 )
doYourThing( url2, 'get some freaking culture dude', 50, 100 )
doYourThing( url3, 'get drunk, meet some people, forget their name in the morning.  you know how it goes.', 5, 20 )
doYourThing( url4, 'the happiest place in the world', 0, 20 )
doYourThing( url5, 'lots of pins and balls', 25, 50 )





#cur.execute("insert into rooms_member(name, points) values('adam', '0')")
#cur.execute("""insert into rooms_member(name, points)
#          values ('adam', '0')""")
#con.commit()

con.close()
