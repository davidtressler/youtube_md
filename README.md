# youtube_md
YouTube Metadata

    import youtube_md

    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    video = youtube_md.metadata(url)

    print(video.url())

    print(video.title())

    print(video.thumbnail())



<h1>Requirements</h1> 

<h2> YouTube_dl </h2>
https://github.com/ytdl-org/youtube-dl

<h2> Firefox and Cookies Add-On </h2>
https://addons.mozilla.org/en-GB/firefox/addon/cookies-txt/


<h2> About </h2>

This program will produce YouTube Metadata for videos similar to https://pypi.org/project/pafy/ <br>
<b>But with the ability to use the -cookies cookies.txt command to fix the 429 issue <b>
  
  


Visit youtube.com with a computer that is not producing the 429 issue and save the cookies.txt from the firefox plugin, Then place into the same location as the youtube_md.py 
