import sqlite3
import urllib2
import json



def doYourThing(url, member_id):
	try:
		result = urllib2.urlopen(url)
		json_data = json.load(result)
		locations = json_data['results']

	
		for location in locations:
			print location['geometry']['location']
			lat = location['geometry']['location']['lat']
			lon = location['geometry']['location']['lng']

			cur.execute("insert into rooms_room(member_id,name,description,size,address,city,state,zip,lat,lon,ctime) values (?,?,?,?,?,?,?,?,?,?,date('now'))", 
					(member_id, location['name'], location['icon'], '40', location['vicinity'], 'new york', 'ny', '10012', lat, lon ))

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

doYourThing( url1,0 )
doYourThing( url2,1 )
doYourThing( url3,2 )
doYourThing( url4,3 )
doYourThing( url5,4 )





#cur.execute("insert into rooms_member(name, points) values('adam', '0')")
#cur.execute("""insert into rooms_member(name, points)
#          values ('adam', '0')""")
#con.commit()

con.close()
