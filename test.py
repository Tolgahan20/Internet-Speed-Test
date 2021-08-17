from speedtest import Speedtest

st = Speedtest()

print("----------------------")
print("YOUR CONNECTION'S ")
print("----------------------")
print("DOWNLOAD SPEED: ", st.download())
print("UPLOAD SPEED: ", st.upload())
