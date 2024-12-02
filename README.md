# makepython_ultrasensors

MakePython will only run boot.py. Download boot.py in the MakePython to run the code

Below explains what the code does
1) Declare the pins to the ultrasensors, red and green LED lights (shown in lines 20 to 29)
2) Define the functions
   a. connect_wifi() [self-explanatory],
   b. get_distance() [determine the distance of the closest vehicle/wall that is directly in front of the sensor]
   c. turn_on/turn_off lights [self_explanatory]
   d. get_sensor_data() [send vacancy of slot depending on the value of get_distance()]
   e. get_distance2() ... get_sensor_data2() [same as b to d but for the next ultrasensor]
   f. send_data() [send both values of get_sensor_data() and get_sensor_data2() to server]
3) After declaring pins, code starts executing from lines 150 onwards.
