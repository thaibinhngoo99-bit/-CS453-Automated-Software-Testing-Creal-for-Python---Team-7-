def create_ship(ship_name, faction_key):
    new_ship = Ship(name=ship_name, faction_key=faction_key)
    new_ship.put()
    return new_ship