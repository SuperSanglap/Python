import speedtest

print('\n\tPlease Wait!\n')

test = speedtest.Speedtest()
download = str(test.download() /1024 /1024)
upload = str(test.upload() /1024 /1024)

download = download[0:3]
upload = upload[0:3]

print(f'\tDownload Speed: {download} Mbps')
print(f'\tUpload Speed: {upload} Mbps')