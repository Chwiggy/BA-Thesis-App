import argparse
import osmfile
import pyrosm
import r5py
import osmnx as ox
from destination import Destination
from gtfs import crop_gtfs

def main(place_name: str, gtfs_path: str):

    place = geocoding(place_name)
    
    osm_file = osmfile.get_osm_data(geodata=place, name = place_name)
    osm_data = pyrosm.pyrosm.OSM(osm_file.path)
    
    gtfs_cropped = crop_gtfs(gtfs_path, place)
    
    transport_network = r5py.TransportNetwork(
        osm_pbf=osm_file.path, gtfs=gtfs_cropped
    )

    for destination in Destination.__members__:
        # TODO clean up processing in batch.py and insert
        raise NotImplementedError

def cli_input():
    parser = argparse.ArgumentParser(description="all closeness centrality calculations for one county")
    parser.add_argument("county")
    parser.add_argument("-g", '--gtfs')
    args = parser.parse_args()
    place_name = args.county
    gtfs_path = args.gtfs
    return place_name,gtfs_path


def geocoding(place_name):
    try:
        location = ox.geocode_to_gdf(query=place_name)
    except ConnectionError:
        raise NotImplementedError
    except ox._errors.InsufficientResponseError:
        raise NotImplementedError
    #TODO error handling


if __name__ == "__main__":
    place_name, gtfs_path = cli_input()
    main(place_name, gtfs_path)