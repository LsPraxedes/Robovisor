from machine import Pin, PWM
from time import sleep, ticks_ms

# Botões
button_a = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_b = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Motor BDLC com ESC interno
motor_pwm = PWM(Pin(16))
motor_pwm.freq(500)  # Frequência analógica comum para ESCs

# Servo motor
servo_pwm = PWM(Pin(17))
servo_pwm.freq(50)  # Frequência padrão de servos

# Duty cycle para o motor (valores de 10% a 90%)
motor_duties = [6553, 16384, 26214, 36044, 45875, 58981]  # 0% até 100%
current_motor_index = 0

# Ângulos do servo motor
servo_positions = [2600, 7700, 12800, 7700, 2600]
servo_index = 0

while True:
    # Botão A: controlar velocidade
    if button_a.value() == 1:
        press_time = ticks_ms()
        while button_a.value() == 1:
            pass
        hold_duration = ticks_ms() - press_time

        if hold_duration > 2000:
            current_motor_index = 0
        else:
            if current_motor_index < len(motor_duties) - 1:
                current_motor_index += 1

        motor_pwm.duty_u16(motor_duties[current_motor_index])
        sleep(0.3)

    # Botão B: controlar servo
    if button_b.value() == 1:
        servo_pwm.duty_u16(servo_positions[servo_index])
        servo_index = (servo_index + 1) % len(servo_positions)
        sleep(0.3)
