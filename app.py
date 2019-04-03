import time

import pigpio

from Sonar import Sonar


if __name__ == "__main__":

    pi = pigpio.pi()

    if not pi.connected:
        exit()

    S = [
        Sonar(pi, 0, 2),
        Sonar(pi, 3, 4),
        Sonar(pi, 5, 6),
        Sonar(pi, 25, 27),
    ]

    end = time.time() + 30.0

    r = 1

    try:
        while time.time() < end:

            for s in S:
                s.trigger()

            time.sleep(0.03)

            for s in S:
                print("{} {:.1f}".format(r, s.read()))

            time.sleep(0.2)

            r += 1

    except KeyboardInterrupt:
        pass

    print("\ntidying up")

    for s in S:
        s.cancel()

    pi.stop()
