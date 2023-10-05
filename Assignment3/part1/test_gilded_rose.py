# -*- coding: utf-8 -*-
import unittest

from gilded_rose_copy import *


class GildedRoseTest(unittest.TestCase):
    # Default Item Tests
    def test_update_quality_default(self):
        # Sell-in and Quality both decrease by 1
        items = [Item(name="Elixir of the Mongoose", sell_in=1, quality=2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Elixir of the Mongoose", items[0].name) and (0, items[0].sell_in) and (1, items[0].quality)

    def test_update_quality_default_past_sell_in(self):
        # Past sell-in, quality decreases twice as fast
        items = [Item(name="Elixir of the Mongoose", sell_in=1, quality=2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("Elixir of the Mongoose", items[0].name) and (-1, items[0].sell_in) and (-1, items[0].quality)
    
    
    # Aged Brie Item Tests
    def test_aged_brie(self):
        # sell-in decreases by 1, while quality increases by 1
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name) and (1, items[0].sell_in) and (1, items[0].quality)

    def test_aged_brie_past_sell_in(self):
        # Bast sell-in, quality increases twice as fast
        items = [Item(name="Aged Brie", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name) and (-1, items[0].sell_in) and (4, items[0].quality)
    
    # Sulfuras Tests
    def test_sulfuras(self):
        # sell-in does not decrease, quality always stays at 80
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name) and (0, items[0].sell_in) and (80, items[0].quality)
    
    # Backstage Passes Tests
    def test_backstage_passes_past_sell_in(self):
        # past sell-in, quality decreases to 0
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name) and (-1, items[0].sell_in) and (0, items[0].quality)
    
    def test_backstage_passes_max_qual(self):
        # an Item cannot have more than 50 quality
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name) and (14, items[0].sell_in) and (50, items[0].quality)

    def test_backstage_passes_10_days(self):
        # between 10-5 days, passes increase quality by 2 per day
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name) and (8, items[0].sell_in) and (24, items[0].quality)

    def test_backstage_passes_5_days(self):
        # between 5-0 days, passes increase quality by 3 per day
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name) and (3, items[0].sell_in) and (26, items[0].quality)
    
    # Conjured Mana Cake Tests
    def test_conjured_mana_cake(self):
        # conjured items decrease in quality twice as fast
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("Conjured Mana Cake", items[0].name) and (1, items[0].sell_in) and (2, items[0].quality)

    def test_conjured_mana_cake_past_sell_in(self):
        # Bast sell-in, quality decreases twice as fast
        items = [Item(name="Conjured Mana Cake", sell_in=1, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals("Conjured Mana Cake", items[0].name) and (-1, items[0].sell_in) and (0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
