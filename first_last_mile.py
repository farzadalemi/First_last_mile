### First and Last Mile

### inputs##########

#DB setup

# Location of Lookup table (closest BART to each TAZs centroid)

# Fixed inputs
all_stations= []
origin_stations=[]
dest_stations=[]

Donut=0
### if Donut = 1 needs to provide lower_buffer too
upper_buffer_origin=
upper_buffer_dest=

lower_buffer_origin=0
lower_buffer_dest=0

Access=1
Egress=0

walk_fixed_time=2.00


Uber_API = 1
## if the use of Uber API = 0 need to provide waiting time and cost 
uber_waiting_time=0.00
uber_cost= #function based on distance to bart station and other factors 

uber_pool=1
## if uber_pool = 1 needs to multiply the travel time = waiting for the bart and travel to bart by x factor
uber_pool_factor=110.00/100.00

## other fixed conditions
trip_purpose=
departure_hour=[]
trip_mode=[]

#### All inputs should be saved as a table in postgres
##### Finding origin and destination based on proximity conditions


#### Identifying potential users from MATSim output


#### Running google API


#### Running Uber API


#### Runnning BART API


#### Merging all dataset together (based on person_id)



		
		
		
		
  




