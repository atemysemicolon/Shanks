#### Sample code to parse the movie name ###
### Check other searchers as well ###
import tmdbsimple as tmdb
tmdb.API_KEY =  None # Removed before commit

def find_closest_matches(name, searcher, movie=True, tv=False):	
	response = searcher.movie(query=name)
	# print (response)
	print (searcher.results)
	results_dict = {"id" : [], "title" : [], "release_date" : [] }
	for res in searcher.results:
		results_dict["id"].append(res["id"])
		results_dict["title"].append(res["title"])
		results_dict["release_date"].append(res["release_date"])
	return results_dict


results = find_closest_matches("bourne identity", searcher = tmdb.Search())
print (results)
		
