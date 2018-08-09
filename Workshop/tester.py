nights = 6
city = "Charlotte"

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
 	if(city == "Charlotte"):
  	 return (183 * nights)
	elif(city == "Tampa"):
   		return 220 * nights
 	elif(city == "Pittsburgh"):
   		return 222 * nights
 	elif(city == "Los Angeles"):
   		return 475 * nights
 	else:
		print "Error"
    