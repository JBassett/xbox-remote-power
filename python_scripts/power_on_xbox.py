import sys, socket, select, time

XBOX_PORT = 5050
XBOX_PING = "dd00000a000000000000000400000002"

ip = data.get('ip', '')
live_id = data.get('live_id', '')
ping_only = data.get('ping_only', False)


def send_power(s, data, times=5):
    for i in range(0, times):
        s.send(data)
        time.sleep(1)

def send_ping(s):
    s.send(bytearray.fromhex(XBOX_PING))
    return select.select([s], [], [], 5)[0]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setblocking(0)
s.bind(("", 0))
s.connect((ip, XBOX_PORT))

live_id = live_id.encode()

if not ping_only:
    power_payload = b'\x00' + chr(len(live_id)).encode() + live_id.upper() + b'\x00'
    power_header = b'\xdd\x02\x00' + chr(len(power_payload)).encode() + b'\x00\x00'
    power_packet = power_header + power_payload
    logger.debug("Sending power on packets to {0}...".format(ip))
    send_power(s, power_packet)
    logger.debug("Xbox should turn on now, pinging to make sure...")

ping_result = send_ping(s)

if ping_result:
    logger.debug("Ping successful!")
else:
    logger.debug("Failed to ping Xbox :(")

s.close()
