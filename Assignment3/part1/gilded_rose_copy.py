# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class legendary_item(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
        self.min_quality = 80
        self.max_quality = 80

    def update_quality(self):
        pass

    def get_item_sell_in(self):
        return self.sell_in
    
    def get_item_quality(self):
        return self.quality

class cheese_item(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
        self.min_quality = 0
        self.max_quality = 50

    def update_quality(self):
        if (self.quality < self.max_quality):
            self.quality += 1
            if (self.sell_in < 0):
                self.quality += 1
        self.sell_in -= 1

    def get_item_sell_in(self):
        return self.sell_in
    
    def get_item_quality(self):
        return self.quality

class concert_ticket_item(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
        self.min_quality = 0
        self.max_quality = 50

    def update_quality(self):
        # Handle keeping the value within max quality
        if (5 < self.sell_in <= 10):
            self.quality += 2
        elif (0 < self.sell_in <= 5):
            self.quality += 3
        elif (self.sell_in <= 0):
            self.quality = 0
        else:
            self.quality = self.quality + 1

        if (self.quality > self.max_quality):
            self.quality = self.max_quality
        
        self.sell_in = self.sell_in - 1

    def get_item_sell_in(self):
        return self.sell_in

    def get_item_quality(self):
        return self.quality

class conjured_item(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
        self.min_quality = 0
        self.max_quality = 50

    def update_quality(self):
        # handle keeping the value above min quality
        if (self.sell_in < 0):
            self.quality -= 2
        self.quality -= 2
        self.sell_in -= 1

    def get_item_sell_in(self):
        return self.sell_in
    
    def get_item_quality(self):
        return self.quality

class default_item(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
        self.min_quality = 0
        self.max_quality = 50

    def update_quality(self):
        # handle keeping the value above min quality
        if (self.sell_in < 0):
            self.quality -= 1
        self.quality -= 1
        self.sell_in -= 1

    def get_item_sell_in(self):
        return self.sell_in
    
    def get_item_quality(self):
        return self.quality

class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
    
        self.my_classes = {
            "Sulfuras, Hand of Ragnaros":legendary_item,
            "Aged Brie":cheese_item,
            "Backstage passes to a TAFKAL80ETC concert":concert_ticket_item,
            "Conjured Mana Cake":conjured_item,
            "Default":default_item
        }
        
    def update_quality(self):
        for item in (self.items):
            if (item.name in self.my_classes):
                item_class = self.my_classes[item.name]
                instance = item_class(item.name, item.sell_in, item.quality)
            else:
                item_class = self.my_classes["Default"]
                instance = item_class(item.name, item.sell_in, item.quality)
            instance.update_quality()
            item.quality = instance.quality
            item.sell_in = instance.sell_in