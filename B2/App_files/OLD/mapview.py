from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from kivy_garden.mapview.view import MapMarkerPopup


class MyMapView(MapView):
    def __init__(self):
        super(MyMapView, self).__init__()
        self.lat = 45.44
        self.lon = 8.62
        self.zoom = 10
        self.add_marker(MapMarkerPopup(lat=-33.8670512,lon=151.206))
        #MyMapView.add_marker(marker=MapMarkerPopup(lat=-33.8670512,lon=151.206))

    # def get_markers_in_fov(self,*args): 
    #     self.add_marker()
    
        #self.marker = MyMapView.add_marker(MapMarkerPopup(lat=-33.8670512,lon=151.206)
        #self.map_mark = MapMarkerPopup (lat = 45.44, lon = 8.62)
        #MapMarkerPopup(lat = 45.44, lon = 8.62)

    # def marker(self):
    #     map_mark = MapMarkerPopup (lat = 45.44, lon = 8.62)

    # def set_marker_position(self, mapview, marker):
    #     x, y = mapview.get_window_xy_from(marker.lat, marker.lon, mapview.zoom)
    #     marker.x = int(x - marker.width * marker.anchor_x)
    #     marker.y = int(y - marker.height * marker.anchor_y)
    #     if isinstance(marker, MapMarkerPopup):
    #         marker.placeholder.x = marker.x - marker.width / 2
    #         marker.placeholder.y = marker.y + marker.height
