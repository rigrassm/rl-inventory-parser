#!/bin/env python3
import csv
from os import path


class Inventory:

    def __init__(self, inv_file):
        if path.isfile(inv_file):
            self.inv_file = inv_file
        else:
            raise FileNotFoundError("Please provide a valid filepath for your inventory CSV")

        self.items, self.item_types, self.certs = self.load_inventory()

    @staticmethod
    def paint_colors():
        return [
            "Titanium White",
            "Grey",
            "Sky Blue",
            "Lime",
            "Saffron",
            "Cobalt",
            "Forest Green",
            "Burnt Sienna",
            "Crimson",
            "Pink",
            "Purple",
            "Black",
            "Orange"
        ]

    @staticmethod
    def all_certifications():
        return [
            "Paragon",
            "Striker",
            "Sweeper",
            "Juggler",
            "Sniper",
            "Acrobat",
            "Aviator",
            "Goalkeeper",
            "Guardian",
            "Playmaker",
            "Scorer",
            "Show-Off",
            "Turtle",
            "Tactician",
            "Victor"
                ]

    def load_inventory(self):
        items = dict()
        types = list()
        certs = list()

        with open(self.inv_file, 'r') as inv:
            reader = csv.DictReader(inv)
            for row in reader:

                if row['slot'].lower() not in types:
                    types.append(row['slot'].lower())

                if row['certification'].lower() not in certs:
                    certs.append(row['certification'].lower())

                if row['name'] not in items:
                    items[row['name']] = dict(item_type=row['slot'].lower(), id=row['product id'], inv=list())

                if row['certification'] == 'none':
                    certified = False
                    cert = None
                else:
                    certified = True
                    cert = row['certification']

                if row['paint'] == 'none':
                    painted = False
                    paint = None
                else:
                    painted = True
                    paint = row['paint'].lower()

                if row['tradeable'] == 'false':
                    tradeable = False
                else:
                    tradeable = True

                items[row['name']]['inv'].append(dict(painted=painted,
                                                      paint=paint,
                                                      certified=certified,
                                                      certification=cert,
                                                      quality=row['quality'],
                                                      tradeable=tradeable
                                          ))
            return items, types, certs


    def get_items_by_type(self, item_type):
        return {k:v for (k,v) in self.items.items() if v['item_type'] == item_type.lower()}


    def get_items_by_paint(self, item_color):
        matches = list()
        for k,v in self.items.items():
            for i in v['inv']:
                if i['painted']:
                    if i['paint'] == item_color.lower():
                        i['name'] = k
                        matches.append(i)
        return matches


    def get_items_by_cert(self, item_cert):
        matches = list()
        for k,v in self.items.items():
            for i in v['inv']:
                if i['certified']:
                    if i['certification'].lower() == item_cert.lower().replace(" ",""):
                        i['name'] = k
                        matches.append(i)
        return matches

