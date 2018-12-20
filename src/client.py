import threading
import requests
from datetime import datetime

n_requests = 20
web_url = "http://132.207.12.110:8080"

def doWork():
    r = requests.get(web_url)
    print(r)

threads = []

start_time = datetime.now()
for i in range(n_requests):
    t = threading.Thread(target=doWork)
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()

average_time = (datetime.now() - start_time) / n_requests
average_time = average_time.total_seconds()
print("Le temps moyen est ", average_time)

# results load_balancer
# 0.251174
# 0.251185
# 0.251282
# 0.251281
# 0.251275

# results centralized
# 0.520318
# 0.508896
# 0.509865
# 0.501767
# 0.506698
