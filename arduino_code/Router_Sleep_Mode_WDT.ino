#include <avr/sleep.h>
#include <avr/power.h>
#include <avr/wdt.h>
#include <DHT.h>

//Constants
#define DHTPIN 7     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
#define LED_PIN (13)

//Variables
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value
int ID = 1;

volatile int f_wdt=1;

volatile int sleep_count = 0;
const int interval = 1;
const int sleep_total = (interval*60)/8;


ISR(WDT_vect)
{
  if(f_wdt == 0)
  {
    f_wdt=1;

    sleep_count ++;
  }
  else
  {
    Serial.println("WDT Overrun!!!");
  }

}

void enterSleep(void)
{
  set_sleep_mode(SLEEP_MODE_PWR_DOWN);   /* EDIT: could also use SLEEP_MODE_PWR_DOWN for lowest power consumption. */
  sleep_enable();
  
  /* Now enter sleep mode. */
  sleep_mode();
  
  /* The program will continue from here after the WDT timeout*/
  sleep_disable(); /* First thing to do is disable sleep. */
  
  /* Re-enable the peripherals. */
  power_all_enable();
}

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("Initialising...");
  delay(100); //Allow for serial print to complete.

  pinMode(LED_PIN,OUTPUT);

  /*** Setup the WDT ***/
  
  /* Clear the reset flag. */
  MCUSR &= ~(1<<WDRF);
  
  /* In order to change WDE or the prescaler, we need to
   * set WDCE (This will allow updates for 4 clock cycles).
   */
  WDTCSR |= (1<<WDCE) | (1<<WDE);

  /* set new watchdog timeout prescaler value */
  WDTCSR = 1<<WDP0 | 1<<WDP3; /* 8.0 seconds */
  
  /* Enable the WD interrupt (note no reset). */
  WDTCSR |= _BV(WDIE);
  
  Serial.println("Initialisation complete.");
  delay(100); //Allow for serial print to complete.

}

void loop() {
    if(f_wdt == 1)
  {
    if(sleep_count == sleep_total){
    /* Toggle the LED */
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    
    //Read data and store it to variables hum and temp
    hum= dht.readTemperature();
    temp = dht.readHumidity();
    //Print temp and humidity values to serial monitor
    Serial.print("Sensor ID: ");
    Serial.print(ID);
    Serial.print("  Humidity: ");
    Serial.print(hum);
    Serial.print("%, Temperature: ");
    Serial.print(temp);
    Serial.print("° "); 
    delay(3000); //Delay 2 sec.
    sleep_count = 0;
    }
    /* Don't forget to clear the flag. */
    f_wdt = 0;
    
    /* Re-enter sleep mode. */
    enterSleep();
  }
  else
  {
    /* Do nothing. */
  }

}
