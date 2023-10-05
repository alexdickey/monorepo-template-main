# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item], max_quality=50, min_quality=0, legendary_quality=80):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        self.max_quality = max_quality
        self.min_quality = min_quality
        self.legendary_quality = legendary_quality

    # You want to handle everything on a unique basis - lots of if statements in one method
    # So lets make many methods
    # update_sulfuras:
    # update_aged_brie:
    # update_concert_tix:
    # update_ conjured: 
    # update_default:

    def update_sulfuras(self, item):
        pass

    def update_aged_brie(self, item):
        if (item.quality < self.max_quality):
            item.quality += 1
            if (item.sell_in < 0):
                item.quality += 1
        item.sell_in -= 1

    def update_concert_tix(self, item):
        # Handle keeping the value within max quality
        if (item.quality < self.max_quality):
            item.quality += 1
            if (item.sell_in <= 10):
                item.quality += 1
            if (item.sell_in <= 5):
                item.quality += 1
        if (item.sell_in <= 0):
            item.quality = 0
        item.sell_in -= 1
    
    def update_conjured(self, item):
        # handle keeping the value above min quality
        if (item.sell_in < 0):
            item.quality -= 2
        item.quality -= 2
        item.sell_in -= 1
    
    def update_default(self, item):
        # handle keeping the value above min quality

        if (item.sell_in < 0):
            item.quality -= 1
        item.quality -= 1
        item.sell_in -= 1

        
    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.update_sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_concert_tix(item)   
            elif item.name == "Conjured Mana Cake":
                self.update_conjured(item)
            else:
                self.update_default(item)
