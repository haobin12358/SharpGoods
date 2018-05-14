# *- coding:utf8 *-
from SBase import SBase, close_session
from models.model import Locations


class SLocations(SBase):
    def __init__(self):
        super(SLocations).__init__()

    @close_session
    def get_all(self, usid):
        all_location = self.session.query(
            Locations.LOid,
            Locations.LOname,
            Locations.LOtelphone,
            Locations.LOno,
            Locations.LOdetail,
            Locations.LOprovince,
            Locations.LOcity,
            Locations.LOarea,
            Locations.LOisedit
        ).filter_by(USid=usid).all()
        return all_location

    @close_session
    def update_locations_by_loid(self, loid, location):
        self.session.query(Locations).filter_by(
            Loid=loid).update(location)
