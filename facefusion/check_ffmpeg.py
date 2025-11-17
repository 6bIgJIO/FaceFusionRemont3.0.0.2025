import subprocess

cmd = ["D:\\2027\\SouthSound\\kids\\FL\\venya\\lib\\site-packages\\imageio_ffmpeg\\binaries\\ffmpeg-win-x86_64-v7.1.exe", "-encoders"]
out = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8', errors='ignore')
print("libx264" in out)