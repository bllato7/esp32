import wifi_conf

wifi_conf.set_connection()
print('\nThe party is started!')

import mpu_stream

mpu_stream.send(0.05)