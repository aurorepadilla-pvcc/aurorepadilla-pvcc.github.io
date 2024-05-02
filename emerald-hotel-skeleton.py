#Name: Aurore Padilla
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights

            else: subtotal = ROOM_RATES[2] * num_nights
                
#STUDENTS: COMPLETE THESE CALCULATIONS        
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + salestax + occupancy
             
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)


def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color :#ffffff; background-image: url(wp-hotel.jpeg); color: #ffffff;">\n')
    
def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "9">'
    sp = " "

    f.write('\n<table border="9"   style ="background-color: #ffa756;  font-family: georgia; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2 style="text-align: center;">Emerald Beach Hotel & Resort Guest Report</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('<tr><th colspan="9" style="text-align: center;">Guest Sales report</th></tr>')


    f.write('<tr>\n<th>Guest Last Name</th><th>Guest First Name</th><th>Room Type</th><th>Number of Nights</th><th>Subtotal</th><th>Sales Tax</th><th>Occupancy Tax</th><th>Total</th></tr>')

    for guest_data in guest:
        f.write('<tr style="text-align: center;">')
        f.write(td + str(guest_data[0]) + td + str(guest_data[1]) + td + str(guest_data[2]) + td + str(guest_data[3]) + td + format(guest_data[4], currency) + td + format(guest_data[5], currency) + td + format(guest_data[6], currency) + td + format(guest_data[7], currency) + endtr)
        f.write('</tr>')

    f.write('<tr><th colspan="9">Grand Total</th><th>' + format(grandtotal, currency) + '</th></tr>')


 #STUDENTS: INSERT ALL THE MISSING f.write STATEMENTS HERE
    
    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

##call on main program to execute##
main()
