import RPi.GPIO as GPIO
import time
import cv2

# Set up the GPIO pin for the lock and buzzer and sensors
lock_pin = 8
buzzer_pin = 10


GPIO.setmode(GPIO.BCM)
GPIO.setup(lock_pin, GPIO.OUT)

# Function to lock the bike
def lock_bike():
    GPIO.output(lock_pin, 1)
    print("Bike locked.")

# Function to unlock the bike
def unlock_bike():
    GPIO.output(lock_pin, 0)
    print("Bike unlocked.")

while True:
    command = input("Enter 'lock' to lock the bike or 'unlock' to unlock the bike: ")
    if command == "lock":
        lock_bike()
    elif command == "unlock":
            unlock_bike()
    else:
        print("Invalid command. Please enter 'lock' or 'unlock'.")
