import random

class Doctor:
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

class Appointment:
    def __init__(self, id, doctor, date_time):
        self.id = id
        self.doctor = doctor
        self.date_time = date_time

class AppointmentSystem:
    def __init__(self):
        self.doctors = []
        self.appointments = []
        self.current_appointment_id = 1
        self.last_assigned_doctor = None  

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, date_time):
        available_doctors = [doctor for doctor in self.doctors if doctor != self.last_assigned_doctor]
        if available_doctors:
            random_doctor = random.choice(available_doctors)
            self.last_assigned_doctor = random_doctor
            appointment = Appointment(self.current_appointment_id, random_doctor, date_time)
            self.appointments.append(appointment)
            self.current_appointment_id += 1
            print(f"Appointment with {appointment.doctor.name} has been  scheduled successfully!")
        else:
            print("No doctors available.")

    def view_appointments(self):
        for appointment in self.appointments:
            print(f"Appointment ID: {appointment.id}, Doctor: {appointment.doctor.name}, Date and Time: {appointment.date_time}")

    def cancel_appointment(self, appointment_id):
        appointment = next((a for a in self.appointments if a.id == appointment_id), None)
        if appointment:
            self.appointments.remove(appointment)
            print(f"Appointment with {appointment.doctor.name} has been cancelled")
        else:
            print("Appointment not found.")



def main():
    system = AppointmentSystem()

    doctor1 = Doctor(1, "Dr. Akimarin", "Optician")
    doctor2 = Doctor(2, "Dr. Okonwo", "Dermatologist")
    doctor3 = Doctor(3, "Dr. Amadi", "Optician")
    doctor4 = Doctor(4, "Dr. Eze", "Dentist")

    system.add_doctor(doctor1)
    system.add_doctor(doctor2)
    system.add_doctor(doctor3)
    system.add_doctor(doctor4)

    while True:
        print("\nAppointment Management System")
        print("----------------------------------")
        print("1. Schedule Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("")
            date_time = input("Enter Date and Time (YYYY-MM-DD HH:MM): ")
            system.schedule_appointment(date_time)
        elif choice == '2':
            print("")
            system.view_appointments()
        elif choice == '3':
            print("")
            appointment_id = int(input("Enter Appointment ID to be cancelled: "))
            system.cancel_appointment(appointment_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
