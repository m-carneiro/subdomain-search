class Subdomains:
    def __init__(self, id, dates, subdomains, where_is):
        self.id = id
        self.dates = dates
        self.subdomains = subdomains
        self.where_is = where_is

    def json(self):
        return {
            'id': self.id,
            'dates': self.dates,
            'subdomains': self.subdomains,
            'whereIs': self.where_is
        }