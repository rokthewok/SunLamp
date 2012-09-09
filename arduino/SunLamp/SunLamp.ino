#include <Time.h>

int NUMBER_OF_INTERVALS = 72;

int greenChange[NUMBER_OF_INTERVALS] = 
                          { 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0,
                            1, 0, 2, 0, 2, 0, 2, 0, 3, 0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4,
                            4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 7, 7, 8, 8, 8, 8, 8, 8, 10, 10,
                            10, 11, 11, 11, 11, 11
                          };

int blueChange[NUMBER_OF_INTERVALS] =
                          { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0
                            0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 2, 1, 1, 2, 1, 1,
                            2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2,
                            2, 2, 2, 3, 3, 4
                          };

int redPin = 3;
int greenPin = 6;
int bluePin = 7;

int red;
int green;
int blue;

void setup() {
  pinMode( redPin, OUTPUT );
  pinMode( greenPin, OUTPUT );
  pinMode( bluePin, OUTPUT );
  
  Serial.begin( 9600 );
}

void loop() {
  
}
