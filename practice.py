from pytube import YouTube

# Get YouTube video link and file name
link = input("Enter YouTube video link:  ")
fileName = input("Enter desired file name: ")

try:
     # Try creting a YouTube object using the link user has entered
     yt = YouTube(link)
except:
     # Handle exceptions
     print("Connection Error")

# Set file name
yt.set_filename(fileName)

# Display video's title and length
print("Title: ", yt.title)
print("Length of video: ",yt.length)

# Get the video's highest resolution
ys = yt.streams.get_highest_resolution()

try:
     # Try downloading the video
     print("Downloading...")
     ys.download()
except:
     # Handle exceptions
     print("Download failed") 
          
print("Download completed!!")