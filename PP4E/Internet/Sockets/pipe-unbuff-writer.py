# e.g. 12-15

import time, sys
for i in range(5):
    print(time.asctime())
    sys.stdout.write('spam\n')
    time.sleep(2)

