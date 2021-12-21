import speedtest

test = speedtest.Speedtest()

print("Loading servers list...")
test.get_servers()
print("Loading best server...")
best = test.get_best_server()

print(best)