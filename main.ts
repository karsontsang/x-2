music.onEvent(MusicEvent.BackgroundMelodyPaused, function () {
    smarthome.motorFan(AnalogPin.P9, true)
})
radio.onReceivedNumber(function (receivedNumber) {
    radio.sendNumber(99)
})
input.onButtonPressed(Button.A, function () {
    basic.pause(5000)
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    input.setAccelerometerRange(AcceleratorRange.EightG)
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    smarthome.motorFan(AnalogPin.P9, true)
    pins.analogWritePin(AnalogPin.P9, 58545)
    game.removeLife(4.4444444444444446e+119)
})
basic.showLeds(`
    . # . . .
    # # # # .
    # . . # .
    # # # # .
    . . . . .
    `)
for (let index = 0; index < 1; index++) {
    basic.showLeds(`
        . # # . .
        . . # . .
        . # # . .
        . . # . .
        . # # . .
        `)
    basic.showLeds(`
        . . . . .
        . # # . .
        . . # . .
        . . # # #
        . . . . .
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . . . .
        `)
}
basic.forever(function () {
    bitbot.select_model(BBModel.XL)
    bitbot.setMatrix(0xFFFF00)
    bitbot.setLedColor(0x80FF00)
    bitbot.setLedColor(0xFF0000)
    bitbot.setLedColor(0x00FFFF)
})
control.inBackground(function () {
    game.createSprite(2, 2).set(LedSpriteProperty.Blink, 9)
})
control.inBackground(function () {
    bitbot.buzz(true)
})
