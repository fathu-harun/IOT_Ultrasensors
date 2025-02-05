# makepython_ultrasensors

The IOT_Project folder are NOT IN ANY WAY used in the final code. Rather, the folder contains the iterations and tests to ensure each component of the final code is working properly.

MakePython will only run boot.py. Download boot.py in the MakePython to run the code.

Below explains what the code does
1) Declare the pins to the ultrasensors, red and green LED lights (shown in lines 20 to 29)
2) Define the functions
   1) connect_wifi() [self-explanatory],
   2) get_distance() [determine the distance of the closest vehicle/wall that is directly in front of the sensor]
   3) turn_on/turn_off lights [self_explanatory]
   4) get_sensor_data() [get vacancy of slot whether it is available or occupied depending on the value of get_distance()]
   5) get_distance2() ... get_sensor_data2() [same as b to d but for the next ultrasensor]
   6) send_data() [send both values of get_sensor_data() and get_sensor_data2() to server]
3) After declaring pins, code starts executing from lines 150 onwards.
