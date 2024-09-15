import tkinter as tk
from tkinter import messagebox


# Class definitions and Tkinter setup
class SensorType:
    def __init__(self):
        global root
        root = tk.Tk()
        root.title("Life Sensor Control Panel")
        root.geometry("500x400")

        # Creates labels and button
        global title_label
        title_label = tk.Label(root, text="Life Sensor Dashboard", font=("Arial", 18))
        title_label.pack(pady=10)

        global message_label
        message_label = tk.Label(root, text="Most Recent Message: ")
        message_label.pack()

        global temp_label
        temp_label = tk.Label(root, text="Temperature Sensor: 0")
        temp_label.pack()

        global humidity_label
        humidity_label = tk.Label(root, text="Humidity Sensor: 0")
        humidity_label.pack()

        global motion_label       
        motion_label = tk.Label(root, text="Motion Sensor: None")
        motion_label.pack()

        global collision_label
        collision_label = tk.Label(root, text="Collision Sensor: None")
        collision_label.pack()

        global update_button
        update_button = tk.Button(root, text="Update Sensors", command=self.update_sensors_from_udp)
        update_button.pack(pady=10)
        #root.after(5000, self.periodic_update)

        # Handle window close
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Starts the GUI event loop
        root.mainloop()

    def update_data(self, new_data):

        self.status = "active"

    def update_status(self, new_status):
        self.status = new_status

    def get_data(self):
        return self.data

    def __repr__(self):
        return f"SensorType(sensor_type={self.sensor_type}, status={self.status}, data={self.data})"
    
    def periodic_update(self):
        return 1
        #self.update_sensors_from_udp()
        #root.after(5000, self.periodic_update)

    def on_closing(self):
        root.destroy()

    def get_sensor_data(self, sensor_name):
        return 1

# Updates the sensors from UDP data
    def update_sensors_from_udp(self):
        try:
            temp_data = self.get_sensor_data("Temperature")
            humidity_data = self.get_sensor_data("Humidity")
            motion_data = self.get_sensor_data("Motion")
            collision_data = self.get_sensor_data("Collision")

            temp_label.config(text=f"Temperature Sensor: {temp_data}")
            humidity_label.config(text=f"Humidity Sensor: {humidity_data}")
            motion_label.config(text=f"Motion Sensor: {motion_data}")
            collision_label.config(text=f"Collision Sensor: {collision_data}")

            self.check_alerts(temp_data, humidity_data, motion_data, collision_data)
        except Exception as e:
            print(f"No new data: {e}")

    # Checks sensor data for alert conditions
    def check_alerts(self, temp_data, humidity_data, motion_data, collision_data):
        try:
            temp_value = float(temp_data)
            if temp_value > 38.0:
                sensors["Temperature"].update_status("Warning")
                messagebox.showwarning("Heat Alert", "Temperature is above normal!")
        except ValueError:
            pass

        try:
            humidity_value = float(humidity_data)
            if humidity_value > 90.0:
                sensors["Humidity"].update_status("Warning")
                messagebox.showwarning("Humidity Alert", "Humidity is above normal!")
        except ValueError:
            pass

        if motion_data == "Motion Detected":
            sensors["Motion"].update_status("Warning")
            messagebox.showwarning("Motion Alert", "Motion detected!")

        if collision_data == "Collision Detected":
            sensors["Collision"].update_status("Warning")
            messagebox.showwarning("Collision Alert", "Collision detected!")

    def message_recieved(self, message):
        message_label.config(text=f"Most Recent Message: {message}")
        root.update()


    


# Instances for default sensors
#sensors = {
#    "Temperature": SensorType("Temperature", {"value": 0}),
#    "Humidity": SensorType("Humidity", {"value": 0}),
#    "Motion": SensorType("Motion", {"value": "None"}),
#    "Collision": SensorType("Collision", {"value": "None"})
#}

# Gets sensor data from UDP

# Cleanup function to stop the server and exit


# Main app window setup
# root = tk.Tk()
# root.title("Life Sensor Control Panel")
# root.geometry("500x400")

# # Creates labels and button
# title_label = tk.Label(root, text="Life Sensor Dashboard", font=("Arial", 18))
# title_label.pack(pady=10)

# temp_label = tk.Label(root, text="Temperature Sensor: 0")
# temp_label.pack()

# humidity_label = tk.Label(root, text="Humidity Sensor: 0")
# humidity_label.pack()

# motion_label = tk.Label(root, text="Motion Sensor: None")
# motion_label.pack()

# collision_label = tk.Label(root, text="Collision Sensor: None")
# collision_label.pack()

# update_button = tk.Button(root, text="Update Sensors", command=update_sensors_from_udp)
# update_button.pack(pady=10)

# Updates sensor readings every 5 seconds


