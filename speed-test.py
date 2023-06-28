import speedtest
print('     => Testando sua velocidade... ')
test = speedtest.Speedtest()
down = test.download()
print(f'     => Velocidade Download: {down/1048576:.2f} MB/s')
upload = test.upload()
print(f'     => Velocidade Upload: {upload/1048576:.2f} MB/s')
