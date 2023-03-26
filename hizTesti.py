import speedtest

st = speedtest.Speedtest()

print("Download: {:.2f}".format(st.download()/(1024*1024)))
print("Upload: {:.2f}".format(st.upload()/(1024*1024)))
print(f'ping: {st.results.ping}')

# Kodun çalıştığını terminal ekranından görebilirsiniz.