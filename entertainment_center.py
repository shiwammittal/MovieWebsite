﻿import movies
import fresh_tomatoes

baahubali = movies.Movie("Baahubali: The Beginning", "An ancient India, an adventurous and daring man becomes involved in a decades old feud between two warring people.", "http://www.hdwallpapers.in/thumbs/2017/prabhas_in_baahubali_2-t1.jpg", "http://www.imdb.com/title/tt2631186/videoplayer/vi3834163993?ref_=tt_ov_vi")
transformers = movies.Movie("Transformers: The Last Knight", "In the absence of Optimus Prime, a battle for survival has commenced between the human race and the Transformers. Cade Yeager forms an alliance with Bumblebee, an English lord, and an Oxford professor to learn why the Transformers keep coming back to Earth. However, new threats arrive in the form of a new syndicate of Decepticons, led by an upgraded Megatron, a new anti-Transformers militia dedicated to destroying all Cybertronians, and the worst of it all: Optimus Prime, now on the side of evi", "http://www.hdwallpapers.in/thumbs/2014/transformers_age_of_extinction_optimus_prime-t2.jpg", "https://www.youtube.com/watch?v=rW1byMeeZNA")
wonder_woman = movies.Movie("Wonder Woman 'Origin'", "In the early 20th century, the Amazon princess Diana, who is living on the island of Themyscira, meets American military pilot Steve Trevor when he is washed ashore. After learning from him about the ongoing events of World War I, she leaves her home to bring an early end to the war", "http://www.hdwallpapers.in/walls/wonder_woman_gal_gadot-wide.jpg","https://www.youtube.com/watch?v=piIUpbIlp8U")
fast_and_furious = movies.Movie("Fаst and Furiоus 8 - The Fate Of The Furious","When a mysterious woman seduces Dom into the world of crime and a betrayal of those closest to him, the crew face trials that will test them as never before.","http://www.hdwallpapers.in/walls/fast_and_furious_6-wide.jpg","https://www.youtube.com/watch?v=ElFz5ObRNgE")
guardians_of_galaxy = movies.Movie("Guardians of the Galaxy Vol. 2","Set two-to-three months after the first film, the Guardians of the Galaxy travel throughout the cosmos and struggle to keep their new-found family together, while helping Peter Quill learn more about his true parentage.","http://www.hdwallpapers.in/thumbs/2016/baby_groot_guardians_of_the_galaxy_vol_2_4k-t1.jpg","https://www.youtube.com/watch?v=4hdv_6gl4gk")

list_of_movies = [baahubali,transformers,wonder_woman,fast_and_furious,guardians_of_galaxy]
fresh_tomatoes.open_movies_page(list_of_movies)
print(movies.Movie.__doc__)
print(movies.Movie.VALID_RATINGS)
