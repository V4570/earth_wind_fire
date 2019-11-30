from Process import Process
import wind_speed as ws

speed, density, cp = ws.get_wind_data()

p = Process()
a = p.dataProcess(speed,density,cp)

print(a)
