from pytube import YouTube

##cole a URL do video desejado aqui
video = YouTube("https://www.youtube.com/watch?v=i7ABlHngi1Q")

##define a resolução do video
video_stream = video.streams.get_highest_resolution()

##pasta de salvamento/destino (não precisa por o nome do vídeo)
video_stream.download(output_path="e:/temp")
