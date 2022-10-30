from speedtest import Speedtest

st = Speedtest()
download = st.download()
upload = st.upload()

servernames = []
st.get_servers(servernames)
ping = st.results.ping

print("YOUR CONNECTION'S ")
print("----------------------")
print('DOWNLOAD SPEED: {:.2f} Kb/s\n'.format(download / 1024))
print('UPLOAD SPEED: {:.2f} Kb/s\n'.format(upload / 1024))
print('Ping:: {} ms'.format(ping))
