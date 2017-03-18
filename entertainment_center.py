import movies

toy_story = movies.Movie("Baahubali: The Beginning", "An ancient India, an adventurous and daring man becomes involved in a decades old feud between two warring people.", "http://www.imdb.com/title/tt2631186/mediaviewer/rm1394795264", "http://www.imdb.com/title/tt2631186/videoplayer/vi3834163993?ref_=tt_ov_vi")
print(toy_story.movie_summary)

transformers = movies.Movie("Transformers: The Last Knight", "In the absence of Optimus Prime, a battle for survival has commenced between the human race and the Transformers. Cade Yeager forms an alliance with Bumblebee, an English lord, and an Oxford professor to learn why the Transformers keep coming back to Earth. However, new threats arrive in the form of a new syndicate of Decepticons, led by an upgraded Megatron, a new anti-Transformers militia dedicated to destroying all Cybertronians, and the worst of it all: Optimus Prime, now on the side of evi", "https://www.google.com/search?q=transformers&safe=off&espv=2&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwicwcXHhOHSAhVBQSYKHflnAhsQ_AUICCgD&biw=1280&bih=659#safe=off&tbm=isch&q=transformers+the+last+knight&*&imgrc=SPY46xdnp2DBGM:", "https://www.youtube.com/watch?v=rW1byMeeZNA")
print(transformers.movie_summary)
#transformers.play_movie_trailer()

wonder_woman = movies.Movie("Wonder Woman 'Origin'", "In the early 20th century, the Amazon princess Diana, who is living on the island of Themyscira, meets American military pilot Steve Trevor when he is washed ashore. After learning from him about the ongoing events of World War I, she leaves her home to bring an early end to the war", "https://www.google.com/search?q=wonder+woman+wiki&safe=off&espv=2&source=lnms&tbm=isch&sa=X&ved=0ahUKEwicyMuYhuHSAhUCQSYKHbZ-CCcQ_AUIBygC&biw=1280&bih=659#safe=off&tbm=isch&q=wonder+woman+gal+gadot&*&imgrc=-TZK5uVxFGpDyM:","https://www.youtube.com/watch?v=piIUpbIlp8U")
print(wonder_woman.movie_summary)
wonder_woman.play_movie_trailer()
