
from pytube import YouTube

link = input("Enter Video URL: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
	
print("Downloading...")
stream.download()
print("Done!")

