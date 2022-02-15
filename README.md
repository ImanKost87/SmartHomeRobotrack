# SmartHomeRobotrack
ID | NAME | PORT | TYPE | VALUES | 
--- | --- | --- | --- | --- |
0 | [IR remote control](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | bool | (True, False)
1 | [IR optocoupler](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | int/bool | (0-1023)/(True, False)
2 | [Color sensor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | int | (0-4, 9)
3 | [Distance sensor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | int | (2-300)
4 | [Light sensor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | int/bool | (0-1023)/(True, False)
5 | [Button](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | bool | True, False
6 | [Temperature sensor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | int | (min(Int)-max(Int))
7 | [Microphone analog (sound sensor)](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | int | (0-1023)
8 | [Threshold microphone](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | bool | True, False
9 | [Position sensor (gyroscope/accelerometer)](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | I2C | float | (min(Float)-max(Float))
10 | [Shaft angle sensor (encoder)](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8, IN1-IN8 | long | (min(Long)-max(Long))
11 | [Tilt sensor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | bool | True, False
12 | [Shock (vibration) sensor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | bool | True, False
13 | [Fire sensor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | bool | True, False
14 | [Magnetic field sensor (reed switch)](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | bool | True, False
15 | [Bending (deformation) sensor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | IN1-IN8 | int | (0-1023)
16 | [Neurohoop](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | ??UART, ??Bluetooth | ?? | ??
17 | [HD camera](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | ?? | ?? | ??
18 | [DC motor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | M1-M4 | int | (-100-100)
19 | [Servo motor](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | OUT1-OUT5 | int | (0-180)
20 | [Display](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | UART1-UART2 | int, int, int, int, char[] | ??(0-320), ??(0-320), (0-2), (0-7)
21 | [LED](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | OUT1-OUT5 | bool/??int | (True, False), ??(0-255)
22 | [Speaker](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | OUT1-OUT5 | int/int, int | (min(Int)-max(Int))/(min(Int)-max(Int)), (min(Int)-max(Int))
23 | [Buzzer](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | OUT1-OUT5 | int/int, int | (min(Int)-max(Int))/(min(Int)-max(Int)), (min(Int)-max(Int))
24 | [Audio track](https://robotrack-rus.ru/wiki/doku.php/ehlektronika/du/ik_pdu) | UART1-UART2 | int/int, int | (000-255)/(00-10), (000-255)
