#include <Time.h>

int redPin = 3;
int greenPin = 6;
int bluePin = 7;

int red;
int green;
int blue;
int transitionTime;

int getIncrementor( int oldValue, int newValue );

void setup()
{
  pinMode( redPin, OUTPUT );
  pinMode( greenPin, OUTPUT );
  pinMode( bluePin, OUTPUT );
  
  randomSeed( analogRead(0) );
  Serial.begin( 9600 );
  red = 100;
  green = 100;
  blue = 100;
  transitionTime = 0;
}

void loop()
{
  
}

int getIncrementor( int oldValue, int newValue )
{
  return ( oldValue - newValue ) < 0 ? 1 : -1;
}
