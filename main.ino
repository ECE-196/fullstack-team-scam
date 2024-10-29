
void setup() {
    pinMode(LED, OUTPUT);

    // register "on_receive" as callback for RX event
    USBSerial.onEvent(ARDUINO_HW_CDC_RX_EVENT, on_receive);
    USBSerial.begin(9600);
}

void loop() {
    USBSerial.println("Hello, World!");
    delay(1000);
}


void on_receive(void* event_handler_arg, esp_event_base_t event_base, int32_t event_id, void* event_data) { 
    
}

// read one byte
char state { 
  USBSerial.read() 
};

// guard byte is valid LED state
if (!(state == LOW || state == HIGH)) {
    // invalid byte received
    // what else should we do?
    return;
}

// update LED with valid state
digitalWrite(LED, state);