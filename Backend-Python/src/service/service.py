from src.repository.dbconnect import GISPlace    
class GisService:

    def get_map_data(self, request):
        return GISPlace.get_map_data(request)