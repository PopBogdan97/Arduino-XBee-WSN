#include <avr/sleep.h>
#include <DHT.h>

int wakePin = 2;  // pin used for waking up
int sleepStatus = 0;  // variable to store a request for sleep
int ID = 1; //ID of the end device 

//Constants
#define DHTPIN 7     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino

//Variables
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value

void wakeUpNow()        // here the interrupt is handled after wakeup
{
}

void setup()
{
   
  pinMode(wakePin, INPUT);

  Serial.begin(9600);
  dht.begin();

  attachInterrupt(0, wakeUpNow, LOW); // use interrupt 0 (pin 2) and run function
                                      // wakeUpNow when pin 2 gets LOW 
}


void sleepNow()         // here we put the arduino to sleep
{
    //Serial.println();
    //Serial.println("Sleeping");
    
    
    set_sleep_mode(SLEEP_MODE_PWR_DOWN);   // sleep mode is set here

    sleep_enable();          // enables the sleep bit in the mcucr register
                             // so sleep is possible. just a safety pin 

    delay(3000);

    attachInterrupt(0,wakeUpNow, LOW); // use interrupt 0 (pin 2) and run function
                                       // wakeUpNow when pin 2 gets LOW 

    sleep_mode();            // here the device is actually put to sleep!!
                             // THE PROGRAM CONTINUES FROM HERE AFTER WAKING UP

    sleep_disable();         // first thing after waking from sleep:
                             // disable sleep...
    detachInterrupt(0);      // disables interrupt 0 on pin 2 so the 
                             // wakeUpNow code will not be executed 
                             // during normal running time.

}

void loop()
{
  //delay(500);
    //Read data and store it to variables hum and temp
    hum = 32.0;
    temp = 87.4;
    //Print temp and humidity values to serial monitor
    Serial.print("ID: ");
    Serial.print(ID);
    Serial.print("; Hum: ");
    Serial.print(hum);
    Serial.print("%; Temp: ");
    Serial.print(temp);
    Serial.println("°");
    delay(3000); //Delay 2 sec.
    sleepNow();
}
