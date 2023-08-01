# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Vegetarbloggen(AbstractScraper):
    @classmethod
    def host(cls):
        return "vegetarbloggen.no"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions().strip()

    def description(self):
        return self.schema.description()