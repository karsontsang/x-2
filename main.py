def on_background_melody_paused():
    smarthome.motor_fan(AnalogPin.P9, True)
music.on_event(MusicEvent.BACKGROUND_MELODY_PAUSED,
    on_background_melody_paused)

def on_received_number(receivedNumber):
    radio.send_number(99)
radio.on_received_number(on_received_number)

def on_gesture_free_fall():
    led.plot(1, 4)
    bitbot.set_led_color(0xFF0000)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_button_pressed_a():
    basic.pause(5000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    input.set_accelerometer_range(AcceleratorRange.EIGHT_G)
input.on_button_pressed(Button.B, on_button_pressed_b)

bitbot.bb_enable_bluetooth(BBBluetooth.BT_ENABLE)
basic.show_leds("""
    . . . . .
        # # # # .
        # . . # .
        # # # # .
        . . . . .
""")
for index in range(1):
    basic.show_leds("""
        . # # . .
                . . # . .
                . # # . .
                . . # . .
                . # # . .
    """)
    basic.show_leds("""
        . . . . .
                . # # . .
                . . # . .
                . . # # #
                . . . . .
    """)
    basic.show_leds("""
        . . # . .
                . . # . .
                . . # . .
                . . . . .
                . . . . .
    """)

def on_forever():
    bitbot.select_model(BBModel.XL)
    bitbot.set_matrix(0xFFFF00)
    bitbot.set_led_color(0x80FF00)
    bitbot.set_led_color(0xFF0000)
    bitbot.set_led_color(0x00FFFF)
basic.forever(on_forever)

def on_in_background():
    game.create_sprite(2, 2).set(LedSpriteProperty.BLINK, 9)
control.in_background(on_in_background)