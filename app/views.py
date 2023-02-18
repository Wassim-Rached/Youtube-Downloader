import shutil
from django.shortcuts import render,redirect
from django.views.generic import View
from pytube import YouTube
from django.http import FileResponse
from base.settings import DOWNLOAD_DIR

class Home(View):
	def __init__(self,url=None):
		self.url = url

	def get(self,request):
		return render(request,'app/home.html')  

	def post(self,request):
		if request.POST.get('fetch-vid'):
			self.url = request.POST.get('given_url')
			try: 
				video = YouTube(self.url)
			except :
				return render(request,'app/home.html',{'error_msg':'Invalid URL'})
			vidTitle,vidThumbnail = video.title,video.thumbnail_url
			qual,stream = [],[]
			for vid in video.streams.filter(progressive=True):
				qual.append(vid.resolution)
				stream.append(vid)
			context = {'vidTitle':vidTitle,'vidThumbnail':vidThumbnail,
						'qual':qual,'stream':stream,
						'url':self.url}
			return render(request,'app/home.html',context)

		elif request.POST.get('download-vid'):
			try:
				shutil.rmtree(DOWNLOAD_DIR)
			except:
				pass
			self.url = request.POST.get('given_url')
			video = YouTube(self.url)
			stream = [x for x in video.streams.filter(progressive=True)]
			video_qual = video.streams[int(request.POST.get('download-vid')) - 1]
			download = video_qual.download(output_path=DOWNLOAD_DIR)

			return FileResponse(open(download,'rb'),as_attachment=True)
		return render(request,'app/home.html')