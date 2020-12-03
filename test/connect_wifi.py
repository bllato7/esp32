import network

station = network.WLAN(network.STA_IF)
station.active(True)

station.connect("blase", "AGLL7HKEB9")

